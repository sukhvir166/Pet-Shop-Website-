import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.environ['MPLCONFIGDIR'] = 'C:/Users/HP/AppData/Local/Temp'
assets_dir = r'C:\Users\HP\.gemini\antigravity\scratch\pawdacity\assets'
os.makedirs(assets_dir, exist_ok=True)

# 1. BANNER
def make_banner():
    fig, ax = plt.subplots(figsize=(12, 4.2), dpi=150)
    fig.patch.set_facecolor('#1a0a7a')
    ax.set_facecolor('#1a0a7a')
    
    rect = patches.FancyBboxPatch((0.02, 0.05), 0.96, 0.9, boxstyle="round,pad=0.02,rounding_size=0.04", 
                                  facecolor='#261596', edgecolor='#f8a62a', linewidth=2.5)
    ax.add_patch(rect)
    
    ax.text(0.08, 0.78, "🐾 PHILIPPINES PET COMMERCE & CARE SUITE", fontsize=11, fontweight='bold', 
            color='#fc7b5f', family='sans-serif', va='center')
    ax.text(0.08, 0.54, "PAWDACITY", fontsize=40, fontweight='black', 
            color='#ffffff', family='sans-serif', va='center')
    ax.text(0.08, 0.34, "Clean pets, happy hearts! • Complete Client-Side Web Application", fontsize=13.5, 
            color='#ffd08a', family='sans-serif', va='center')
    
    pills = ["Vanilla JS", "Owner Studio (Ctrl+K)", "SheetJS .XLSX", "GCash & Maya", "Booking Engine", "Dark/Light Theme"]
    x_pos = 0.08
    for p in pills:
        pw = len(p)*0.0105 + 0.028
        pill_box = patches.FancyBboxPatch((x_pos, 0.12), pw, 0.11, boxstyle="round,pad=0.01", 
                                          facecolor='#f8a62a', edgecolor='none')
        ax.add_patch(pill_box)
        ax.text(x_pos + pw/2, 0.175, p, fontsize=8, fontweight='bold', 
                color='#1a0a7a', family='sans-serif', ha='center', va='center')
        x_pos += pw + 0.018

    circle = patches.Circle((0.84, 0.5), 0.32, facecolor='#f8a62a', alpha=0.18)
    ax.add_patch(circle)
    circle2 = patches.Circle((0.84, 0.5), 0.25, facecolor='#ffffff', alpha=0.1)
    ax.add_patch(circle2)
    ax.text(0.84, 0.5, "🐾🐕🐈", fontsize=38, ha='center', va='center')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join(assets_dir, 'banner.png'), facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print("Created banner.png")

