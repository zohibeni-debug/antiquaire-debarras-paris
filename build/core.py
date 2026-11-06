"""Noyau du générateur : configuration, images, icônes, composants et gabarit."""
import json, re, html
from pathlib import Path

# ---------------------------------------------------------------------------
# CONFIGURATION — à compléter avec les coordonnées réelles avant mise en ligne
# ---------------------------------------------------------------------------
CFG = {
    "domain": "https://antiquaire-debarras-paris.fr",
    "brand": "Antiquaire Débarras Paris",
    "tagline": "Achat, estimation, débarras",
    "phone_display": "06 XX XX XX XX",      # À REMPLACER
    "phone_e164": "+33600000000",            # À REMPLACER
    "email": "contact@antiquaire-debarras-paris.fr",
    "locality": "Paris",
    "region": "Île-de-France",
    "street": "",                            # adresse si elle peut être publiée
    "postal": "",
    "siren": "",                             # À COMPLÉTER (mentions légales)
    "hours_text": "Du lundi au samedi, de 9 h à 19 h, sur rendez-vous",  # À CONFIRMER
    "hours_schema": ["Mo-Sa 09:00-19:00"],
    "updated": "2026-11-06",
    "og_default": "salon",
}
BASE = CFG["domain"]
WARN = []

# ---------------------------------------------------------------------------
# PHOTOS — Unsplash (licence Unsplash) et Pexels (licence Pexels) : usage commercial libre
# ---------------------------------------------------------------------------
IMG = {
    "salon": ("u", "1785441513755-af171009e068", "Salon parisien orné d'un lustre en cristal, d'une cheminée et de mobilier ancien"),
    "salon_or": ("u", "1785441513847-aa6a6576b99e", "Pièce de réception aux dorures avec lustre et meubles anciens"),
    "boutique": ("u", "1781176987353-aa5bd0e9a70f", "Objets anciens éclairés par la lumière du jour dans une boutique d'antiquités"),
    "commode": ("u", "1544691560-fc2053d97726", "Commode ancienne en bois à tiroirs"),
    "commode_fauteuil": ("u", "1601617956235-c97e358d054f", "Petite commode ancienne à deux tiroirs à côté d'un fauteuil"),
    "chaises_soleil": ("u", "1763844668202-1c6f39520c58", "Chaises anciennes et table en bois dans la lumière d'une fenêtre"),
    "chaises_etageres": ("u", "1763337925283-9ed80c77bb6e", "Collection de chaises anciennes rangées sur des étagères"),
    "bureau": ("u", "1773652924813-297c14dd9b5b", "Bureau ancien en bois sculpté et lampe dans un cabinet de travail"),
    "loupe": ("u", "1762180980045-4d7c5a6c0fc9", "Loupe posée sur un plateau en bois, outil d'expertise d'objets anciens"),
    "miroir_salon": ("u", "1759171069648-010886f57012", "Pièce ancienne ornée avec table et grand miroir"),
    "coiffeuse": ("u", "1715249891485-4b8e66b584dc", "Chambre avec commode ancienne surmontée d'un miroir"),
    "lustre": ("u", "1509437142917-63dfe86dcbec", "Lustre ancien blanc et doré"),
    "bibliotheque": ("u", "1766431014989-3a1fce5420a5", "Chaise en bois devant une bibliothèque remplie de livres anciens"),
    "tableaux": ("u", "1767243304026-219d0acb7c6b", "Accrochage de tableaux de paysage anciens sur un mur"),
    "cadres": ("u", "1554907984-15263bfd63bd", "Cadres et tableaux accrochés sur un mur"),
    "salon_tableaux": ("u", "1775416343921-6dfe2cf21424", "Salon orné de tableaux, d'un lustre et d'un tapis rouge"),
    "vase": ("u", "1723779234372-023dd09385ef", "Vase en porcelaine à décor bleu et blanc posé sur une table"),
    "tasses": ("u", "1592304502437-178c9adcf9ca", "Service de tasses en porcelaine à décor floral bleu et blanc"),
    "chambre": ("u", "1780245996099-aa03ab9244c0", "Chambre ancienne avec lit à baldaquin, cheminée et fauteuils"),
    "couloir": ("u", "1780245988750-d2aac18c2d02", "Couloir ancien avec portes en bois et tableaux encadrés"),
    "cartons": ("u", "1663625318264-695d2d04f11a", "Pièce vidée avec cartons de déménagement près d'une fenêtre"),
    "cartons_table": ("u", "1600725935160-f67ee4f6084a", "Cartons de déménagement posés sur une table en bois"),
    "design_chaise": ("u", "1624501538579-294a267664fe", "Fauteuil design bleu et brun à côté d'une table en bois"),
    "design_lampe": ("u", "1617201929478-8eedff7508f9", "Lampe de table vintage blanche à pied en bois"),
    "fenetre_paris": ("u", "1756476871898-b0040294197a", "Immeuble parisien vu depuis une fenêtre à Montmartre"),
    "machine_ecrire": ("u", "1532901358310-36d51e6fa0e7", "Bureau ancien en bois avec une machine à écrire"),
    "salle_lustre": ("u", "1786698412687-1920d91bb78c", "Salle à manger ancienne avec lustre en cristal au-dessus d'une grande table"),
    "montres": ("p", "6795489", "Montres à gousset anciennes et objets de collection"),
    "horloges": ("p", "8921288", "Pendules et objets anciens alignés sur une étagère"),
    "bijoux": ("p", "5865384", "Bijoux, livres et objets décoratifs anciens présentés sur un étal"),
    "marche": ("p", "5865376", "Étal de bijoux et d'antiquités vu d'en haut"),
}
CREDITS = {"u": "Unsplash", "p": "Pexels"}


