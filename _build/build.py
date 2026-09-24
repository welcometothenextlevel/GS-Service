"""Builds the static pages from shared partials. Run: python3 _build/build.py"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://welcometothenextlevel.github.io/GS-Service/"
TEL = "tel:+41766900663"
WA = "https://wa.me/41766900663?text=" + "Bonjour%2C%20je%20souhaite%20un%20devis%20pour%20"
MAIL = "mailto:s.gocevski@outlook.com"

I = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.2-.3-.3-.6-.4zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4a9.8 9.8 0 0 1-1.5-5.2c0-5.4 4.4-9.8 9.8-9.8 2.6 0 5.1 1 6.9 2.9a9.7 9.7 0 0 1 2.9 6.9c0 5.4-4.4 9.8-9.8 9.8zm8.4-18.2A11.8 11.8 0 0 0 12 0C5.5 0 .2 5.3.2 11.9c0 2.1.5 4.1 1.6 5.9L.1 24l6.3-1.7c1.7.9 3.7 1.4 5.7 1.4 6.5 0 11.9-5.3 11.9-11.9 0-3.2-1.2-6.2-3.5-8.4z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>',
    "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
    "doc": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>',
}

LOGO_MARK = '<span class="logo-mark"><svg viewBox="0 0 40 40" aria-hidden="true"><text x="3" y="25" font-family="Archivo,sans-serif" font-weight="800" font-size="21" fill="#131a16" style="font-stretch:80%">GS</text><path d="M4 31c6-2.4 14-3 32-1.6" stroke="#131a16" stroke-width="4" stroke-linecap="round" fill="none"/></svg></span>'


def head(title, desc, path, extra=""):
    url = BASE + path
    return f"""<!doctype html>
<html lang="fr-CH">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#131a16">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_CH">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}img/og.jpg">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css?v=4">
{extra}</head>
<body>
"""


def header(active):
    def link(href, label, key):
        cur = ' aria-current="page"' if key == active else ""
        return f'<a href="{href}"{cur}>{label}</a>'
    return f"""<div class="topbar"><div class="wrap">
  <div><span class="open-dot"></span><span data-status>Lun–Sam · 8h00–17h00</span></div>
  <div class="tb-right">Puidoux · Lavaux · Riviera — <a href="{TEL}">076 690 06 63</a> · <a href="{MAIL}">s.gocevski@outlook.com</a></div>
</div></div>
<header class="header"><div class="wrap">
  <a class="logo" href="./" aria-label="GS Service – Gotsevski, accueil">{LOGO_MARK}<span class="logo-text"><b>GS Service</b><span>Gotsevski · Puidoux</span></span></a>
  <nav class="nav" id="nav" aria-label="Navigation principale">
    {link('./#services','Prestations','services')}
    {link('realisations','Réalisations','realisations')}
    {link('./#avis','Avis clients','avis')}
    {link('contact','Contact & devis','contact')}
  </nav>
  <div class="header-cta">
    <a class="btn btn-green" href="{TEL}" aria-label="Appeler le 076 690 06 63">{I['phone']}<span class="lbl">076 690 06 63</span></a>
    <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav">{I['menu']}</button>
  </div>
</div></header>
"""


BAND = f"""<section class="band"><div class="wrap">
  <h2>Un projet de peinture, de façade ou de rénovation ? Parlons-en.</h2>
  <div class="acts">
    <a class="btn btn-ink" href="{TEL}">{I['phone']} 076 690 06 63</a>
    <a class="btn btn-line" href="contact">Demander un devis {I['arrow']}</a>
  </div>
