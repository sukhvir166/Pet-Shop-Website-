import re
import os

path = r'C:\Users\HP\.gemini\antigravity\scratch\pawdacity\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

title = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
print('Title:', title.group(1) if title else 'N/A')

sections = re.findall(r'<section[^>]*id=["\'](.*?)["\']', html)
print('Sections:', sections)

funcs = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', html)
print(f'Total functions: {len(funcs)}')
print('Sample functions:', funcs[:40])

storage = set(re.findall(r'localStorage\.(?:getItem|setItem|removeItem)\([\'"]([^\'"]+)[\'"]', html))
print('localStorage keys:', sorted(list(storage)))

products = re.search(r'const\s+PRODUCTS\s*=\s*(\[.*?\]);', html, re.DOTALL)
if products:
    print('Found PRODUCTS constant!')
else:
    # check other product structures
    m = re.findall(r'(PRODUCTS|products|catalog|services)\s*[:=]', html)
    print('Product matches:', m)

print('File size in KB:', round(len(html)/1024, 2))
