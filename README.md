 🐾 Pawdacity – Pet Shop Philippines
<p align="center">
  <img src="assets/banner.svg" alt="Pawdacity Pet Shop Philippines Banner" width="100%" />
</p>
<p align="center">
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript"><img src="https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript ES6+" /></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties"><img src="https://img.shields.io/badge/CSS3-Custom_Properties-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3 Custom Properties" /></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/HTML"><img src="https://img.shields.io/badge/HTML5-Semantic_SPA-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5 SPA" /></a>
  <a href="https://sheetjs.com/"><img src="https://img.shields.io/badge/SheetJS-XLSX_Export-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" alt="SheetJS Export" /></a>
  <a href="https://en.wikipedia.org/wiki/Philippine_peso"><img src="https://img.shields.io/badge/Currency-Philippine_Peso_(₱)-008080?style=for-the-badge" alt="Philippine Peso" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge" alt="License MIT" /></a>
</p>
---
## 📌 Executive Overview
**Pawdacity** is a high-performance, single-file e-commerce web application and pet salon booking suite tailored specifically for pet owners and businesses across the **Philippines**. 
Built entirely with standard web technologies (**Vanilla HTML5**, **CSS3 Custom Properties**, and **modern ES6+ JavaScript**), Pawdacity functions without any Node.js build pipeline, bundling phase, or mandatory server infrastructure. It includes an embedded image dictionary, real-time procedural SVG rendering, responsive cart operations, coupon rules, appointment collision management, and an interactive **Live Owner Studio (Ctrl+K)**.
---
## 🌟 Key Features
<p align="center">
  <img src="assets/features.svg" alt="Pawdacity Core Capabilities" width="100%" />
</p>
| Capability | Technical Realization | User Experience |
| :--- | :--- | :--- |
| **🛍️ 30-Product Catalog** | Data tuple `[id, cat, name, price, images]` with procedural SVG fallback generator | Instant loading, category chips, live keyword search, dynamic price slider, and multi-image photo carousels. |
| **🔍 Quick View Modal** | HTML5 `<dialog>` API with thumbnail photo switcher | Seamless product inspection without navigating away from the current scroll position. |
| **🛒 Reactive Shopping Cart** | Real-time `tot()` pure calculation with local persistence in `pc_cart` | Slide-out cart drawer, quantity selectors, live subtotals, and animated badge counter. |
| **🚚 Free Shipping Meter** | Dynamic CSS percentage bar calculated relative to ₱999 threshold | Live countdown showing exact pesos remaining to unlock free delivery across the Philippines. |
| **🏷️ Promotional Coupons** | Functional discount rules dictionary (`CP`) | `PAW10` (10% off), `WELCOME50` (₱50 off), and `FREESHIP` (Free delivery). |
| **💳 Philippine Checkout** | Simulated checkout accommodating **GCash**, **Maya**, **Cards**, and **Cash on Delivery (COD)** | Regex card validation, synthesis of unique order serial `PAW-XXXXXX`, and itemized `mailto:` customer order dispatch. |
| **📅 Salon & Vet Booking** | Interactive scheduling form with collision prevention | Double-booking protection preventing overlapping appointments, plus instant confirmation mailers. |
| **🎨 Live Owner Studio (`Ctrl+K`)** | Dynamic CSS Variable engine mutating `--ind`, `--or`, `--co`, `--pk`, `--fd`, `--rad` | Instant brand customization: switch among 4 built-in palettes, 8 Google Fonts, border radius, and card shadows. |
