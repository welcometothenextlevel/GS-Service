// GS Service – Gotsevski
const CONTACT = {
  phone: "+41766900663",
  phoneLabel: "076 690 06 63",
  whatsapp: "41766900663",
  email: "s.gocevski@outlook.com",
};

const LANG = (document.documentElement.lang || "fr").slice(0, 2);
const TXT = {
  fr: { open: "Ouvert maintenant · jusqu’à 17h", closed: "Fermé · laissez un message WhatsApp",
        hello: "Bonjour, je souhaite un devis (via le site web).", name: "Nom", tel: "Téléphone", email: "E-mail",
        svc: "Prestation(s)", place: "Lieu des travaux", when: "Délai souhaité", subject: "Demande de devis", site: "site web" },
  en: { open: "Open now · until 5pm", closed: "Closed · send us a WhatsApp message",
        hello: "Hello, I would like a quote (via the website).", name: "Name", tel: "Phone", email: "E-mail",
        svc: "Service(s)", place: "Location", when: "Timing", subject: "Quote request", site: "website" },
  de: { open: "Jetzt geöffnet · bis 17 Uhr", closed: "Geschlossen · schreiben Sie uns auf WhatsApp",
        hello: "Guten Tag, ich möchte eine Offerte (über die Website).", name: "Name", tel: "Telefon", email: "E-Mail",
        svc: "Leistung(en)", place: "Ort der Arbeiten", when: "Zeitraum", subject: "Offertanfrage", site: "Website" },
}[LANG] || {};

// Header border on scroll + mobile menu
const header = document.querySelector(".header");
const onScroll = () => header && header.classList.toggle("scrolled", window.scrollY > 8);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

const burger = document.querySelector(".burger");
const nav = document.querySelector(".nav");
if (burger && nav) {
  burger.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    burger.setAttribute("aria-expanded", open);
  });
  nav.querySelectorAll("a").forEach((a) =>
    a.addEventListener("click", () => {
      nav.classList.remove("open");
      burger.setAttribute("aria-expanded", "false");
    })
  );
}

// Open / closed status, Swiss time. Mon–Sat 08:00–17:00 (Mon–Fri on appointment)
(function status() {
  const parts = new Intl.DateTimeFormat("fr-CH", {
    timeZone: "Europe/Zurich", weekday: "short", hour: "2-digit", minute: "2-digit", hour12: false,
  }).formatToParts(new Date());
  const get = (t) => parts.find((p) => p.type === t)?.value || "";
  const days = ["dim.", "lun.", "mar.", "mer.", "jeu.", "ven.", "sam."];
  const day = days.indexOf(get("weekday"));
  const mins = parseInt(get("hour"), 10) * 60 + parseInt(get("minute"), 10);
  const open = day >= 1 && day <= 6 && mins >= 480 && mins < 1020;
  document.querySelectorAll("[data-status]").forEach((el) => {
    el.textContent = open ? TXT.open : TXT.closed;
  });
  document.querySelectorAll(".open-dot").forEach((d) => d.classList.toggle("closed", !open));
  document.querySelectorAll(`.hours tr[data-day="${day}"]`).forEach((tr) => tr.classList.add("today"));
})();

// Reveal on scroll
const io = "IntersectionObserver" in window
  ? new IntersectionObserver((entries) => entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    }), { rootMargin: "0px 0px -8% 0px" })
  : null;
document.querySelectorAll(".rv").forEach((el) => (io ? io.observe(el) : el.classList.add("in")));

