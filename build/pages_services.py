from core import *
from pages_home import lots_html, balance_html, LOTS

ETAPES_ACHAT = '''<ol class="etapes">
<li><h3>Photos ou appel</h3><p>Vue d’ensemble, détails (signatures, poinçons, étiquettes, marques), dimensions. Un premier avis vous est donné rapidement.</p></li>
<li><h3>Visite à domicile</h3><p>Gratuite dans Paris et la petite couronne. Examen de chaque objet, à la lumière et à la loupe.</p></li>
<li><h3>Offre écrite</h3><p>Prix par objet ou global. Vous acceptez tout, une partie ou rien, sans frais.</p></li>
<li><h3>Paiement et enlèvement</h3><p>Virement ou chèque, reçu détaillé, inscription au registre d’objets mobiliers, emballage et transport par nos soins.</p></li>
</ol>'''

ETAPES_DEBARRAS = '''<ol class="etapes">
<li><h3>Visite et inventaire</h3><p>Nous parcourons chaque pièce, cave et grenier compris, repérons les objets de valeur et les accès.</p></li>
<li><h3>Devis écrit</h3><p>Coût du débarras, valeur des objets rachetés et solde final : tout figure noir sur blanc.</p></li>
<li><h3>Tri et enlèvement</h3><p>Souvenirs et papiers mis de côté, rachat, dons, recyclage et déchetterie pour le reste.</p></li>
<li><h3>Logement rendu vide</h3><p>Lieux balayés, prêts pour l’état des lieux, la vente ou les travaux. Remise des clés si besoin.</p></li>
</ol>'''


def service_page(path, crumb_label, crumb_parent, title, desc, h1, lead, image, legende, body_sections, faq, related, cta=None, extra_ld=None):
    items = ([crumb_parent] if crumb_parent else []) + [(crumb_label, None)]
    body = page_hero(items, h1, lead, image, legende, preuves_html())
    body += body_sections
    if faq:
        body += f'<section class="section section--tint"><div class="container narrow">{faq_html(faq)}</div></section>'
    if related:
        body += f'<section class="section"><div class="container">{associes(related, "Prestations liées")}</div></section>'
    body += cta_band(*(cta or ()))
    ld = [breadcrumb_ld(items, path), service_ld(crumb_label, path, desc)]
    if faq:
        ld.append(faq_ld(faq))
    ld += extra_ld or []
    return path, render(path, title, desc, body, ld, og_image=image)


REL = {
    "achat": ("/achat-antiquites-paris", "Achat d’antiquités", "Meubles, objets d’art et collections"),
    "meubles": ("/rachat-meubles-anciens", "Rachat de meubles anciens", "Commodes, armoires, secrétaires"),
    "estim": ("/estimation-antiquites-gratuite", "Estimation gratuite", "Sur photos ou à domicile"),
    "domicile": ("/brocanteur-a-domicile-paris", "Brocanteur à domicile", "Nous nous déplaçons"),
    "objets": ("/objets-achetes", "Objets que nous achetons", "La liste par famille"),
    "succ": ("/debarras-succession", "Débarras de succession", "Après décès, avec inventaire"),
    "appart": ("/debarras-appartement-paris", "Débarras d’appartement", "Paris, tous étages"),
    "maison": ("/debarras-maison", "Débarras de maison", "Petite couronne"),
    "cave": ("/debarras-cave-grenier", "Cave, grenier, garage", "Espaces encombrés"),
    "rachat": ("/debarras-avec-rachat", "Débarras avec rachat", "La valeur déduit le coût"),
    "g_fisc": ("/guides/fiscalite-vente-objets-anciens", "Guide : fiscalité de la vente", "Taxe forfaitaire, seuils, paiement"),
    "g_meuble": ("/guides/reconnaitre-un-meuble-ancien", "Guide : reconnaître un meuble ancien", "Styles, estampilles, assemblages"),
    "g_succ": ("/guides/que-faire-des-meubles-succession", "Guide : les meubles d’une succession", "Partage, vente, débarras"),
    "g_prix": ("/guides/prix-debarras-paris", "Guide : le prix d’un débarras", "Ce qui fait varier le devis"),
    "g_cp": ("/guides/antiquaire-ou-commissaire-priseur", "Guide : antiquaire ou commissaire-priseur", "Vente directe ou enchères"),
}
R = lambda *keys: [REL[k] for k in keys]


