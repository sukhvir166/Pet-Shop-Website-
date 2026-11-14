import os

assets_dir = r'C:\Users\HP\.gemini\antigravity\scratch\pawdacity\assets'
os.makedirs(assets_dir, exist_ok=True)

# 1. banner.svg
banner_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="100%" height="auto">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#12065e"/>
      <stop offset="50%" stop-color="#1a0a7a"/>
      <stop offset="100%" stop-color="#2a0845"/>
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffd08a"/>
      <stop offset="100%" stop-color="#f8a62a"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fc7b5f"/>
      <stop offset="100%" stop-color="#ff4f8b"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="15" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="1200" height="420" rx="24" fill="url(#bgGrad)"/>
  <rect x="15" y="15" width="1170" height="390" rx="18" fill="none" stroke="#f8a62a" stroke-width="2" stroke-opacity="0.4"/>

  <!-- Background Decorative Circles -->
  <circle cx="1050" cy="210" r="160" fill="url(#goldGrad)" opacity="0.08"/>
  <circle cx="1050" cy="210" r="120" fill="url(#accentGrad)" opacity="0.12"/>
  <circle cx="150" cy="380" r="90" fill="#27b4e0" opacity="0.05"/>

  <!-- Eyebrow Pill -->
  <g transform="translate(60, 55)">
    <rect width="320" height="34" rx="17" fill="#ffffff" fill-opacity="0.1" stroke="#fc7b5f" stroke-width="1.5"/>
    <text x="160" y="22" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="12" font-weight="bold" fill="#fc7b5f" text-anchor="middle" letter-spacing="1.5">PHILIPPINES PET COMMERCE SUITE</text>
  </g>

  <!-- Main Headline -->
  <text x="60" y="160" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="64" font-weight="900" fill="#ffffff" letter-spacing="-1">PAWDACITY</text>
  <text x="445" y="160" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="28" font-weight="bold" fill="url(#goldGrad)">PET SHOP PH</text>

  <!-- Subtitle -->
  <text x="60" y="210" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="20" font-weight="500" fill="#ffd08a">Clean pets, happy hearts! • Complete Zero-Dependency Client-Side Web App</text>
  <text x="60" y="240" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="15" fill="#cdd6f4">30 Products Catalog • Multi-Payment (GCash / Maya) • Salon Booking • Owner Studio (Ctrl+K) • SheetJS .XLSX</text>

  <!-- Feature Pills -->
  <g transform="translate(60, 290)">
    <!-- Pill 1 -->
    <rect x="0" y="0" width="135" height="42" rx="21" fill="#f8a62a"/>
    <text x="67" y="26" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1a0a7a" text-anchor="middle">Vanilla JS (ES6+)</text>
    <!-- Pill 2 -->
    <rect x="150" y="0" width="165" height="42" rx="21" fill="#ffffff" fill-opacity="0.15" stroke="#f8a62a" stroke-width="1.5"/>
    <text x="232" y="26" font-family="sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">Owner Studio [Ctrl+K]</text>
    <!-- Pill 3 -->
    <rect x="330" y="0" width="145" height="42" rx="21" fill="#ffffff" fill-opacity="0.15" stroke="#27b4e0" stroke-width="1.5"/>
    <text x="402" y="26" font-family="sans-serif" font-size="13" font-weight="bold" fill="#27b4e0" text-anchor="middle">SheetJS Multi-Sheet</text>
    <!-- Pill 4 -->
    <rect x="490" y="0" width="145" height="42" rx="21" fill="#ffffff" fill-opacity="0.15" stroke="#fc7b5f" stroke-width="1.5"/>
    <text x="562" y="26" font-family="sans-serif" font-size="13" font-weight="bold" fill="#fc7b5f" text-anchor="middle">GCash, Maya &amp; COD</text>
    <!-- Pill 5 -->
    <rect x="650" y="0" width="140" height="42" rx="21" fill="#ffffff" fill-opacity="0.15" stroke="#8cc63f" stroke-width="1.5"/>
    <text x="720" y="26" font-family="sans-serif" font-size="13" font-weight="bold" fill="#8cc63f" text-anchor="middle">Salon Appointments</text>
  </g>

  <!-- Right Graphic Badge -->
  <g transform="translate(1000, 150)">
    <circle cx="50" cy="50" r="75" fill="#f8a62a" fill-opacity="0.2" stroke="#f8a62a" stroke-width="3"/>
    <circle cx="50" cy="50" r="55" fill="#1a0a7a" stroke="#fc7b5f" stroke-width="2"/>
    <!-- Paw shape drawing -->
    <ellipse cx="50" cy="58" rx="22" ry="17" fill="#ffffff"/>
    <circle cx="34" cy="38" r="7.5" fill="#ffffff"/>
    <circle cx="45" cy="31" r="7.5" fill="#ffffff"/>
    <circle cx="56" cy="31" r="7.5" fill="#ffffff"/>
    <circle cx="67" cy="38" r="7.5" fill="#ffffff"/>
    <text x="50" y="98" font-family="sans-serif" font-size="11" font-weight="bold" fill="#ffd08a" text-anchor="middle">100% OFFLINE</text>
  </g>