# 2. ARCHITECTURE DIAGRAM
def make_architecture():
    fig, ax = plt.subplots(figsize=(12, 7), dpi=150)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8f9fa')
    
    # Outer frame
    frame = patches.FancyBboxPatch((0.02, 0.02), 0.96, 0.96, boxstyle="round,pad=0.02", 
                                  facecolor='#ffffff', edgecolor='#e2e8f0', linewidth=1.5)
    ax.add_patch(frame)
    
    ax.text(0.5, 0.94, "PAWDACITY SYSTEM ARCHITECTURE & DATA FLOW", fontsize=18, fontweight='black',
            color='#1a0a7a', ha='center', va='center')
    ax.text(0.5, 0.90, "Single-File Client-Side Architecture with Reactive Local State", fontsize=11,
            color='#64748b', ha='center', va='center')
    
    # Columns: 
    # Col 1: Presentation & UI Layer
    # Col 2: Reactive State & Engine Core
    # Col 3: Storage & Persistence (localStorage)
    # Col 4: Integrations & Fallbacks
    cols = [
        {"title": "1. PRESENTATION LAYER", "color": "#1a0a7a", "x": 0.05, "w": 0.27, "items": [
            ("Hero & Dynamic Banner", "Configurable headlines, logo, responsive navigation"),
            ("Catalog Grid (30 Items)", "Multi-image carousel, category chips, quick view"),
            ("Cart Drawer & Promo Bar", "Threshold progress bar (₱999 free ship), coupons"),
            ("Service Booking Form", "Date/time collision check, instant confirmation"),
            ("Owner Studio (Ctrl+K)", "Live theme editor, palette switch, product overrides"),
            ("Developer Easter Egg", "Matrix falling-code terminal & dev bio modal")
        ]},
        {"title": "2. ENGINE & LOGIC CORE", "color": "#f8a62a", "x": 0.36, "w": 0.28, "items": [
            ("CSS Variables Engine", "apply() drives live colors, fonts, radius & shadows"),
            ("Filtering & Search Engine", "render() live query, max price slider, category sort"),
            ("Discount & Pricing Rules", "tot() handles PAW10, WELCOME50, FREESHIP logic"),
            ("Client Image Downscaler", "rd() downsamples uploaded photos using HTML5 Canvas"),
            ("Order ID Generator", "PAW-XXXXXX sequence with multi-payment handler"),
            ("Auth & Role Validation", "logMode(), password reset generator & role toggles")
        ]},
        {"title": "3. PERSISTENCE & EXPORTS", "color": "#27b4e0", "x": 0.68, "w": 0.27, "items": [
            ("pc_set (Theme & Settings)", "Branding, palette, custom typography & overrides"),
            ("pc_cart (Cart Items)", "Array of {id, q} persisted across page refreshes"),
            ("pc_orders (Purchase History)", "Full audit logs of purchases, customer email, items"),
            ("pc_bk (Service Bookings)", "Persistent calendar of vet/grooming reservations"),
            ("pc_users & pc_user (Auth)", "User registry, hashed/stored roles & active session"),
            ("SheetJS Multi-Sheet Excel", "xl() creates Purchases, Users & Products workbook")
        ]}
    ]
    
    for c in cols:
        col_box = patches.FancyBboxPatch((c["x"], 0.06), c["w"], 0.81, boxstyle="round,pad=0.015",
                                         facecolor='#f8fafc', edgecolor=c["color"], linewidth=2)
        ax.add_patch(col_box)
        
        # Header banner
        hdr = patches.FancyBboxPatch((c["x"], 0.81), c["w"], 0.06, boxstyle="round,pad=0.01",
                                     facecolor=c["color"], edgecolor='none')
        ax.add_patch(hdr)
        ax.text(c["x"] + c["w"]/2, 0.84, c["title"], fontsize=10.5, fontweight='bold',
                color='#ffffff' if c["color"]!='#f8a62a' else '#1a0a7a', ha='center', va='center')
        
        # Items
        y = 0.74
        for name, desc in c["items"]:
            item_box = patches.FancyBboxPatch((c["x"] + 0.012, y - 0.09), c["w"] - 0.024, 0.095,
                                              boxstyle="round,pad=0.01", facecolor='#ffffff',
                                              edgecolor='#e2e8f0', linewidth=1)
            ax.add_patch(item_box)
            ax.text(c["x"] + 0.022, y - 0.025, name, fontsize=9.5, fontweight='bold', color='#1e293b')
            ax.text(c["x"] + 0.022, y - 0.065, desc, fontsize=7.5, color='#64748b', family='sans-serif')
            y -= 0.118

    # Connecting directional arrows
    ax.annotate('', xy=(0.355, 0.5), xytext=(0.325, 0.5),
                arrowprops=dict(facecolor='#1a0a7a', shrink=0.05, width=2, headwidth=7))
    ax.annotate('', xy=(0.675, 0.5), xytext=(0.645, 0.5),
                arrowprops=dict(facecolor='#f8a62a', shrink=0.05, width=2, headwidth=7))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join(assets_dir, 'architecture.png'), bbox_inches='tight')
    plt.close()
    print("Created architecture.png")

