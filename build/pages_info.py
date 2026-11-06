from core import *


def form_html():
    return f'''<form class="form-card" id="formulaire" data-estimation action="/api/estimation" method="post" enctype="multipart/form-data" novalidate>
<h2 style="font-size:var(--step-3)">Demande d’estimation gratuite</h2>
<p class="muted">Quelques photos suffisent pour un premier avis. Réponse par téléphone ou par e-mail.</p>
<div class="form-grid">
<div class="champ"><label for="f-nom">Nom</label><input id="f-nom" name="nom" type="text" autocomplete="name" required></div>
<div class="champ"><label for="f-tel">Téléphone</label><input id="f-tel" name="telephone" type="tel" autocomplete="tel" inputmode="tel" required pattern="[0-9 +().-]{{8,}}"></div>
<div class="champ"><label for="f-email">E-mail</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
<div class="champ"><label for="f-lieu">Ville ou arrondissement</label><input id="f-lieu" name="lieu" type="text" autocomplete="address-level2" placeholder="Paris 16e, Neuilly…" required></div>
<div class="champ full"><label for="f-type">Votre demande</label>
<select id="f-type" name="type" required>
<option value="">Choisir…</option>
<option>Vendre un ou plusieurs objets</option>
<option>Faire estimer un objet</option>
<option>Débarras d’appartement ou de maison</option>
<option>Succession : inventaire et débarras</option>
<option>Cave, grenier ou garage</option>
<option>Autre demande</option>
</select></div>
<div class="champ full"><label for="f-msg">Description</label><textarea id="f-msg" name="message" placeholder="Quels objets ou quel lieu, étage, ascenseur, échéance éventuelle…" required></textarea></div>
<div class="champ full"><label for="f-photos">Photos (facultatif)</label>
<div class="depot">{ico("image-plus")}<span class="aide">Jusqu’à 8 photos, 20 Mo au total. Une vue d’ensemble, puis les détails : signature, poinçons, étiquettes, marques.</span>
<input id="f-photos" name="photos" type="file" accept="image/*" multiple><ul class="liste-fichiers" aria-live="polite"></ul></div></div>
<div class="hp" aria-hidden="true"><label for="f-site">Ne pas remplir</label><input id="f-site" name="site" type="text" tabindex="-1" autocomplete="off"></div>
<input type="hidden" name="t" value="">
<label class="consent full"><input type="checkbox" name="consentement" value="oui" required><span>J’accepte que mes informations et photos soient utilisées pour traiter ma demande. Elles ne sont ni cédées ni utilisées à d’autres fins. <a href="/confidentialite">Confidentialité</a></span></label>
<div class="full"><button class="btn" type="submit" style="width:100%">{ico("mail")}Envoyer ma demande</button></div>
<p class="form-statut full" role="status"></p>
</div></form>'''


def p_contact():
    path = "/contact"
    body = f'''
<section class="page-hero"><div class="container">{crumbs([("Contact et estimation", None)])}
<div class="split split--top" style="margin-top:1.4rem">
<div>
<h1>Contact et estimation gratuite</h1>
<p class="lead">Décrivez votre demande et joignez quelques photos : nous vous répondons avec un premier avis, puis nous fixons une visite si besoin.</p>
<div class="coord" style="margin-top:2rem">
<div>{ico("phone")}<span><b>Téléphone</b><a href="tel:{CFG["phone_e164"]}">{CFG["phone_display"]}</a></span></div>
<div>{ico("mail")}<span><b>E-mail</b><a href="mailto:{CFG["email"]}">{CFG["email"]}</a></span></div>
<div>{ico("clock")}<span><b>Horaires</b>{CFG["hours_text"]}</span></div>
<div>{ico("map-pin")}<span><b>Zone</b>Paris, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne. <a href="/zones-intervention">Voir les zones</a></span></div>
</div>
<div class="encart" style="margin-top:2rem"><h4>{ico("camera")}Les photos qui permettent une estimation fiable</h4>
<ul class="liste-check" style="margin:.6rem 0 0">
<li>{ico("check")}<span>L’objet en entier, à la lumière du jour, sans flash</span></li>
<li>{ico("check")}<span>Les marques : signature, poinçons, étiquettes, cachets, dessous et dos</span></li>
<li>{ico("check")}<span>Les défauts visibles : éclats, fentes, manques</span></li>
<li>{ico("check")}<span>Les dimensions, même approximatives</span></li>
</ul></div>
</div>
{form_html()}
</div></div></section>
'''
    ld = [breadcrumb_ld([("Contact et estimation", None)], path),
          {"@type": "ContactPage", "url": BASE + path, "name": "Contact et estimation gratuite", "about": {"@id": BASE + "/#entreprise"}}]
    return path, render(path, "Contact et estimation gratuite : antiquaire à Paris",
                        "Demandez une estimation gratuite de vos meubles et objets anciens à Paris : formulaire avec photos, téléphone ou e-mail. Réponse rapide, sans engagement.", body, ld)


