from core import *

ARR = {
 1: dict(quartiers=["Saint-Germain-l’Auxerrois", "Halles", "Palais-Royal", "Place-Vendôme"], img="salon_or",
   intro="Autour du Palais-Royal et de la place Vendôme, les immeubles des XVIIe et XVIIIe siècles abritent des appartements où le mobilier se transmet souvent depuis plusieurs générations.",
   habitat="Beaucoup d’escaliers anciens étroits, d’ascenseurs de poche et de rues où le stationnement d’un camion se négocie : nous prévoyons le portage à la main et les sangles pour les pièces lourdes comme les armoires ou les buffets à deux corps.",
   objets="On y rencontre volontiers des pendules en bronze doré, des miroirs à parecloses, des sièges cannés et des bibliothèques d’amateurs."),
 2: dict(quartiers=["Gaillon", "Vivienne", "Mail", "Bonne-Nouvelle"], img="bureau",
   intro="Entre la galerie Vivienne et le passage des Panoramas, haut lieu historique de la philatélie, le 2e arrondissement mêle appartements anciens, bureaux et ateliers.",
   habitat="Les débarras y concernent autant des logements que des locaux professionnels : anciens cabinets, ateliers de confection, réserves sous les toits accessibles par l’escalier de service.",
   objets="Collections de timbres et de cartes postales, mobilier de bureau ancien, lampes et objets de vitrine y sont fréquents."),
 3: dict(quartiers=["Arts-et-Métiers", "Enfants-Rouges", "Archives", "Sainte-Avoie"], img="couloir",
   intro="Dans le haut Marais, les hôtels particuliers et les immeubles sur cour cachent des intérieurs très divers, du grand appartement familial à l’atelier d’artisan.",
   habitat="Cours pavées, porches à double battant, escaliers à vis : chaque adresse demande un repérage, que nous faisons lors de l’estimation pour chiffrer l’enlèvement au plus juste.",
   objets="Mobilier XVIIIe et XIXe, objets de curiosité, outillage d’artisans, luminaires industriels et mobilier de métier."),
 4: dict(quartiers=["Saint-Merri", "Saint-Gervais", "Arsenal", "Notre-Dame"], img="salon_tableaux",
   intro="De l’île Saint-Louis au Village Saint-Paul, connu pour ses antiquaires, le 4e concentre des appartements anciens aux volumes souvent modestes mais aux contenus remarquables.",
   habitat="Rues étroites et zones piétonnes imposent d’organiser le chargement à l’avance ; nous vérifions les horaires de livraison autorisés pour l’adresse.",
   objets="Tableaux et gravures, petits meubles de salon, porcelaine, argenterie de table, livres et objets religieux anciens."),
 5: dict(quartiers=["Saint-Victor", "Jardin-des-Plantes", "Val-de-Grâce", "Sorbonne"], img="bibliotheque",
   intro="Quartier latin oblige, le 5e est l’arrondissement des bibliothèques : professeurs, médecins et chercheurs y ont souvent accumulé des milliers de volumes.",
   habitat="Nous savons évaluer une bibliothèque entière sur place, trier les éditions recherchées des ouvrages courants et organiser leur mise en cartons dans les étages.",
   objets="Livres anciens et reliés, instruments scientifiques, cartes et gravures, bureaux et fauteuils de cabinet."),
 6: dict(quartiers=["Monnaie", "Odéon", "Notre-Dame-des-Champs", "Saint-Germain-des-Prés"], img="tableaux",
   intro="Rue de Seine, rue Jacob, rue des Saints-Pères : le 6e reste un quartier de galeries, d’éditeurs et de collectionneurs, et cela se voit dans les intérieurs.",
   habitat="Immeubles sur rue et sur cour, souvent sans ascenseur au-delà du quatrième étage, avec des caves voûtées qui servent de réserve depuis des décennies.",
   objets="Tableaux modernes et anciens, dessins, sculptures, mobilier de décorateurs, livres d’art et objets de la seconde moitié du XXe siècle."),
 7: dict(quartiers=["Saint-Thomas-d’Aquin", "Invalides", "École-Militaire", "Gros-Caillou"], img="salon",
   intro="Entre le Carré Rive Gauche, quartier d’antiquaires réputé, et le faubourg Saint-Germain, le 7e rassemble certains des plus beaux appartements de réception de Paris.",
   habitat="Grands volumes, enfilades de salons et chambres de service sous les combles : les successions y représentent souvent un travail de plusieurs jours, que nous planifions pièce par pièce.",
   objets="Mobilier d’époque Louis XV et Louis XVI, sièges estampillés, bronzes, pendules, argenterie et porcelaine de grandes manufactures."),
 8: dict(quartiers=["Champs-Élysées", "Faubourg-du-Roule", "Madeleine", "Europe"], img="miroir_salon",
   intro="Du faubourg Saint-Honoré à la plaine Monceau, le 8e associe appartements haussmanniens, hôtels particuliers et bureaux installés dans d’anciens logements.",
   habitat="Ascenseurs souvent petits mais escaliers de service présents : nous coordonnons l’intervention avec le gardien ou le syndic et protégeons les parties communes.",
   objets="Mobilier Napoléon III, trumeaux et miroirs dorés, lustres en cristal, tapis, objets d’art asiatiques et argenterie."),
 9: dict(quartiers=["Saint-Georges", "Chaussée-d’Antin", "Faubourg-Montmartre", "Rochechouart"], img="cadres",
   intro="L’arrondissement de l’hôtel Drouot et de la Nouvelle Athènes connaît mieux que tout autre le commerce des objets anciens.",
   habitat="Immeubles de la Restauration et haussmanniens, cours intérieures, logements d’artistes et de musiciens : chaque intervention commence par un repérage des accès.",
   objets="Instruments de musique, partitions et pianos, tableaux, mobilier romantique, bibelots et objets de vitrine."),
 10: dict(quartiers=["Saint-Vincent-de-Paul", "Porte-Saint-Denis", "Porte-Saint-Martin", "Hôpital-Saint-Louis"], img="machine_ecrire",
   intro="Du canal Saint-Martin aux faubourgs Saint-Denis et Saint-Martin, le 10e alterne immeubles faubouriens, cours artisanales et anciens ateliers.",
   habitat="Beaucoup de débarras de locaux et d’ateliers au fond des cours, avec des accès par passage couvert : nous adaptons l’équipe et le véhicule à l’adresse.",
   objets="Mobilier de métier, établis, luminaires industriels, machines anciennes, mobilier des années 1930 à 1970."),
 11: dict(quartiers=["Folie-Méricourt", "Roquette", "Sainte-Marguerite", "Saint-Ambroise"], img="chaises_etageres",
   intro="Le faubourg Saint-Antoine, berceau des ébénistes parisiens, déborde sur le 11e : on y trouve encore des meubles fabriqués à quelques rues de là.",
   habitat="Immeubles faubouriens, lofts dans d’anciens ateliers, cours à plusieurs corps de bâtiment : idéal pour le mobilier volumineux, à condition de bien préparer le chargement.",
   objets="Meubles de style et d’époque du Faubourg, sièges, mobilier Art déco, objets industriels et design."),
 12: dict(quartiers=["Bel-Air", "Picpus", "Bercy", "Quinze-Vingts"], img="commode",
   intro="De l’avenue Daumesnil, où le Viaduc des Arts accueille des artisans d’art, au bois de Vincennes, le 12e garde une forte tradition du meuble.",
   habitat="Grands immeubles familiaux des années 1900 à 1930 autour de Daumesnil et de Picpus, avec caves et chambres de bonne à vider en même temps que l’appartement.",
   objets="Mobilier de salle à manger complet, armoires, buffets, pendules, faïence et services de table."),
 13: dict(quartiers=["Salpêtrière", "Gare", "Maison-Blanche", "Croulebarbe"], img="chaises_soleil",
   intro="De la Butte-aux-Cailles à la Manufacture des Gobelins, le 13e mêle maisons de ville, immeubles anciens et grands ensembles.",
   habitat="Les accès sont souvent plus simples qu’au centre : ascenseurs plus grands, parkings, rues larges, ce qui allège le coût d’un débarras complet.",
   objets="Mobilier des années 1950 à 1970, objets asiatiques, tapisseries et textiles, bibliothèques et collections diverses."),
 14: dict(quartiers=["Montparnasse", "Parc-de-Montsouris", "Petit-Montrouge", "Plaisance"], img="fenetre_paris",
   intro="Montparnasse et ses ateliers d’artistes, les villas autour du parc Montsouris, les puces de Vanves le week-end : le 14e est une terre de chineurs.",
   habitat="Ateliers vitrés, maisons de ville avec jardin, petits immeubles d’avant-guerre : nous intervenons aussi bien dans une villa que dans un sixième sans ascenseur.",
   objets="Tableaux et sculptures d’atelier, chevalets et matériel d’artiste, mobilier Art déco, céramiques et objets de décoration."),
 15: dict(quartiers=["Saint-Lambert", "Necker", "Grenelle", "Javel"], img="salle_lustre",
   intro="Arrondissement le plus peuplé de Paris, le 15e abrite aussi le Village Suisse, ensemble d’antiquaires et de brocanteurs de l’avenue de Suffren.",
   habitat="Immeubles en pierre de taille, en brique des années 1930 et résidences récentes : grande variété de logements, et autant de débarras d’appartements familiaux.",
   objets="Mobilier de famille, salles à manger, services de porcelaine, argenterie, pendules et tableaux décoratifs."),
 16: dict(quartiers=["Auteuil", "Muette", "Porte-Dauphine", "Chaillot"], img="salon_or",
   intro="Entre les immeubles Art nouveau d’Auteuil et les grands appartements de Passy et de Chaillot, le 16e concentre une part importante des successions parisiennes.",
   habitat="Appartements de 150 m² et plus, caves, chambres de service et parfois box : nous établissons un inventaire complet avant de proposer un rachat global.",
   objets="Mobilier d’époque, sièges dorés, lustres, tapis, argenterie, tableaux, bibliothèques et objets de décoration de qualité."),
 17: dict(quartiers=["Ternes", "Plaine-de-Monceaux", "Batignolles", "Épinettes"], img="coiffeuse",
   intro="Hôtels particuliers de la plaine Monceau, immeubles bourgeois des Ternes, maisons et petits immeubles des Batignolles : le 17e est très contrasté.",
   habitat="Les rues résidentielles facilitent le stationnement, mais beaucoup d’immeubles réservent l’ascenseur aux personnes : nous passons alors par l’escalier de service.",
   objets="Mobilier Napoléon III et Louis-Philippe, pianos, miroirs, porcelaine, mobilier design et luminaires."),
 18: dict(quartiers=["Grandes-Carrières", "Clignancourt", "Goutte-d’Or", "Chapelle"], img="fenetre_paris",
   intro="À deux pas des puces de Saint-Ouen, le 18e est l’arrondissement de Montmartre, de ses ateliers d’artistes et de ses escaliers.",
   habitat="Rues en pente, escaliers publics et ruelles étroites rendent certains enlèvements délicats : nous les anticipons dès l’estimation pour éviter les mauvaises surprises.",
   objets="Tableaux et dessins d’artistes du quartier, affiches anciennes, mobilier bistrot, vinyles, objets de brocante et curiosités."),
 19: dict(quartiers=["Villette", "Pont-de-Flandre", "Amérique", "Combat"], img="design_lampe",
   intro="Des Buttes-Chaumont au bassin de la Villette, le 19e associe immeubles de 1900 à 1930, villas pavées du quartier Mouzaïa et lofts aménagés.",
   habitat="Maisons de ville et villas sans accès camion direct : nous prévoyons le portage jusqu’à la rue et l’intervention en une seule journée lorsque c’est possible.",
   objets="Mobilier des années 1930 à 1970, objets de famille, vaisselle, luminaires et petits meubles."),
 20: dict(quartiers=["Belleville", "Saint-Fargeau", "Père-Lachaise", "Charonne"], img="cartons_table",
   intro="Belleville, Ménilmontant, Charonne : le 20e garde des maisons de faubourg, des ateliers et des cités où l’on vit souvent depuis longtemps.",
   habitat="Logements occupés pendant des décennies, greniers et caves pleins : un débarras avec tri soigné permet de retrouver des objets de valeur au milieu du quotidien.",
   objets="Mobilier ancien et populaire, outils, objets de collection, vaisselle, mobilier des années 1950 à 1970."),
}

