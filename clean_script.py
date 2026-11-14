-- clean_script.py

with open(r'C:\Users\HP\.gemini\antigravity\scratch\pawdacity\index.html', 'r', encoding='utf-8') as f:
    html = f.read()
import re
script = re.findall(r'<script.*?>([\s\S]*?)</script>', html)[1]
# Remove the huge base64 IMG dictionary for analysis
script_clean = re.sub(r'const IMG=\{.*?\};', 'const IMG={/* images */};', script)
with open(r'C:\Users\HP\.gemini\antigravity\scratch\pawdacity\script_analyzed.js', 'w', encoding='utf-8') as f:
    f.write(script_clean)
print("Saved script_analyzed.js without image blobs. Size:", len(script_clean))