// Quote form → WhatsApp or e-mail, pre-filled
document.querySelectorAll("form.form").forEach((form) => {
  const err = form.querySelector(".form-error");
  const build = () => {
    const d = new FormData(form);
    const services = d.getAll("service");
    const lines = [
      TXT.hello,
      "",
      `${TXT.name} : ${d.get("name") || ""}`,
      `${TXT.tel} : ${d.get("tel") || ""}`,
      d.get("email") ? `${TXT.email} : ${d.get("email")}` : null,
      services.length ? `${TXT.svc} : ${services.join(", ")}` : null,
      d.get("lieu") ? `${TXT.place} : ${d.get("lieu")}` : null,
      d.get("delai") ? `${TXT.when} : ${d.get("delai")}` : null,
      "",
      d.get("message") || "",
    ].filter((l) => l !== null);
    return lines.join("\n").trim();
  };
  const valid = () => {
    let ok = true;
    ["name", "tel"].forEach((n) => {
      const f = form.elements[n];
      const bad = !f.value.trim();
      f.classList.toggle("input-bad", bad);
      if (bad) ok = false;
    });
    err.classList.toggle("show", !ok);
    if (!ok) form.elements[form.elements.name.value.trim() ? "tel" : "name"].focus();
    return ok;
  };
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!valid()) return;
    window.open(`https://wa.me/${CONTACT.whatsapp}?text=${encodeURIComponent(build())}`, "_blank", "noopener");
  });
  form.querySelector("[data-mail]")?.addEventListener("click", () => {
    if (!valid()) return;
    const subject = encodeURIComponent(TXT.subject + " – " + (form.elements.name.value || TXT.site));
    window.location.href = `mailto:${CONTACT.email}?subject=${subject}&body=${encodeURIComponent(build())}`;
  });
  form.querySelectorAll("input").forEach((i) => i.addEventListener("input", () => i.classList.remove("input-bad")));
});

// Pre-select a service from ?service= or a link with data-service
const pre = new URLSearchParams(location.search).get("service");
if (pre) document.querySelectorAll(`input[name=service][value="${CSS.escape(pre)}"]`).forEach((i) => (i.checked = true));
document.querySelectorAll("[data-service]").forEach((a) =>
  a.addEventListener("click", () => {
    document.querySelectorAll(`input[name=service][value="${CSS.escape(a.dataset.service)}"]`).forEach((i) => (i.checked = true));
  })
);

// Gallery filters
const filterBtns = document.querySelectorAll(".filters button");
filterBtns.forEach((b) =>
  b.addEventListener("click", () => {
    filterBtns.forEach((x) => x.setAttribute("aria-pressed", x === b));
    const f = b.dataset.filter;
    document.querySelectorAll(".gallery a").forEach((a) => (a.hidden = f !== "all" && a.dataset.cat !== f));
  })
);

// Lightbox
const lb = document.querySelector(".lb");
if (lb) {
  const img = lb.querySelector("img");
  const cap = lb.querySelector(".lb-cap");
  let items = [], idx = 0, last = null;
  const show = (i) => {
    idx = (i + items.length) % items.length;
    const a = items[idx];
    img.src = a.getAttribute("href");
    img.alt = a.querySelector("img")?.alt || "";
    cap.textContent = a.dataset.caption || img.alt;
  };
  document.querySelectorAll("[data-lb] a").forEach((a) =>
    a.addEventListener("click", (e) => {
      e.preventDefault();
      last = a;
      items = [...a.closest("[data-lb]").querySelectorAll("a")].filter((x) => !x.hidden);
      show(items.indexOf(a));
      lb.classList.add("open");
      document.body.style.overflow = "hidden";
      lb.querySelector(".lb-close").focus();
    })
  );
  const close = () => { lb.classList.remove("open"); document.body.style.overflow = ""; last?.focus(); };
  lb.querySelector(".lb-close").addEventListener("click", close);
  lb.querySelector(".lb-prev").addEventListener("click", () => show(idx - 1));
  lb.querySelector(".lb-next").addEventListener("click", () => show(idx + 1));
  lb.addEventListener("click", (e) => { if (e.target === lb) close(); });
  document.addEventListener("keydown", (e) => {
    if (!lb.classList.contains("open")) return;
    if (e.key === "Escape") close();
    if (e.key === "ArrowLeft") show(idx - 1);
    if (e.key === "ArrowRight") show(idx + 1);
  });
  let sx = null;
  lb.addEventListener("touchstart", (e) => (sx = e.touches[0].clientX), { passive: true });
  lb.addEventListener("touchend", (e) => {
    if (sx === null) return;
    const dx = e.changedTouches[0].clientX - sx;
    if (Math.abs(dx) > 50) show(idx + (dx < 0 ? 1 : -1));
    sx = null;
  });
}

document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
