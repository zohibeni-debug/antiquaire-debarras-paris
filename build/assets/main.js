(() => {
  // Menus déroulants : ouverture au clic (écrans tactiles larges) + Échap
  document.querySelectorAll(".nav-group > button").forEach((btn) => {
    btn.addEventListener("click", () => {
      const g = btn.parentElement;
      const open = g.classList.toggle("open");
      btn.setAttribute("aria-expanded", String(open));
    });
  });
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    document.querySelectorAll(".nav-group.open").forEach((g) => {
      g.classList.remove("open");
      g.querySelector("button")?.setAttribute("aria-expanded", "false");
    });
    document.querySelectorAll("details.menu-mobile[open]").forEach((d) => d.removeAttribute("open"));
  });
  document.addEventListener("click", (e) => {
    document.querySelectorAll(".nav-group.open").forEach((g) => {
      if (!g.contains(e.target)) { g.classList.remove("open"); g.querySelector("button")?.setAttribute("aria-expanded", "false"); }
    });
  });

  // Formulaire d'estimation
  const form = document.querySelector("form[data-estimation]");
  if (!form) return;
  const t0 = form.querySelector('input[name="t"]');
  if (t0) t0.value = String(Date.now());

  const input = form.querySelector('input[type="file"]');
  const zone = form.querySelector(".depot");
  const liste = form.querySelector(".liste-fichiers");
  const MAX_FILES = 8;
  const MAX_TOTAL = 20 * 1024 * 1024;

  const kb = (n) => (n > 1024 * 1024 ? (n / 1024 / 1024).toFixed(1) + " Mo" : Math.round(n / 1024) + " Ko");
  const renderFiles = () => {
    if (!input || !liste) return;
    const files = Array.from(input.files || []);
    liste.innerHTML = "";
    let total = 0;
    files.forEach((f) => { total += f.size; const li = document.createElement("li"); li.textContent = f.name + " (" + kb(f.size) + ")"; liste.appendChild(li); });
    if (files.length > MAX_FILES) input.setCustomValidity("Ajoutez au maximum " + MAX_FILES + " photos.");
    else if (total > MAX_TOTAL) input.setCustomValidity("Les photos dépassent 20 Mo au total : retirez-en ou réduisez leur taille.");
    else input.setCustomValidity("");
  };
  input?.addEventListener("change", renderFiles);
  if (zone && input) {
    ["dragenter", "dragover"].forEach((ev) => zone.addEventListener(ev, (e) => { e.preventDefault(); zone.classList.add("survol"); }));
    ["dragleave", "drop"].forEach((ev) => zone.addEventListener(ev, () => zone.classList.remove("survol")));
    zone.addEventListener("drop", (e) => { e.preventDefault(); if (e.dataTransfer?.files?.length) { input.files = e.dataTransfer.files; renderFiles(); } });
  }

  const statut = form.querySelector(".form-statut");
  const bouton = form.querySelector('button[type="submit"]');
  form.addEventListener("submit", async (e) => {
    if (!window.fetch || !window.FormData) return; // envoi classique
    e.preventDefault();
    if (!form.reportValidity()) return;
    bouton.setAttribute("aria-busy", "true");
    bouton.disabled = true;
    const libelle = bouton.textContent;
    bouton.textContent = "Envoi en cours…";
    statut.className = "form-statut";
    try {
      const res = await fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
      const data = await res.json().catch(() => ({}));
      if (!res.ok || !data.ok) throw new Error(data.error || "L'envoi n'a pas abouti.");
      form.reset();
      if (liste) liste.innerHTML = "";
      statut.className = "form-statut ok";
      statut.textContent = "Demande envoyée. Nous vous répondons rapidement, par téléphone ou par e-mail.";
      if (typeof window.gtag === "function") window.gtag("event", "generate_lead");
    } catch (err) {
      statut.className = "form-statut ko";
      statut.textContent = (err && err.message ? err.message : "L'envoi n'a pas abouti.") + " Vous pouvez aussi nous appeler ou écrire directement par e-mail.";
    } finally {
      bouton.removeAttribute("aria-busy");
      bouton.disabled = false;
      bouton.textContent = libelle;
      statut.setAttribute("tabindex", "-1");
      statut.focus({ preventScroll: false });
    }
  });
})();