def p_achat():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Un antiquaire acheteur, pas un intermédiaire</h2>
<p>Nous achetons pour notre propre compte : le prix proposé est celui que vous recevez, sans commission ni frais de vente déduits ensuite. C’est la différence essentielle avec un dépôt-vente ou une vente aux enchères, où le produit final dépend du résultat de la vente et des frais appliqués.</p>
<p>Notre offre tient compte de l’époque, de la qualité d’exécution, de l’état, de la rareté et de la demande actuelle du marché. Un meuble d’époque signé et un meuble de style du XXe siècle peuvent se ressembler au premier regard ; leur valeur n’a rien à voir. C’est précisément ce que nous vous expliquons lors de l’estimation.</p>
<h2>Les antiquités que nous achetons à Paris</h2>
<p>Mobilier des XVIIIe et XIXe siècles, objets d’art, tableaux, bronzes, pendules, argenterie, porcelaine, luminaires, livres anciens, mais aussi mobilier et objets design du XXe siècle. Nous achetons une pièce isolée comme l’intégralité d’un appartement.</p>
<h2>Ce qui fait monter, ou baisser, une offre</h2>
<ul>
<li><strong>L’authenticité de l’époque</strong> : un meuble Louis XV d’époque n’a pas la cote d’un meuble « style Louis XV » fabriqué en 1920.</li>
<li><strong>La signature</strong> : estampille d’ébéniste, signature d’un bronzier ou d’un horloger, marque de manufacture.</li>
<li><strong>L’état et l’origine des éléments</strong> : marbre d’origine, bronzes non refaits, placages complets, mécanisme d’origine.</li>
<li><strong>La provenance</strong> : une facture ancienne, un inventaire de succession ou une photo de famille ajoutent de la confiance.</li>
<li><strong>Le marché</strong> : certaines catégories, comme le mobilier design des années 1950 à 1970, sont aujourd’hui plus recherchées que le mobilier rustique.</li>
</ul>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("boutique", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>Chaque objet est examiné à la lumière du jour : marques, usure, restaurations.</figcaption></figure>
</div></section>
<section class="section section--tint"><div class="container"><div class="section-head"><h2>Familles d’objets recherchées</h2></div>{lots_html(LOTS[:6])}</div></section>
<section class="section"><div class="container"><div class="section-head"><h2>Comment se passe un achat</h2></div>{ETAPES_ACHAT}</div></section>
'''
    faq = [
        ("Achetez-vous un seul objet ou seulement des lots ?", "<p>Les deux. Nous nous déplaçons pour une seule pièce si elle le justifie, et nous achetons aussi des contenus complets d’appartements. Une première estimation sur photos permet de le savoir sans attendre.</p>"),
        ("Le prix proposé est-il négociable ?", "<p>Notre offre est argumentée objet par objet. Si vous disposez d’éléments que nous n’avons pas vus (facture, expertise, provenance), ils peuvent la faire évoluer. Vous restez libre de ne pas vendre.</p>"),
        ("Quels documents dois-je fournir ?", "<p>Une pièce d’identité en cours de validité : ses références sont inscrites au registre d’objets mobiliers, comme pour tout rachat par un professionnel. Si vous agissez pour une succession, les héritiers doivent être d’accord sur la vente.</p>"),
        ("Faut-il nettoyer ou restaurer avant de vendre ?", "<p>Non, surtout pas. Un nettoyage maladroit peut effacer une patine, abîmer une dorure ou faire disparaître une marque. Laissez les objets dans leur état.</p>"),
    ]
    return service_page("/achat-antiquites-paris", "Achat d’antiquités", None,
        "Achat d’antiquités à Paris : meubles et objets d’art",
        "Antiquaire acheteur à Paris : achat d’antiquités, meubles anciens, tableaux, argenterie et objets d’art à domicile. Offre écrite, paiement par virement.",
        "Achat d’antiquités à Paris", "Nous achetons meubles d’époque, objets d’art, tableaux, pendules et argenterie directement chez vous, à un prix ferme annoncé avant l’enlèvement.",
        "boutique", ("Antiquités et objets de curiosité", "Ce que nous estimons : époque, signature, état, demande du marché."),
        sections, faq, R("meubles", "estim", "objets", "g_cp"))


def p_meubles():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Rachat de meubles anciens à domicile</h2>
<p>Commode, armoire, buffet deux corps, secrétaire, bureau plat, bonheur-du-jour, guéridon, sièges : nous rachetons le mobilier ancien chez vous, à Paris et en petite couronne. Vous n’avez rien à déplacer. Nous emballons, démontons si nécessaire et transportons.</p>
<p>Le marché du meuble ancien a beaucoup changé : le mobilier d’époque de qualité, signé ou bien conservé, reste recherché, tandis que le mobilier rustique massif ou de style se revend plus difficilement. Nous vous le disons franchement, et nous proposons, pour les meubles sans valeur marchande, une solution d’enlèvement dans le cadre d’un <a href="/debarras-avec-rachat">débarras avec rachat</a>.</p>
<h2>Les meubles les plus recherchés</h2>
<ul>
<li><strong>Mobilier d’époque XVIIIe</strong> : commodes Louis XV galbées, commodes Louis XVI à ressaut, sièges estampillés.</li>
<li><strong>Mobilier Empire et Restauration</strong> : acajou, bronzes dorés, secrétaires à abattant, consoles.</li>
<li><strong>Napoléon III</strong> : meubles en bois noirci et marqueterie Boulle, tables à jeux, petits meubles de salon.</li>
<li><strong>Art nouveau et Art déco</strong> : mobilier de grands décorateurs, marqueterie, laques, galuchat.</li>
<li><strong>Design 1950–1970</strong> : enfilades, sièges et tables d’éditeurs français et scandinaves.</li>
</ul>
<h2>Les indices que nous vérifions</h2>
<p>Estampille frappée sur le bâti, assemblages à queue d’aronde taillés à la main, chevilles en bois, traces de scie, revers de tiroirs, marbre d’origine, bronzes et entrées de serrure, état des placages. Notre <a href="/guides/reconnaitre-un-meuble-ancien">guide pour reconnaître un meuble ancien</a> détaille ces points.</p>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("commode_fauteuil", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>Petite commode et fauteuil : deux pièces que nous estimons séparément.</figcaption></figure>
</div></section>
<section class="section section--tint"><div class="container"><div class="section-head"><h2>Rachat de meubles : les quatre étapes</h2></div>{ETAPES_ACHAT}</div></section>
'''
    faq = [
        ("Rachetez-vous les armoires et buffets massifs ?", "<p>Nous les examinons toujours : certains ont une valeur réelle (bois précieux, époque, qualité régionale). Les autres sont aujourd’hui difficiles à revendre ; nous pouvons alors les enlever dans le cadre d’un débarras, en déduisant la valeur des pièces que nous rachetons.</p>"),
        ("Vous démontez les meubles ?", "<p>Oui, quand c’est nécessaire pour l’escalier ou l’ascenseur : armoires démontables, lits, bibliothèques. Les meubles sont protégés pendant le transport.</p>"),
        ("Achetez-vous les meubles abîmés ?", "<p>Un meuble d’époque abîmé garde souvent une valeur : un placage soulevé ou un pied cassé se restaurent. Nous tenons compte du coût de restauration dans l’offre, et nous vous l’expliquons.</p>"),
    ]
    return service_page("/rachat-meubles-anciens", "Rachat de meubles anciens", None,
        "Rachat de meubles anciens à Paris : estimation et enlèvement",
        "Rachat de meubles anciens à Paris et petite couronne : commodes, armoires, secrétaires, mobilier d’époque et design. Estimation gratuite, enlèvement inclus.",
        "Rachat de meubles anciens à Paris", "Commodes, armoires, secrétaires, sièges et mobilier design : estimation gratuite chez vous, prix ferme, démontage et transport à notre charge.",
        "commode", ("Commode ancienne à tiroirs", "Estampille, marbre, bronzes, placages : les quatre premiers points d’une estimation."),
        sections, faq, R("achat", "estim", "rachat", "g_meuble"))


def p_estimation():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Deux façons d’obtenir une estimation gratuite</h2>
<h3>Sur photos, sans vous déplacer</h3>
<p>C’est la méthode la plus rapide. Photographiez l’objet en entier, de face et de côté, à la lumière du jour, puis les détails qui comptent : signature, poinçons, étiquettes, marques sous le socle ou au dos, mécanisme, revers d’un tiroir. Ajoutez les dimensions. Vous recevez un premier avis de valeur, et nous vous disons si une visite est utile.</p>
<h3>À domicile, dans Paris et la petite couronne</h3>
<p>Pour un ensemble d’objets, un appartement complet ou une pièce importante, nous venons sur place. L’examen direct permet de vérifier ce qu’une photo ne montre pas : le poids d’une argenterie, l’état d’un placage, la nature d’un marbre, le fonctionnement d’une pendule.</p>
<h2>Estimation, avis de valeur, expertise : quelles différences ?</h2>
<div class="table-wrap"><table>
<thead><tr><th>Type</th><th>À quoi ça sert</th><th>Coût</th></tr></thead>
<tbody>
<tr><td><strong>Estimation en vue d’un rachat</strong></td><td>Connaître le prix auquel nous achetons l’objet, avec une offre ferme.</td><td>Gratuite</td></tr>
<tr><td><strong>Avis de valeur</strong></td><td>Situer un objet sur le marché, pour un partage familial ou une décision de vente.</td><td>Gratuit, dans le cadre d’un projet de vente</td></tr>
<tr><td><strong>Expertise ou inventaire officiel</strong></td><td>Document à valeur juridique (assurance, déclaration de succession, inventaire notarial), établi par un commissaire de justice ou un expert agréé.</td><td>Payant, auprès de ces professionnels</td></tr>
</tbody></table></div>
<p style="margin-top:1rem">Nous vous orientons vers un commissaire-priseur ou un expert spécialisé lorsque l’objet le justifie, par exemple pour une œuvre importante destinée aux enchères. Voir notre guide <a href="/guides/antiquaire-ou-commissaire-priseur">antiquaire ou commissaire-priseur</a>.</p>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("loupe", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>La loupe sert à lire un poinçon, une signature ou une estampille.</figcaption></figure>
</div></section>
<section class="section section--dark"><div class="container cols-3">
<div class="bloc"><span class="ico-rond" style="border-color:var(--or-clair);color:var(--or-clair)">{ico("camera")}</span><h3>Bonnes photos</h3><p>Lumière du jour, sans flash, fond neutre. Une vue d’ensemble puis trois ou quatre détails.</p></div>
<div class="bloc"><span class="ico-rond" style="border-color:var(--or-clair);color:var(--or-clair)">{ico("search")}</span><h3>Détails décisifs</h3><p>Signature, poinçons, marques de manufacture, étiquettes d’éditeur, numéros, cachets au dos.</p></div>
<div class="bloc"><span class="ico-rond" style="border-color:var(--or-clair);color:var(--or-clair)">{ico("file-text")}</span><h3>Ce que vous savez</h3><p>Origine familiale, date d’achat, facture, ancienne expertise : tout élément aide à affiner la valeur.</p></div>
</div></section>
'''
    faq = [
        ("L’estimation m’oblige-t-elle à vendre ?", "<p>Non. Elle est gratuite et sans engagement. Vous pouvez la demander pour préparer un partage ou simplement savoir ce que vous possédez.</p>"),
        ("Combien de temps pour recevoir une estimation sur photos ?", "<p>En général dans la journée ouvrée qui suit votre envoi pour un objet isolé. Pour un ensemble important, nous proposons plutôt une visite.</p>"),
        ("Pouvez-vous estimer un objet sans le voir ?", "<p>Sur photos, nous donnons une fourchette et, souvent, une offre de principe. Le prix définitif est confirmé après examen de l’objet, ce qui évite les mauvaises surprises des deux côtés.</p>"),
        ("Faites-vous des estimations pour une déclaration de succession ?", "<p>Nous établissons un inventaire estimatif utile à la famille et au notaire. Lorsque la loi ou le notaire exige un inventaire officiel, il est réalisé par un commissaire de justice ; nous pouvons travailler en complément.</p>"),
    ]
    return service_page("/estimation-antiquites-gratuite", "Estimation gratuite", None,
        "Estimation d’antiquités gratuite à Paris : photos ou domicile",
        "Estimation gratuite d’antiquités, de meubles anciens et d’objets d’art à Paris : sur photos en ligne ou à domicile. Avis de valeur argumenté, sans engagement.",
        "Estimation d’antiquités gratuite", "Envoyez des photos ou recevez-nous chez vous : nous estimons meubles anciens, tableaux, argenterie et objets d’art, gratuitement et sans engagement de vente.",
        "loupe", ("Examen à la loupe", "Signature, poinçon, estampille : les détails qui changent une estimation."),
        sections, faq, R("achat", "objets", "meubles", "g_cp"))


def p_domicile():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Un brocanteur qui se déplace chez vous</h2>
<p>Inutile de charger une voiture ou de photographier chaque objet. Nous venons à votre domicile, dans Paris et la petite couronne, pour voir l’ensemble de ce que vous souhaitez vendre : un meuble, le contenu d’une pièce, une cave ou tout un appartement.</p>
<p>Sur place, nous faisons le tri avec vous : ce que nous rachetons, ce qui peut être donné, ce qui relève du débarras. Vous savez immédiatement où vous en êtes, et vous recevez une offre écrite.</p>
<h2>Brocante ou antiquité : nous achetons les deux</h2>
<p>L’antiquaire s’intéresse aux objets de plus de cent ans et aux pièces de qualité ; le brocanteur, à tout ce qui a une seconde vie possible : vaisselle, petits meubles, luminaires, objets de décoration, vinyles, jouets anciens, outils, linge ancien. Nous exerçons les deux métiers, ce qui évite d’avoir à faire venir plusieurs acheteurs.</p>
<h2>Ce que la loi prévoit, et que nous appliquons</h2>
<ul>
<li>Inscription de chaque achat au <strong>registre d’objets mobiliers</strong>, avec l’identité du vendeur (article 321-7 du Code pénal).</li>
<li><strong>Aucun paiement en espèces</strong> pour l’or, l’argent et les métaux précieux (article L112-6 du Code monétaire et financier).</li>
<li>Un <strong>reçu détaillé</strong> remis pour chaque transaction.</li>
</ul>
<div class="encart"><h4>{ico("shield-check")}Démarchage : la règle simple</h4><p>Nous ne faisons pas de porte-à-porte et ne venons que sur rendez-vous, à votre demande. Méfiez-vous des « acheteurs » qui sonnent sans prévenir, surtout chez des personnes âgées, et proposent un paiement immédiat en liquide.</p></div>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("marche", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>Bijoux, livres, bibelots : la brocante a aussi sa valeur.</figcaption></figure>
</div></section>
<section class="section section--tint"><div class="container"><div class="section-head"><h2>Le déroulement d’une visite</h2></div>{ETAPES_ACHAT}</div></section>
'''
    faq = [
        ("Le déplacement est-il payant ?", "<p>Non, il est gratuit dans Paris et la petite couronne, que vous vendiez ou non.</p>"),
        ("Achetez-vous la vaisselle, le linge, les petits objets ?", "<p>Oui, quand ils ont une valeur de revente : services complets, verrerie ancienne, linge brodé, objets de décoration. Le reste peut être pris en charge dans un débarras.</p>"),
        ("Puis-je être absent le jour de l’enlèvement ?", "<p>Oui, si la vente a été conclue avant et qu’une personne de confiance nous ouvre. Le paiement et le reçu sont alors adressés au vendeur.</p>"),
    ]
    return service_page("/brocanteur-a-domicile-paris", "Brocanteur à domicile", None,
        "Brocanteur à domicile à Paris : achat d’objets anciens",
        "Brocanteur qui achète à domicile à Paris et en petite couronne : meubles, objets anciens, vaisselle, bibelots, collections. Déplacement gratuit, offre écrite.",
        "Brocanteur à domicile à Paris", "Nous venons chez vous pour acheter meubles, objets anciens, vaisselle, luminaires et collections. Déplacement gratuit, offre écrite, paiement par virement ou chèque.",
        "marche", ("Étal d’objets anciens", "De la brocante à l’antiquité : un seul acheteur pour tout voir."),
        sections, faq, R("achat", "estim", "appart", "rachat"))


OBJETS = [
    ("tableaux", "tableaux", "Tableaux, dessins et gravures", "Huiles sur toile ou sur panneau, aquarelles, pastels, dessins, gravures et lithographies signées, cadres anciens dorés.", "Signature, cachets d’atelier ou de vente au dos, étiquettes de galerie, état de la toile, cadre d’origine."),
    ("argenterie", "montres", "Argenterie, bijoux et montres", "Ménagères, couverts, plats, timbales, objets de vitrine en argent massif ; bijoux anciens ; montres à gousset et montres-bracelets de collection.", "Poinçons : tête de Minerve pour l’argent depuis 1838, tête d’aigle pour l’or 18 carats ; poids ; signature du maître orfèvre ou de l’horloger. Paiement par virement ou chèque uniquement."),
    ("horlogerie", "horloges", "Pendules et horlogerie", "Pendules de cheminée en bronze doré ou en marbre, cartels, régulateurs, horloges de parquet, baromètres.", "Mouvement signé, cadran émaillé intact, dorure au mercure, présence du balancier, de la clé et de la cloche."),
    ("porcelaine", "vase", "Porcelaine, faïence et verrerie", "Sèvres, porcelaine de Paris, Limoges, Meissen, Chine et Japon, faïences de Gien, Quimper, Moustiers ; cristal de Baccarat, verrerie Art nouveau.", "Marques sous la pièce, finesse du décor peint, égrenures, fêles et restaurations visibles en lumière rasante."),
    ("luminaires", "lustre", "Luminaires et miroirs", "Lustres à pampilles, appliques, lampes bouillotte, lampadaires design, miroirs dorés, trumeaux, glaces à parecloses.", "Bronze ou laiton, cristaux taillés, tain ancien, dorure à la feuille, électrification d’origine ou refaite."),
    ("sculptures", "salon_tableaux", "Sculptures et bronzes", "Bronzes d’édition, sujets en marbre ou en terre cuite, régule, ivoire ancien sous conditions réglementaires.", "Signature du sculpteur, cachet de fondeur, numéro de tirage, qualité de la ciselure et de la patine."),
    ("livres", "bibliotheque", "Livres anciens et bibliothèques", "Éditions originales, livres illustrés, reliures en cuir, ouvrages scientifiques, bibliothèques entières.", "Date et édition, état des reliures, rousseurs, ex-libris, envois d’auteur, complétude des séries."),
    ("collections", "bijoux", "Collections", "Timbres, monnaies, cartes postales, jouets anciens, soldats de plomb, appareils photo, stylos, objets de vitrine.", "Rareté, état de conservation, complétude, présence des boîtes et documents d’origine."),
    ("instruments", "cadres", "Instruments de musique", "Violons, violoncelles, archets, instruments à vent anciens, pianos de marque selon modèle.", "Étiquette du luthier, qualité du bois, état de la table, archet signé."),
    ("design", "design_chaise", "Mobilier et objets design", "Mobilier des années 1950 à 1970, luminaires d’éditeurs, céramiques et objets de décoration du XXe siècle.", "Éditeur et étiquettes, matériaux d’origine, état des assises et des piètements."),
    ("luxe", "montres", "Mode et accessoires de luxe", "Sacs, foulards, bagages et accessoires de grandes maisons, selon état.", "Numéros de série, état du cuir et des coutures, boîte et documents."),
]


def p_objets():
    blocs = []
    for anchor, key, titre, quoi, indices in OBJETS:
        blocs.append(f'''<div class="cas" id="{anchor}" style="grid-template-columns:220px 1fr;align-items:start;scroll-margin-top:100px">
<figure class="photo-simple" style="aspect-ratio:1">{img(key, (1, 1), "220px", widths=(240, 440))}</figure>
<div><h3>{titre}</h3><p>{quoi}</p><p style="margin-top:.6rem"><strong style="color:var(--encre)">Ce que nous regardons :</strong> {indices}</p></div></div>''')
    sections = f'''
<section class="section" style="padding-top:0"><div class="container">
<div class="section-head"><h2>Les familles d’objets que nous rachetons</h2><p>Les <a href="/rachat-meubles-anciens">meubles anciens</a> ont leur propre page. Voici les autres catégories, avec les indices qui déterminent leur valeur.</p></div>
<div class="balance">{"".join(blocs)}</div>
<p class="small muted" style="margin-top:1.5rem">Certains matériaux, comme l’ivoire, l’écaille de tortue ou certaines essences de bois, sont soumis à des règles de commerce spécifiques. Nous vérifions leur conformité avant tout achat.</p>
</div></section>
'''
    faq = [
        ("Achetez-vous les objets en argent métal ou plaqué ?", "<p>Le métal argenté se revend moins bien que l’argent massif, mais certaines pièces signées par de grandes maisons d’orfèvrerie restent recherchées. Le poinçon permet de faire la différence en quelques secondes.</p>"),
        ("Comment savoir si mon tableau a de la valeur ?", "<p>Envoyez une photo de face, une du dos (châssis, étiquettes, cachets) et un gros plan de la signature. Nous vous disons si l’œuvre relève d’un rachat direct ou d’une vente aux enchères spécialisée.</p>"),
        ("Achetez-vous les pièces de monnaie et l’or ?", "<p>Nous achetons les monnaies de collection. Pour l’or de placement (lingots, pièces courantes), un comptoir spécialisé est souvent mieux placé ; nous vous le disons si c’est le cas.</p>"),
    ]
    return service_page("/objets-achetes", "Objets que nous achetons", None,
        "Objets anciens rachetés : tableaux, argenterie, pendules",
        "Tableaux, argenterie, bijoux, montres, pendules, porcelaine, luminaires, bronzes, livres anciens, collections et design : ce que nous rachetons et pourquoi.",
        "Objets anciens que nous achetons", "Tableaux, argenterie, pendules, porcelaine, luminaires, sculptures, livres, collections et design : pour chaque famille, les indices que nous examinons pour fixer un prix.",
        "horloges", ("Pendules et objets de vitrine", "Mouvement, cadran, dorure : ce qui fait la valeur d’une pendule."),
        sections, faq, R("achat", "estim", "meubles", "g_fisc"))


def p_succession():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Débarras après décès : une méthode en trois temps</h2>
<h3>1. Inventorier avant de décider</h3>
<p>Nous parcourons le logement avec la famille, ou avec la personne qu’elle désigne, et dressons un inventaire estimatif des objets de valeur. Ce document aide à préparer le partage entre héritiers et à échanger avec le notaire, sans rien déplacer.</p>
<h3>2. Mettre de côté ce qui ne se vend pas</h3>
<p>Photos, correspondances, papiers administratifs, bijoux de famille, objets de souvenir : tout ce qui est retrouvé au cours du tri est réuni et remis aux héritiers. Vous nous indiquez à l’avance ce que chacun souhaite garder.</p>
<h3>3. Racheter, donner, évacuer</h3>
<p>Nous rachetons ce qui a une valeur marchande, ce qui vient en déduction du coût du débarras. Le mobilier utilisable est proposé à des associations, le reste trié et évacué en déchetterie. Le logement est rendu vide et balayé, prêt pour la vente, la restitution au bailleur ou les travaux.</p>
<div class="encart" style="margin-top:2rem"><h4>{ico("scale")}Le point juridique à connaître avant de vider</h4>
<p>En droit français, un héritier qui vend ou donne des biens du défunt peut être considéré comme ayant accepté la succession purement et simplement, avec les dettes éventuelles (articles 782 et 783 du Code civil). Seuls les actes conservatoires et d’administration provisoire, listés à l’article 784, n’emportent pas acceptation. Si la succession risque d’être déficitaire, consultez le notaire avant toute vente : nous pouvons réaliser l’inventaire immédiatement et intervenir une fois l’option des héritiers clarifiée.</p></div>
<h2>Les situations que nous prenons en charge</h2>
<ul>
<li>Appartement familial à vider avant la vente ou la mise en location</li>
<li>Logement locatif à restituer au bailleur avant la fin du préavis</li>
<li>Chambre en EHPAD ou en résidence à libérer rapidement</li>
<li>Héritiers éloignés de Paris : intervention en leur absence, avec compte rendu et photos</li>
<li>Maison de famille avec cave, grenier et dépendances</li>
</ul>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("chambre", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>Chaque pièce est traitée selon les consignes de la famille.</figcaption></figure>
</div></section>
<section class="section section--tint"><div class="container"><div class="section-head"><h2>Les étapes d’un débarras de succession</h2></div>{ETAPES_DEBARRAS}</div></section>
<section class="section"><div class="container split split--top"><div><h2>Ce que le rachat change au coût</h2><p class="muted" style="font-size:var(--step-1);line-height:1.5">Dans une succession, le mobilier et les objets ont souvent assez de valeur pour couvrir une partie ou la totalité du débarras.</p><p><a href="/debarras-avec-rachat">Comprendre le calcul</a></p></div>{balance_html()}</div></section>
'''
    faq = [
        ("Pouvez-vous intervenir si les héritiers ne sont pas à Paris ?", "<p>Oui. Après une visite (avec un proche, le notaire ou le gardien), nous réalisons l’intervention en votre absence et vous adressons un compte rendu avec photos, la liste des objets rachetés et ceux mis de côté.</p>"),
        ("Tous les héritiers doivent-ils être d’accord ?", "<p>Oui, la vente de biens d’une succession nécessite l’accord des héritiers, ou d’un mandataire qu’ils ont désigné. Nous demandons une confirmation écrite avant tout rachat.</p>"),
        ("Que faites-vous des papiers et des photos retrouvés ?", "<p>Ils sont systématiquement mis de côté et remis à la famille, comme les bijoux, les clés, les documents bancaires ou les objets personnels.</p>"),
        ("Fournissez-vous un inventaire pour le notaire ?", "<p>Nous établissons un inventaire estimatif détaillé. S’il faut un inventaire officiel (par exemple pour une acceptation à concurrence de l’actif net), il est dressé par un commissaire de justice, un notaire ou un commissaire-priseur.</p>"),
    ]
    return service_page("/debarras-succession", "Débarras de succession", None,
        "Débarras de succession et après décès à Paris, avec rachat",
        "Débarras de succession et après décès à Paris : inventaire, rachat des meubles et objets de valeur, souvenirs remis à la famille, logement rendu vide et propre.",
        "Débarras de succession à Paris", "Inventaire avant toute décision, souvenirs et papiers remis à la famille, rachat des objets de valeur déduit du coût, logement rendu vide et balayé.",
        "chambre", ("Chambre et mobilier d’une maison de famille", "Rien n’est déplacé avant l’accord des héritiers."),
        sections, faq, R("rachat", "appart", "maison", "g_succ"),
        ("Une succession à régler à Paris ?", "Commencez par une visite d’inventaire, gratuite et sans engagement. Nous vous aidons à décider, puis nous vidons le logement à votre rythme."))


def p_appart():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Vider un appartement parisien : les vraies contraintes</h2>
<p>À Paris, la difficulté d’un débarras tient moins au volume qu’aux accès : ascenseur de trois personnes, escalier de service, cinquième étage sans ascenseur, cour pavée, stationnement interdit devant l’immeuble. Nous repérons tout cela lors de la visite, pour un devis qui ne bouge pas le jour de l’intervention.</p>
<ul>
<li><strong>Parties communes protégées</strong> : couvertures, cartons de protection, coordination avec le gardien ou le syndic.</li>
<li><strong>Stationnement</strong> : véhicule adapté à la rue, demande d’emplacement si nécessaire.</li>
<li><strong>Cave et chambre de service</strong> traitées dans la même intervention.</li>
<li><strong>Démontage</strong> des meubles et des éléments fixés si vous le souhaitez.</li>
</ul>
<h2>Pourquoi faire appel à un antiquaire pour un débarras</h2>
<p>Une entreprise de débarras classique facture au volume et évacue l’essentiel. Un antiquaire-brocanteur repère ce qui a de la valeur, du tableau oublié au service en argent rangé au fond d’un placard, et le rachète. Le prix du débarras en est réduit d’autant, parfois jusqu’à zéro.</p>
<h2>Pour qui</h2>
<p>Héritiers, propriétaires qui vendent, locataires en fin de bail, bailleurs après le départ d’un locataire, agences immobilières et notaires qui nous confient des logements à libérer.</p>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("cartons", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>Un logement rendu vide, prêt pour l’état des lieux ou la vente.</figcaption></figure>
</div></section>
<section class="section section--tint"><div class="container"><div class="section-head"><h2>Les étapes</h2></div>{ETAPES_DEBARRAS}</div></section>
'''
    faq = [
        ("Combien coûte le débarras d’un appartement à Paris ?", "<p>Le prix dépend du volume, de l’étage, de l’ascenseur, de la distance de portage et de la part d’objets revendables. Nous établissons un devis après visite, en déduisant la valeur de ce que nous rachetons. Notre <a href=\"/guides/prix-debarras-paris\">guide sur le prix d’un débarras</a> détaille ces critères.</p>"),
        ("En combien de temps l’appartement est-il vidé ?", "<p>Un studio ou un deux-pièces se vide généralement en une journée ; un grand appartement avec cave peut demander deux ou trois jours. Nous nous calons sur votre échéance.</p>"),
        ("Le logement est-il nettoyé après ?", "<p>Il est rendu vide et balayé. Un nettoyage approfondi peut être organisé en complément si l’état des lieux l’exige.</p>"),
    ]
    return service_page("/debarras-appartement-paris", "Débarras d’appartement", None,
        "Débarras d’appartement à Paris : vidage avec rachat des objets",
        "Débarras d’appartement à Paris, tous étages : tri, rachat des meubles et objets de valeur, évacuation, cave et chambre de service comprises. Devis après visite.",
        "Débarras d’appartement à Paris", "Tous étages, avec ou sans ascenseur : nous vidons l’appartement, la cave et la chambre de service, et nous rachetons ce qui a de la valeur pour réduire la facture.",
        "cartons", ("Appartement en cours de débarras", "Accès, étage, stationnement : vérifiés avant le devis."),
        sections, faq, R("rachat", "succ", "cave", "g_prix"))


def p_maison():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Une maison se vide autrement qu’un appartement</h2>
<p>Plus d’espace, plus d’années d’accumulation : sous-sol, garage, grenier, abri de jardin, chambres d’amis. Une maison de famille réserve souvent les meilleures découvertes, et le plus gros volume. Nous traitons chaque espace séparément dans le devis, pour que vous puissiez décider pièce par pièce.</p>
<h2>Ce que comprend un débarras de maison</h2>
<ul>
<li>Visite complète et inventaire des objets de valeur</li>
<li>Rachat du mobilier ancien, des objets d’art, de l’outillage de qualité et des collections</li>
<li>Tri des souvenirs et des papiers, remis à la famille</li>
<li>Dons aux associations, recyclage des métaux, du bois et des encombrants</li>
<li>Évacuation complète et maison rendue balayée</li>
</ul>
<h2>Petite couronne et Île-de-France</h2>
<p>Nous intervenons dans les <a href="/antiquaire-hauts-de-seine">Hauts-de-Seine</a>, la <a href="/antiquaire-seine-saint-denis">Seine-Saint-Denis</a> et le <a href="/antiquaire-val-de-marne">Val-de-Marne</a>, et au-delà pour les maisons dont le contenu le justifie.</p>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("salle_lustre", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>Salle à manger d’une maison de famille.</figcaption></figure>
</div></section>
<section class="section section--tint"><div class="container"><div class="section-head"><h2>Les étapes</h2></div>{ETAPES_DEBARRAS}</div></section>
'''
    faq = [
        ("Videz-vous aussi le garage et l’abri de jardin ?", "<p>Oui, ainsi que le sous-sol, le grenier et les dépendances. Chaque espace est chiffré séparément.</p>"),
        ("La maison est en vente : pouvez-vous intervenir avant la signature ?", "<p>Oui, nous planifions l’intervention en fonction de la date de signature de l’acte authentique, pour que la maison soit libre le jour prévu.</p>"),
        ("Rachetez-vous l’outillage et le mobilier de jardin ?", "<p>L’outillage de qualité, les établis anciens et certains mobiliers de jardin en fonte ou en fer forgé ont une valeur ; nous les rachetons.</p>"),
    ]
    return service_page("/debarras-maison", "Débarras de maison", None,
        "Débarras de maison en Île-de-France, avec rachat des meubles",
        "Débarras de maison à Paris et petite couronne : pièces, cave, grenier, garage. Rachat des meubles anciens et objets de valeur déduit du devis. Visite gratuite.",
        "Débarras de maison", "Pièces de vie, sous-sol, grenier, garage et dépendances : nous vidons la maison entière et rachetons ce qui a de la valeur, déduit directement du devis.",
        "salle_lustre", ("Maison de famille", "Chaque espace est chiffré à part."),
        sections, faq, R("succ", "cave", "rachat", "g_prix"))


def p_cave():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Caves, greniers, garages, box</h2>
<p>Ce sont les espaces où les objets s’accumulent depuis des décennies, et où se cachent souvent les surprises : un tableau roulé, une malle de vaisselle, des livres, un meuble démonté, des affiches anciennes. Nous trions sur place avant toute évacuation.</p>
<h2>Accès difficiles : nous connaissons</h2>
<p>Caves voûtées accessibles par un escalier raide, greniers sous les toits sans éclairage, box en sous-sol de résidence : l’équipe est équipée en conséquence (éclairage, diables, sangles, protections). Si la copropriété exige un créneau ou une autorisation, nous nous en occupons avec le gardien.</p>
<h2>Cave seule ou avec le reste du logement</h2>
<p>Nous intervenons pour une cave isolée, par exemple avant la vente d’un appartement ou à la demande d’un syndic, comme dans le cadre d’un débarras complet.</p>
</div>
<figure class="photo-simple" style="aspect-ratio:4/5;position:sticky;top:100px">{img("cartons_table", (4, 5), "(max-width: 900px) 100vw, 45vw")}<figcaption>Tout est trié avant d’être évacué.</figcaption></figure>
</div></section>
'''
    faq = [
        ("Pouvez-vous vider une cave sans le reste de l’appartement ?", "<p>Oui, c’est une demande fréquente avant une vente ou des travaux dans les parties communes.</p>"),
        ("Que faites-vous des produits dangereux (peintures, solvants) ?", "<p>Ils sont séparés et déposés dans les filières adaptées. Signalez-les-nous lors de la visite.</p>"),
        ("Le grenier n’a pas d’éclairage, est-ce un problème ?", "<p>Non, nous venons équipés. Il faut simplement un accès sécurisé (trappe, escalier escamotable en bon état).</p>"),
    ]
    return service_page("/debarras-cave-grenier", "Débarras de cave et grenier", None,
        "Débarras de cave, grenier et garage à Paris",
        "Débarras de cave, grenier, garage et box à Paris : tri sur place, rachat des objets anciens retrouvés, évacuation complète. Accès difficiles pris en charge.",
        "Débarras de cave, grenier et garage", "Caves voûtées, greniers sous les toits, garages et box : nous trions sur place, rachetons les objets anciens retrouvés et évacuons le reste.",
        "cartons_table", ("Objets sortis d’un grenier", "Le tri vient toujours avant l’évacuation."),
        sections, faq, R("appart", "maison", "rachat", "g_prix"))


def p_rachat():
    sections = f'''
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Le principe, en une phrase</h2>
<p>Nous chiffrons d’un côté le coût du débarras (main-d’œuvre, véhicule, évacuation), de l’autre la valeur des objets que nous rachetons, et nous faisons la différence. Les deux montants figurent sur le même devis écrit.</p>
<h2>Trois issues possibles</h2>
<p>Si les objets valent plus que le débarras, nous vous versons la différence. S’ils valent autant, le débarras ne vous coûte rien. S’ils valent moins, vous ne payez que le solde. C’est le seul cas où l’on peut parler honnêtement de « débarras gratuit » : quand la valeur reprise le couvre réellement.</p>
<h2>Ce qui fait la valeur d’un contenu</h2>
<ul>
<li>Le mobilier ancien et design de qualité, les tableaux, l’argenterie, les pendules</li>
<li>Les collections et les bibliothèques</li>
<li>La vaisselle et la verrerie de marque, en services complets</li>
<li>Les luminaires, miroirs et objets de décoration anciens</li>
</ul>
<h2>Ce qui fait le coût d’un débarras</h2>
<ul>
<li>Le volume à évacuer et le nombre de personnes nécessaires</li>
<li>L’étage, l’ascenseur, la distance de portage, le stationnement</li>
<li>Les frais de déchetterie et de traitement des encombrants</li>
<li>Le démontage éventuel et le nettoyage final</li>
</ul>
</div>
<div style="position:sticky;top:100px">{balance_html()}</div>
</div></section>
<section class="section section--tint"><div class="container"><div class="section-head"><h2>Les étapes</h2></div>{ETAPES_DEBARRAS}</div></section>
'''
    faq = [
        ("Le débarras gratuit existe-t-il vraiment ?", "<p>Oui, mais seulement lorsque la valeur des objets rachetés couvre le coût réel de l’intervention. Méfiez-vous des offres « gratuites » annoncées sans visite : elles se rattrapent souvent sur des frais annexes ou sur le prix des objets.</p>"),
        ("Puis-je garder certains objets ?", "<p>Bien sûr. Vous indiquez ce que vous conservez ; le devis est établi sur le reste.</p>"),
        ("Et si je refuse de vendre un objet que vous voulez racheter ?", "<p>Vous gardez l’objet ; il est simplement retiré du calcul et le solde est ajusté.</p>"),
    ]
    return service_page("/debarras-avec-rachat", "Débarras avec rachat", None,
        "Débarras avec rachat à Paris : la valeur des objets déduite",
        "Débarras avec rachat à Paris : la valeur de vos meubles et objets anciens est déduite du coût, parfois jusqu’à la gratuité. Devis écrit après visite gratuite.",
        "Débarras avec rachat des objets", "La valeur de ce que nous rachetons est déduite du coût du débarras. Selon le contenu, vous payez moins, rien du tout, ou c’est nous qui vous payons la différence.",
        "salon_or", ("Contenu d’un appartement ancien", "Mobilier, luminaires, tableaux : autant de valeur déduite."),
        sections, faq, R("succ", "appart", "maison", "g_prix"))


def build_all_services():
    return [p_achat(), p_meubles(), p_estimation(), p_domicile(), p_objets(),
            p_succession(), p_appart(), p_maison(), p_cave(), p_rachat()]
