"""Hub-and-spoke footer: every page links to /solutions/, the FAQ hub and the calculator (idempotent).
Usage: python3 footer_links.py <site root>"""
import re, sys
from pathlib import Path

LINKS = [("/solutions/", "Solutions"), ("/freight-quote-faq.html", "Freight quote FAQ"),
         ("/freight-calculator.html", "Freight calculator")]
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
changed = 0
for f in sorted(ROOT.rglob("*.html")):
    rel = f.relative_to(ROOT).as_posix()
    if rel.startswith(".") or "/." in rel:
        continue
    html = f.read_text(encoding="utf-8")
    m = re.search(r"<footer[^>]*>(.*?)</footer>", html, re.S)
    if not m:
        continue
    foot = m.group(1)
    add = [f'<a href="{h}">{t}</a>' for h, t in LINKS
           if f'href="{h}"' not in foot and rel not in (h.lstrip("/"), h.lstrip("/") + "index.html")]
    if not add:
        continue
    extra = " · " + " · ".join(add)
    for anchor in ('<a href="/blog/">Articles</a>', '<a href="/privacy.html">Privacy</a>'):
        if anchor in foot:
            new_foot = foot.replace(anchor, anchor + extra, 1)
            break
    else:
        new_foot = foot.rstrip() + extra
    html = html[:m.start(1)] + new_foot + html[m.end(1):]
    f.write_text(html, encoding="utf-8")
    changed += 1
print(changed, "page(s) updated")