</svg>
'''

with open(os.path.join(assets_dir, 'banner.svg'), 'w', encoding='utf-8') as f:
    f.write(banner_svg)
print("Saved banner.svg")

# 2. architecture.svg
arch_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 560" width="100%" height="auto">
  <defs>
    <linearGradient id="boxHdr" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1a0a7a"/>
      <stop offset="100%" stop-color="#2a109e"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect width="1100" height="560" rx="16" fill="#f8fafc"/>
  <rect x="12" y="12" width="1076" height="536" rx="12" fill="none" stroke="#e2e8f0" stroke-width="1.5"/>

  <!-- Title -->
  <text x="550" y="48" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="22" font-weight="900" fill="#1a0a7a" text-anchor="middle">PAWDACITY SYSTEM ARCHITECTURE &amp; DATA ENGINE</text>
  <text x="550" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Single-File Architecture with Reactive CSS Properties and Partitioned Web Storage</text>

  <!-- Col 1: Presentation Layer -->
  <g transform="translate(40, 100)" filter="url(#shadow)">
    <rect width="300" height="410" rx="12" fill="#ffffff" stroke="#1a0a7a" stroke-width="2"/>
    <path d="M0,12 Q0,0 12,0 L288,0 Q300,0 300,12 L300,45 L0,45 Z" fill="#1a0a7a"/>
    <text x="150" y="28" font-family="sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. PRESENTATION LAYER (UI)</text>
    
    <g transform="translate(15, 60)">
      <rect width="270" height="50" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Hero &amp; Category Tiles</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#64748b">Dynamic headings, brand logo &amp; quick chips</text>
    </g>
    <g transform="translate(15, 118)">
      <rect width="270" height="50" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Product Catalog &amp; QuickView</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#64748b">30 items, multi-image carousels, modal viewer</text>
    </g>
    <g transform="translate(15, 176)">
      <rect width="270" height="50" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Cart Drawer &amp; Promos</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#64748b">₱999 free shipping meter &amp; active coupon codes</text>
    </g>
    <g transform="translate(15, 234)">
      <rect width="270" height="50" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Salon Booking Form</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#64748b">Grooming &amp; vet scheduling with slot verification</text>
    </g>
    <g transform="translate(15, 292)">
      <rect width="270" height="50" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Owner Panel (Ctrl+K)</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#64748b">Live styling, palettes, fonts, product editor</text>
    </g>
    <g transform="translate(15, 350)">
      <rect width="270" height="45" rx="8" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="12" y="20" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0f172a">Developer Easter Egg</text>
      <text x="12" y="34" font-family="sans-serif" font-size="10" fill="#64748b">Matrix rain falling-code terminal &amp; dev profile</text>
    </g>
  </g>

  <!-- Arrow 1 to 2 -->
  <path d="M355,300 L385,300" stroke="#1a0a7a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>

  <!-- Col 2: Logic & Reactive Core -->
  <g transform="translate(400, 100)" filter="url(#shadow)">
    <rect width="300" height="410" rx="12" fill="#ffffff" stroke="#f8a62a" stroke-width="2"/>
    <path d="M0,12 Q0,0 12,0 L288,0 Q300,0 300,12 L300,45 L0,45 Z" fill="#f8a62a"/>
    <text x="150" y="28" font-family="sans-serif" font-size="13" font-weight="bold" fill="#1a0a7a" text-anchor="middle">2. LOGIC &amp; STATE ENGINE</text>
    
    <g transform="translate(15, 60)">
      <rect width="270" height="50" rx="8" fill="#fffbeb" stroke="#fde68a"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#92400e">CSS Variables Engine [apply()]</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#78350f">Mutates --ind, --or, --co, --pk, --fd, --rad, --shd</text>
    </g>
    <g transform="translate(15, 118)">
      <rect width="270" height="50" rx="8" fill="#fffbeb" stroke="#fde68a"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#92400e">Search &amp; Filter [render()]</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#78350f">Live text query, category sorting, price slider</text>
    </g>
    <g transform="translate(15, 176)">
      <rect width="270" height="50" rx="8" fill="#fffbeb" stroke="#fde68a"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#92400e">Cart Calculator [tot()]</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#78350f">Subtotal, PAW10 / WELCOME50, shipping rules</text>
    </g>
    <g transform="translate(15, 234)">
      <rect width="270" height="50" rx="8" fill="#fffbeb" stroke="#fde68a"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#92400e">Collision Checker [drawBk()]</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#78350f">Validates date &amp; time slots against pc_bk</text>
    </g>
    <g transform="translate(15, 292)">
      <rect width="270" height="50" rx="8" fill="#fffbeb" stroke="#fde68a"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#92400e">Canvas Downscaler [rd()]</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#78350f">Resamples images to 800px JPEG (82% quality)</text>
    </g>
    <g transform="translate(15, 350)">
      <rect width="270" height="45" rx="8" fill="#fffbeb" stroke="#fde68a"/>
      <text x="12" y="20" font-family="sans-serif" font-size="12" font-weight="bold" fill="#92400e">Order Dispatcher [pay()]</text>
      <text x="12" y="34" font-family="sans-serif" font-size="10" fill="#78350f">Generates PAW-XXXXXX &amp; mailto order intent</text>
    </g>
  </g>

  <!-- Arrow 2 to 3 -->
  <path d="M715,300 L745,300" stroke="#f8a62a" stroke-width="3" fill="none"/>

  <!-- Col 3: Storage & Integration -->
  <g transform="translate(760, 100)" filter="url(#shadow)">
    <rect width="300" height="410" rx="12" fill="#ffffff" stroke="#27b4e0" stroke-width="2"/>
    <path d="M0,12 Q0,0 12,0 L288,0 Q300,0 300,12 L300,45 L0,45 Z" fill="#27b4e0"/>
    <text x="150" y="28" font-family="sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. PERSISTENCE &amp; EXPORTS</text>
    
    <g transform="translate(15, 60)">
      <rect width="270" height="50" rx="8" fill="#f0f9ff" stroke="#bae6fd"/>
      <text x="12" y="22" font-family="monospace" font-size="12" font-weight="bold" fill="#0369a1">pc_set</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#0284c7">Branding, colors, fonts, shadow, overrides</text>
    </g>
    <g transform="translate(15, 118)">
      <rect width="270" height="50" rx="8" fill="#f0f9ff" stroke="#bae6fd"/>
      <text x="12" y="22" font-family="monospace" font-size="12" font-weight="bold" fill="#0369a1">pc_cart</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#0284c7">Array of [{id: Number, q: Number}] items</text>
    </g>
    <g transform="translate(15, 176)">
      <rect width="270" height="50" rx="8" fill="#f0f9ff" stroke="#bae6fd"/>
      <text x="12" y="22" font-family="monospace" font-size="12" font-weight="bold" fill="#0369a1">pc_orders</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#0284c7">Ledger: order no, customer, total, date, items</text>
    </g>
    <g transform="translate(15, 234)">
      <rect width="270" height="50" rx="8" fill="#f0f9ff" stroke="#bae6fd"/>
      <text x="12" y="22" font-family="monospace" font-size="12" font-weight="bold" fill="#0369a1">pc_bk &amp; pc_users</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#0284c7">Appointment schedules &amp; user credentials</text>
    </g>
    <g transform="translate(15, 292)">
      <rect width="270" height="50" rx="8" fill="#f0f9ff" stroke="#bae6fd"/>
      <text x="12" y="22" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1">SheetJS Multi-Sheet XLSX</text>
      <text x="12" y="38" font-family="sans-serif" font-size="10" fill="#0284c7">Compiles Purchases, Users, Products sheets</text>
    </g>
    <g transform="translate(15, 350)">
      <rect width="270" height="45" rx="8" fill="#f0f9ff" stroke="#bae6fd"/>
      <text x="12" y="20" font-family="sans-serif" font-size="12" font-weight="bold" fill="#0369a1">CSV Fallback with Escaping</text>
      <text x="12" y="34" font-family="sans-serif" font-size="10" fill="#0284c7">Formula sanitization (prevents =/@ injection)</text>
    </g>
  </g>
</svg>
'''