</div></section>
"""

FOOTER = f"""<footer class="footer"><div class="wrap">
  <div class="footer-grid">
    <div>
      <a class="logo" href="./">{LOGO_MARK}<span class="logo-text"><b style="color:#fff">GS Service</b><span>Gotsevski · Puidoux</span></span></a>
      <p style="margin-top:18px;max-width:22em">Peinture, façades et rénovation dans le Lavaux. Un seul interlocuteur, du premier coup de fil au chantier rendu propre.</p>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="{TEL}">076 690 06 63</a></li>
        <li><a href="https://wa.me/41766900663" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="{MAIL}">s.gocevski@outlook.com</a></li>
        <li><a href="https://www.google.com/maps/search/?api=1&query=Chemin+de+Publoz+15,+1070+Puidoux" target="_blank" rel="noopener">Chemin de Publoz 15<br>1070 Puidoux VD</a></li>
      </ul>
    </div>
    <div>
      <h4>Horaires</h4>
      <ul>
        <li>Lun–Ven · 8h00–17h00<br><span style="color:#8d978f">sur rendez-vous</span></li>
        <li>Samedi · 8h00–17h00</li>
        <li>Dimanche · fermé</li>
      </ul>
    </div>
    <div>
      <h4>Prestations</h4>
      <ul>
        <li><a href="./#services">Peinture</a></li>
        <li><a href="./#services">Rénovation</a></li>
        <li><a href="./#services">Façades</a></li>
        <li><a href="realisations">Réalisations</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>© <span data-year>2026</span> GS Service – Gotsevski · Entreprise individuelle · IDE CHE-290.495.935</span>
    <span>Paiement sur facture ou TWINT</span>
  </div>
</div></footer>
"""

DOCK = f"""<div class="dock" role="complementary" aria-label="Contact rapide">
  <a class="d-wa" href="https://wa.me/41766900663" target="_blank" rel="noopener" aria-label="Écrire sur WhatsApp">{I['wa']}</a>
  <a class="d-call" href="{TEL}"><span class="ring">{I['phone']}</span><span class="t"><small>Appelez-nous</small>076 690 06 63</span></a>
  <a class="d-quote" href="contact#devis">{I['doc']} Devis</a>
</div>
"""

LB = """<div class="lb" role="dialog" aria-modal="true" aria-label="Photo agrandie">
  <img alt="">
  <div class="lb-cap"></div>
  <button class="lb-close" aria-label="Fermer"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg></button>
  <button class="lb-prev" aria-label="Photo précédente"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 18-6-6 6-6"/></svg></button>
  <button class="lb-next" aria-label="Photo suivante"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg></button>
</div>
"""

END = '<script src="js/main.js?v=1" defer></script>\n</body>\n</html>\n'

SERVICES = ["Peinture intérieure", "Façade", "Rénovation", "Boiseries / avant-toit", "Autre"]


def form(title="Demande de devis"):
    chips = "\n".join(
        f'<label><input type="checkbox" name="service" value="{s}"><span>{s}</span></label>' for s in SERVICES
    )
    return f"""<form class="form" id="devis" novalidate>
  <h3>{title}</h3>
  <p>Quelques détails suffisent. Votre demande part directement chez GS Service, par WhatsApp ou par e-mail.</p>
  <p class="form-error" role="alert">Merci d’indiquer votre nom et votre numéro de téléphone.</p>
  <fieldset class="field"><legend>Que pouvons-nous faire pour vous ?</legend><div class="chips">
{chips}
  </div></fieldset>
  <div class="row2">
    <div class="field"><label for="f-name">Nom</label><input type="text" id="f-name" name="name" autocomplete="name" required></div>
    <div class="field"><label for="f-tel">Téléphone</label><input type="tel" id="f-tel" name="tel" autocomplete="tel" inputmode="tel" placeholder="07x xxx xx xx" required></div>
  </div>
  <div class="row2">
    <div class="field"><label for="f-lieu">Lieu des travaux <em>(localité)</em></label><input type="text" id="f-lieu" name="lieu" placeholder="ex. Chexbres"></div>
    <div class="field"><label for="f-delai">Quand ?</label><select id="f-delai" name="delai"><option value="">Choisir…</option><option>Dès que possible</option><option>Dans le mois</option><option>Dans 1 à 3 mois</option><option>Pas encore défini</option></select></div>
  </div>
  <div class="field"><label for="f-email">E-mail <em>(facultatif)</em></label><input type="email" id="f-email" name="email" autocomplete="email"></div>
  <div class="field"><label for="f-msg">Votre projet</label><textarea id="f-msg" name="message" placeholder="Surface, nombre de pièces, intérieur ou extérieur, étage, accès…"></textarea></div>
  <div class="form-actions">
    <button class="btn btn-wa" type="submit">{I['wa']} Envoyer par WhatsApp</button>
    <button class="btn btn-line" type="button" data-mail>{I['mail']} Envoyer par e-mail</button>
  </div>
  <p class="form-note">Plus rapide encore : appelez le <a href="{TEL}"><b>076 690 06 63</b></a>, lundi à samedi de 8h à 17h.</p>