def p_apropos():
    path = "/a-propos"
    body = f'''
{page_hero([("À propos", None)], "Une antiquaire-brocanteuse à Paris", "Un métier de regard et de confiance : savoir ce que vaut un objet, le dire franchement, et traiter chaque intérieur avec le respect dû à ceux qui y ont vécu.", "boutique")}
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Notre façon de travailler</h2>
<p>Nous exerçons trois métiers qui se complètent : l’achat d’antiquités, la brocante et le débarras. Cette combinaison permet de traiter un appartement entier en une seule fois, de la commode signée au dernier carton de cave, et de faire jouer la valeur des objets en faveur de nos clients.</p>
<h3>Dire ce que vaut un objet, même quand ce n’est pas ce qu’on espère</h3>
<p>Beaucoup de familles pensent posséder des pièces de grande valeur, et c’est parfois vrai. D’autres fois, le meuble est de style, le tableau une reproduction, l’argenterie du métal argenté. Nous expliquons toujours pourquoi, objet par objet. Et quand une pièce mérite une vente aux enchères spécialisée, nous le disons aussi.</p>
<h3>Des règles appliquées sans exception</h3>
<ul>
<li>Déclaration préalable en préfecture et registre d’objets mobiliers tenu quotidiennement</li>
<li>Paiement par virement ou chèque, reçu détaillé pour chaque achat</li>
<li>Offre écrite avant tout enlèvement, sans frais cachés</li>
<li>Aucun démarchage : nous venons uniquement sur rendez-vous</li>
</ul>
<h3>Le respect des lieux et des familles</h3>
<p>Un débarras de succession n’est pas un chantier comme un autre. Papiers, photos, objets de souvenir sont mis de côté et remis aux proches. Les parties communes sont protégées, les voisins et le gardien prévenus. Le logement est rendu vide et balayé.</p>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("loupe", (4, 5), "(max-width: 900px) 100vw, 45vw")}</figure>
</div></section>
<section class="section section--tint"><div class="container cols-3">
<div class="bloc"><span class="ico-rond">{ico("search")}</span><h3>Regarder</h3><p>Chaque objet est examiné : époque, signature, matériaux, état, demande du marché.</p></div>
<div class="bloc"><span class="ico-rond">{ico("file-text")}</span><h3>Expliquer</h3><p>Une offre écrite et argumentée, que vous êtes libre d’accepter en tout ou en partie.</p></div>
<div class="bloc"><span class="ico-rond">{ico("truck")}</span><h3>Emporter</h3><p>Emballage, démontage, transport et évacuation : vous n’avez rien à porter.</p></div>
</div></section>
{cta_band()}
'''
    ld = [breadcrumb_ld([("À propos", None)], path), {"@type": "AboutPage", "url": BASE + path, "about": {"@id": BASE + "/#entreprise"}}]
    return path, render(path, "À propos : antiquaire-brocanteuse et débarras à Paris",
                        "Antiquaire, brocanteuse et spécialiste du débarras à Paris : notre méthode, nos engagements, le respect des règles et des familles. Estimation gratuite.", body, ld)


def p_mentions():
    path = "/mentions-legales"
    body = f'''
<section class="page-hero"><div class="container narrow">{crumbs([("Mentions légales", None)])}<h1 style="font-size:var(--step-4);margin-top:1.4rem">Mentions légales</h1></div></section>
<section class="section" style="padding-top:0"><div class="container narrow prose">
<h2>Éditeur du site</h2>
<p>{CFG["brand"]}<br>Entreprise individuelle — nom et forme juridique : <em>à compléter</em><br>SIREN : <em>{CFG["siren"] or "à compléter"}</em><br>Adresse : <em>{CFG["street"] or "à compléter"}</em><br>Téléphone : {CFG["phone_display"]}<br>E-mail : <a href="mailto:{CFG["email"]}">{CFG["email"]}</a><br>Directrice de la publication : <em>à compléter</em></p>
<p>Activité de revendeur d’objets mobiliers déclarée en préfecture conformément à l’article R321-1 du Code pénal ; registre d’objets mobiliers tenu conformément à l’article 321-7 du même code.</p>
<h2>Hébergement</h2>
<p>Cloudflare, Inc., 101 Townsend Street, San Francisco, CA 94107, États-Unis — www.cloudflare.com</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes de ce site sont la propriété de l’éditeur. Les photographies d’illustration proviennent des banques d’images Unsplash et Pexels, utilisées conformément à leurs licences respectives, qui autorisent l’usage commercial. Elles illustrent le type d’objets et d’intérieurs traités et ne représentent pas des réalisations de l’entreprise.</p>
<h2>Responsabilité</h2>
<p>Les informations des guides pratiques sont fournies à titre indicatif et ne constituent pas un conseil juridique ou fiscal personnalisé.</p>
</div></section>'''
    return path, render(path, "Mentions légales", "Mentions légales du site antiquaire-debarras-paris.fr : éditeur, hébergeur, propriété intellectuelle et crédits des photographies d’illustration.", body,
                        [breadcrumb_ld([("Mentions légales", None)], path)])


