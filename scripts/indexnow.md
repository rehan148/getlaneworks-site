# IndexNow (Bing / Yandex / Copilot index) for getlaneworks.com

Key file: /8feac553b0bd86565a86c37d7205e98b.txt (public by design). Submitted all 61 sitemap URLs on 4 Nov 2026
(HTTP 200). After publishing or changing pages, resubmit from any browser tab open on getlaneworks.com
(the API refuses cross-origin POSTs, so use one no-cors GET per URL):

    const urls = await fetch('/sitemap.xml',{cache:'no-store'}).then(r=>r.text()).then(t=>[...t.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m=>m[1]));
    for (const u of urls) await fetch('https://api.indexnow.org/indexnow?url='+encodeURIComponent(u)+'&key=8feac553b0bd86565a86c37d7205e98b&keyLocation='+encodeURIComponent('https://getlaneworks.com/8feac553b0bd86565a86c37d7205e98b.txt'),{mode:'no-cors',cache:'no-store'});

Google ignores IndexNow; Search Console + sitemap covers Google.
