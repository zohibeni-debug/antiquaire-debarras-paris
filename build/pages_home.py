from core import *

LOTS = [
    ("commode", "Meubles anciens", "Commodes, armoires, secrétaires, bureaux plats — XVIIIe au XIXe siècle",
     "<b>On regarde :</b> l’estampille de l’ébéniste, le marbre d’origine, les bronzes, l’état des placages et des serrures.", "/rachat-meubles-anciens", True),
    ("tableaux", "Tableaux et dessins", "Huiles, aquarelles, gravures, cadres anciens",
     "<b>On regarde :</b> la signature, la toile et le châssis, les cachets et étiquettes au dos, le cadre d’époque.", "/objets-achetes#tableaux", False),
    ("horloges", "Pendules et horlogerie", "Pendules de cheminée, cartels, régulateurs",
     "<b>On regarde :</b> le mouvement signé, le cadran émaillé, la dorure des bronzes, la présence du balancier et de la clé.", "/objets-achetes#horlogerie", False),
    ("tasses", "Porcelaine et faïence", "Sèvres, Paris, Limoges, Gien, Chine",
     "<b>On regarde :</b> les marques de manufacture, les égrenures et restaurations, la qualité du décor peint.", "/objets-achetes#porcelaine", False),
    ("montres", "Montres, bijoux, argenterie", "Montres à gousset, ménagères, orfèvrerie",
     "<b>On regarde :</b> les poinçons (tête de Minerve pour l’argent, tête d’aigle pour l’or), le poids, la signature.", "/objets-achetes#argenterie", False),
    ("lustre", "Luminaires et miroirs", "Lustres, appliques, glaces dorées, trumeaux",
     "<b>On regarde :</b> le bronze ou le laiton, les cristaux taillés, le tain ancien, la dorure à la feuille.", "/objets-achetes#luminaires", False),
    ("bibliotheque", "Livres anciens", "Bibliothèques entières, éditions originales, reliures",
     "<b>On regarde :</b> l’édition, la reliure, l’état des coiffes et des mors, les ex-libris et envois.", "/objets-achetes#livres", False),
    ("bijoux", "Collections", "Timbres, monnaies, cartes postales, jouets anciens",
     "<b>On regarde :</b> la rareté, l’état de conservation, la complétude des séries, les boîtes et documents d’origine.", "/objets-achetes#collections", False),
    ("design_chaise", "Mobilier design 1950–1970", "Sièges, enfilades, luminaires d’éditeurs",
     "<b>On regarde :</b> l’éditeur et ses étiquettes, les matériaux d’origine (teck, palissandre, laiton), l’état des assises.", "/objets-achetes#design", False),
]


def lots_html(lots=LOTS):
    out = ['<div class="catalogue">']
    for key, titre, epoque, regarde, url, grand in lots:
        cls = "lot lot--grand" if grand else "lot"
        ratio = (16, 11) if grand else (4, 3)
        sizes = "(max-width: 1000px) 100vw, 66vw" if grand else "(max-width: 620px) 100vw, (max-width: 1000px) 50vw, 33vw"
        out.append(f'''<figure class="{cls}"><div class="img">{img(key, ratio, sizes)}</div>
<figcaption><h3><a href="{url}" style="color:inherit;text-decoration:none">{titre}</a></h3><span class="epoque">{epoque}</span><p class="regarde">{regarde}</p></figcaption></figure>''')
    out.append("</div>")
    return "".join(out)


