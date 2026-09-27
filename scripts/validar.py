#!/usr/bin/env python3
"""Valida o marketplace: frontmatter de cada SKILL.md, nome = pasta, JSONs válidos,
scripts compilam, e nenhum travessão (em dash) nos textos."""
import json, glob, os, re, py_compile, sys
raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
erros = []
for f in glob.glob(f"{raiz}/**/*.json", recursive=True):
    try: json.load(open(f, encoding="utf-8"))
    except Exception as e: erros.append(f"JSON inválido: {f}: {e}")
skills = sorted(glob.glob(f"{raiz}/plugins/*/skills/*/SKILL.md"))
for s in skills:
    txt = open(s, encoding="utf-8").read()
    m = re.match(r"^---\nname: (.+)\ndescription: (.+)\n---\n", txt)
    if not m: erros.append(f"frontmatter inválido: {s}"); continue
    pasta = os.path.basename(os.path.dirname(s))
    if m.group(1).strip() != pasta: erros.append(f"name '{m.group(1)}' difere da pasta '{pasta}'")
    if len(m.group(2)) < 120: erros.append(f"descrição curta demais: {s}")
    if txt.count("\n") > 500: erros.append(f"SKILL.md acima de 500 linhas: {s}")
for f in glob.glob(f"{raiz}/plugins/**/*.md", recursive=True) + glob.glob(f"{raiz}/plugins/**/*.html", recursive=True):
    if "—" in open(f, encoding="utf-8").read(): erros.append(f"travessão encontrado: {f}")
for f in glob.glob(f"{raiz}/plugins/**/*.py", recursive=True):
    try: py_compile.compile(f, doraise=True)
    except Exception as e: erros.append(f"script não compila: {f}: {e}")
mk = json.load(open(f"{raiz}/.claude-plugin/marketplace.json"))
for p in mk["plugins"]:
    if not os.path.isfile(os.path.join(raiz, p["source"], ".claude-plugin", "plugin.json")):
        erros.append(f"plugin sem manifest: {p['source']}")
print(f"{len(skills)} skills encontradas")
if erros:
    print("\n".join(erros)); sys.exit(1)
print("tudo válido")
