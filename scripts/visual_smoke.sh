#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
out="/home/ubuntu/Capital-uiux-v2-screens"
mkdir -p "$out"
for page in index.html availability.html leasing.html visit.html resources.html; do
  name="${page%.html}"
  chromium --headless --no-sandbox --disable-gpu --hide-scrollbars --run-all-compositor-stages-before-draw --window-size=1440,1000 --screenshot="$out/${name}-desktop.png" "http://127.0.0.1:4173/$page" >/tmp/chromium-${name}-desktop.log 2>&1
  chromium --headless --no-sandbox --disable-gpu --hide-scrollbars --run-all-compositor-stages-before-draw --window-size=390,844 --screenshot="$out/${name}-mobile.png" "http://127.0.0.1:4173/$page" >/tmp/chromium-${name}-mobile.log 2>&1
done
printf '%s\n' "Visual smoke screenshots written to $out"