def plaques_html():
    from pages_local import ARR
    tiles = []
    for n in range(1, 21):
        q = ARR[n]["quartiers"]
        tiles.append(f'<a class="plaque" href="/antiquaire-paris-{n}"><small>750{n:02d}</small><b>{plaque_label(n)}</b><span>{esc(q[0])}, {esc(q[1])}</span></a>')
    deps = [("/antiquaire-hauts-de-seine", "92", "Hauts-de-Seine", "Neuilly, Boulogne, Saint-Cloud"),
            ("/antiquaire-seine-saint-denis", "93", "Seine-Saint-Denis", "Saint-Ouen, Montreuil, Le Raincy"),
            ("/antiquaire-val-de-marne", "94", "Val-de-Marne", "Vincennes, Saint-Maur, Nogent")]
    dep = "".join(f'<a class="plaque plaque--large" href="{u}"><small>{c}</small><b><span class="u">{esc(n)}</span></b><span>{esc(v)}</span></a>' for u, c, n, v in deps)
    return f'<div class="plaques plaques--20">{"".join(tiles)}</div><div class="plaques-dep">{dep}</div>'


def balance_html():
    cas = [
        ("Les objets couvrent le débarras", "Mobilier ancien, tableaux ou argenterie en nombre : leur valeur de reprise égale ou dépasse le coût de l’intervention.",
         92, 60, "Débarras sans frais, et nous vous versons la différence s’il y en a une."),
        ("Les objets couvrent une partie", "Quelques pièces intéressantes au milieu d’un mobilier courant.",
         38, 70, "La valeur reprise est déduite : vous ne payez que le solde."),
        ("Peu d’objets revendables", "Mobilier récent ou abîmé, cave encombrée, logement à vider vite.",
         8, 64, "Devis classique, au volume et selon l’accès, sans surprise."),
    ]
    out = ['<div class="balance">']
    for t, p, v, c, verdict in cas:
        out.append(f'''<div class="cas"><div><h3>{t}</h3><p>{p}</p></div>
<div class="barres" aria-hidden="true"><div class="barre"><span>Valeur des objets repris</span><i class="val" style="width:{v}%"></i></div>
<div class="barre"><span>Coût du débarras</span><i class="cout" style="width:{c}%"></i></div></div>
<p class="verdict">{verdict}</p></div>''')
    out.append("</div>")
    return "".join(out)


FAQ_HOME = [
    ("L’estimation est-elle vraiment gratuite ?",
     "<p>Oui. L’estimation sur photos comme la visite à domicile dans Paris et la petite couronne sont gratuites et ne vous engagent à rien. Vous recevez une proposition chiffrée, objet par objet ou pour l’ensemble, et vous restez libre de la refuser.</p>"),
    ("Un débarras peut-il être gratuit ?",
     "<p>Il peut l’être lorsque la valeur des meubles et objets que nous rachetons couvre le coût de l’intervention (main-d’œuvre, camion, évacuation en déchetterie). Si la valeur dépasse ce coût, nous vous versons la différence. Si elle ne le couvre qu’en partie, elle est déduite du devis. Nous le précisons par écrit après la visite.</p>"),
    ("Comment êtes-vous payé, et comment payez-vous ?",
     "<p>Nous réglons nos achats par virement ou par chèque, au moment de l’enlèvement, avec un reçu qui détaille chaque objet. Pour les bijoux, l’argenterie et tout objet en métal précieux, la loi interdit le paiement en espèces (article L112-6 du Code monétaire et financier).</p>"),
    ("Pourquoi demandez-vous une pièce d’identité au vendeur ?",
     "<p>Tout professionnel qui rachète des objets d’occasion doit tenir un registre d’objets mobiliers, coté et paraphé, où figurent la description de chaque objet et l’identité de son vendeur (article 321-7 du Code pénal). C’est une protection pour vous comme pour nous : elle garantit la traçabilité de chaque transaction.</p>"),
    ("Dois-je payer un impôt sur la vente d’objets anciens ?",
     "<p>Pour les bijoux, objets d’art, de collection ou d’antiquité, une taxe forfaitaire de 6,5 % s’applique uniquement si le prix de vente dépasse 5 000 € par objet ou par ensemble. Pour les métaux précieux (or, argent, platine), elle est de 11,5 % dès le premier euro. Lorsqu’elle est due, c’est le professionnel acheteur qui la déclare et la reverse. Le détail est expliqué dans notre <a href=\"/guides/fiscalite-vente-objets-anciens\">guide sur la fiscalité</a>.</p>"),
    ("Intervenez-vous rapidement en cas de fin de bail ou de vente du logement ?",
     "<p>Oui. Indiquez-nous la date à laquelle les clés doivent être rendues : nous organisons la visite, le tri et l’enlèvement en fonction de cette échéance, y compris quand le logement est déjà en vente ou que le syndic doit être prévenu pour l’ascenseur.</p>"),
]


