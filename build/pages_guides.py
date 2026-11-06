from core import *


def guide_page(slug, title, desc, h1, chapo, image, sommaire, contenu, sources, faq=None, related=None):
    path = f"/guides/{slug}"
    items = [("Guides", "/guides"), (h1, None)]
    som = "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in sommaire)
    src = ""
    if sources:
        src = '<div class="sources"><b>Références</b><ul>' + "".join(f"<li>{s}</li>" for s in sources) + "</ul></div>"
    faq_block = faq_html(faq) if faq else ""
    rel = f'<section class="section section--tint"><div class="container">{associes(related)}</div></section>' if related else ""
    body = f'''
<section class="page-hero"><div class="container">{crumbs(items)}
<div class="hero-grid"><div><h1>{h1}</h1><p class="lead">{chapo}</p>
<p class="article-meta">Mis à jour le 6 novembre 2026</p></div>
<figure class="cadre drape"><div class="photo">{img(image, (4, 5), "(max-width: 900px) 100vw, 40vw", eager=True)}</div></figure></div></div></section>
<section class="section" style="padding-top:0"><div class="container layout-article">
<article class="prose">
<nav class="sommaire" aria-label="Sommaire"><b>Sommaire</b><ol>{som}</ol></nav>
{contenu}
{faq_block}
{src}
</article>
<aside class="aside-sticky">
<div class="aside-card"><h3>Faire estimer vos objets</h3><p>Envoyez quelques photos : premier avis de valeur gratuit, sans engagement.</p>{btn_estimation("Envoyer des photos")}</div>
<div class="aside-card"><h3>Besoin d’en parler ?</h3><p>{CFG["hours_text"]}.</p>{btn_tel("btn btn--ghost")}</div>
</aside>
</div></section>
{rel}
{cta_band()}
'''
    ld = [breadcrumb_ld(items, path), {
        "@type": "Article", "headline": h1, "description": desc, "inLanguage": "fr-FR",
        "image": img_url(image, 1200, 800), "datePublished": "2026-11-06", "dateModified": CFG["updated"],
        "mainEntityOfPage": BASE + path, "author": {"@id": BASE + "/#entreprise"}, "publisher": {"@id": BASE + "/#entreprise"}}]
    if faq:
        ld.append(faq_ld(faq))
    return path, render(path, title, desc, body, ld, og_image=image, og_type="article")


SRC_ROM = '<a href="https://bpifrance-creation.fr/activites-reglementees/antiquaire-brocanteur" rel="noopener">Bpifrance Création, fiche réglementaire « Antiquaire-brocanteur »</a> (articles 321-7 et R321-1 à R321-8 du Code pénal)'
SRC_R3211 = '<a href="https://www.legifrance.gouv.fr/codes/id/LEGIARTI000043531943/2021-11-01" rel="noopener">Légifrance, article R321-1 du Code pénal</a> (déclaration préalable et registre)'
SRC_ESP = '<a href="https://bofip.impots.gouv.fr/node/13824" rel="noopener">BOFiP, interdiction de paiement en espèces de certaines créances</a> (article L112-6 du Code monétaire et financier)'


