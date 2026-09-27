#!/usr/bin/env bash
# Gera um .zip por skill (para subir no claude.ai em Configurações > Capacidades > Skills)
# e um .zip por plugin (para entrega paga). Saída em ./dist
set -e
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist/skills dist/plugins
for plugin in plugins/*/; do
  p=$(basename "$plugin")
  (cd plugins && zip -qr "../dist/plugins/$p.zip" "$p")
  for skill in "$plugin"skills/*/; do
    s=$(basename "$skill")
    (cd "$plugin/skills" && zip -qr "../../../dist/skills/$s.zip" "$s")
  done
done
echo "Skills individuais:"; ls dist/skills
echo "Plugins:"; ls dist/plugins
