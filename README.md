# antiquaire-debarras-paris.fr

Site statique de 47 pages, généré en Python, servi par un Worker Cloudflare qui traite aussi le formulaire d'estimation (envoi via Resend, photos en pièces jointes).

## Structure

```
build/            générateur (Python 3, sans dépendance)
  core.py         CONFIGURATION (coordonnées), photos, gabarit, composants, schema.org
  pages_*.py      contenus : accueil, services, zones, guides, pages d'info
  assets/         style.css, main.js
  icons/          icônes Lucide utilisées (licence ISC)
public/           site généré : NE PAS éditer à la main, relancer le build
src/worker.js     Worker : redirection www, formulaire /api/estimation, service des fichiers
wrangler.jsonc    configuration Cloudflare
```

## Avant la mise en ligne : à remplacer dans `build/core.py` (bloc `CFG`)

- `phone_display` / `phone_e164` : numéro réel
- `siren`, `street`, `postal` : pour les mentions légales et la fiche entreprise
- `hours_text` / `hours_schema` : horaires réels
- Mentions légales (`build/pages_info.py`) : nom, forme juridique, directrice de la publication

Puis : `npm run build`

## Engagements écrits sur le site, à faire confirmer par la cliente

Estimation et déplacement gratuits ; intervention dans le 92, 93 et 94 ; paiement par virement ou chèque à l'enlèvement ; débarras gratuit lorsque la valeur reprise couvre le coût ; réponse sur photos dans la journée ouvrée ; intervention possible en l'absence des héritiers ; déclaration en préfecture et registre d'objets mobiliers à jour ; page « À propos » rédigée pour une professionnelle indépendante.

## Déploiement (GitHub → Cloudflare)

1. Pousser ce dossier dans un dépôt GitHub privé.
2. Cloudflare → Workers & Pages → Créer → Importer un dépôt Git → choisir le dépôt.
   Commande de build : aucune (le dossier `public/` est déjà généré). Commande de déploiement : `npx wrangler deploy`.
3. Ajouter le secret : Paramètres du Worker → Variables et secrets → `RESEND_API_KEY` (type Secret).
4. Resend : vérifier le domaine `antiquaire-debarras-paris.fr` (enregistrements DNS fournis par Resend) pour que `MAIL_FROM` soit accepté.
5. Domaine : ajouter `antiquaire-debarras-paris.fr` et `www.` comme Custom Domains du Worker (ou décommenter `routes` dans `wrangler.jsonc`). Le www redirige en 301 vers le domaine nu.

En local : `npm install`, puis `npx wrangler dev` (créer un fichier `.dev.vars` avec `RESEND_API_KEY=...` pour tester l'envoi).

## SEO : après la mise en ligne

- Google Search Console : ajouter le domaine, soumettre `https://antiquaire-debarras-paris.fr/sitemap.xml`.
- Fiche d'établissement Google : mêmes nom, téléphone et zone que le site (zone desservie, sans adresse si elle n'est pas publique), catégorie principale « Antiquaire », secondaires « Service de débarras » et « Brocanteur ».
- Remplacer progressivement les photos d'illustration par des photos réelles (objets achetés, chantiers avant/après avec accord des clients) : c'est le signal de confiance le plus fort, pour Google comme pour les visiteurs.
- Ajouter des avis clients authentiques dès qu'ils existent.

## Photos

Photos d'illustration Unsplash et Pexels (usage commercial autorisé, sans attribution obligatoire ; crédit global en pied de page), chargées depuis leurs CDN en AVIF/WebP redimensionné. La liste est dans `IMG` (`build/core.py`) : remplacer un identifiant suffit à changer une photo partout.
