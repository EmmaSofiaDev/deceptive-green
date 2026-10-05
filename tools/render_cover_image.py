#!/usr/bin/env python3
"""
Render a studio-grade 3D conceptual cover image for 'The Deceptive Green'.
Strictly adheres to AGENTS.md / GEMINI.md rules:
- Dark studio gradient (midnight obsidian with deep emerald fill and warm amber rim)
- Centerpiece: Glossy 3D translucent glass geometric prism with glowing dual emerald/crimson core
- Orbiting glass refraction nodes and subtle particle dust
- ZERO code blocks, ZERO UI cards, ZERO text overlays
- Exact 1000 x 420 px aspect ratio (rendered at 2000 x 840 high-DPI)
"""

import os
from pathlib import Path
from playwright.sync_api import sync_playwright

OUTPUT_DIR = Path("deceptive-green/assets")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_PATH = OUTPUT_DIR / "deceptive_green_cover.png"

CANVAS_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    width: 1000px;
    height: 420px;
    overflow: hidden;
    background: #050a0a;
}
canvas {
    width: 1000px;
    height: 420px;
    display: block;
}
</style>
</head>
<body>
<canvas id="cv" width="2000" height="840"></canvas>
<script>
const cv = document.getElementById('cv');
const ctx = cv.getContext('2d');
const W = 2000;
const H = 840;

// 1. Studio Backdrop with Atmospheric Volumetric Lighting
const bgGrad = ctx.createLinearGradient(0, 0, W, H);
bgGrad.addColorStop(0, '#040d0c');
bgGrad.addColorStop(0.5, '#061311');
bgGrad.addColorStop(1, '#020606');
ctx.fillStyle = bgGrad;
ctx.fillRect(0, 0, W, H);

// Warm amber studio rim light (top right)
const amberGlow = ctx.createRadialGradient(W * 0.90, H * 0.10, 50, W * 0.90, H * 0.10, 900);
amberGlow.addColorStop(0, 'rgba(245, 158, 11, 0.35)');
amberGlow.addColorStop(0.5, 'rgba(217, 119, 6, 0.12)');
amberGlow.addColorStop(1, 'rgba(0, 0, 0, 0)');
ctx.fillStyle = amberGlow;
ctx.fillRect(0, 0, W, H);

// Deep emerald glow from below (the 'green checkmark' aura)
const emeraldGlow = ctx.createRadialGradient(W * 0.5, H * 0.55, 100, W * 0.5, H * 0.55, 1000);
emeraldGlow.addColorStop(0, 'rgba(16, 185, 129, 0.28)');
emeraldGlow.addColorStop(0.4, 'rgba(5, 150, 105, 0.12)');
emeraldGlow.addColorStop(1, 'rgba(0, 0, 0, 0)');
ctx.fillStyle = emeraldGlow;
ctx.fillRect(0, 0, W, H);

// Subtle Crimson/Amber fault-line glow (representing hidden deception)
const crimsonGlow = ctx.createRadialGradient(W * 0.45, H * 0.48, 20, W * 0.45, H * 0.48, 500);
crimsonGlow.addColorStop(0, 'rgba(239, 68, 68, 0.30)');
crimsonGlow.addColorStop(0.6, 'rgba(185, 28, 28, 0.08)');
crimsonGlow.addColorStop(1, 'rgba(0, 0, 0, 0)');
ctx.fillStyle = crimsonGlow;
ctx.fillRect(0, 0, W, H);

// 2. Isometric 3D Translucent Glass Monolith
const cx = W * 0.5;
const cy = H * 0.48;
const size = 260;