VOISINS = {1: [2, 3, 4, 8, 6, 7], 2: [1, 3, 9, 10], 3: [2, 4, 10, 11], 4: [1, 3, 11, 12, 5], 5: [4, 6, 13, 14, 12],
           6: [5, 7, 14, 15], 7: [6, 15, 8, 16], 8: [1, 9, 17, 16, 7], 9: [2, 8, 10, 17, 18], 10: [2, 3, 9, 11, 18, 19],
           11: [3, 4, 10, 12, 20], 12: [4, 11, 20, 13], 13: [5, 12, 14], 14: [5, 6, 13, 15], 15: [6, 7, 14, 16],
           16: [7, 8, 15, 17], 17: [8, 9, 16, 18], 18: [9, 10, 17, 19], 19: [10, 18, 20], 20: [11, 12, 19]}

DEPS = {
 "hauts-de-seine": dict(code="92", nom="Hauts-de-Seine", article="dans les Hauts-de-Seine", img="salle_lustre",
   villes=["Neuilly-sur-Seine", "Boulogne-Billancourt", "Levallois-Perret", "Saint-Cloud", "Sèvres", "Issy-les-Moulineaux", "Rueil-Malmaison", "Sceaux", "Courbevoie", "Meudon"],
   intro="Neuilly, Boulogne, Saint-Cloud ou Sceaux : les Hauts-de-Seine comptent de nombreuses maisons de famille et de grands appartements dont le contenu justifie une estimation sur place. Sèvres y abrite aussi la manufacture de porcelaine la plus célèbre de France.",
   habitat="Maisons avec cave, grenier et dépendances, garages pleins, jardins d’hiver : les débarras y sont souvent plus volumineux qu’à Paris, mais l’accès en camion est généralement plus simple.",
   objets="Mobilier de maison bourgeoise, salles à manger complètes, porcelaine de Sèvres et de Limoges, tableaux, outillage et mobilier de jardin ancien."),
 "seine-saint-denis": dict(code="93", nom="Seine-Saint-Denis", article="en Seine-Saint-Denis", img="marche",
   villes=["Saint-Ouen-sur-Seine", "Montreuil", "Le Raincy", "Les Lilas", "Bagnolet", "Pantin", "Le Pré-Saint-Gervais", "Saint-Denis", "Aubervilliers", "Gagny"],
   intro="Le département des puces de Saint-Ouen, le plus grand marché d’antiquités au monde, compte aussi des pavillons, des maisons de maître au Raincy et des ateliers reconvertis à Montreuil.",
   habitat="Pavillons avec sous-sol et grenier, ateliers et entrepôts : nous intervenons pour des débarras complets, y compris de locaux professionnels et de garages.",
   objets="Mobilier ancien et de style, mobilier industriel, outillage, objets de brocante, collections et mobilier des années 1950 à 1970."),
 "val-de-marne": dict(code="94", nom="Val-de-Marne", article="dans le Val-de-Marne", img="chambre",
   villes=["Vincennes", "Saint-Mandé", "Nogent-sur-Marne", "Le Perreux-sur-Marne", "Saint-Maur-des-Fossés", "Charenton-le-Pont", "Joinville-le-Pont", "Ivry-sur-Seine", "Créteil", "Fontenay-sous-Bois"],
   intro="Des villas de bord de Marne à Nogent et au Perreux aux appartements de Vincennes et de Saint-Mandé, le Val-de-Marne offre des intérieurs très variés, souvent restés dans la même famille.",
   habitat="Maisons sur plusieurs niveaux, caves et combles aménagés, parfois une dépendance au fond du jardin : nous chiffrons chaque espace séparément pour un devis clair.",
   objets="Mobilier de famille, salles à manger, pendules, faïence, services de table, tableaux et mobilier de jardin."),
}


