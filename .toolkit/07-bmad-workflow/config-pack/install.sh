#!/usr/bin/env bash
# Wire the Hackathon Toolkit into a BMad-enabled hackathon repo.
# Usage (from anywhere):  bash install.sh /path/to/your-hackathon-repo [--dry-run]
# Safe by default: never overwrites existing files (prints SKIP instead).
set -euo pipefail

TARGET="${1:?usage: install.sh <hackathon-repo> [--dry-run]}"
DRY="${2:-}"
PACK="$(cd "$(dirname "$0")" && pwd)"
TOOLKIT="$(cd "$PACK/../.." && pwd)"

run() { if [ "$DRY" = "--dry-run" ]; then echo "DRY  $*"; else eval "$@"; fi; }
copy_new() {  # copy_new <src> <dst>
  if [ -e "$2" ]; then echo "SKIP $2 (exists)"; else run "mkdir -p \"$(dirname "$2")\" && cp \"$1\" \"$2\""; echo "ADD  $2"; fi
}

[ -d "$TARGET/_bmad" ] || { echo "No _bmad/ in $TARGET: run 'npx bmad-method install' there first."; exit 1; }

# 1. Vendor the toolkit (docs only, no research raw data) into .toolkit/
if [ -e "$TARGET/.toolkit" ]; then echo "SKIP $TARGET/.toolkit (exists; delete it to refresh)"; else
  run "mkdir -p \"$TARGET/.toolkit\""
  for d in 07-bmad-workflow 01-hackathon-playbook 02-frontend 03-backend 04-ai-and-rag 05-tools-and-mcp 06-repo-catalog skills README.md; do
    run "cp -r \"$TOOLKIT/$d\" \"$TARGET/.toolkit/\""
  done
  echo "ADD  $TARGET/.toolkit/"
fi

# 2. BMad overrides (_bmad/custom/*.toml): these wire the toolkit into each skill
for f in "$PACK"/_bmad/custom/*.toml; do copy_new "$f" "$TARGET/_bmad/custom/$(basename "$f")"; done

# 3. The hub file every BMad skill auto-loads
copy_new "$PACK/project-context.template.md" "$TARGET/project-context.md"

# 4. Project docs from templates (docs-as-code)
for t in research prd tech-stack design; do copy_new "$TOOLKIT/01-hackathon-playbook/templates/$t.md" "$TARGET/docs/$t.md"; done
[ -e "$TARGET/AI_USAGE.md" ] || { run "printf '# AI Usage Disclosure\n\n| When | Tool | What for | Files / assets | Human edits |\n| --- | --- | --- | --- | --- |\n' > \"$TARGET/AI_USAGE.md\""; echo "ADD  $TARGET/AI_USAGE.md"; }

# 5. Project-scoped Claude Code skills
for s in "$TOOLKIT"/skills/hackathon-*; do
  dst="$TARGET/.claude/skills/$(basename "$s")"
  if [ -e "$dst" ]; then echo "SKIP $dst (exists)"; else run "mkdir -p \"$TARGET/.claude/skills\" && cp -r \"$s\" \"$dst\""; echo "ADD  $dst"; fi
done

echo
echo "Next: fill project-context.md + docs/research.md, then in Claude Code run /bmad-help."