def g_meuble():
    contenu = f'''
<p>Distinguer un meuble d’époque d’un meuble « de style » fabriqué plus tard est la première question d’une estimation. Les deux peuvent porter le même nom (commode Louis XV, fauteuil Louis XVI), mais leur valeur peut varier de un à dix, voire davantage. Voici les indices que nous examinons, du plus visible au plus technique.</p>
<h2 id="styles">Repères de styles et d’époques</h2>
<p>Les dates ci-dessous sont des repères : les styles se chevauchent, et les ateliers de province ont souvent prolongé une mode plusieurs décennies après Paris.</p>
<div class="table-wrap"><table>
<thead><tr><th>Style</th><th>Période indicative</th><th>Signes reconnaissables</th></tr></thead>
<tbody>
<tr><td>Louis XIII</td><td>vers 1610 – 1660</td><td>Bois massif, tournages en chapelet ou en spirale, formes rectilignes et robustes</td></tr>
<tr><td>Louis XIV</td><td>vers 1660 – 1715</td><td>Majesté et symétrie, marqueterie Boulle (écaille et laiton), bronzes</td></tr>
<tr><td>Régence</td><td>vers 1715 – 1730</td><td>Assouplissement des lignes, premiers pieds galbés, coquilles</td></tr>
<tr><td>Louis XV</td><td>vers 1730 – 1760</td><td>Courbes partout : façades galbées, pieds cambrés, rocaille, marqueterie de fleurs</td></tr>
<tr><td>Transition et Louis XVI</td><td>vers 1760 – 1790</td><td>Retour à l’Antique : lignes droites, pieds fuselés et cannelés, rais-de-cœur, perles</td></tr>
<tr><td>Directoire, Consulat, Empire</td><td>vers 1795 – 1815</td><td>Acajou, colonnes, bronzes dorés à motifs antiques et égyptiens, formes architecturées</td></tr>
<tr><td>Restauration, Louis-Philippe</td><td>vers 1815 – 1848</td><td>Bois clairs (Restauration), puis acajou et palissandre, formes plus confortables</td></tr>
<tr><td>Napoléon III</td><td>vers 1850 – 1870</td><td>Éclectisme, bois noirci, marqueterie Boulle revisitée, capitonnage, petits meubles de salon</td></tr>
<tr><td>Art nouveau</td><td>vers 1890 – 1910</td><td>Lignes végétales, motifs floraux sculptés, École de Nancy</td></tr>
<tr><td>Art déco</td><td>vers 1920 – 1939</td><td>Géométrie, bois précieux, laque, galuchat, ivoire et métal</td></tr>
</tbody></table></div>
<h2 id="estampille">L’estampille : la signature de l’ébéniste</h2>
<p>À Paris, les maîtres de la corporation des menuisiers-ébénistes devaient frapper leur nom au fer sur leurs meubles, entre le milieu du XVIIIe siècle et la suppression des corporations en 1791. L’estampille se trouve sur le bâti, souvent sous le marbre, sur un montant arrière ou sous la ceinture d’un siège ; elle est fréquemment accompagnée du poinçon « JME » de la jurande.</p>
<p>Attention : une estampille peut être fausse ou rapportée. Elle doit être cohérente avec le style, la qualité d’exécution et l’usure du meuble. Une estampille seule ne fait pas un meuble d’époque.</p>
<h2 id="assemblages">Assemblages, vis et traces d’outils</h2>
<ul>
<li><strong>Queues d’aronde des tiroirs</strong> : taillées à la main, elles sont irrégulières, peu nombreuses et inégales ; usinées à la machine, elles sont parfaitement régulières.</li>
<li><strong>Chevilles en bois</strong> : les assemblages anciens sont chevillés ; les chevilles dépassent légèrement avec le retrait du bois.</li>
<li><strong>Vis et clous</strong> : vis anciennes à tête irrégulière et fente souvent décentrée, clous forgés à section carrée.</li>
<li><strong>Traces de scie</strong> : des stries droites et parallèles indiquent un sciage manuel ou au cadre ; des stries en arc de cercle, une scie circulaire, généralisée au XIXe siècle.</li>
<li><strong>Revers et intérieurs</strong> : un fond de tiroir ancien est oxydé, patiné, jamais uniformément propre. Un intérieur trop clair doit interroger.</li>
</ul>
<h2 id="materiaux">Bois, placages, marbres et bronzes</h2>
<p>Le bâti des meubles parisiens de qualité est souvent en chêne, plaqué de bois précieux (bois de rose, amarante, satiné, acajou). Les placages anciens sont épais, sciés à la main ; les placages industriels, très fins. Un marbre d’origine est ajusté au meuble, ses moulures sont usées aux angles. Les bronzes dorés au mercure ont une teinte chaude et un ciselé précis ; les bronzes refaits ou vernis sont plus mous et plus jaunes.</p>
<h2 id="usure">Usure et patine : la cohérence avant tout</h2>
<p>Un meuble qui a deux siècles porte une usure logique : bas des pieds frottés, bords de plateau arrondis, poignées polies par les mains, serrures retouchées. Une usure uniforme ou placée à des endroits illogiques signale souvent un vieillissement artificiel.</p>
<h2 id="que-faire">Que faire si vous pensez avoir un meuble d’époque</h2>
<p>Ne le restaurez pas et ne le décapez pas : une intervention maladroite peut faire perdre une part importante de sa valeur. Photographiez-le à la lumière du jour, de face, de profil, de dos, puis les détails : tiroir ouvert, revers, sous le marbre, bronzes, marques. Envoyez-nous ces photos pour une <a href="/estimation-antiquites-gratuite">estimation gratuite</a>.</p>
'''
    faq = [("Un meuble de style a-t-il une valeur ?", "<p>Oui, quand il est de belle facture : certains meubles de style de la fin du XIXe siècle, réalisés par de grandes maisons parisiennes, sont recherchés. Mais leur valeur reste en général inférieure à celle d’un meuble d’époque équivalent.</p>"),
           ("Un meuble restauré perd-il sa valeur ?", "<p>Une restauration soignée et réversible est normale sur un meuble ancien. Ce qui pèse sur la valeur, ce sont les éléments remplacés (marbre, bronzes, placages entiers) et les finitions modernes.</p>")]
    return guide_page("reconnaitre-un-meuble-ancien", "Reconnaître un meuble ancien : styles, estampille, assemblages",
        "Distinguer un meuble d’époque d’un meuble de style : repères de styles, estampille d’ébéniste, assemblages, placages et usure. Le guide d’un antiquaire.",
        "Reconnaître un meuble ancien", "Époque ou style ? Les indices qu’un antiquaire examine pour dater un meuble et en estimer la valeur, du style à l’estampille en passant par les queues d’aronde.",
        "commode", [("styles", "Repères de styles et d’époques"), ("estampille", "L’estampille"), ("assemblages", "Assemblages, vis et traces d’outils"),
                    ("materiaux", "Bois, placages, marbres et bronzes"), ("usure", "Usure et patine"), ("que-faire", "Que faire ensuite")],
        contenu, [], faq, [("/rachat-meubles-anciens", "Rachat de meubles anciens", "Estimation et enlèvement à domicile"),
                           ("/estimation-antiquites-gratuite", "Estimation gratuite", "Sur photos ou à domicile"),
                           ("/guides/antiquaire-ou-commissaire-priseur", "Antiquaire ou commissaire-priseur ?", "Choisir comment vendre")])


