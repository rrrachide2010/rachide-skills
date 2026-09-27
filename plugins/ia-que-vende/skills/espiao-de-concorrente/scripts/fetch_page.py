#!/usr/bin/env python3
"""Baixa uma página pública, limpa parâmetros de rastreio e extrai texto e links.

Uso: python fetch_page.py <url> [--links-only]
"""
import sys, re, html, urllib.request, urllib.parse

def limpar(url):
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((p.scheme or "https", p.netloc, p.path, "", ""))

def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; espiao/1.0)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.geturl(), r.read().decode("utf-8", "ignore")

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    url = limpar(sys.argv[1])
    final, body = baixar(url)
    links = sorted(set(re.findall(r'href=["\']([^"\']+)["\']', body)))
    links = [urllib.parse.urljoin(final, l) for l in links if not l.startswith(("#", "javascript:", "mailto:"))]
    if "--links-only" not in sys.argv:
        texto = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body, flags=re.S | re.I)
        texto = re.sub(r"<[^>]+>", " ", texto)
        texto = html.unescape(re.sub(r"\s+", " ", texto)).strip()
        print(f"URL final: {final}\n")
        print(texto[:12000])
        print("\n\n=== LINKS ===")
    for l in links:
        print(l)

if __name__ == "__main__":
    main()