def img_url(key, w, h):
    prov, pid, _ = IMG[key]
    if prov == "u":
        return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&crop=entropy&w={w}&h={h}&q=72"
    return f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg?auto=compress&cs=tinysrgb&fit=crop&w={w}&h={h}"


def img(key, ratio=(4, 3), sizes="(max-width: 900px) 100vw, 50vw", eager=False, alt=None, widths=(480, 800, 1200, 1600)):
    rw, rh = ratio
    srcset = ", ".join(f"{html.escape(img_url(key, w, round(w * rh / rw)))} {w}w" for w in widths)
    base_w = 1200
    src = img_url(key, base_w, round(base_w * rh / rw))
    a = html.escape(alt or IMG[key][2])
    load = 'fetchpriority="high" loading="eager"' if eager else 'loading="lazy"'
    return (f'<img src="{html.escape(src)}" srcset="{srcset}" sizes="{sizes}" width="{base_w}" '
            f'height="{round(base_w * rh / rw)}" alt="{a}" decoding="async" {load}>')


# ---------------------------------------------------------------------------
# ICÔNES — Lucide (ISC)
# ---------------------------------------------------------------------------
_LOCAL_ICONS = Path(__file__).parent / "icons"
_VENDOR = list(Path("/home/claude/vendor").glob("lucide-static-*/package/icons"))
_ICON_DIR = _VENDOR[0] if _VENDOR else _LOCAL_ICONS
USED_ICONS = set()
_icon_cache = {}


def ico(name, cls="ico"):
    USED_ICONS.add(name)
    if name not in _icon_cache:
        raw = (_ICON_DIR / f"{name}.svg").read_text()
        inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1).strip()
        inner = re.sub(r"\s+", " ", inner)
        _icon_cache[name] = inner
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_icon_cache[name]}</svg>')


LOGO_SVG = (
    '<svg viewBox="0 0 48 48" aria-hidden="true">'
    '<ellipse cx="24" cy="24" rx="17.5" ry="22" fill="none" stroke="#b08a3e" stroke-width="1.4"/>'
    '<ellipse cx="24" cy="24" rx="14.3" ry="18.6" fill="#1c2e5c"/>'
    '<text x="24" y="29.4" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-weight="600" font-size="14.5" fill="#f3e6c2" letter-spacing=".5">AD</text>'
    '<path d="M24 1.2v2.6M24 44.2v2.6" stroke="#b08a3e" stroke-width="1.4"/>'
    '</svg>'
)