function drawIsometricPrism(x, y, s) {
    ctx.save();
    
    // Top Face (Emerald Reflective)
    ctx.beginPath();
    ctx.moveTo(x, y - s);
    ctx.lineTo(x + s * 1.732 * 0.5, y - s * 0.5);
    ctx.lineTo(x, y);
    ctx.lineTo(x - s * 1.732 * 0.5, y - s * 0.5);
    ctx.closePath();
    const topGrad = ctx.createLinearGradient(x - s, y - s, x + s, y);
    topGrad.addColorStop(0, 'rgba(52, 211, 153, 0.65)');
    topGrad.addColorStop(0.5, 'rgba(16, 185, 129, 0.40)');
    topGrad.addColorStop(1, 'rgba(6, 95, 70, 0.70)');
    ctx.fillStyle = topGrad;
    ctx.fill();
    ctx.strokeStyle = 'rgba(110, 231, 183, 0.85)';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Left Face (Shadowed Glass with Crimson Refraction)
    ctx.beginPath();
    ctx.moveTo(x - s * 1.732 * 0.5, y - s * 0.5);
    ctx.lineTo(x, y);
    ctx.lineTo(x, y + s * 1.2);
    ctx.lineTo(x - s * 1.732 * 0.5, y + s * 0.7);
    ctx.closePath();
    const leftGrad = ctx.createLinearGradient(x - s, y, x, y + s);
    leftGrad.addColorStop(0, 'rgba(239, 68, 68, 0.45)');
    leftGrad.addColorStop(0.4, 'rgba(15, 118, 110, 0.35)');
    leftGrad.addColorStop(1, 'rgba(4, 47, 46, 0.80)');
    ctx.fillStyle = leftGrad;
    ctx.fill();
    ctx.strokeStyle = 'rgba(52, 211, 153, 0.40)';
    ctx.lineWidth = 2;
    ctx.stroke();

    // Right Face (Deep Refraction with Amber Rim Edge)
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x + s * 1.732 * 0.5, y - s * 0.5);
    ctx.lineTo(x + s * 1.732 * 0.5, y + s * 0.7);
    ctx.lineTo(x, y + s * 1.2);
    ctx.closePath();
    const rightGrad = ctx.createLinearGradient(x, y, x + s, y + s);
    rightGrad.addColorStop(0, 'rgba(251, 191, 36, 0.35)');
    rightGrad.addColorStop(0.5, 'rgba(5, 150, 105, 0.25)');
    rightGrad.addColorStop(1, 'rgba(2, 44, 34, 0.85)');
    ctx.fillStyle = rightGrad;
    ctx.fill();
    ctx.strokeStyle = 'rgba(251, 191, 36, 0.60)';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Inner Glowing Core (The Fractured Diamond)
    ctx.beginPath();
    ctx.arc(x, y + s * 0.2, 50, 0, Math.PI * 2);
    const coreGrad = ctx.createRadialGradient(x, y + s * 0.2, 5, x, y + s * 0.2, 55);
    coreGrad.addColorStop(0, '#ffffff');
    coreGrad.addColorStop(0.3, '#34d399');
    coreGrad.addColorStop(0.7, '#f59e0b');
    coreGrad.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = coreGrad;
    ctx.fill();

    ctx.restore();
}

drawIsometricPrism(cx, cy, size);

// 3. Orbiting Glass Nodes (Verification Spheres)
const nodes = [
    { x: cx - 420, y: cy - 90, r: 28, color: 'rgba(52, 211, 153, 0.75)' },
    { x: cx + 460, y: cy - 140, r: 36, color: 'rgba(251, 191, 36, 0.80)' },
    { x: cx - 350, y: cy + 180, r: 22, color: 'rgba(239, 68, 68, 0.70)' },
    { x: cx + 380, y: cy + 160, r: 30, color: 'rgba(16, 185, 129, 0.75)' },
    { x: cx + 60, y: cy - 240, r: 18, color: 'rgba(245, 158, 11, 0.65)' }
];

nodes.forEach(n => {
    // Subtle ray connecting to center
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(n.x, n.y);
    ctx.strokeStyle = 'rgba(52, 211, 153, 0.12)';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    // Node sphere
    ctx.beginPath();
    ctx.arc(n.x, n.y, n.r, 0, Math.PI * 2);
    const rad = ctx.createRadialGradient(n.x - n.r * 0.3, n.y - n.r * 0.3, n.r * 0.1, n.x, n.y, n.r);
    rad.addColorStop(0, '#ffffff');
    rad.addColorStop(0.4, n.color);
    rad.addColorStop(1, 'rgba(0,0,0,0.6)');
    ctx.fillStyle = rad;
    ctx.fill();
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
    ctx.lineWidth = 1;
    ctx.stroke();
});

// 4. Subtle Bokeh and Floating Dust
for (let i = 0; i < 40; i++) {
    const px = (Math.sin(i * 99) * 0.5 + 0.5) * W;
    const py = (Math.cos(i * 33) * 0.5 + 0.5) * H;
    const pr = 2 + (i % 5);
    ctx.beginPath();
    ctx.arc(px, py, pr, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(110, 231, 183, ${0.15 + (i % 4) * 0.08})`;
    ctx.fill();
}
</script>
</body>
</html>
"""

def generate_cover():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1000, "height": 420})
        page.set_content(CANVAS_HTML)
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUTPUT_PATH))
        browser.close()
    print(f"Cover image rendered successfully to: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate_cover()
