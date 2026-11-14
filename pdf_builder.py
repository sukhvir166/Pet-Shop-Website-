import os
import sys
import shutil

os.environ['MPLCONFIGDIR'] = 'C:/Users/HP/AppData/Local/Temp'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches

pdf_path = r'C:\Users\HP\.gemini\antigravity\scratch\pawdacity\Pawdacity_System_Architecture_and_Guide.pdf'
artifact_pdf_path = r'C:\Users\HP\.gemini\antigravity\brain\7d6abd5a-ae3e-42e4-bb12-2416df9eaf6b\Pawdacity_System_Architecture_and_Guide.pdf'

TOTAL_PAGES = 6
PAGE_W = 8.5
PAGE_H = 11.0

def safe_txt(s):
    if s is None:
        return ""
    # Escape dollar signs for matplotlib's mathtext parser
    return str(s).replace('$', r'\$')

def create_base_page(page_num, total_pages, title="PAWDACITY: ARCHITECTURAL & TECHNICAL SPECIFICATION"):
    fig = plt.figure(figsize=(PAGE_W, PAGE_H), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor('#ffffff')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # Header Bar
    top_bar = patches.Rectangle((0, 0.95), 1, 0.05, facecolor='#1a0a7a', edgecolor='none')
    ax.add_patch(top_bar)
    ax.text(0.04, 0.975, safe_txt(title), fontsize=9, fontweight='bold', color='#ffffff', va='center')
    ax.text(0.96, 0.975, "SYSTEM GUIDE & ESSENTIALS", fontsize=8, color='#f8a62a', ha='right', va='center', fontweight='bold')
    
    # Bottom Footer Bar
    bot_line = patches.Rectangle((0.04, 0.045), 0.92, 0.0012, facecolor='#cbd5e1', edgecolor='none')
    ax.add_patch(bot_line)
    ax.text(0.04, 0.028, "Pawdacity: Pet Shop Philippines • Developed by Sunny Rajput (github.com/sukhvir166)", 
            fontsize=7.5, color='#64748b', va='center')
    ax.text(0.96, 0.028, f"Page {page_num} of {total_pages}", 
            fontsize=7.5, color='#1a0a7a', fontweight='bold', ha='right', va='center')
    
    return fig, ax

def add_card(ax, x, y, w, h, bg="#f8fafc", border="#e2e8f0", lw=1):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.008,rounding_size=0.012",
                                 facecolor=bg, edgecolor=border, linewidth=lw)
    ax.add_patch(box)
    return box

def draw_section_hdr(ax, x, y, title, subtitle=None, badge=None):
    if badge:
        bw = len(badge)*0.009 + 0.02
        b_box = patches.FancyBboxPatch((x, y - 0.004), bw, 0.022, boxstyle="round,pad=0.003",
                                      facecolor='#1a0a7a', edgecolor='none')
        ax.add_patch(b_box)
        ax.text(x + bw/2, y + 0.007, safe_txt(badge), fontsize=7, color='#ffffff', fontweight='bold', ha='center', va='center')
        ax.text(x + bw + 0.015, y + 0.007, safe_txt(title), fontsize=12, fontweight='bold', color='#1a0a7a', va='center')
    else:
        ax.text(x, y + 0.007, safe_txt(title), fontsize=12, fontweight='bold', color='#1a0a7a', va='center')
    
    if subtitle:
        ax.text(x, y - 0.016, safe_txt(subtitle), fontsize=8.2, color='#64748b', va='center')

def draw_code_box(ax, x, y, w, h, title, lines):
    # Container
    add_card(ax, x, y, w, h, bg="#1e1e2e", border="#313244", lw=1)
    # Header bar
    hbar = patches.Rectangle((x, y + h - 0.03), w, 0.03, facecolor='#282a36', edgecolor='none')
    ax.add_patch(hbar)
    ax.text(x + 0.015, y + h - 0.015, safe_txt(title), fontsize=7.5, color='#f8a62a', fontweight='bold', va='center', family='monospace')
    
    cur_y = y + h - 0.05
    for l in lines:
        ax.text(x + 0.015, cur_y, safe_txt(l), fontsize=7.2, color='#cdd6f4', family='monospace', va='top')
        cur_y -= 0.022