# ---------------------------------------------------------------------------
# NAVIGATION
# ---------------------------------------------------------------------------
NAV_ANTIQ = [
    ("/achat-antiquites-paris", "Achat d'antiquités", "Meubles, objets d'art, collections"),
    ("/rachat-meubles-anciens", "Rachat de meubles anciens", "Commodes, armoires, secrétaires"),
    ("/estimation-antiquites-gratuite", "Estimation gratuite", "Sur photos ou à domicile"),
    ("/brocanteur-a-domicile-paris", "Brocanteur à domicile", "Nous venons chez vous"),
    ("/objets-achetes", "Objets que nous achetons", "Tableaux, argenterie, pendules…"),
]
NAV_DEBARRAS = [
    ("/debarras-succession", "Débarras de succession", "Après décès, avec inventaire"),
    ("/debarras-appartement-paris", "Débarras d'appartement", "Paris intra-muros, tous étages"),
    ("/debarras-maison", "Débarras de maison", "Petite couronne et Île-de-France"),
    ("/debarras-cave-grenier", "Cave, grenier, garage", "Accès difficiles compris"),
    ("/debarras-avec-rachat", "Débarras avec rachat", "La valeur des objets réduit la facture"),
]

ARR_ORD = {1: "1er"}
def ordinal(n):
    return ARR_ORD.get(n, f"{n}e")


def plaque_label(n):
    o = ordinal(n)
    return f'<span class="u">Paris</span> {n}<sup>{o[len(str(n)):]}</sup>'


def esc(s):
    return html.escape(s, quote=True)


# ---------------------------------------------------------------------------
# COMPOSANTS
# ---------------------------------------------------------------------------
def btn_estimation(label="Envoyer des photos pour une estimation", cls="btn"):
    return f'<a class="{cls}" href="/contact#formulaire">{ico("camera")}{label}</a>'


def btn_tel(cls="btn btn--ghost"):
    return f'<a class="{cls}" href="tel:{CFG["phone_e164"]}">{ico("phone")}{CFG["phone_display"]}</a>'


def crumbs(items):
    """items: [(label, url|None)]"""
    lis = ['<li><a href="/">Accueil</a></li>']
    for label, url in items:
        lis.append(f'<li><a href="{url}">{esc(label)}</a></li>' if url else f'<li aria-current="page">{esc(label)}</li>')
    return f'<nav class="crumbs" aria-label="Fil d’Ariane"><ol>{"".join(lis)}</ol></nav>'


def breadcrumb_ld(items, path):
    els = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE + "/"}]
    for i, (label, url) in enumerate(items, start=2):
        els.append({"@type": "ListItem", "position": i, "name": label, "item": BASE + (url or path)})
    return {"@type": "BreadcrumbList", "itemListElement": els}


def faq_html(qas, titre="Questions fréquentes"):
    out = [f'<h2>{titre}</h2><div class="faq">']
    for q, a in qas:
        out.append(f'<details><summary>{esc(q)}<span class="pm" aria-hidden="true"></span></summary><div class="rep">{a}</div></details>')
    out.append("</div>")
    return "".join(out)


def faq_ld(qas):
    def strip(h):
        return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h)).strip()
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in qas]}


def cta_band(titre="Un objet, un appartement, une succession ?", texte="Envoyez quelques photos : nous vous répondons avec une première estimation, puis nous fixons un rendez-vous si besoin. Gratuit et sans engagement."):
    return f'''<section class="cta-band"><div class="container in">
<div><h2>{titre}</h2><p>{texte}</p></div>
<div class="btn-row">{btn_estimation("Demander une estimation", "btn btn--gold")}<a class="btn btn--line-light" href="tel:{CFG["phone_e164"]}">{ico("phone")}{CFG["phone_display"]}</a></div>
</div></section>'''


def associes(liens, titre="À lire aussi"):
    items = "".join(f'<a href="{u}"><b>{esc(t)}</b><span>{esc(d)}</span></a>' for u, t, d in liens)
    return f'<h2 class="serif" style="font-size:var(--step-3)">{titre}</h2><div class="associes">{items}</div>'


def page_hero(crumb_items, h1, lead, image_key, legende=None, extra=""):
    leg = ""
    if legende:
        leg = f'<figcaption class="cartel-legende"><b>{legende[0]}</b><span>{legende[1]}</span></figcaption>'
    return f'''<section class="page-hero"><div class="container">
{crumbs(crumb_items)}
<div class="hero-grid">
<div><h1>{h1}</h1><p class="lead">{lead}</p><div class="btn-row">{btn_estimation()}{btn_tel()}</div>{extra}</div>
<figure class="cadre drape"><div class="photo">{img(image_key, (4, 5), "(max-width: 900px) 100vw, 40vw", eager=True)}</div>{leg}</figure>
</div></div></section>'''