</form>"""


HOURS = """<div class="hours"><table>
  <tr data-day="1"><td>Lundi</td><td>8h00 – 17h00*</td></tr>
  <tr data-day="2"><td>Mardi</td><td>8h00 – 17h00*</td></tr>
  <tr data-day="3"><td>Mercredi</td><td>8h00 – 17h00*</td></tr>
  <tr data-day="4"><td>Jeudi</td><td>8h00 – 17h00*</td></tr>
  <tr data-day="5"><td>Vendredi</td><td>8h00 – 17h00*</td></tr>
  <tr data-day="6"><td>Samedi</td><td>8h00 – 17h00</td></tr>
  <tr data-day="0"><td>Dimanche</td><td>Fermé</td></tr>
</table><p class="note">* sur rendez-vous</p></div>"""

SCHEMA = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"HousePainter","name":"GS Service - Gotsevski",
"description":"Peinture, façades et rénovation à Puidoux et dans le Lavaux.",
"url":"%s","telephone":"+41 76 690 06 63","email":"s.gocevski@outlook.com","image":"%simg/chalet-fini.webp",
"address":{"@type":"PostalAddress","streetAddress":"Chemin de Publoz 15","postalCode":"1070","addressLocality":"Puidoux","addressRegion":"VD","addressCountry":"CH"},
"geo":{"@type":"GeoCoordinates","latitude":46.4907,"longitude":6.7631},
"areaServed":["Puidoux","Chexbres","Rivaz","Saint-Saphorin","Lavaux"],
"paymentAccepted":"Facture, TWINT",
"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"08:00","closes":"17:00"}]}
</script>
""" % (BASE, BASE)


def img(name, alt, cls="", sizes="100vw", eager=False):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img src="img/{name}.webp" srcset="img/{name}-sm.webp 720w, img/{name}.webp 1400w" '
            f'sizes="{sizes}" alt="{alt}" {load} decoding="async"{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>')


# ---------- HOME ----------
svc_rows = [
    ("Peinture", "Murs, plafonds, boiseries, portes : peinture intérieure soignée, sur supports bien préparés. Pour une ambiance apaisante, une touche audacieuse ou simplement un coup de frais.",
     ["Murs & plafonds", "Boiseries", "Portes", "Cages d’escalier"], "plafond-peinture", "Plafond et poutres repeints en blanc"),
    ("Rénovation", "Des petites retouches aux projets d’envergure : préparation des supports, enduits, finitions. Une équipe qualifiée qui donne vie à vos idées.",
     ["Enduits & lissage", "Combles", "Salles de bain", "Terrasses bois"], "combles-renoves", "Combles rénovés avec parquet et murs blancs"),
    ("Façades", "Façades en bois, crépi et avant-toits : échafaudage sécurisé, préparation et protection des abords, puis traitement et peinture. Votre maison retrouve son allure, et elle est protégée pour les années à venir.",
     ["Façades bois", "Crépi", "Avant-toits", "Volets & fenêtres", "Échafaudage"], "chalet-fini", "Chalet en bois après travaux de façade, avec le véhicule GS Service"),
]

svc_html = "\n".join(
    f"""<article class="svc rv">
  <span class="svc-num">{i+1:02d}</span>
  <h3>{t}</h3>
  <div class="svc-desc"><p>{d}</p><ul>{''.join(f'<li>{x}</li>' for x in tags)}</ul></div>
  <div class="svc-img">{img(im, alt, sizes="(max-width:600px) 100vw, 220px")}</div>
</article>""" for i, (t, d, tags, im, alt) in enumerate(svc_rows)
)

ticker_items = "".join(f"<span>{s}</span>" for s in ["Peinture intérieure", "Façades bois", "Rénovation", "Crépi", "Avant-toits", "Boiseries", "Plafonds", "Salles de bain"])

