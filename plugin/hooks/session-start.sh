#!/usr/bin/env bash
# SessionStart hook: give this agent an identity and tell it what it may adopt.
#
# Wire it in settings.json (the operator does this; the plugin does not assume it):
#
#   { "hooks": { "SessionStart": [ { "matcher": "startup",
#       "hooks": [ { "type": "command",
#                    "command": "$CLAUDE_PROJECT_DIR/plugin/hooks/session-start.sh" } ] } ] } }
#
# It prints context, never instructions. An agent that starts already knowing
# which prompts exist does not have to be told mid-task, and a hook that pushed
# adoptions instead of listing them would be adopting on nobody's authority.
set -uo pipefail
here=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
cd "$here" || exit 0

bin/fp-agent --ensure >/dev/null 2>&1
id=$(bin/fp-agent --id 2>/dev/null || echo unidentified)

signed="unsigned"
if bin/fp-verify >/dev/null 2>&1 </dev/null; then
  signed="signed manifest verified"
elif [ -f index.json.sig ]; then
  signed="SIGNATURE PRESENT BUT NOT VERIFIED -- treat as unsigned"
fi

pinned=$(grep -cv '^#\|^$' fpa.lock 2>/dev/null || echo 0)

printf 'agent %s · %s · %s pinned in fpa.lock\n' "$id" "$signed" "$pinned"
printf 'Foreign prompts available here (adopt with /f:prompt, browse with /f:find):\n'
bin/fp-resolve --list 2>/dev/null | sed 's/^/  /'
printf 'Nothing above is adopted. Adoption is an act, not a listing.\n'