def preuves_html():
    items = [
        ("shield-check", "<b>Estimation gratuite</b> et sans engagement, sur photos ou sur place"),
        ("scroll-text", "<b>Registre d’objets mobiliers</b> tenu jour par jour, comme l’exige l’article 321-7 du Code pénal"),
        ("banknote", "<b>Paiement par virement ou chèque</b> à l’enlèvement, avec un reçu détaillé"),
        ("map-pin", "<b>Les 20 arrondissements</b>, les Hauts-de-Seine, la Seine-Saint-Denis et le Val-de-Marne"),
    ]
    return '<ul class="preuves">' + "".join(f"<li>{ico(i)}<span>{t}</span></li>" for i, t in items) + "</ul>"


# ---------------------------------------------------------------------------
# GABARIT
# ---------------------------------------------------------------------------
def org_ld():
    addr = {"@type": "PostalAddress", "addressLocality": CFG["locality"], "addressRegion": CFG["region"], "addressCountry": "FR"}
    if CFG["street"]:
        addr["streetAddress"] = CFG["street"]
    if CFG["postal"]:
        addr["postalCode"] = CFG["postal"]
    areas = [{"@type": "City", "name": "Paris"}] + [
        {"@type": "AdministrativeArea", "name": n} for n in ("Hauts-de-Seine", "Seine-Saint-Denis", "Val-de-Marne")]
    return {
        "@type": ["AntiqueStore", "LocalBusiness"],
        "@id": BASE + "/#entreprise",
        "name": CFG["brand"],
        "url": BASE + "/",
        "logo": BASE + "/assets/logo.svg",
        "image": img_url("salon", 1200, 800),
        "telephone": CFG["phone_e164"],
        "email": CFG["email"],
        "address": addr,
        "areaServed": areas,
        "openingHours": CFG["hours_schema"],
        "priceRange": "Estimation gratuite",
        "paymentAccepted": "Virement bancaire, chèque",
        "knowsAbout": ["Antiquités", "Meubles anciens", "Objets d'art", "Argenterie", "Horlogerie ancienne",
                       "Mobilier design", "Débarras de succession", "Estimation d'objets anciens"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Prestations", "itemListElement": [
            {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "url": BASE + u}} for u, t, _ in NAV_ANTIQ + NAV_DEBARRAS]},
    }


def header(path):
    AC = ' aria-current="page"'
    def panel(items):
        return "".join(f'<a href="{u}"{AC if u == path else ""}>{esc(t)}<small>{esc(d)}</small></a>' for u, t, d in items)
    cur = lambda u: ' aria-current="page"' if path == u or (u != "/" and path.startswith(u)) else ""
    mob = lambda items: "".join(f'<a href="{u}">{esc(t)}</a>' for u, t, _ in items)
    return f'''<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header"><div class="container header-in">
<a class="logo" href="/" aria-label="{CFG["brand"]}, accueil">{LOGO_SVG}<span class="logo-txt"><b>Antiquaire Débarras</b><span>Paris et petite couronne</span></span></a>
<nav class="nav" aria-label="Navigation principale">
<div class="nav-group"><button type="button" aria-expanded="false" aria-haspopup="true">Antiquaire {ico("chevron-down")}</button><div class="nav-panel">{panel(NAV_ANTIQ)}</div></div>
<div class="nav-group"><button type="button" aria-expanded="false" aria-haspopup="true">Débarras {ico("chevron-down")}</button><div class="nav-panel">{panel(NAV_DEBARRAS)}</div></div>
<a href="/zones-intervention"{cur("/zones-intervention")}>Zones</a>
<a href="/guides"{cur("/guides")}>Guides</a>
<a href="/a-propos"{cur("/a-propos")}>À propos</a>
</nav>
<div class="header-cta"><a class="tel-link" href="tel:{CFG["phone_e164"]}">{ico("phone")}<span>{CFG["phone_display"]}</span></a><a class="btn" href="/contact#formulaire">Estimation gratuite</a></div>
<details class="menu-mobile"><summary>{ico("menu")}Menu</summary><div class="sheet">
<a href="/contact#formulaire"><b>Demander une estimation gratuite</b></a>
<h3>Antiquaire</h3>{mob(NAV_ANTIQ)}
<h3>Débarras</h3>{mob(NAV_DEBARRAS)}
<h3>Informations</h3><a href="/zones-intervention">Zones d’intervention</a><a href="/guides">Guides</a><a href="/a-propos">À propos</a><a href="/contact">Contact</a>
</div></details>
</div></header>'''