home = head(
    "GS Service – Gotsevski | Peintre, façades & rénovation à Puidoux",
    "Peintre et entreprise de rénovation à Puidoux (Lavaux, VD). Peinture intérieure, façades et rénovation. 5,0/5 sur 4 avis. Appelez le 076 690 06 63.",
    "", SCHEMA) + header("home") + f"""<main>
<section class="hero"><div class="wrap hero-grid">
  <div>
    <span class="eyebrow">Peinture · Façades · Rénovation · Puidoux</span>
    <h1>Peinture, façades, rénovation. <span class="stroke">Bien fait</span>, du début à la fin.</h1>
    <p class="lead">GS Service Gotsevski, c’est votre partenaire tout-en-un dans le Lavaux : on repeint vos intérieurs, on remet vos façades à neuf et on rénove vos pièces. Un seul numéro à appeler.</p>
    <div class="hero-actions">
      <a class="btn btn-green" href="{TEL}">{I['phone']} Appeler le 076 690 06 63</a>
      <a class="btn btn-line" href="#devis">Demander un devis {I['arrow']}</a>
    </div>
    <div class="proof">
      <div><span class="stars">★★★★★</span> <strong>5,0/5</strong> · 4 avis clients</div>
      <div><strong>Lun–Sam</strong> · 8h–17h</div>
      <div>Facture ou <strong>TWINT</strong></div>
    </div>
  </div>
  <div class="hero-media">
    <div class="main">{img("chalet-fini", "Chalet en bois après travaux, avec le véhicule GS Service devant", sizes="(max-width:900px) 100vw, 45vw", eager=True)}</div>
    <div class="inset">{img("chalet-echafaudage", "Le même chalet sous échafaudage pendant les travaux", sizes="20vw")}</div>
    <span class="tag"><i></i>Chantier réalisé par GS Service</span>
  </div>
</div></section>

<div class="ticker" aria-hidden="true"><div class="ticker-track">{ticker_items}{ticker_items}</div></div>

<section class="section" id="services"><div class="wrap">
  <div class="section-head">
    <div><span class="eyebrow">Prestations</span><h2>Peinture, façades, rénovation. Trois métiers, une seule équipe.</h2></div>
    <p>Que vous rénoviez votre espace ou vouliez simplement lui redonner un coup de neuf, dedans comme dehors, on vous accompagne à chaque étape.</p>
  </div>
  <div class="svc-list">
{svc_html}
  </div>
  <div class="center-cta"><a class="btn btn-green" href="{TEL}">{I['phone']} Parler de mon projet</a><a class="btn btn-line" href="#devis">Devis en ligne {I['arrow']}</a></div>
</div></section>

<section class="section on-dark" id="methode"><div class="wrap">
  <div class="section-head">
    <div><span class="eyebrow">Comment on travaille</span><h2>Un chantier propre, du premier appel au dernier coup de balai.</h2></div>
    <p>Protection des sols et des meubles, échafaudage sécurisé en extérieur, nettoyage à la fin. Vous retrouvez votre maison comme il se doit.</p>
  </div>
  <div class="steps">
    <div class="step rv"><b>01</b><h3>Vous appelez</h3><p>Un appel, un WhatsApp ou le formulaire. On discute de votre projet et on fixe un rendez-vous.</p></div>
    <div class="step rv"><b>02</b><h3>Visite & devis</h3><p>On passe voir sur place pour vous donner un prix clair, sans surprise.</p></div>
    <div class="step rv"><b>03</b><h3>On protège</h3><p>Bâches, films et rubans sur tout ce qui ne doit pas être touché. Échafaudage pour l’extérieur.</p></div>
    <div class="step rv"><b>04</b><h3>Travaux & nettoyage</h3><p>Travail soigné et ponctuel, puis on laisse les lieux propres. Paiement sur facture ou TWINT.</p></div>
  </div>
  <div class="process-photo">
    <figure class="rv">{img("facade-bois-echafaudage", "Échafaudage monté contre une façade en bois", sizes="(max-width:760px) 100vw, 40vw")}<figcaption>Échafaudage sécurisé</figcaption></figure>
    <figure class="rv">{img("cuisine-protection", "Cuisine protégée par des films plastique pendant les travaux", sizes="(max-width:760px) 50vw, 30vw")}<figcaption>Cuisine protégée</figcaption></figure>
    <figure class="rv">{img("facade-escalier-protection", "Escalier et soubassement protégés au ruban avant peinture", sizes="(max-width:760px) 50vw, 30vw")}<figcaption>Bords masqués</figcaption></figure>
  </div>
</div></section>

<section class="section" id="realisations"><div class="wrap">
  <div class="section-head">
    <div><span class="eyebrow">Réalisations</span><h2>Nos chantiers, en photos.</h2></div>
    <p>Façades en bois, avant-toits, intérieurs, salles de bain et terrasses. Des photos de chantiers réels, prises par l’équipe.</p>
  </div>
  <div class="mosaic" data-lb>
    <a class="m1 rv" href="img/facade-bois-passerelle-2.webp" data-caption="Façade en bois – travaux depuis l’échafaudage">{img("facade-bois-passerelle-2", "Façade en bois vue depuis l’échafaudage, vue sur le village", sizes="(max-width:760px) 100vw, 42vw")}<span>Façade bois</span></a>
    <a class="m2 rv" href="img/salle-de-bain.webp" data-caption="Salle de bain sous les combles">{img("salle-de-bain", "Salle de bain rénovée sous velux", sizes="(max-width:760px) 50vw, 33vw")}<span>Salle de bain</span></a>
    <a class="m3 rv" href="img/avant-toit-noir.webp" data-caption="Avant-toit repeint en noir">{img("avant-toit-noir", "Avant-toit repeint en noir, vu depuis l’échafaudage", sizes="(max-width:760px) 50vw, 25vw")}<span>Avant-toit</span></a>
    <a class="m4 rv" href="img/porte-repeinte.webp" data-caption="Porte repeinte">{img("porte-repeinte", "Porte ancienne avec hublot repeinte", sizes="(max-width:760px) 50vw, 25vw")}<span>Portes</span></a>
    <a class="m5 rv" href="img/terrasse-bois-2.webp" data-caption="Terrasse en bois nettoyée">{img("terrasse-bois-2", "Terrasse en bois", sizes="(max-width:760px) 50vw, 33vw")}<span>Terrasse</span></a>
  </div>
  <div class="center-cta"><a class="btn btn-ink" href="realisations">Voir toutes les photos {I['arrow']}</a></div>
</div></section>

<section class="section" id="avis" style="padding-top:0"><div class="wrap">
  <div class="section-head">
    <div><span class="eyebrow">Avis clients</span><h2>5 étoiles sur chaque avis.</h2></div>
    <p>Avis publiés par des clients sur local.ch et search.ch.</p>
  </div>
  <div class="reviews">
    <div class="score rv">
      <div class="big">5,0<small>/5</small></div>
      <div class="stars">★★★★★</div>
      <p>Note moyenne sur 4 avis · aucun avis en dessous de 5 étoiles</p>
      <div class="src">
        <a href="https://www.local.ch/en/d/puidoux/1070/painting/gs-service-gotsevski-khm1VBmaaDtW8iqlW9epsw" target="_blank" rel="noopener">local.ch <span>5,0 · 4 avis ↗</span></a>
        <a href="https://search.ch/tel/puidoux/chemin-de-publoz-15/gs-service-gotsevski" target="_blank" rel="noopener">search.ch <span>5,0 · 4 avis ↗</span></a>
      </div>
    </div>
    <div>
      <figure class="quote rv">
        <blockquote>Très efficace, ponctuel et travail sérieux […] Merci beaucoup et très contente de leur service !</blockquote>
        <figcaption><span class="avatar">S</span><span><b>Je recommande cette entreprise !</b>shih-yi.huang · avril 2024 · ★★★★★</span></figcaption>
      </figure>
      <div class="mini-reviews">
        <div class="mini rv"><span class="stars">★★★★★</span><b>« Efficace et précis »</b><span>Client local.ch · novembre 2023</span></div>
        <div class="mini rv"><span class="stars">★★★★★</span><b>👍 ✅</b><span>Client search.ch · novembre 2023</span></div>
      </div>
    </div>
  </div>
</div></section>

<section class="section" style="padding-top:0"><div class="wrap about">
  <div class="about-img rv">{img("facade-crepi", "Façade crépie avec échafaudage et volets", sizes="(max-width:860px) 100vw, 50vw")}</div>
  <div class="rv">
    <span class="eyebrow">L’entreprise</span>
    <h2>Une entreprise locale, installée à Puidoux.</h2>
    <p>GS Service Gotsevski est une entreprise individuelle inscrite au registre du commerce, basée Chemin de Publoz 15 à Puidoux. Peinture intérieure, façades et rénovation : une équipe qui prépare, protège et finit proprement chaque chantier.</p>
    <p>Notre engagement envers votre satisfaction et la qualité du travail est inébranlable. Faites-nous confiance pour chaque aspect de votre projet.</p>
    <div class="towns"><span>Puidoux</span><span>Chexbres</span><span>Rivaz</span><span>Saint-Saphorin</span><span>Lavaux & environs</span></div>
    <dl class="facts">
      <div><dt>Siège</dt><dd>1070 Puidoux VD</dd></div>
      <div><dt>IDE</dt><dd>CHE-290.495.935</dd></div>
      <div><dt>Horaires</dt><dd>Lun–Sam · 8h–17h</dd></div>
      <div><dt>Paiement</dt><dd>Facture · TWINT</dd></div>
    </dl>
  </div>
</div></section>

<section class="section quote-sec" id="contact"><div class="wrap qgrid">
  <div class="qside rv">
    <span class="eyebrow">Devis</span>
    <h2>Parlez-nous de votre projet.</h2>
    <p>Décrivez en deux lignes ce que vous souhaitez faire. On vous recontacte pour convenir d’une visite et vous remettre un devis.</p>
    <div class="call-card">
      <small>Le plus rapide : un appel</small>
      <a class="num" href="{TEL}">076 690 06 63</a>
      <div class="row">
        <a class="btn btn-green" href="{TEL}">{I['phone']} Appeler</a>
        <a class="btn btn-wa" href="https://wa.me/41766900663" target="_blank" rel="noopener">{I['wa']} WhatsApp</a>
      </div>
    </div>
    {HOURS}
  </div>
  <div class="rv">{form()}</div>
</div></section>
</main>
""" + BAND + FOOTER + DOCK + LB + END