with open(os.path.join(assets_dir, 'architecture.svg'), 'w', encoding='utf-8') as f:
    f.write(arch_svg)
print("Saved architecture.svg")

# 3. features.svg
feat_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 480" width="100%" height="auto">
  <defs>
    <filter id="fShadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.06"/>
    </filter>
  </defs>

  <rect width="1100" height="480" rx="16" fill="#ffffff"/>
  <rect x="12" y="12" width="1076" height="456" rx="12" fill="none" stroke="#e2e8f0" stroke-width="1.5"/>

  <text x="550" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="22" font-weight="900" fill="#1a0a7a" text-anchor="middle">PAWDACITY CORE CAPABILITIES</text>
  <text x="550" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Engineered for seamless user discovery, shopping resilience, and rapid store operations</text>

  <!-- Feature Grid: 2 rows of 3 -->
  <!-- Card 1 -->
  <g transform="translate(40, 95)" filter="url(#fShadow)">
    <rect width="320" height="160" rx="12" fill="#ffffff" stroke="#1a0a7a" stroke-width="2"/>
    <rect x="18" y="18" width="44" height="44" rx="10" fill="#1a0a7a" fill-opacity="0.1"/>
    <text x="40" y="46" font-family="sans-serif" font-size="20" text-anchor="middle">🛍️</text>
    <text x="75" y="45" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Catalog &amp; QuickView</text>
    <text x="20" y="85" font-family="sans-serif" font-size="11.5" fill="#475569">30 products across 8 categories with procedural SVG badges, multi-photo carousels, and quick-view modal dialog.</text>
  </g>

  <!-- Card 2 -->
  <g transform="translate(390, 95)" filter="url(#fShadow)">
    <rect width="320" height="160" rx="12" fill="#ffffff" stroke="#f8a62a" stroke-width="2"/>
    <rect x="18" y="18" width="44" height="44" rx="10" fill="#f8a62a" fill-opacity="0.15"/>
    <text x="40" y="46" font-family="sans-serif" font-size="20" text-anchor="middle">🛒</text>
    <text x="75" y="45" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Cart &amp; Promotion Engine</text>
    <text x="20" y="85" font-family="sans-serif" font-size="11.5" fill="#475569">Persistent cart with dynamic ₱999 free delivery threshold meter, coupon deductions (PAW10, WELCOME50, FREESHIP).</text>
  </g>

  <!-- Card 3 -->
  <g transform="translate(740, 95)" filter="url(#fShadow)">
    <rect width="320" height="160" rx="12" fill="#ffffff" stroke="#fc7b5f" stroke-width="2"/>
    <rect x="18" y="18" width="44" height="44" rx="10" fill="#fc7b5f" fill-opacity="0.15"/>
    <text x="40" y="46" font-family="sans-serif" font-size="20" text-anchor="middle">💳</text>
    <text x="75" y="45" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Philippine Checkout</text>
    <text x="20" y="85" font-family="sans-serif" font-size="11.5" fill="#475569">Localized payment rails: GCash, Maya, Cards, &amp; COD. Synthesizes PAW-XXXXXX IDs and mailto order dispatch.</text>
  </g>

  <!-- Card 4 -->
  <g transform="translate(40, 280)" filter="url(#fShadow)">
    <rect width="320" height="160" rx="12" fill="#ffffff" stroke="#27b4e0" stroke-width="2"/>
    <rect x="18" y="18" width="44" height="44" rx="10" fill="#27b4e0" fill-opacity="0.15"/>
    <text x="40" y="46" font-family="sans-serif" font-size="20" text-anchor="middle">📅</text>
    <text x="75" y="45" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Salon Booking Engine</text>
    <text x="20" y="85" font-family="sans-serif" font-size="11.5" fill="#475569">Interactive scheduler for pet grooming and vet exams with strict slot collision prevention and confirmation mailers.</text>
  </g>

  <!-- Card 5 -->
  <g transform="translate(390, 280)" filter="url(#fShadow)">
    <rect width="320" height="160" rx="12" fill="#ffffff" stroke="#8cc63f" stroke-width="2"/>
    <rect x="18" y="18" width="44" height="44" rx="10" fill="#8cc63f" fill-opacity="0.15"/>
    <text x="40" y="46" font-family="sans-serif" font-size="20" text-anchor="middle">🎨</text>
    <text x="75" y="45" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">Owner Studio (Ctrl+K)</text>
    <text x="20" y="85" font-family="sans-serif" font-size="11.5" fill="#475569">Real-time theme editor: custom color pickers, 4 palettes, 8 Google fonts, border radius, canvas image downscaler.</text>
  </g>

  <!-- Card 6 -->
  <g transform="translate(740, 280)" filter="url(#fShadow)">
    <rect width="320" height="160" rx="12" fill="#ffffff" stroke="#ff4f8b" stroke-width="2"/>
    <rect x="18" y="18" width="44" height="44" rx="10" fill="#ff4f8b" fill-opacity="0.15"/>
    <text x="40" y="46" font-family="sans-serif" font-size="20" text-anchor="middle">📊</text>
    <text x="75" y="45" font-family="sans-serif" font-size="15" font-weight="bold" fill="#0f172a">SheetJS Multi-Sheet .XLSX</text>
    <text x="20" y="85" font-family="sans-serif" font-size="11.5" fill="#475569">Generates 3-sheet Excel reports (Purchases, Users, Products) or RFC CSV fallback with formula injection safety.</text>
  </g>
