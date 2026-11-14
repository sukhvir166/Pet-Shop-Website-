with open(r'C:\Users\HP\.gemini\antigravity\scratch\pawdacity\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
scripts = re.findall(r'<script.*?>([\s\S]*?)</script>', html)
print('Number of scripts:', len(scripts))
for i, s in enumerate(scripts):
    print(f'Script {i} length: {len(s)}')
    lines = s.strip().split('\n')
    print(f'Script {i} first 10 lines:')
    for line in lines[:15]:
        print('  ', line[:100])