# ---------- REALISATIONS ----------
gal = [
    ("chalet-fini", "ext", "Chalet en bois après travaux"),
    ("facade-bois-passerelle-2", "ext", "Façade en bois – vue depuis l’échafaudage"),
    ("salle-de-bain", "int", "Salle de bain sous les combles"),
    ("chalet-echafaudage", "ext", "Chalet sous échafaudage"),
    ("combles-renoves", "int", "Combles rénovés"),
    ("avant-toit-noir", "ext", "Avant-toit repeint en noir"),
    ("terrasse-bois", "bois", "Terrasse en bois"),
    ("mur-enduit", "int", "Mur en cours d’enduit et de lissage"),
    ("facade-crepi", "ext", "Façade crépie et fenêtres"),
    ("porte-repeinte", "int", "Porte ancienne repeinte"),
    ("poutres-bois", "bois", "Poutres et plafond en bois"),
    ("sejour-fini", "int", "Séjour repeint, prêt à être habité"),
    ("facade-bois-echafaudage", "ext", "Façade en bois – échafaudage complet"),
    ("buanderie", "int", "Buanderie et salle d’eau"),
    ("boiseries-interieur", "bois", "Boiseries intérieures"),
    ("avant-toit-preparation", "ext", "Avant-toit en préparation"),
    ("plafond-peinture", "int", "Plafond et poutres repeints"),
    ("terrasse-bois-2", "bois", "Terrasse en bois nettoyée"),
    ("facade-escalier-protection", "ext", "Escalier et soubassement masqués avant peinture"),
    ("cuisine-protection", "int", "Cuisine protégée pendant les travaux"),
    ("avant-toit-blanc", "ext", "Sous-face d’avant-toit en blanc"),
    ("protection-chantier", "int", "Protection plastique d’une pièce"),
    ("facade-bois-passerelle", "ext", "Passerelle le long d’une façade en bois"),
]
cat_label = {"ext": "Façades & extérieur", "int": "Intérieur", "bois": "Bois & terrasses"}
gal_html = "\n".join(
    f'<a href="img/{n}.webp" data-cat="{c}" data-caption="{cap}" class="rv">{img(n, cap, sizes="(max-width:520px) 50vw, 33vw")}<span>{cat_label[c]}</span></a>'
    for n, c, cap in gal
)

