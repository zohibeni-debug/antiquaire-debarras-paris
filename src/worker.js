/**
 * Worker Cloudflare : sert le site statique (dossier public/) et traite le formulaire d'estimation.
 * Secrets / variables :
 *   RESEND_API_KEY (secret)  — clé API Resend
 *   MAIL_TO                  — adresse qui reçoit les demandes
 *   MAIL_FROM                — expéditeur vérifié dans Resend, ex. "Site <site@antiquaire-debarras-paris.fr>"
 */
const MAX_FILES = 8;
const MAX_TOTAL = 20 * 1024 * 1024;
const REQUIRED = ["nom", "telephone", "email", "lieu", "type", "message"];

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // www → domaine nu (une seule version indexée)
    if (url.hostname.startsWith("www.")) {
      url.hostname = url.hostname.slice(4);
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname === "/api/estimation") {
      if (request.method !== "POST") return json({ ok: false, error: "Méthode non autorisée." }, 405);
      try {
        return await handleEstimation(request, env);
      } catch (err) {
        console.error("estimation", err && err.stack ? err.stack : err);
        return reply(request, { ok: false, error: "Une erreur technique a empêché l'envoi." }, 500);
      }
    }

    return env.ASSETS.fetch(request);
  },
};

async function handleEstimation(request, env) {
  const fd = await request.formData();

  // Anti-robots : champ piège rempli ou formulaire soumis en moins de 3 secondes
  const trap = String(fd.get("site") || "");
  const t = Number(fd.get("t") || 0);
  if (trap || (t && Date.now() - t < 3000)) return reply(request, { ok: true });

  const data = {};
  for (const k of REQUIRED) {
    data[k] = String(fd.get(k) || "").trim().slice(0, k === "message" ? 5000 : 200);
    if (!data[k]) return reply(request, { ok: false, error: "Merci de remplir tous les champs obligatoires." }, 400);
  }
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)) return reply(request, { ok: false, error: "L'adresse e-mail semble incorrecte." }, 400);
  if (fd.get("consentement") !== "oui") return reply(request, { ok: false, error: "Merci de cocher la case de consentement." }, 400);

  const files = fd.getAll("photos").filter((f) => f && typeof f === "object" && f.size > 0);
  if (files.length > MAX_FILES) return reply(request, { ok: false, error: `Ajoutez au maximum ${MAX_FILES} photos.` }, 400);
  let total = 0;
  const attachments = [];
  for (const f of files) {
    if (!String(f.type || "").startsWith("image/")) return reply(request, { ok: false, error: "Seules les photos sont acceptées." }, 400);
    total += f.size;
    if (total > MAX_TOTAL) return reply(request, { ok: false, error: "Les photos dépassent 20 Mo au total." }, 400);
    attachments.push({ filename: safeName(f.name), content: toBase64(await f.arrayBuffer()) });
  }

  if (!env.RESEND_API_KEY || !env.MAIL_TO || !env.MAIL_FROM) {
    console.error("Configuration e-mail manquante");
    return reply(request, { ok: false, error: "Le formulaire n'est pas encore configuré." }, 503);
  }

  const rows = [
    ["Nom", data.nom], ["Téléphone", data.telephone], ["E-mail", data.email],
    ["Lieu", data.lieu], ["Demande", data.type], ["Photos jointes", String(attachments.length)],
  ];
  const html = `<h2 style="font-family:Georgia,serif">Nouvelle demande : ${esc(data.type)}</h2>
<table cellpadding="6" style="border-collapse:collapse;font-family:Arial,sans-serif;font-size:14px">
${rows.map(([k, v]) => `<tr><td style="color:#555;border-bottom:1px solid #eee"><b>${k}</b></td><td style="border-bottom:1px solid #eee">${esc(v)}</td></tr>`).join("")}
</table>
<p style="font-family:Arial,sans-serif;font-size:14px;white-space:pre-wrap;margin-top:16px">${esc(data.message)}</p>`;
  const text = rows.map(([k, v]) => `${k} : ${v}`).join("\n") + "\n\n" + data.message;

  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: env.MAIL_FROM,
      to: env.MAIL_TO.split(",").map((s) => s.trim()),
      reply_to: data.email,
      subject: `Estimation : ${data.type} — ${data.nom} (${data.lieu})`,
      html, text, attachments,
    }),
  });
  if (!res.ok) {
    console.error("Resend", res.status, await res.text());
    return reply(request, { ok: false, error: "L'envoi n'a pas abouti." }, 502);
  }
  return reply(request, { ok: true });
}

function reply(request, body, status = 200) {
  const wantsJson = (request.headers.get("Accept") || "").includes("application/json");
  if (wantsJson) return json(body, status);
  if (body.ok) return Response.redirect(new URL("/merci", request.url).toString(), 303);
  return new Response(`<!doctype html><meta charset="utf-8"><title>Erreur</title><p>${esc(body.error || "Erreur")}</p><p><a href="/contact">Retour au formulaire</a></p>`,
    { status, headers: { "Content-Type": "text/html; charset=utf-8" } });
}

function json(body, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" } });
}

function esc(s) {
  return String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function safeName(name) {
  const n = String(name || "photo.jpg").normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^\w.\-]+/g, "_");
  return n.slice(-80) || "photo.jpg";
}

function toBase64(buf) {
  const bytes = new Uint8Array(buf);
  let bin = "";
  for (let i = 0; i < bytes.length; i += 0x8000) bin += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  return btoa(bin);
}