def g_fisc():
    contenu = f'''
<p>Vendre une commode de famille, une ménagère en argent ou un tableau hérité n’est pas toujours neutre fiscalement. La règle est pourtant simple une fois les catégories comprises. Ce guide résume ce qui s’applique à un particulier résidant en France qui vend à un professionnel.</p>
<p class="small muted">Ce guide est informatif : il ne remplace pas l’avis d’un notaire ou d’un conseiller fiscal pour votre situation personnelle.</p>
<h2 id="categories">Trois catégories d’objets, trois régimes</h2>
<div class="table-wrap"><table>
<thead><tr><th>Catégorie</th><th>Exemples</th><th>Régime à la vente</th></tr></thead>
<tbody>
<tr><td><strong>Meubles meublants courants</strong></td><td>Mobilier usuel, électroménager, objets d’usage</td><td>Pas d’imposition de la plus-value</td></tr>
<tr><td><strong>Bijoux, objets d’art, de collection ou d’antiquité</strong></td><td>Tableaux, sculptures originales, montres, bijoux, meubles et objets de plus de cent ans, pièces de collection</td><td>Exonération jusqu’à 5 000 € par objet ou ensemble ; au-delà, taxe forfaitaire de 6,5 % du prix (ou régime des plus-values sur option)</td></tr>
<tr><td><strong>Métaux précieux</strong></td><td>Or, argent, platine bruts ou en lingots, pièces d’or postérieures à 1800</td><td>Taxe forfaitaire de 11,5 % du prix dès le premier euro (ou régime des plus-values sur option)</td></tr>
</tbody></table></div>
<h2 id="taxe">La taxe forfaitaire de 6,5 %</h2>
<p>Pour les bijoux et les objets d’art, de collection ou d’antiquité, la taxe est de 6 % du prix de vente, plus 0,5 % de CRDS, soit 6,5 %. Elle ne s’applique que si le prix dépasse 5 000 €. Le seuil s’apprécie objet par objet, sauf lorsque les objets vendus forment un ensemble (une paire de fauteuils, un service complet, une collection) : c’est alors le prix de l’ensemble qui compte. Attention, au-delà du seuil, la taxe porte sur la totalité du prix, pas seulement sur la part qui dépasse 5 000 €.</p>
<h2 id="option">L’option pour le régime des plus-values</h2>
<p>Si vous pouvez justifier de la date et du prix d’acquisition (facture, acte de partage, déclaration de succession), vous pouvez opter pour l’imposition de la plus-value réelle. Elle bénéficie d’un abattement de 5 % par année de détention au-delà de la deuxième, ce qui conduit à une exonération totale après 22 ans. Pour un objet hérité depuis longtemps, cette option peut donc aboutir à une imposition nulle. La date retenue pour un objet reçu en héritage est celle de la succession.</p>
<h2 id="qui">Qui déclare et qui paie</h2>
<p>Lorsque vous vendez à un professionnel, c’est lui qui calcule la taxe, la déclare et la reverse à l’administration ; le montant est déduit du prix qui vous est versé et figure sur le bordereau d’achat. Vous n’avez pas de formulaire à remplir dans ce cas.</p>
<h2 id="paiement">Comment le professionnel doit vous payer</h2>
<ul>
<li><strong>Métaux précieux</strong> (bijoux, argenterie, pièces) : le paiement en espèces est interdit, quel que soit le montant. Il se fait par virement ou par chèque.</li>
<li><strong>Autres objets</strong> : un professionnel ne peut pas payer un particulier en espèces au-delà de 1 000 €. Le virement ou le chèque laisse une trace utile en cas d’option pour les plus-values.</li>
</ul>
<h2 id="registre">Pourquoi on vous demande une pièce d’identité</h2>
<p>Tout antiquaire ou brocanteur doit avoir fait une déclaration préalable en préfecture et tenir un registre d’objets mobiliers, coté et paraphé, mis à jour chaque jour. Chaque objet acheté y est décrit, avec son prix et l’identité du vendeur. C’est une obligation de lutte contre le recel : un professionnel qui ne vous demande rien n’est pas en règle.</p>
'''
    sources = [SRC_ROM, SRC_R3211, SRC_ESP, "Articles 150 UA, 150 VI à 150 VM du Code général des impôts (taxe forfaitaire sur les métaux précieux, bijoux, objets d’art, de collection et d’antiquité)"]
    faq = [("Dois-je déclarer la vente de vieux meubles sans valeur ?", "<p>Non. Les meubles meublants courants ne sont pas imposés à la vente. Seuls les objets précieux, d’art, de collection ou d’antiquité vendus plus de 5 000 €, et les métaux précieux, relèvent de la taxe forfaitaire.</p>"),
           ("Vendre en plusieurs fois permet-il d’éviter le seuil ?", "<p>Non lorsque les objets forment un ensemble : le fractionnement artificiel d’une paire ou d’un service ne change pas son appréciation. Pour des objets distincts vendus séparément, le seuil s’applique objet par objet.</p>")]
    return guide_page("fiscalite-vente-objets-anciens", "Vendre des objets anciens : taxe, seuils et paiement",
        "Taxe forfaitaire de 6,5 % au-delà de 5 000 €, 11,5 % sur les métaux précieux, option plus-values, paiement sans espèces : vendre des objets anciens.",
        "Vendre des objets anciens : ce que dit la fiscalité", "Taxe forfaitaire, seuil de 5 000 €, métaux précieux, option pour les plus-values, moyens de paiement : ce qu’un particulier doit savoir avant de vendre à un antiquaire.",
        "montres", [("categories", "Trois catégories d’objets"), ("taxe", "La taxe forfaitaire de 6,5 %"), ("option", "L’option plus-values"),
                    ("qui", "Qui déclare et qui paie"), ("paiement", "Les moyens de paiement"), ("registre", "Le registre d’objets mobiliers")],
        contenu, sources, faq, [("/objets-achetes", "Objets que nous achetons", "Argenterie, bijoux, tableaux"),
                                ("/achat-antiquites-paris", "Achat d’antiquités", "Offre écrite, paiement tracé"),
                                ("/guides/que-faire-des-meubles-succession", "Les meubles d’une succession", "Partage, vente, débarras")])