def build_arr(n):
    d = ARR[n]
    o = ordinal(n)
    path = f"/antiquaire-paris-{n}"
    cp = f"750{n:02d}"
    h1 = f"Antiquaire Paris {o} : achat, estimation et débarras"
    lead = f"Rachat de meubles anciens et d’objets d’art, estimation gratuite à domicile et débarras d’appartements dans le {o} arrondissement ({cp}). {d['intro']}"
    voisins = "".join(f'<a class="plaque" href="/antiquaire-paris-{v}"><small>750{v:02d}</small><b>{plaque_label(v)}</b><span>{esc(ARR[v]["quartiers"][0])}</span></a>' for v in VOISINS[n])
    quart = "".join(f"<li>{esc(q)}</li>" for q in d["quartiers"])
    faq = [
        (f"Vous déplacez-vous gratuitement dans le {o} arrondissement ?",
         f"<p>Oui. L’estimation à domicile est gratuite dans tout le {o}, comme dans le reste de Paris. Vous pouvez aussi commencer par nous envoyer des photos pour un premier avis.</p>"),
        (f"Pouvez-vous vider entièrement un appartement du {o} ?",
         f"<p>Oui, cave et chambre de service comprises. Nous rachetons ce qui a de la valeur, donnons ce qui peut l’être et évacuons le reste. {d['habitat']}</p>"),
        ("Comment êtes-vous payé et comment nous payez-vous ?",
         "<p>Nos achats sont réglés par virement ou chèque à l’enlèvement, avec un reçu détaillé. Les objets en or ou en argent ne peuvent légalement pas être payés en espèces.</p>"),
    ]
    body = f'''
<section class="page-hero"><div class="container">
{crumbs([("Zones d’intervention", "/zones-intervention"), (f"Paris {o}", None)])}
<div class="hero-grid"><div>
<div class="plaque-titre" style="margin-top:1.4rem"><small>{cp}</small><b>{plaque_label(n)} <span class="u">arr.</span></b></div>
<h1>{h1}</h1><p class="lead">{lead}</p>
<div class="btn-row">{btn_estimation()}{btn_tel()}</div></div>
<figure class="cadre drape"><div class="photo">{img(d["img"], (4, 5), "(max-width: 900px) 100vw, 40vw", eager=True)}</div></figure>
</div></div></section>

<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Les intérieurs du {o} et ce que l’on y trouve</h2>
<p>{d["objets"]} Nous estimons chaque pièce selon son époque, sa qualité de fabrication, sa signature éventuelle et son état, puis nous vous faisons une proposition écrite, objet par objet ou pour l’ensemble.</p>
<h2>Accès, étages et logistique</h2>
<p>{d["habitat"]}</p>
<p>Ce repérage nous permet d’annoncer un prix d’enlèvement ou de débarras sans supplément le jour J. Les objets rachetés sont inscrits au registre d’objets mobiliers et payés par virement ou chèque.</p>
<h3>Quartiers desservis dans le {o}</h3>
<ul class="quartiers">{quart}</ul>
</div>
<div class="aside-card" style="position:sticky;top:100px">
<h3>Ce que nous faisons dans le {o}</h3>
<ul class="liste-check">
<li>{ico("check")}<span><a href="/achat-antiquites-paris">Achat d’antiquités</a> et d’objets d’art</span></li>
<li>{ico("check")}<span><a href="/rachat-meubles-anciens">Rachat de meubles anciens</a> à domicile</span></li>
<li>{ico("check")}<span><a href="/estimation-antiquites-gratuite">Estimation gratuite</a> sur photos ou sur place</span></li>
<li>{ico("check")}<span><a href="/debarras-succession">Débarras de succession</a> avec inventaire</span></li>
<li>{ico("check")}<span><a href="/debarras-appartement-paris">Débarras d’appartement</a>, cave et chambre de service</span></li>
</ul>
{btn_estimation("Envoyer des photos")}
</div></div></section>

<section class="section section--tint"><div class="container narrow">{faq_html(faq)}</div></section>

<section class="section"><div class="container">
<div class="section-head"><h2>Arrondissements voisins</h2><p>Nous intervenons dans les mêmes conditions dans tout Paris.</p></div>
<div class="plaques">{voisins}<a class="plaque" href="/zones-intervention"><small>PARIS</small><b><span class="u">Toutes zones</span></b><span>Paris et petite couronne</span></a></div>
</div></section>
{cta_band(f"Un objet ou un appartement à vider dans le {o} ?")}
'''
    desc = f"Antiquaire dans le {o} arrondissement de Paris ({cp}) : rachat de meubles anciens et objets d’art, estimation gratuite à domicile, débarras de succession."
    title = f"Antiquaire Paris {o} ({cp}) : achat, estimation, débarras"
    ld = [breadcrumb_ld([("Zones d’intervention", "/zones-intervention"), (f"Paris {o}", None)], path), faq_ld(faq),
          service_ld(f"Antiquaire et débarras à Paris {o}", path, desc)]
    return path, render(path, title, desc, body, ld, og_image=d["img"])


