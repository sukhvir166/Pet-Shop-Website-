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