def g_succession():
    contenu = f'''
<p>Après un décès, la question du mobilier arrive vite : le logement doit être rendu, vendu ou loué, et chacun a ses souvenirs. Prendre le temps de faire les choses dans l’ordre évite des erreurs coûteuses, juridiques comme financières.</p>
<p class="small muted">Ce guide est informatif : votre notaire reste l’interlocuteur de référence pour toute question sur la succession.</p>
<h2 id="attendre">Avant tout : ne rien vendre ni donner trop tôt</h2>
<p>Un héritier qui vend, donne ou partage des biens du défunt peut être considéré comme ayant accepté la succession purement et simplement (articles 782 et 783 du Code civil). Il devient alors tenu des dettes éventuelles, même si elles dépassent l’actif. Seuls certains actes sont permis sans prendre parti : actes purement conservatoires, de surveillance ou d’administration provisoire, paiement des frais funéraires et des dettes urgentes (article 784). Si vous avez un doute sur l’équilibre de la succession, interrogez le notaire avant de vider le logement.</p>
<h2 id="inventaire">Faire l’inventaire</h2>
<p>Un inventaire estimatif, pièce par pièce, permet de savoir ce que contient réellement le logement, de repérer les objets de valeur et de préparer le partage. Il est aussi utile pour la déclaration de succession : à défaut d’inventaire ou de vente, l’administration fiscale retient en principe pour les meubles meublants un forfait de 5 % de l’actif successoral (article 764 du Code général des impôts). Un inventaire ou une vente peuvent justifier une valeur inférieure.</p>
<p>Lorsque les héritiers acceptent à concurrence de l’actif net, un inventaire officiel est obligatoire ; il est dressé par un commissaire de justice, un notaire ou un commissaire-priseur.</p>
<h2 id="partager">Partager entre héritiers</h2>
<p>Chacun indique les objets qu’il souhaite conserver. Lorsque plusieurs héritiers veulent le même objet, une estimation neutre aide à équilibrer les parts. Les souvenirs sans valeur marchande (photos, lettres, petits objets) se partagent en général simplement ; les objets de valeur doivent être pris en compte dans le partage.</p>
<h2 id="vendre">Vendre ce qui a de la valeur</h2>
<ul>
<li><strong>À un antiquaire</strong> : prix ferme, paiement rapide, enlèvement inclus, possibilité de racheter tout le contenu.</li>
<li><strong>Aux enchères</strong> : pertinent pour les pièces importantes, avec un délai de plusieurs semaines et des frais vendeur. Voir <a href="/guides/antiquaire-ou-commissaire-priseur">antiquaire ou commissaire-priseur</a>.</li>
<li><strong>Entre particuliers</strong> : possible pour quelques objets, mais long et peu adapté à tout un appartement.</li>
</ul>
<p>La vente doit recueillir l’accord de tous les héritiers, ou de la personne qu’ils ont mandatée.</p>
<h2 id="vider">Vider le reste</h2>
<p>Une fois le partage fait et les objets de valeur vendus, reste souvent l’essentiel du volume : mobilier courant, vaisselle, linge, papiers. Un <a href="/debarras-succession">débarras de succession</a> réalisé par un antiquaire combine les deux : la valeur des objets rachetés vient en déduction du coût du débarras, et les papiers et souvenirs retrouvés sont remis à la famille.</p>
<h2 id="calendrier">Le calendrier à garder en tête</h2>
<ul>
<li>La déclaration de succession doit en principe être déposée dans les six mois du décès lorsque celui-ci a lieu en France métropolitaine.</li>
<li>Un héritier ne peut être contraint de choisir avant quatre mois ; passé ce délai, il peut être mis en demeure de prendre parti.</li>
<li>Pour un logement loué, le préavis et la date de restitution des clés fixent souvent l’échéance pratique du débarras.</li>
</ul>
'''
    sources = ["Articles 771, 772, 782 à 784, 787 à 789 du Code civil (option successorale, actes autorisés, inventaire)",
               "Article 764 du Code général des impôts (évaluation des meubles meublants)"]
    return guide_page("que-faire-des-meubles-succession", "Meubles d’une succession : partager, vendre, vider",
        "Que faire des meubles d’une succession : précautions avant de vider, inventaire, forfait de 5 %, partage entre héritiers, vente à un antiquaire ou aux enchères.",
        "Que faire des meubles d’une succession ?", "Inventorier, partager, vendre, vider : l’ordre qui évite les erreurs, et le point juridique à vérifier avec le notaire avant de toucher au mobilier.",
        "chambre", [("attendre", "Ne rien vendre trop tôt"), ("inventaire", "Faire l’inventaire"), ("partager", "Partager entre héritiers"),
                    ("vendre", "Vendre ce qui a de la valeur"), ("vider", "Vider le reste"), ("calendrier", "Le calendrier")],
        contenu, sources, None, [("/debarras-succession", "Débarras de succession", "Inventaire et rachat"),
                                 ("/guides/fiscalite-vente-objets-anciens", "Fiscalité de la vente", "Taxe et seuils"),
                                 ("/estimation-antiquites-gratuite", "Estimation gratuite", "Avant le partage")])