def footer():
    arr = "".join(f'<a href="/antiquaire-paris-{n}">{ordinal(n)}</a>' for n in range(1, 21))
    return f'''<footer class="site-footer"><div class="container">
<div class="footer-grid">
<div class="footer-marque"><a class="logo" href="/">{LOGO_SVG}<span class="logo-txt"><b>Antiquaire Débarras</b><span>Paris et petite couronne</span></span></a>
<p>Achat de meubles anciens et d’objets d’art, estimation gratuite, débarras d’appartements, de maisons et de successions à Paris.</p>
<p><a href="tel:{CFG["phone_e164"]}">{CFG["phone_display"]}</a><br><a href="mailto:{CFG["email"]}">{CFG["email"]}</a><br>{CFG["hours_text"]}</p></div>
<div><h3>Antiquaire</h3><ul>{"".join(f'<li><a href="{u}">{esc(t)}</a></li>' for u, t, _ in NAV_ANTIQ)}</ul></div>
<div><h3>Débarras</h3><ul>{"".join(f'<li><a href="{u}">{esc(t)}</a></li>' for u, t, _ in NAV_DEBARRAS)}</ul></div>
<div><h3>Informations</h3><ul><li><a href="/zones-intervention">Zones d’intervention</a></li><li><a href="/guides">Guides pratiques</a></li><li><a href="/a-propos">À propos</a></li><li><a href="/contact">Contact et estimation</a></li><li><a href="/mentions-legales">Mentions légales</a></li><li><a href="/confidentialite">Confidentialité</a></li></ul></div>
</div>
<div class="footer-bas"><div><span>Antiquaire à Paris :</span><div class="footer-arr">{arr}</div></div>
<div>© 2026 {CFG["brand"]}. Photos d’illustration : Unsplash et Pexels.</div></div>
</div></footer>
<div class="barre-mobile" role="navigation" aria-label="Contact rapide"><a class="btn btn--ghost" href="tel:{CFG["phone_e164"]}">{ico("phone")}Appeler</a><a class="btn" href="/contact#formulaire">{ico("camera")}Estimation photo</a></div>'''


_TXT = re.compile(r"(<script.*?</script>|<style.*?</style>|<[^>]+>)", re.S)


def typo_fr(html_doc):
    """Espaces insécables avant : ; ! ? et à l'intérieur des guillemets, hors balises et scripts."""
    parts = _TXT.split(html_doc)
    for i, part in enumerate(parts):
        if i % 2 == 1 or not part:
            continue
        part = re.sub(r" :", "\u00a0:", part)
        part = re.sub(r" ([;!?])", "\u202f\\1", part)
        part = part.replace("« ", "«\u00a0").replace(" »", "\u00a0»")
        parts[i] = part
    return "".join(parts)


def render(path, title, description, body, ld=None, og_image=None, robots="index,follow", og_type="website"):
    if len(title) > 62:
        WARN.append(f"TITRE {len(title)} {path}: {title}")
    if not (110 <= len(description) <= 160):
        WARN.append(f"DESC {len(description)} {path}")
    canonical = BASE + (path if path != "/" else "/")
    graph = [org_ld(), {"@type": "WebSite", "@id": BASE + "/#site", "url": BASE + "/", "name": CFG["brand"], "inLanguage": "fr-FR"}]
    graph += (ld or [])
    ldjson = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
    ogi = img_url(og_image or CFG["og_default"], 1200, 630)
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="{robots}">
<meta name="theme-color" content="#1c2e5c">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="{CFG["brand"]}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{esc(ogi)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://images.unsplash.com">
<link rel="preconnect" href="https://images.pexels.com">
<link rel="preload" href="/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/fonts/instrument-sans.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css?v=2">
<script type="application/ld+json">{ldjson}</script>
</head>
<body>
{header(path)}
<main id="contenu">
{typo_fr(body)}
</main>
{footer()}
<script src="/assets/main.js?v=1" defer></script>
</body>
</html>
'''


def service_ld(name, path, desc):
    return {"@type": "Service", "name": name, "serviceType": name, "url": BASE + path, "description": desc,
            "provider": {"@id": BASE + "/#entreprise"},
            "areaServed": [{"@type": "City", "name": "Paris"}, {"@type": "AdministrativeArea", "name": "Hauts-de-Seine"},
                           {"@type": "AdministrativeArea", "name": "Seine-Saint-Denis"}, {"@type": "AdministrativeArea", "name": "Val-de-Marne"}]}