real = head(
    "Réalisations – GS Service Gotsevski, peintre à Puidoux",
    "Photos de chantiers de GS Service Gotsevski : façades en bois, avant-toits, intérieurs, salles de bain, terrasses. Puidoux et Lavaux. 076 690 06 63.",
    "realisations") + header("realisations") + f"""<main>
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Réalisations</span>
  <h1>Des chantiers réels, photographiés sur place.</h1>
  <p>Façades de chalets, avant-toits, pièces repeintes, salles de bain, terrasses en bois. Cliquez sur une photo pour l’agrandir.</p>
</div></section>
<section style="padding-bottom:clamp(64px,9vw,110px)"><div class="wrap">
  <div class="filters" role="group" aria-label="Filtrer les photos">
    <button data-filter="all" aria-pressed="true">Tout ({len(gal)})</button>
    <button data-filter="ext" aria-pressed="false">Façades & extérieur</button>
    <button data-filter="int" aria-pressed="false">Intérieur</button>
    <button data-filter="bois" aria-pressed="false">Bois & terrasses</button>
  </div>
  <div class="gallery" data-lb>
{gal_html}
  </div>
</div></section>
</main>
""" + BAND + FOOTER + DOCK + LB + END

# ---------- CONTACT ----------
contact = head(
    "Contact & devis – GS Service Gotsevski, Puidoux",
    "Contactez GS Service Gotsevski à Puidoux : 076 690 06 63, WhatsApp ou formulaire de devis. Peinture, façades, rénovation. Lun–Sam 8h–17h.",
    "contact", SCHEMA) + header("contact") + f"""<main>
<section class="page-hero"><div class="wrap">
  <span class="eyebrow">Contact & devis</span>
  <h1>Un appel suffit pour démarrer.</h1>
  <p>Appelez, écrivez sur WhatsApp ou remplissez le formulaire. On vous répond pour fixer une visite et établir votre devis.</p>
</div></section>
<section style="padding-bottom:clamp(64px,9vw,110px)"><div class="wrap qgrid">
  <div>
    <div class="contact-grid">
      <a class="c-card" href="{TEL}"><small>Téléphone</small><b>076 690 06 63</b><span>Lun–Sam · 8h–17h</span></a>
      <a class="c-card" href="https://wa.me/41766900663" target="_blank" rel="noopener"><small>WhatsApp</small><b>Écrire un message</b><span>Envoyez aussi vos photos</span></a>
      <a class="c-card" href="{MAIL}"><small>E-mail</small><b style="font-size:17px">s.gocevski@outlook.com</b><span>Réponse par e-mail</span></a>
      <a class="c-card" href="https://www.google.com/maps/search/?api=1&query=Chemin+de+Publoz+15,+1070+Puidoux" target="_blank" rel="noopener"><small>Adresse</small><b>Chemin de Publoz 15</b><span>1070 Puidoux VD · Itinéraire ↗</span></a>
    </div>
    <div class="map"><iframe title="Carte : Chemin de Publoz 15, 1070 Puidoux" loading="lazy" src="https://www.google.com/maps?q=Chemin+de+Publoz+15,+1070+Puidoux&z=15&output=embed"></iframe></div>
    <h3 style="font-size:22px;margin:32px 0 6px">Horaires</h3>
    {HOURS}
  </div>
  <div>{form()}</div>
</div></section>
</main>
""" + FOOTER + DOCK + END

(ROOT / "index.html").write_text(home)
(ROOT / "realisations.html").write_text(real)
(ROOT / "contact.html").write_text(contact)
print("built")
