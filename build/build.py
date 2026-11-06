"""Génère le site statique dans /home/claude/site/public."""
import shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from core import CFG, BASE, LOGO_SVG, WARN, USED_ICONS, _ICON_DIR
from pages_home import build_home
from pages_services import build_all_services
from pages_local import build_all_local
from pages_guides import build_all_guides
from pages_info import build_all_info

OUT = Path(__file__).resolve().parent.parent / "public"
ASSETS = Path(__file__).parent / "assets"


def path_to_file(path):
    if path == "/":
        return OUT / "index.html"
    return OUT / (path.strip("/") + ".html")


def main():
    for p in OUT.glob("**/*.html"):
        p.unlink()
    pages = [build_home()] + build_all_services() + build_all_local() + build_all_guides() + build_all_info()
    seen = set()
    for path, html in pages:
        assert path not in seen, path
        seen.add(path)
        f = path_to_file(path)
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(html, encoding="utf-8")

    (OUT / "assets").mkdir(exist_ok=True)
    for a in ASSETS.iterdir():
        shutil.copy(a, OUT / "assets" / a.name)
    (OUT / "assets" / "logo.svg").write_text(LOGO_SVG.replace('<svg viewBox', '<svg xmlns="http://www.w3.org/2000/svg" viewBox'), encoding="utf-8")
    (OUT / "favicon.svg").write_text(LOGO_SVG.replace('<svg viewBox', '<svg xmlns="http://www.w3.org/2000/svg" viewBox'), encoding="utf-8")

    excl = {"/merci", "/404"}
    prio = lambda p: "1.0" if p == "/" else ("0.9" if p.count("/") == 1 and not p.startswith("/antiquaire-") and p not in ("/mentions-legales", "/confidentialite") else "0.7")
    urls = "".join(
        f"<url><loc>{BASE}{'' if p == '/' else p}{'/' if p == '/' else ''}</loc><lastmod>{CFG['updated']}</lastmod><priority>{prio(p)}</priority></url>\n"
        for p, _ in pages if p not in excl)
    (OUT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n', encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /api/\nDisallow: /merci\n\nSitemap: {BASE}/sitemap.xml\n", encoding="utf-8")
    (OUT / "_headers").write_text(
        "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n"
        "  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Strict-Transport-Security: max-age=31536000; includeSubDomains\n"
        "/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n"
        "/assets/*\n  Cache-Control: public, max-age=604800\n", encoding="utf-8")
    (OUT / "_redirects").write_text("/index.html / 301\n/accueil / 301\n/estimation /estimation-antiquites-gratuite 301\n/debarras /debarras-appartement-paris 301\n", encoding="utf-8")
    icons = Path(__file__).parent / "icons"
    icons.mkdir(exist_ok=True)
    for n in sorted(USED_ICONS):
        src = _ICON_DIR / f"{n}.svg"
        if src.resolve() != (icons / f"{n}.svg").resolve():
            shutil.copy(src, icons / f"{n}.svg")
    print(f"{len(pages)} pages générées dans {OUT}")
    print("\n".join(WARN))


if __name__ == "__main__":
    main()