def p_confid():
    path = "/confidentialite"
    body = f'''
<section class="page-hero"><div class="container narrow">{crumbs([("Confidentialité", None)])}<h1 style="font-size:var(--step-4);margin-top:1.4rem">Politique de confidentialité</h1></div></section>
<section class="section" style="padding-top:0"><div class="container narrow prose">
<h2>Données collectées</h2>
<p>Via le formulaire d’estimation : nom, téléphone, e-mail, ville ou arrondissement, description de la demande et photos éventuelles. Aucune donnée n’est collectée à votre insu ; le site n’utilise pas de cookies publicitaires ni de traceurs tiers.</p>
<h2>Finalité et base légale</h2>
<p>Ces données servent uniquement à répondre à votre demande d’estimation, de rachat ou de débarras (mesures précontractuelles, article 6.1.b du RGPD). Lors d’un achat, l’identité du vendeur est inscrite au registre d’objets mobiliers en application d’une obligation légale (article 321-7 du Code pénal ; article 6.1.c du RGPD).</p>
<h2>Destinataires</h2>
<p>Les demandes sont transmises par e-mail à l’éditeur via le prestataire d’envoi Resend, agissant comme sous-traitant. Elles ne sont ni vendues ni cédées.</p>
<h2>Durée de conservation</h2>
<p>Les demandes sans suite sont conservées au maximum trois ans après le dernier contact. Les mentions du registre d’objets mobiliers sont conservées pendant la durée prévue par la réglementation.</p>
<h2>Vos droits</h2>
<p>Vous disposez d’un droit d’accès, de rectification, d’effacement, d’opposition et de limitation. Écrivez à <a href="mailto:{CFG["email"]}">{CFG["email"]}</a>. Vous pouvez aussi saisir la CNIL (www.cnil.fr).</p>
</div></section>'''
    return path, render(path, "Politique de confidentialité", "Politique de confidentialité : données collectées par le formulaire d’estimation, finalités, durée de conservation, destinataires et droits RGPD.", body,
                        [breadcrumb_ld([("Confidentialité", None)], path)])


def p_merci():
    path = "/merci"
    body = f'''<section class="section page-404"><div class="container narrow"><h1 style="font-size:var(--step-4)">Demande envoyée</h1>
<p class="lead" style="margin:1.2rem auto 2rem">Merci. Nous revenons vers vous rapidement, par téléphone ou par e-mail.</p><div class="btn-row" style="justify-content:center"><a class="btn" href="/">Retour à l’accueil</a>{btn_tel()}</div></div></section>'''
    return path, render(path, "Demande envoyée", "Votre demande d’estimation gratuite a bien été envoyée à notre antiquaire. Nous vous répondons rapidement par téléphone ou par e-mail.", body, robots="noindex,follow")


def p_404():
    path = "/404"
    body = f'''<section class="section page-404"><div class="container narrow"><h1 style="font-size:var(--step-4)">Cette page n’existe pas</h1>
<p class="lead" style="margin:1.2rem auto 2rem">Elle a peut-être été déplacée. Les pages principales sont accessibles ci-dessous.</p>
<div class="btn-row" style="justify-content:center"><a class="btn" href="/">Accueil</a><a class="btn btn--ghost" href="/contact">Estimation gratuite</a><a class="btn btn--ghost" href="/zones-intervention">Zones d’intervention</a></div></div></section>'''
    return path, render(path, "Page introuvable", "La page demandée n’existe pas ou a été déplacée. Retrouvez nos services d’antiquaire et de débarras à Paris depuis l’accueil.", body, robots="noindex,follow")


def build_all_info():
    return [p_contact(), p_apropos(), p_mentions(), p_confid(), p_merci(), p_404()]