def build_dep(slug):
    d = DEPS[slug]
    path = f"/antiquaire-{slug}"
    villes = "".join(f"<li>{esc(v)}</li>" for v in d["villes"])
    faq = [
        (f"Vous déplacez-vous {d['article']} ?",
         f"<p>Oui, dans tout le département ({d['code']}), notamment à {esc(', '.join(d['villes'][:5]))}. L’estimation sur place est gratuite.</p>"),
        ("Videz-vous les maisons entières, cave et grenier compris ?",
         "<p>Oui. Nous chiffrons chaque espace (pièces de vie, cave, grenier, garage, dépendances), rachetons ce qui a de la valeur et évacuons le reste. La valeur reprise est déduite du devis.</p>"),
        ("Sous quel délai pouvez-vous intervenir ?",
         "<p>Indiquez-nous votre échéance (vente, remise des clés, fin de bail) : nous organisons la visite puis l’intervention en fonction de cette date.</p>"),
    ]
    body = f'''
<section class="page-hero"><div class="container">
{crumbs([("Zones d’intervention", "/zones-intervention"), (d["nom"], None)])}
<div class="hero-grid"><div>
<div class="plaque-titre" style="margin-top:1.4rem"><small>DÉPARTEMENT {d["code"]}</small><b><span class="u">{esc(d["nom"])}</span></b></div>
<h1>Antiquaire {d["article"]} : achat, estimation, débarras</h1>
<p class="lead">{d["intro"]}</p>
<div class="btn-row">{btn_estimation()}{btn_tel()}</div></div>
<figure class="cadre drape"><div class="photo">{img(d["img"], (4, 5), "(max-width: 900px) 100vw, 40vw", eager=True)}</div></figure>
</div></div></section>
<section class="section" style="padding-top:0"><div class="container split split--top">
<div class="prose">
<h2>Ce que nous rachetons {d["article"]}</h2>
<p>{d["objets"]} Chaque objet est estimé sur place selon son époque, sa fabrication et son état ; vous recevez une proposition écrite avant tout enlèvement.</p>
<h2>Maisons, caves, greniers : une logistique adaptée</h2>
<p>{d["habitat"]}</p>
<p>Pour un <a href="/debarras-maison">débarras de maison</a> ou une <a href="/debarras-succession">succession</a>, la valeur des objets que nous rachetons vient en déduction du coût. Selon le contenu, l’intervention peut ne rien vous coûter.</p>
<h3>Communes desservies</h3><ul class="quartiers">{villes}</ul>
<p class="small muted" style="margin-top:1rem">Et l’ensemble des autres communes du département.</p>
</div>
<div class="aside-card" style="position:sticky;top:100px"><h3>Estimation gratuite</h3><p>Envoyez des photos : nous vous répondons avec un premier avis de valeur, puis nous fixons une visite si besoin.</p>{btn_estimation("Envoyer des photos")}</div>
</div></section>
<section class="section section--tint"><div class="container narrow">{faq_html(faq)}</div></section>
{cta_band(f"Une maison ou un appartement à vider {d['article']} ?")}
'''
    desc = f"Antiquaire {d['article']} ({d['code']}) : rachat de meubles anciens et d’objets d’art, estimation gratuite à domicile, débarras de maison et de succession."
    title = f"Antiquaire {d['nom']} ({d['code']}) : achat et débarras"
    ld = [breadcrumb_ld([("Zones d’intervention", "/zones-intervention"), (d["nom"], None)], path), faq_ld(faq),
          service_ld(f"Antiquaire et débarras {d['article']}", path, desc)]
    return path, render(path, title, desc, body, ld, og_image=d["img"])


