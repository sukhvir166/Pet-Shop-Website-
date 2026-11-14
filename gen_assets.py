mport os
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