def build_home():
    body = f'''
<section class="hero"><div class="container hero-grid">
<div>
<h1>Antiquaire à Paris<span class="l2">Achat de meubles anciens, estimation gratuite et débarras de successions</span></h1>
<p class="lead">Nous achetons le mobilier ancien, les tableaux, l’argenterie et les objets d’art, chez vous ou sur photos. Et quand il faut vider tout l’appartement, la valeur de ce que nous reprenons vient en déduction du débarras.</p>
<div class="btn-row">{btn_estimation()}{btn_tel()}</div>
{preuves_html()}
</div>
<figure class="cadre drape"><div class="photo photo--hero" style="aspect-ratio:4/5">{img("salon", (4, 5), "(max-width: 900px) 100vw, 44vw", eager=True)}</div>
<figcaption class="cartel-legende"><b>Salon parisien, mobilier et luminaires du XIXe siècle</b><span>Le type d’intérieur que nous estimons pièce par pièce, du lustre au dernier tiroir.</span></figcaption></figure>
</div></section>

<section class="section" style="padding-top:0"><div class="container">
<div class="section-head"><h2>Vendre, faire estimer ou vider un lieu</h2><p>Trois demandes différentes, souvent liées. Commencez par celle qui vous amène.</p></div>
<div class="index-demandes">
<div class="demande"><div><span class="verbe">Vendre</span><h3>Vous avez des objets anciens à vendre</h3></div>
<p>Une commode de famille, une pendule, un service en argent, une bibliothèque entière : nous rachetons à domicile, à un prix ferme annoncé avant l’enlèvement, payé par virement ou chèque.</p>
<ul><li><a href="/achat-antiquites-paris">Achat d’antiquités à Paris</a></li><li><a href="/rachat-meubles-anciens">Rachat de meubles anciens</a></li><li><a href="/brocanteur-a-domicile-paris">Brocanteur à domicile</a></li></ul></div>
<div class="demande"><div><span class="verbe">Estimer</span><h3>Vous voulez connaître la valeur d’un objet</h3></div>
<p>Envoyez des photos de l’ensemble et des détails : signature, poinçons, étiquettes, dimensions. Vous recevez un avis de valeur argumenté, puis une visite si l’objet le justifie.</p>
<ul><li><a href="/estimation-antiquites-gratuite">Estimation gratuite</a></li><li><a href="/objets-achetes">Objets que nous achetons</a></li><li><a href="/guides/reconnaitre-un-meuble-ancien">Reconnaître un meuble ancien</a></li></ul></div>
<div class="demande"><div><span class="verbe">Vider</span><h3>Vous devez vider un appartement ou une maison</h3></div>
<p>Succession, vente, fin de bail, déménagement : tri, mise de côté des souvenirs et des papiers, rachat de ce qui a de la valeur, évacuation du reste et logement rendu balayé.</p>
<ul><li><a href="/debarras-succession">Débarras de succession</a></li><li><a href="/debarras-appartement-paris">Débarras d’appartement</a></li><li><a href="/debarras-avec-rachat">Débarras avec rachat</a></li></ul></div>
</div></div></section>

<section class="section section--tint"><div class="container">
<div class="section-head"><h2>Ce que nous achetons</h2><p>Chaque famille d’objets a ses indices de valeur. Voici ceux que nous examinons en premier lors d’une estimation.</p></div>
{lots_html()}
<p style="margin-top:2rem"><a href="/objets-achetes">Voir la liste complète des objets que nous achetons</a></p>
</div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>Comment se déroule un rachat</h2><p>De la première photo au paiement, quatre étapes. Vous pouvez vous arrêter à chacune.</p></div>
<ol class="etapes">
<li><h3>Vous envoyez des photos</h3><p>Une vue d’ensemble, les détails (signature, poinçons, étiquettes, marques sous les pièces) et les dimensions, via le formulaire ou par message.</p></li>
<li><h3>Nous venons voir sur place</h3><p>Si les objets le justifient, rendez-vous à votre domicile dans Paris ou la petite couronne. Déplacement et estimation gratuits.</p></li>
<li><h3>Vous recevez une offre écrite</h3><p>Prix par objet ou pour l’ensemble, sans frais cachés. Vous pouvez accepter tout, une partie, ou rien.</p></li>
<li><h3>Paiement et enlèvement</h3><p>Paiement par virement ou chèque, reçu détaillé, inscription au registre d’objets mobiliers. Nous emballons et emportons.</p></li>
</ol></div></section>

<section class="section section--dark"><div class="container split">
<figure class="photo-simple" style="aspect-ratio:4/5">{img("chambre", (4, 5), "(max-width: 900px) 100vw, 45vw")}</figure>
<div>
<h2>Une succession à régler, sans rien précipiter</h2>
<p>Vider le logement d’un parent est rarement une simple affaire de mobilier. Nous travaillons pièce par pièce, avec la famille ou en son absence, en suivant vos consignes.</p>
<ul class="liste-check">
<li>{ico("check")}<span>Souvenirs, photos et papiers personnels retrouvés mis de côté et remis aux héritiers</span></li>
<li>{ico("check")}<span>Inventaire estimatif des objets de valeur, utile au notaire et au partage</span></li>
<li>{ico("check")}<span>Rachat des meubles et objets intéressants, déduit du coût du débarras</span></li>
<li>{ico("check")}<span>Dons aux associations et dépôt en déchetterie pour le reste, logement rendu balayé</span></li>
</ul>
<div class="encart"><h3>{ico("scale")}Avant de vendre ou de vider : parlez-en au notaire</h3><p>Disposer des biens d’un défunt peut valoir acceptation de la succession, avec ses dettes éventuelles (articles 782 et 784 du Code civil). Nous pouvons établir l’inventaire tout de suite et n’intervenir qu’une fois la décision des héritiers prise.</p></div>
<p style="margin-top:1.6rem"><a href="/debarras-succession">Notre méthode pour les débarras de succession</a></p>
</div></div></section>

<section class="section"><div class="container split split--top">
<div><h2>Débarras avec rachat : la valeur des objets réduit la facture</h2>
<p class="muted" style="font-size:var(--step-1);line-height:1.5">Un débarras a un coût : main-d’œuvre, camion, évacuation. Un antiquaire qui vide lui-même le logement peut le compenser avec ce qu’il rachète. Trois situations reviennent le plus souvent.</p>
<p><a href="/debarras-avec-rachat">Comprendre le calcul en détail</a></p></div>
{balance_html()}
</div></section>

<section class="section section--tint"><div class="container">
<div class="section-head"><h2>Antiquaire dans les 20 arrondissements</h2><p>Nous nous déplaçons partout dans Paris et dans les trois départements de la petite couronne. Chaque arrondissement a ses immeubles, ses accès et ses intérieurs.</p></div>
{plaques_html()}
</div></section>

<section class="section"><div class="container narrow">
{faq_html(FAQ_HOME)}
</div></section>
{cta_band()}
'''
    ld = [faq_ld(FAQ_HOME)]
    return "/", render("/", "Antiquaire Paris : achat, estimation gratuite et débarras",
                  "Antiquaire à Paris et petite couronne : rachat de meubles anciens et d’objets d’art, estimation gratuite sur photos ou à domicile, débarras de succession.",
                  body, ld)