# 3. FEATURES GRID (features_grid.png)
def make_features_grid():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=150)
    fig.patch.set_facecolor('#fdfaf6')
    ax.set_facecolor('#fdfaf6')
    
    ax.text(0.5, 0.93, "PAWDACITY CORE FEATURE HIGHLIGHTS", fontsize=18, fontweight='black',
            color='#1a0a7a', ha='center', va='center')
    ax.text(0.5, 0.88, "Comprehensive Pet Commerce, Salon Scheduling, and Live Customizer", fontsize=11,
            color='#64748b', ha='center', va='center')
            
    features = [
        {"icon": "🛍️", "title": "Catalog & Quick View", "desc": "30 pet items, 8 categories, SVG badges, live search filter, multi-photo carousels, and quick view modal.", "color": "#1a0a7a"},
        {"icon": "🛒", "title": "Dynamic Cart & Coupons", "desc": "Persistent cart, automatic free delivery meter (₱999), and coupon codes: PAW10, WELCOME50, FREESHIP.", "color": "#f8a62a"},
        {"icon": "💳", "title": "Philippine Checkout", "desc": "GCash, Maya, Cards, & Cash On Delivery. Validates cards, assigns PAW-XXXXXX IDs, and creates email orders.", "color": "#fc7b5f"},
        {"icon": "📅", "title": "Service Booking Engine", "desc": "Interactive appointment booker for grooming, vet care, and day care with slot collision detection.", "color": "#27b4e0"},
        {"icon": "🎨", "title": "Live Owner Studio (Ctrl+K)", "desc": "Change shop branding, color schemes, Google fonts, card shadows, wallpapers, and modify products in real time.", "color": "#8cc63f"},
        {"icon": "📊", "title": "Multi-Sheet Excel Export", "desc": "SheetJS integration downloads comprehensive .xlsx audit reports with Purchases, Users, and Product performance.", "color": "#ff4f8b"},
    ]
    
    positions = [
        (0.05, 0.48), (0.36, 0.48), (0.68, 0.48),
        (0.05, 0.08), (0.36, 0.08), (0.68, 0.08)
    ]
    
    for (x, y), feat in zip(positions, features):
        card = patches.FancyBboxPatch((x, y), 0.28, 0.35, boxstyle="round,pad=0.015",
                                      facecolor='#ffffff', edgecolor=feat["color"], linewidth=2)
        ax.add_patch(card)
        
        # Icon badge
        circle = patches.Circle((x + 0.04, y + 0.28), 0.035, facecolor=feat["color"], alpha=0.15)
        ax.add_patch(circle)
        ax.text(x + 0.04, y + 0.28, feat["icon"], fontsize=18, ha='center', va='center')
        
        # Title
        ax.text(x + 0.09, y + 0.28, feat["title"], fontsize=11, fontweight='bold',
                color='#1e293b', va='center')
                
        # Description
        ax.text(x + 0.02, y + 0.14, feat["desc"], fontsize=9, color='#475569',
                wrap=True, va='center')
                
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join(assets_dir, 'features_grid.png'), bbox_inches='tight')
    plt.close()
    print("Created features_grid.png")

# 4. PALETTES SHOWCASE (color_palettes.png)
def make_palettes():
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=150)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#f8fafc')
    
    ax.text(0.5, 0.90, "BUILT-IN BRAND COLOR PALETTES", fontsize=16, fontweight='black',
            color='#1a0a7a', ha='center', va='center')
    ax.text(0.5, 0.82, "Instantly switch the entire storefront vibe via Owner Panel (Ctrl+K)", fontsize=10.5,
            color='#64748b', ha='center', va='center')
            
    palettes = [
        {"name": "Pawdacity Classic", "swatches": [("#1a0a7a", "Indigo Primary"), ("#f8a62a", "Warm Amber"), ("#fc7b5f", "Coral Accent"), ("#ff4f8b", "Hot Pink Price"), ("#fff8ee", "Cream Canvas")]},
        {"name": "Ocean Breeze", "swatches": [("#0b2a5b", "Deep Navy"), ("#27b4e0", "Cyan Accent"), ("#4f8cff", "Sky Blue"), ("#0aa5a0", "Teal Highlight"), ("#f1f9ff", "Ice White")]},
        {"name": "Forest Emerald", "swatches": [("#12361f", "Dark Pine"), ("#8cc63f", "Lime Leaf"), ("#e8a33d", "Golden Bark"), ("#d9544d", "Berry Red"), ("#f6fbef", "Sage Tint")]},
        {"name": "Berry Velvet", "swatches": [("#4a0f3d", "Deep Plum"), ("#ff8fb1", "Rose Quartz"), ("#c94fa0", "Magenta"), ("#e0245e", "Ruby Pink"), ("#fff3f8", "Blush Cream")]}
    ]
    
    y = 0.65
    for pal in palettes:
        ax.text(0.06, y + 0.04, pal["name"], fontsize=11, fontweight='bold', color='#1e293b')
        x = 0.28
        for color_hex, label in pal["swatches"]:
            box = patches.FancyBboxPatch((x, y - 0.02), 0.12, 0.08, boxstyle="round,pad=0.005",
                                         facecolor=color_hex, edgecolor='#cbd5e1', linewidth=1)
            ax.add_patch(box)
            ax.text(x + 0.06, y + 0.02, color_hex, fontsize=7.5, fontweight='bold',
                    color='#ffffff' if label not in ['Cream Canvas', 'Ice White', 'Sage Tint', 'Blush Cream', 'Lime Leaf', 'Warm Amber'] else '#1e293b',
                    ha='center', va='center')
            x += 0.138
        y -= 0.17
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(os.path.join(assets_dir, 'color_palettes.png'), bbox_inches='tight')
    plt.close()
    print("Created color_palettes.png")

make_banner()
make_architecture()
make_features_grid()
make_palettes()
print("All graphic assets successfully created!")
