#!/usr/bin/env python3
import json, sys
try:
    d = json.load(open('/Users/laplace/.zcode/workspace/default/gpt-image-25-run/progress.json'))
except Exception:
    d = {}
mode = sys.argv[1] if len(sys.argv) > 1 else 'done'
if mode == 'done':
    print(sum(1 for v in d.values() if v.get('status') == 'done'))
elif mode == 'ratelimit':
    print(any(v.get('status') == 'ratelimit' for v in d.values()))
elif mode == 'failed':
    for k, v in sorted(d.items(), key=lambda x: int(x[0])):
        if v.get('status') not in ('done',):
            print(k, v.get('status'), (v.get('err') or '')[:60])