def g_prix():
    contenu = f'''
<p>« Combien coûte un débarras ? » La seule réponse honnête est : cela dépend de ce qu’il y a à enlever, d’où, et de ce que cela vaut. Voici les critères qui construisent un devis, et comment le lire.</p>
<h2 id="criteres">Les cinq critères qui font le prix</h2>
<ol>
<li><strong>Le volume</strong> : nombre de pièces, densité, présence d’une cave, d’un grenier ou d’un garage.</li>
<li><strong>Les accès</strong> : étage, ascenseur et sa taille, escalier de service, distance entre la porte et le camion, stationnement possible dans la rue.</li>
<li><strong>Le temps de tri</strong> : un logement à trier finement (papiers, souvenirs à mettre de côté) demande plus de temps qu’un local à vider.</li>
<li><strong>L’évacuation</strong> : volume à déposer en déchetterie, filières spécifiques (électroménager, peintures, gravats).</li>
<li><strong>La valeur des objets repris</strong> : c’est le seul critère qui fait baisser le prix, parfois jusqu’à zéro.</li>
</ol>
<h2 id="paris">Ce qui est propre à Paris</h2>
<p>À volume égal, un débarras parisien coûte souvent plus cher qu’en province ou en grande couronne : petits ascenseurs, étages élevés sans ascenseur, rues étroites, stationnement contraint, portage plus long. Inversement, les appartements parisiens contiennent fréquemment du mobilier et des objets de valeur qui compensent ce surcoût.</p>
<h2 id="devis">Lire un devis de débarras</h2>
<p>Un devis sérieux est établi après visite et distingue clairement :</p>
<ul>
<li>le coût de l’intervention (main-d’œuvre, véhicule, évacuation) ;</li>
<li>la liste et la valeur des objets rachetés ;</li>
<li>le solde, à payer ou à percevoir ;</li>
<li>ce qui est inclus : cave, démontage, balayage final, protection des parties communes.</li>
</ul>
<h2 id="alertes">Les signaux d’alerte</h2>
<ul>
<li>Un « débarras gratuit » promis au téléphone, sans visite.</li>
<li>Un paiement demandé ou proposé en espèces, sans reçu.</li>
<li>Aucune pièce d’identité demandée pour le rachat d’objets : le professionnel ne tient pas son registre.</li>
<li>Pas de raison sociale, de numéro SIREN ni d’adresse sur le devis.</li>
<li>Des objets emportés avant la signature du devis.</li>
</ul>
<h2 id="reduire">Comment réduire la facture</h2>
<p>Faites estimer avant de jeter : un objet que vous pensiez sans intérêt peut couvrir une partie du débarras. Regroupez cave, grenier et logement dans une seule intervention. Indiquez votre échéance tôt pour éviter une intervention en urgence. Et confiez le tout à un <a href="/debarras-avec-rachat">professionnel qui rachète</a>.</p>
'''
    faq = [("Pourquoi ne donnez-vous pas de prix au mètre cube ?", "<p>Parce qu’un mètre cube de mobilier courant au sixième sans ascenseur et un mètre cube de meubles anciens au rez-de-chaussée n’ont ni le même coût ni la même valeur. Seule la visite permet un prix juste.</p>"),
           ("La visite de devis est-elle payante ?", "<p>Non, elle est gratuite dans Paris et la petite couronne.</p>")]
    return guide_page("prix-debarras-paris", "Prix d’un débarras à Paris : ce qui fait le devis",
        "Prix d’un débarras à Paris : volume, accès, tri, évacuation et valeur des objets repris. Comment lire un devis, éviter les pièges et réduire la facture.",
        "Prix d’un débarras à Paris : comment se construit le devis", "Volume, étage, accès, évacuation et valeur des objets repris : les cinq critères d’un devis de débarras, les signaux d’alerte et les moyens de payer moins.",
        "cartons", [("criteres", "Les cinq critères"), ("paris", "Ce qui est propre à Paris"), ("devis", "Lire un devis"),
                    ("alertes", "Les signaux d’alerte"), ("reduire", "Réduire la facture")],
        contenu, [], faq, [("/debarras-avec-rachat", "Débarras avec rachat", "La valeur déduit le coût"),
                           ("/debarras-appartement-paris", "Débarras d’appartement", "Paris, tous étages"),
                           ("/debarras-maison", "Débarras de maison", "Petite couronne")])