</svg>
'''

with open(os.path.join(assets_dir, 'features.svg'), 'w', encoding='utf-8') as f:
    f.write(feat_svg)
print("Saved features.svg")

# 4. palettes.svg
pal_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 380" width="100%" height="auto">
  <rect width="1000" height="380" rx="16" fill="#f8fafc"/>
  <rect x="12" y="12" width="976" height="356" rx="12" fill="none" stroke="#e2e8f0" stroke-width="1.5"/>

  <text x="500" y="45" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="20" font-weight="900" fill="#1a0a7a" text-anchor="middle">BUILT-IN COLOR THEME PALETTES</text>
  <text x="500" y="70" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12" fill="#64748b" text-anchor="middle">Switchable instantaneously via Owner Panel (Ctrl+K) or custom palette buttons</text>

  <!-- Palettes list -->
  <!-- 1. Pawdacity Classic -->
  <g transform="translate(50, 95)">
    <text x="0" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">Pawdacity Classic</text>
    <!-- Swatches -->
    <rect x="180" y="10" width="130" height="38" rx="6" fill="#1a0a7a"/>
    <text x="245" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#1a0a7a (Primary)</text>

    <rect x="325" y="10" width="130" height="38" rx="6" fill="#f8a62a"/>
    <text x="390" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#1a0a7a" text-anchor="middle">#f8a62a (Accent 1)</text>

    <rect x="470" y="10" width="130" height="38" rx="6" fill="#fc7b5f"/>
    <text x="535" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#fc7b5f (Accent 2)</text>

    <rect x="615" y="10" width="130" height="38" rx="6" fill="#ff4f8b"/>
    <text x="680" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#ff4f8b (Highlight)</text>

    <rect x="760" y="10" width="130" height="38" rx="6" fill="#fff8ee" stroke="#cbd5e1"/>
    <text x="825" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">#fff8ee (Page BG)</text>
  </g>

  <!-- 2. Ocean Breeze -->
  <g transform="translate(50, 160)">
    <text x="0" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">Ocean Breeze</text>
    <rect x="180" y="10" width="130" height="38" rx="6" fill="#0b2a5b"/>
    <text x="245" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#0b2a5b</text>

    <rect x="325" y="10" width="130" height="38" rx="6" fill="#27b4e0"/>
    <text x="390" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#27b4e0</text>

    <rect x="470" y="10" width="130" height="38" rx="6" fill="#4f8cff"/>
    <text x="535" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#4f8cff</text>

    <rect x="615" y="10" width="130" height="38" rx="6" fill="#0aa5a0"/>
    <text x="680" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#0aa5a0</text>

    <rect x="760" y="10" width="130" height="38" rx="6" fill="#f1f9ff" stroke="#cbd5e1"/>
    <text x="825" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">#f1f9ff</text>
  </g>

  <!-- 3. Forest Emerald -->
  <g transform="translate(50, 225)">
    <text x="0" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">Forest Emerald</text>
    <rect x="180" y="10" width="130" height="38" rx="6" fill="#12361f"/>
    <text x="245" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#12361f</text>

    <rect x="325" y="10" width="130" height="38" rx="6" fill="#8cc63f"/>
    <text x="390" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#12361f" text-anchor="middle">#8cc63f</text>

    <rect x="470" y="10" width="130" height="38" rx="6" fill="#e8a33d"/>
    <text x="535" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#e8a33d</text>

    <rect x="615" y="10" width="130" height="38" rx="6" fill="#d9544d"/>
    <text x="680" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#d9544d</text>

    <rect x="760" y="10" width="130" height="38" rx="6" fill="#f6fbef" stroke="#cbd5e1"/>
    <text x="825" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">#f6fbef</text>
  </g>

  <!-- 4. Berry Velvet -->
  <g transform="translate(50, 290)">
    <text x="0" y="32" font-family="sans-serif" font-size="14" font-weight="bold" fill="#1e293b">Berry Velvet</text>
    <rect x="180" y="10" width="130" height="38" rx="6" fill="#4a0f3d"/>
    <text x="245" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#4a0f3d</text>

    <rect x="325" y="10" width="130" height="38" rx="6" fill="#ff8fb1"/>
    <text x="390" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#4a0f3d" text-anchor="middle">#ff8fb1</text>

    <rect x="470" y="10" width="130" height="38" rx="6" fill="#c94fa0"/>
    <text x="535" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#c94fa0</text>

    <rect x="615" y="10" width="130" height="38" rx="6" fill="#e0245e"/>
    <text x="680" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">#e0245e</text>

    <rect x="760" y="10" width="130" height="38" rx="6" fill="#fff3f8" stroke="#cbd5e1"/>
    <text x="825" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">#fff3f8</text>
  </g>
</svg>
'''

with open(os.path.join(assets_dir, 'palettes.svg'), 'w', encoding='utf-8') as f:
    f.write(pal_svg)
print("Saved palettes.svg")
print("All vector SVG assets generated!")