def build_zones():
    from pages_home import plaques_html
    path = "/zones-intervention"
    body = f'''
{page_hero([("Zones d’intervention", None)], "Zones d’intervention : Paris et petite couronne",
 "Nous nous déplaçons gratuitement dans les 20 arrondissements de Paris et dans les Hauts-de-Seine, la Seine-Saint-Denis et le Val-de-Marne, pour estimer, racheter et débarrasser.",
 "fenetre_paris")}
<section class="section" style="padding-top:0"><div class="container">
<div class="section-head"><h2>Choisissez votre arrondissement</h2><p>Chaque page décrit les intérieurs, les accès et les objets que nous rencontrons le plus souvent dans le secteur.</p></div>
{plaques_html()}
</div></section>
<section class="section section--tint"><div class="container cols-3">
<div class="bloc"><span class="ico-rond">{ico("map-pin")}</span><h3>Déplacement gratuit</h3><p>Pour une estimation à domicile dans Paris et la petite couronne, sans engagement de vente.</p></div>
<div class="bloc"><span class="ico-rond">{ico("truck")}</span><h3>Accès repérés</h3><p>Étages, ascenseur, escalier de service, stationnement : tout est vérifié lors de la visite pour un prix ferme.</p></div>
<div class="bloc"><span class="ico-rond">{ico("calendar-check")}</span><h3>Selon votre échéance</h3><p>Remise des clés, vente, fin de bail : nous planifions l’intervention à partir de votre date limite.</p></div>
</div></section>
<section class="section"><div class="container narrow prose">
<h2>Au-delà de la petite couronne</h2>
<p>Pour une succession importante ou une collection, nous pouvons nous déplacer ailleurs en Île-de-France (Yvelines, Essonne, Val-d’Oise, Seine-et-Marne). Envoyez d’abord des photos : nous vous dirons si le déplacement se justifie.</p>
</div></section>
{cta_band()}
'''
    desc = "Antiquaire et débarras dans les 20 arrondissements de Paris, les Hauts-de-Seine, la Seine-Saint-Denis et le Val-de-Marne. Déplacement et estimation gratuits."
    ld = [breadcrumb_ld([("Zones d’intervention", None)], path)]
    return path, render(path, "Zones d’intervention : antiquaire Paris et petite couronne", desc, body, ld, og_image="fenetre_paris")


def build_all_local():
    pages = [build_arr(n) for n in range(1, 21)]
    pages += [build_dep(s) for s in DEPS]
    pages.append(build_zones())
    return pages