def g_cp():
    contenu = f'''
<p>Pour vendre un objet de valeur, deux grandes voies existent : le vendre directement à un antiquaire, ou le confier à une maison de ventes pour une vente aux enchères. Aucune n’est meilleure dans l’absolu ; tout dépend de l’objet, de votre calendrier et de votre tolérance à l’incertitude.</p>
<h2 id="comparatif">Le comparatif en un tableau</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Vente à un antiquaire</th><th>Vente aux enchères</th></tr></thead>
<tbody>
<tr><td><strong>Prix</strong></td><td>Ferme, connu avant la vente</td><td>Inconnu jusqu’à l’adjudication ; estimation indicative</td></tr>
<tr><td><strong>Frais</strong></td><td>Aucun pour le vendeur</td><td>Frais vendeur (commission, parfois photos, transport, assurance)</td></tr>
<tr><td><strong>Délai</strong></td><td>Paiement à l’enlèvement</td><td>Plusieurs semaines entre le dépôt, la vente et le paiement</td></tr>
<tr><td><strong>Logistique</strong></td><td>Enlèvement à domicile inclus</td><td>Dépôt à l’étude ou enlèvement souvent facturé</td></tr>
<tr><td><strong>Invendus</strong></td><td>Sans objet</td><td>À récupérer, ou à remettre en vente</td></tr>
<tr><td><strong>Adapté à</strong></td><td>Contenus complets, mobilier, objets de qualité courante à élevée</td><td>Pièces rares ou importantes, œuvres d’artistes cotés, collections spécialisées</td></tr>
</tbody></table></div>
<h2 id="antiquaire">Quand vendre à un antiquaire</h2>
<p>Lorsque vous voulez un prix certain, rapidement, sans démarche ni frais ; lorsque vous vendez un ensemble (un appartement, une maison) plutôt qu’une pièce exceptionnelle ; lorsque le calendrier est contraint par une vente immobilière ou une fin de bail.</p>
<h2 id="encheres">Quand préférer les enchères</h2>
<p>Lorsque l’objet est rare et susceptible d’attirer des collectionneurs du monde entier : œuvre d’un artiste important, pièce historique, collection spécialisée. La mise en concurrence des acheteurs peut alors dépasser l’estimation. Un antiquaire honnête vous le dira, et pourra vous orienter.</p>
<h2 id="vocabulaire">Commissaire-priseur, commissaire de justice : qui fait quoi</h2>
<p>Depuis le 1er juillet 2022, les huissiers de justice et les commissaires-priseurs judiciaires ont fusionné dans la profession de commissaire de justice, qui réalise notamment les inventaires et ventes judiciaires. Les commissaires-priseurs de ventes volontaires, eux, dirigent les ventes aux enchères des maisons de ventes. Pour une simple vente d’objets hérités, c’est cette seconde catégorie que l’on consulte.</p>
<h2 id="combiner">Combiner les deux</h2>
<p>C’est souvent la meilleure solution pour une succession : la pièce exceptionnelle part aux enchères, et l’antiquaire rachète le reste du contenu, ce qui finance en partie ou en totalité le débarras.</p>
'''
    return guide_page("antiquaire-ou-commissaire-priseur", "Antiquaire ou commissaire-priseur : comment vendre ?",
        "Vendre à un antiquaire ou aux enchères ? Prix ferme ou aléatoire, frais, délais, logistique : le comparatif pour choisir selon l’objet et votre calendrier.",
        "Antiquaire ou commissaire-priseur : comment vendre ?", "Prix ferme ou enchères, frais, délais, logistique : le comparatif honnête pour choisir la bonne voie selon l’objet à vendre et votre calendrier.",
        "salon_tableaux", [("comparatif", "Le comparatif"), ("antiquaire", "Quand vendre à un antiquaire"), ("encheres", "Quand préférer les enchères"),
                           ("vocabulaire", "Qui fait quoi"), ("combiner", "Combiner les deux")],
        contenu, [], None, [("/achat-antiquites-paris", "Achat d’antiquités", "Prix ferme, sans frais"),
                            ("/estimation-antiquites-gratuite", "Estimation gratuite", "Savoir avant de choisir"),
                            ("/guides/que-faire-des-meubles-succession", "Les meubles d’une succession", "Partage, vente, débarras")])