def draw_table(ax, x, y, w, headers, rows, col_widths):
    row_h = 0.028
    # Header
    hdr_box = patches.Rectangle((x, y - row_h), w, row_h, facecolor='#1a0a7a', edgecolor='none')
    ax.add_patch(hdr_box)
    
    cur_x = x + 0.01
    for h, cw in zip(headers, col_widths):
        ax.text(cur_x, y - row_h/2, safe_txt(h), fontsize=7.5, fontweight='bold', color='#ffffff', va='center')
        cur_x += cw * w
        
    cur_y = y - row_h
    for r_idx, row in enumerate(rows):
        cur_y -= row_h
        bg_col = "#ffffff" if r_idx % 2 == 0 else "#f1f5f9"
        row_box = patches.Rectangle((x, cur_y), w, row_h, facecolor=bg_col, edgecolor='#e2e8f0', linewidth=0.5)
        ax.add_patch(row_box)
        
        cur_x = x + 0.01
        for cell, cw in zip(row, col_widths):
            ax.text(cur_x, cur_y + row_h/2, safe_txt(cell), fontsize=7.2, color='#1e293b', va='center')
            cur_x += cw * w

print("Building pages...")

with PdfPages(pdf_path) as pdf:
    # -------------------------------------------------------------
    # PAGE 1: TITLE, EXECUTIVE SUMMARY & PROJECT SCOPE
    # -------------------------------------------------------------
    fig, ax = create_base_page(1, TOTAL_PAGES)
    
    # Hero Title Banner
    hero = add_card(ax, 0.04, 0.77, 0.92, 0.16, bg="#1a0a7a", border="#f8a62a", lw=2)
    ax.text(0.08, 0.89, "PAWDACITY", fontsize=28, fontweight='black', color='#ffffff')
    ax.text(0.08, 0.84, "Pet Shop Philippines • Complete Technical Architecture & System Guide", 
            fontsize=12, fontweight='bold', color='#f8a62a')
    ax.text(0.08, 0.795, "Clean pets, happy hearts! • Zero-Dependency Single-File Web Application Suite", 
            fontsize=9.5, color='#e2e8f0')
    
    # Metadata pill
    meta_box = add_card(ax, 0.65, 0.79, 0.28, 0.12, bg="#261596", border="#fc7b5f", lw=1.5)
    ax.text(0.67, 0.88, "DOCUMENT METADATA", fontsize=7.5, fontweight='bold', color='#fc7b5f')
    ax.text(0.67, 0.85, "Author: Sunny Rajput", fontsize=7.5, color='#ffffff')
    ax.text(0.67, 0.825, "Repo: github.com/sukhvir166", fontsize=7.5, color='#ffffff')
    ax.text(0.67, 0.80, "Currency: Philippine Peso (PHP, ₱)", fontsize=7.5, color='#ffffff')
    
    # Section: Executive Overview
    draw_section_hdr(ax, 0.04, 0.73, "1. Executive Summary & Project Genesis", 
                     "Modern, resilient single-page e-commerce architecture engineered for the Philippine market", "MODULE 1")
    
    summary_text = (
        "Pawdacity is a high-performance, single-file client-side e-commerce web application and salon booking platform "
        "specifically designed for pet owners across the Philippine archipelago. Built entirely in vanilla standards (HTML5, "
        "CSS3 Custom Properties, and ES6+ JavaScript), the application operates with zero external build-step dependencies "
        "and zero mandatory server requirements. Every catalog image, category glyph, user profile state, cart mutation, and "
        "customizer override operates directly in the client browser with lightning-fast offline persistence via the Web Storage API."
    )
    add_card(ax, 0.04, 0.62, 0.92, 0.09, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.69, safe_txt(summary_text), fontsize=8.2, color='#1e293b', wrap=True, va='top', linespacing=1.4)
    
    # Section: Core Architectural Pillars (3 Cards)
    draw_section_hdr(ax, 0.04, 0.58, "2. Core Architectural Pillars", 
                     "Three foundations powering reliability, visual excellence, and zero-latency interaction")
    
    pillars = [
        ("Zero Build Dependencies", "#1a0a7a", 
         "Operates directly in any modern browser without npm, webpack, or transpilers. Ships with self-contained SVG generation and embedded image dictionaries for 100% offline uptime."),
        ("Reactive CSS Custom Properties", "#f8a62a", 
         "Live styling engine driven by CSS variables (--ind, --or, --co, --pk, --fd, --rad). The Owner Panel updates palettes, corner roundness, and shadows instantaneously."),
        ("State Isolation & Persistence", "#27b4e0", 
         "Fully partitioned localStorage schema encapsulating shopping carts, coupon codes, service reservations, registered user credentials, order history, and catalog overrides.")
    ]
    
    px = 0.04
    for title, col, desc in pillars:
        c_box = add_card(ax, px, 0.44, 0.29, 0.12, bg="#ffffff", border=col, lw=1.5)
        ax.text(px + 0.015, 0.535, safe_txt(title), fontsize=9, fontweight='bold', color=col)
        ax.text(px + 0.015, 0.51, safe_txt(desc), fontsize=7.5, color='#475569', wrap=True, va='top', linespacing=1.3)
        px += 0.315
        
    # Section: Feature Breakdown Grid
    draw_section_hdr(ax, 0.04, 0.40, "3. Feature Inventory & Specification", 
                     "Comprehensive breakdown of end-user and administrative capabilities", "CAPABILITIES")
    
    features_list = [
        ("Product Catalog & Carousel", "30 pet items across 8 categories with live search, SVG fallbacks & carousel controls."),
        ("Cart, Promos & Free Shipping", "Interactive drawer with dynamic ₱999 free delivery progress meter and coupon engine."),
        ("Multi-Payment Checkout", "Localized for the Philippines: GCash, Maya, Cards, and COD with automated mailto order dispatch."),
        ("Salon & Vet Booking Engine", "Collision-checked scheduling system for grooming, veterinary exams, and pet daycare."),
        ("Owner Customizer Panel (Ctrl+K)", "Comprehensive live control panel to re-brand the store, re-color palettes, and edit catalog prices."),
        ("Multi-Sheet Excel Reporting", "Native SheetJS integration (.xlsx) compiling Purchases, Users, and Product performance audits."),
        ("Developer Matrix Easter Egg", "Interactive canvas terminal rendering falling Matrix rain and developer profile details.")
    ]
    
    fy = 0.35
    for f_title, f_desc in features_list:
        ax.text(0.06, fy, "✓", fontsize=9, color='#16a34a', fontweight='bold', va='top')
        ax.text(0.08, fy, safe_txt(f_title) + " — ", fontsize=8, color='#0f172a', fontweight='bold', va='top')
        ax.text(0.08 + len(f_title)*0.0075 + 0.02, fy, safe_txt(f_desc), fontsize=8, color='#475569', va='top')
        fy -= 0.038
        
    pdf.savefig(fig)
    plt.close()
    print("Page 1 generated.")

    # -------------------------------------------------------------
    # PAGE 2: SYSTEM ARCHITECTURE & DATA FLOW
    # -------------------------------------------------------------
    fig, ax = create_base_page(2, TOTAL_PAGES)
    
    draw_section_hdr(ax, 0.04, 0.90, "4. System Architecture & Lifecycle Model", 
                     "Single-Page Application (SPA) reactive pipeline and execution lifecycle", "ARCHITECTURE")
    
    # Lifecycle steps
    diag = add_card(ax, 0.04, 0.67, 0.92, 0.21, bg="#f8fafc", border="#1a0a7a", lw=1.5)
    ax.text(0.06, 0.855, "CLIENT BROWSER EXECUTION LIFECYCLE (UNIDIRECTIONAL REACTIVE FLOW)", fontsize=8.5, fontweight='bold', color='#1a0a7a')
    
    steps = [
        ("1. INITIAL LOAD", "HTML/CSS parsing\nFont load from Google\nRead localStorage", "#1a0a7a", 0.06),
        ("2. STATE RECONCILIATION", "Merge default 'D' with 'pc_set'\nApply product overrides 'ovr()'\nCompute Cart & Booking totals", "#f8a62a", 0.285),
        ("3. DOM GENERATION", "apply() drives CSS variables\ntiles() generates category links\nrender() builds filtered grid", "#fc7b5f", 0.51),
        ("4. USER DISPATCH & SYNC", "Clicks, Cart add, Booking\nOwner tweaks (Ctrl+K)\nW() persists back to Storage", "#16a34a", 0.735)
    ]
    
    for title, desc, col, x_pos in steps:
        s_box = patches.FancyBboxPatch((x_pos, 0.70), 0.20, 0.13, boxstyle="round,pad=0.006",
                                       facecolor='#ffffff', edgecolor=col, linewidth=1.5)
        ax.add_patch(s_box)
        ax.text(x_pos + 0.01, 0.81, safe_txt(title), fontsize=8, fontweight='bold', color=col)
        ax.text(x_pos + 0.01, 0.78, safe_txt(desc), fontsize=7.2, color='#475569', va='top', linespacing=1.3)
        if x_pos < 0.7:
            ax.annotate('', xy=(x_pos + 0.22, 0.765), xytext=(x_pos + 0.20, 0.765),
                        arrowprops=dict(facecolor=col, shrink=0.05, width=1.5, headwidth=5))
    
    # Section: LocalStorage Schema Data Dictionary
    draw_section_hdr(ax, 0.04, 0.63, "5. Web Storage State Persistence Schema", 
                     "Detailed specification of all localStorage keys, data formats, and fallbacks", "DATA MODEL")
                     
    headers = ["Storage Key", "Type", "Default Value", "Description & Usage"]
    col_w = [0.16, 0.12, 0.22, 0.50]
    rows = [
        ["pc_set", "Object", "{...D} (Default theme)", "Stores brand name, theme mode, colors, typography, border radius & overrides."],
        ["pc_cart", "Array<Obj>", "[]", "Stores active cart items as [{id: Number, q: Number}], persisted across sessions."],
        ["pc_orders", "Array<Obj>", "[]", "Full transaction ledger: order number (PAW-XXXXXX), customer, timestamp, total, items."],
        ["pc_bk", "Array<Obj>", "[]", "Appointment reservations: service name, pet name, date, time slot, and contact phone."],
        ["pc_users", "Object", "{}", "Simulated user credentials dictionary: {email: {name, pw, role: 'user'|'admin'}}."],
        ["pc_user", "Object|null", "null", "Active session pointer containing authenticated user's name, email, and role."],
        ["pc_wl", "Array<Num>", "[]", "Wishlist array containing product IDs flagged as favorites by the user."],
        ["pc_cp", "String", "''", "Currently applied coupon code string (PAW10, WELCOME50, or FREESHIP)."]
    ]
    
    draw_table(ax, 0.04, 0.60, 0.92, headers, rows, col_w)
    
    # Section: Key Utility Functions
    draw_section_hdr(ax, 0.04, 0.32, "6. Core Helper Primitives", 
                     "Compact micro-utilities for sanitization, storage reading/writing, and currency formatting")
                     
    code_lines = [
        "const $ = s => document.querySelector(s);",
        "const E = s => String(s).replace(/[&<>\"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]));",
        "const L = (k,d) => { try { const v=JSON.parse(localStorage.getItem(k)); return v==null?d:v } catch(e){return d} };",
        "const W = (k,v) => { try { localStorage.setItem(k, JSON.stringify(v)); return 1 } catch(e){ return 0 } };",
        "const peso = n => '₱' + n.toLocaleString('en-PH');"
    ]
    draw_code_box(ax, 0.04, 0.08, 0.92, 0.21, "UTILITY PRIMITIVES (script.js lines 3-5)", code_lines)
    
    pdf.savefig(fig)
    plt.close()
    print("Page 2 generated.")

    # -------------------------------------------------------------
    # PAGE 3: HOW IT WORKS - CATALOG, CART & PROMOTIONS
    # -------------------------------------------------------------
    fig, ax = create_base_page(3, TOTAL_PAGES)
    
    draw_section_hdr(ax, 0.04, 0.90, "7. Deep Dive: Product Catalog & Procedural Graphics", 
                     "How Pawdacity structures 30 pet items, procedural SVGs, and multi-image carousels", "SUBSYSTEM 1")
    
    catalog_desc = (
        "The catalog is declared as an array P of product tuples: [id, category, title, price, [images]]. "
        "Each product category maps to CATS. If no external photographic asset is provided, Pawdacity uses a procedural "
        "SVG generator function a(emoji, color1, color2) which creates a resolution-independent Data URI with linear "
        "gradients and centered emoji symbols, ensuring crisp visuals on Retina displays with zero network latency."
    )
    add_card(ax, 0.04, 0.77, 0.92, 0.105, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.855, safe_txt(catalog_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    code_catalog = [
        "// Procedural SVG Generator with Linear Gradient & Circular Badge",
        "const a = (e, x, y) => 'data:image/svg+xml,' + encodeURIComponent(",
        "  `<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 300 300\">` +",
        "  `<defs><linearGradient id=\"g\" x1=\"0\" y1=\"0\" x2=\"1\" y2=\"1\">` +",
        "  `<stop offset=\"0\" stop-color=\"${x}\"/><stop offset=\"1\" stop-color=\"${y}\"/></linearGradient></defs>` +",
        "  `<rect width=\"300\" height=\"300\" fill=\"url(#g)\"/>` +",
        "  `<circle cx=\"150\" cy=\"150\" r=\"105\" fill=\"#fff\" fill-opacity=\".4\" stroke=\"#fff\" stroke-width=\"6\"/>` +",
        "  `<text x=\"150\" y=\"195\" font-size=\"125\" text-anchor=\"middle\">${e}</text></svg>`",
        ");"
    ]
    draw_code_box(ax, 0.04, 0.54, 0.92, 0.21, "PROCEDURAL SVG ENGINE (script.js line 6)", code_catalog)
    
    draw_section_hdr(ax, 0.04, 0.50, "8. Deep Dive: Dynamic Cart, Coupons & Threshold Meter", 
                     "Mathematical rules governing subtotals, coupon deductions, and free delivery thresholds", "SUBSYSTEM 2")
                     
    cart_desc = (
        "The shopping cart maintains a persistent collection of line items ({id, q}). The tot() pure function computes "
        "the financial summary on every cart mutation. Free delivery in the Philippines is awarded automatically when the "
        "subtotal exceeds ₱999, or when the 'FREESHIP' coupon is entered. The drawer features a live CSS progress bar "
        "indicating how many more pesos are required to unlock free shipping."
    )
    add_card(ax, 0.04, 0.38, 0.92, 0.095, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.455, safe_txt(cart_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    code_cart = [
        "// Coupon Rules Dictionary & Mathematical Total Computation",
        "const CP = {",
        "  PAW10:     ['10% off',       s => Math.round(s * 0.10)],",
        "  WELCOME50: ['₱50 off',       s => Math.min(50, s)],",
        "  FREESHIP:  ['Free delivery', () => 0]",
        "};",
        "const tot = () => {",
        "  const s  = cart.reduce((n, x) => n + x.q * P.find(p => p[0] == x.id)[3], 0);",
        "  const c  = CP[cp];",
        "  const ds = c ? c[1](s) : 0;",
        "  const d  = (!s || s >= 999 || cp == 'FREESHIP') ? 0 : 50; // ₱50 standard shipping",
        "  return { s, ds, d, t: s - ds + d };",
        "};"
    ]
    draw_code_box(ax, 0.04, 0.08, 0.92, 0.28, "CART CALCULATOR & COUPONS (script.js lines 92-93)", code_cart)
    
    pdf.savefig(fig)
    plt.close()
    print("Page 3 generated.")

    # -------------------------------------------------------------
    # PAGE 4: HOW IT WORKS - CHECKOUT, BOOKINGS & AUTH
    # -------------------------------------------------------------
    fig, ax = create_base_page(4, TOTAL_PAGES)
    
    draw_section_hdr(ax, 0.04, 0.90, "9. Deep Dive: Philippine Checkout & Multi-Channel Payment", 
                     "Simulated transaction processing, card validation, and email order dispatch", "SUBSYSTEM 3")
                     
    checkout_desc = (
        "The checkout workflow accommodates the primary payment rails in the Philippines: GCash, Maya, Credit/Debit Card, "
        "and Cash on Delivery (COD). When Card is selected, card number inputs are unhidden and validated via a numeric "
        "regex (^\\d{13,19}$). Upon completion, a unique order serial 'PAW-XXXXXX' is synthesized from Date.now(), "
        "transaction history is recorded in pc_orders, and a mailto link is constructed with all itemized lines."
    )
    add_card(ax, 0.04, 0.77, 0.92, 0.105, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.855, safe_txt(checkout_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    code_pay = [
        "// Order Generation & Email Intent Dispatch (pay() in script.js)",
        "const no = 'PAW-' + Date.now().toString().slice(-6);",
        "const lines = cart.map(x => x.q + ' x ' + P.find(p => p[0] == x.id)[2]).join('%0A');",
        "const os = L('pc_orders', []);",
        "os.unshift({ no, name: user.name, email: user.email, at: new Date().toISOString(),",
        "             m: paymentMethod, t: t.t, it: cart.map(x => ({n: p[2], q: x.q, p: p[3]})) });",
        "W('pc_orders', os);",
        "// Constructs mailto: hyperlink with complete line items for store staff verification"
    ]
    draw_code_box(ax, 0.04, 0.58, 0.92, 0.17, "TRANSACTION DISPATCH (script.js lines 101-104)", code_pay)
    
    draw_section_hdr(ax, 0.04, 0.54, "10. Deep Dive: Service Booking & Collision Detection", 
                     "Scheduling appointments for salon grooming, vet checkups, and day care", "SUBSYSTEM 4")
                     
    bk_desc = (
        "Pawdacity includes an interactive appointment scheduler for pet grooming and medical exams. "
        "To prevent double-booking, the submission handler evaluates existing records in pc_bk. If any appointment matches "
        "both date and time slot (bk.some(x => x.d == b.d && x.t == b.t)), the user is alerted with a toast notification. "
        "Confirmed bookings generate ready-to-send appointment request emails to pawdacity98@gmail.com."
    )
    add_card(ax, 0.04, 0.42, 0.92, 0.095, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.495, safe_txt(bk_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    draw_section_hdr(ax, 0.04, 0.38, "11. Deep Dive: Authentication & Role-Based Access Control", 
                     "Simulated account creation, session management, and admin elevation", "SUBSYSTEM 5")
                     
    auth_desc = (
        "User authentication is simulated entirely in the client browser. Users can register with their name, email, and "
        "password. Passwords and roles ('user' or 'admin') are stored in pc_users. Through the Owner Panel (Ctrl+K), "
        "administrators can view all registered users, elevate or demote roles, trigger instant password resets (which "
        "generates a 'pawXXXX' temporary password), or permanently delete accounts."
    )
    add_card(ax, 0.04, 0.25, 0.92, 0.105, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.335, safe_txt(auth_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    # 2 Cards for Booking Collision & Auth Reset
    add_card(ax, 0.04, 0.08, 0.44, 0.14, bg="#ffffff", border="#27b4e0", lw=1.5)
    ax.text(0.06, 0.20, "COLLISION DETECTION RULE", fontsize=8.5, fontweight='bold', color='#0b2a5b')
    ax.text(0.06, 0.17, safe_txt("if (bk.some(x => x.d == b.d && x.t == b.t)) {\n  toast('That slot is taken, pick another time');\n  return;\n}"), 
            fontsize=7.5, family='monospace', color='#334155', va='top')
            
    add_card(ax, 0.52, 0.08, 0.44, 0.14, bg="#ffffff", border="#ff4f8b", lw=1.5)
    ax.text(0.54, 0.20, "ADMIN PASSWORD RESET GENERATOR", fontsize=8.5, fontweight='bold', color='#4a0f3d')
    ax.text(0.54, 0.17, safe_txt("us[email].pw = rp[email] =\n  'paw' + Math.floor(1000 + Math.random() * 9000);\nW('pc_users', us);"), 
            fontsize=7.5, family='monospace', color='#334155', va='top')
    
    pdf.savefig(fig)
    plt.close()
    print("Page 4 generated.")

    # -------------------------------------------------------------
    # PAGE 5: OWNER STUDIO & REAL-TIME CUSTOMIZATION
    # -------------------------------------------------------------
    fig, ax = create_base_page(5, TOTAL_PAGES)
    
    draw_section_hdr(ax, 0.04, 0.90, "12. Deep Dive: Live Owner Studio & Theming Engine", 
                     "Real-time visual customization via CSS custom properties and client-side canvas", "SUBSYSTEM 6")
                     
    owner_desc = (
        "Pressing Ctrl+K or clicking the hidden owner trigger opens the comprehensive Owner Panel. "
        "This tool enables store managers to re-brand the storefront in real time. All changes immediately mutate the "
        "global state T and update root CSS Custom Properties via apply(), with zero page reload required. "
        "The customizer provides 4 preset color palettes, 8 Google Font pairings, card shadow physics, and border radiuses."
    )
    add_card(ax, 0.04, 0.77, 0.92, 0.105, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.855, safe_txt(owner_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    code_apply = [
        "// Reactive CSS Custom Properties Synchronization (apply() in script.js)",
        "function apply() {",
        "  const r = document.documentElement, s = r.style;",
        "  ['ind','or','co','pk'].forEach(k => s.setProperty('--'+k, T[k]));",
        "  s.setProperty('--fd', `'${T.fd}', system-ui, sans-serif`);",
        "  s.setProperty('--fb', `'${T.fb}', system-ui, sans-serif`);",
        "  s.setProperty('--rad', T.rad + 'px');",
        "  const h = { pop: ['6px 6px 0 var(--ind)', '6px 12px 0 var(--or)'], ... }[T.sh];",
        "  s.setProperty('--shd', h[0]); s.setProperty('--shh', h[1]);",
        "  document.querySelectorAll('.bnm').forEach(e => e.textContent = T.brand);",
        "}"
    ]
    draw_code_box(ax, 0.04, 0.52, 0.92, 0.23, "CSS VARIABLES SYNCHRONIZATION (script.js lines 50-58)", code_apply)
    
    draw_section_hdr(ax, 0.04, 0.48, "13. Client-Side Image Downscaling Engine", 
                     "Preventing localStorage quota exhaustion with in-browser HTML5 Canvas resampling", "SUBSYSTEM 7")
                     
    img_desc = (
        "Because Web Storage is limited to ~5MB per origin, uploading multi-megabyte photos directly would crash storage. "
        "Pawdacity implements an intelligent client-side downscaling function rd(file, maxWidth, callback). "
        "It uses FileReader and HTML5 Canvas to resample large camera images down to 800px (or 1600px for wallpapers), "
        "compressing the result to JPEG at 82% quality before storing in localStorage."
    )
    add_card(ax, 0.04, 0.35, 0.92, 0.105, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.435, safe_txt(img_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    code_rd = [
        "// Client-Side Canvas Image Compressor & Downscaler",
        "function rd(file, w, cb) {",
        "  const r = new FileReader();",
        "  r.onload = () => {",
        "    const i = new Image();",
        "    i.onload = () => {",
        "      const k = Math.min(1, w / Math.max(i.width, i.height));",
        "      const c = document.createElement('canvas');",
        "      c.width = i.width * k; c.height = i.height * k;",
        "      c.getContext('2d').drawImage(i, 0, 0, c.width, c.height);",
        "      cb(c.toDataURL('image/jpeg', 0.82)); // 82% JPEG Quality",
        "    }; i.src = r.result;",
        "  }; r.readAsDataURL(file);",
        "}"
    ]
    draw_code_box(ax, 0.04, 0.08, 0.92, 0.25, "CANVAS RESAMPLING (script.js line 49)", code_rd)
    
    pdf.savefig(fig)
    plt.close()
    print("Page 5 generated.")

    # -------------------------------------------------------------
    # PAGE 6: REPORTING, SECURITY, MATRIX EASTER EGG & DEPLOYMENT
    # -------------------------------------------------------------
    fig, ax = create_base_page(6, TOTAL_PAGES)
    
    draw_section_hdr(ax, 0.04, 0.90, "14. Business Auditing & Multi-Sheet Excel Export", 
                     "SheetJS integration for automated accounting, customer analytics, and stock performance", "SUBSYSTEM 8")
                     
    excel_desc = (
        "Pawdacity provides automated commercial reporting via xl(). When SheetJS (XLSX) is available, it constructs a "
        "multi-tab workbook (pawdacity-history.xlsx) with 3 discrete analytical sheets: 'Purchases' (granular order records), "
        "'Users' (customer order frequency and total spend), and 'Products' (item velocity and generated revenue). "
        "If SheetJS is absent, it gracefully falls back to sanitized RFC-compliant CSV with formula injection prevention."
    )
    add_card(ax, 0.04, 0.77, 0.92, 0.105, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.855, safe_txt(excel_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    draw_section_hdr(ax, 0.04, 0.73, "15. Developer Easter Egg: Matrix Rain Terminal", 
                     "Hidden terminal emulator showcasing creator bio and interactive visual effects", "EASTER EGG")
                     
    matrix_desc = (
        "Accessible from the bottom of the Owner Panel, the '> About the developer' button triggers openDev(). "
        "This function launches an interactive HTML5 canvas dialog that computes vertical streaming green binary digits ('0'/'1') "
        "reminiscent of the Matrix film terminal, overlaid with creator Sunny Rajput's portfolio, GitHub, and email contact."
    )
    add_card(ax, 0.04, 0.60, 0.92, 0.105, bg="#f8fafc", border="#cbd5e1", lw=1)
    ax.text(0.06, 0.685, safe_txt(matrix_desc), fontsize=8, color='#1e293b', wrap=True, va='top', linespacing=1.35)
    
    draw_section_hdr(ax, 0.04, 0.56, "16. Production Readiness & Deployment Guide", 
                     "Deployment steps, hosting recommendations, and transition to server-backed database", "DEPLOYMENT")
                     
    deploy_steps = [
        ("Static Web Hosting", "Deploy index.html directly to GitHub Pages, Cloudflare Pages, Netlify, or Vercel. Zero configuration required."),
        ("Custom Domain Setup", "Configure CNAME records for your custom domain (e.g., petshop.ph). SSL certificates are provisioned automatically."),
        ("Backend Migration Path", "To scale from localStorage to multi-tenant cloud storage, replace L() and W() with REST or Supabase/PostgreSQL APIs."),
        ("Real Payment Gateway", "Replace simulated radio options with Maya Checkout API and GCash PayMaya Webhook integrations.")
    ]
    
    dy = 0.50
    for d_title, d_text in deploy_steps:
        ax.text(0.06, dy, "▶", fontsize=8.5, color='#1a0a7a', fontweight='bold', va='top')
        ax.text(0.08, dy, safe_txt(d_title) + ": ", fontsize=8, color='#0f172a', fontweight='bold', va='top')
        ax.text(0.08 + len(d_title)*0.0075 + 0.015, dy, safe_txt(d_text), fontsize=8, color='#475569', va='top')
        dy -= 0.038
        
    # Developer Credit Card Box
    dev_box = add_card(ax, 0.04, 0.08, 0.92, 0.22, bg="#1a0a7a", border="#f8a62a", lw=2)
    ax.text(0.08, 0.26, "DEVELOPER PROFILE & REPOSITORY INFORMATION", fontsize=11, fontweight='black', color='#ffffff')
    ax.text(0.08, 0.225, "Architect & Developer: Sunny Rajput", fontsize=9.5, fontweight='bold', color='#f8a62a')
    ax.text(0.08, 0.19, "• GitHub Profile:  https://github.com/sukhvir166", fontsize=8.5, color='#ffffff')
    ax.text(0.08, 0.16, "• Direct Contact:  sssrajput166@gmail.com", fontsize=8.5, color='#ffffff')
    ax.text(0.08, 0.13, "• Specializations:  Engineering, AI/ML, Full-Stack Web Development, Reverse Engineering", fontsize=8.5, color='#e2e8f0')
    ax.text(0.08, 0.10, "• Store Inquiry:   pawdacity98@gmail.com (Pet Shop Philippines Customer Support)", fontsize=8.5, color='#ffd08a')

    pdf.savefig(fig)
    plt.close()
    print("Page 6 generated.")

print("PDF successfully compiled!")

# Copy to artifact directory
shutil.copy2(pdf_path, artifact_pdf_path)
print("Copied PDF to artifact directory:", artifact_pdf_path)