GUIDES_LIST = [
    ("/guides/reconnaitre-un-meuble-ancien", "Reconnaître un meuble ancien", "Styles, estampille, assemblages : époque ou style ?", "commode"),
    ("/guides/que-faire-des-meubles-succession", "Que faire des meubles d’une succession ?", "Inventaire, partage, vente, débarras, et le point juridique à vérifier.", "chambre"),
    ("/guides/fiscalite-vente-objets-anciens", "Vendre des objets anciens : la fiscalité", "Taxe forfaitaire, seuil de 5 000 €, métaux précieux, paiement.", "montres"),
    ("/guides/prix-debarras-paris", "Prix d’un débarras à Paris", "Les cinq critères du devis et les signaux d’alerte.", "cartons"),
    ("/guides/antiquaire-ou-commissaire-priseur", "Antiquaire ou commissaire-priseur ?", "Prix ferme ou enchères : comment choisir.", "salon_tableaux"),
]


def g_index():
    path = "/guides"
    cards = "".join(f'<a class="carte-guide" href="{u}"><div class="img">{img(k, (16, 10), "(max-width: 700px) 100vw, 33vw")}</div><div class="txt"><b>{t}</b><span>{d}</span></div></a>' for u, t, d, k in GUIDES_LIST)
    body = f'''
<section class="page-hero"><div class="container">{crumbs([("Guides", None)])}
<h1 style="max-width:18ch">Guides pratiques : antiquités, successions, débarras</h1>
<p class="lead" style="max-width:60ch">Ce qu’il faut savoir avant de vendre, de partager ou de vider : des réponses précises, appuyées sur la réglementation et la pratique du métier.</p></div></section>
<section class="section" style="padding-top:0"><div class="container"><div class="cartes-guides">{cards}</div></div></section>
{cta_band()}
'''
    ld = [breadcrumb_ld([("Guides", None)], path)]
    return path, render(path, "Guides pratiques : antiquités, successions et débarras",
                        "Guides d’antiquaire : reconnaître un meuble ancien, fiscalité de la vente d’objets, meubles d’une succession, prix d’un débarras, enchères ou vente directe.", body, ld)


def build_all_guides():
    return [g_index(), g_meuble(), g_fisc(), g_succession(), g_prix(), g_cp()]
