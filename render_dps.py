import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
base_dir = r'c:\Users\dell\Downloads\insight222'

# 1. DP Badge Style (Corrected curved text, bolder typography, luxurious glow)
dp_badge_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1080px;
    height: 1080px;
    background: #06050f;
    font-family: 'Montserrat', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
  }
  
  /* Nebula background glow */
  .glow-center {
    position: absolute;
    width: 750px;
    height: 750px;
    top: 48%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.32) 0%, rgba(217, 70, 239, 0.16) 40%, rgba(107, 70, 193, 0.05) 65%, transparent 75%);
    filter: blur(40px);
    pointer-events: none;
  }
  .glow-accent {
    position: absolute;
    width: 480px;
    height: 480px;
    top: 36%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    background: radial-gradient(circle, rgba(217, 70, 239, 0.28) 0%, transparent 60%);
    filter: blur(35px);
    pointer-events: none;
  }

  /* Fine cyber grid & subtle particle dust */
  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(rgba(139, 92, 246, 0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(139, 92, 246, 0.035) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    mask-image: radial-gradient(circle at 50% 50%, black 40%, transparent 75%);
    -webkit-mask-image: radial-gradient(circle at 50% 50%, black 40%, transparent 75%);
  }

  .sparkles {
    position: absolute;
    inset: 0;
    background-image: 
      radial-gradient(2px 2px at 180px 220px, rgba(255,255,255,0.8), transparent),
      radial-gradient(2.5px 2.5px at 880px 260px, rgba(196,181,253,0.9), transparent),
      radial-gradient(2px 2px at 240px 840px, rgba(232,121,249,0.8), transparent),
      radial-gradient(2px 2px at 840px 820px, rgba(251,191,36,0.7), transparent),
      radial-gradient(1.5px 1.5px at 340px 420px, rgba(255,255,255,0.7), transparent),
      radial-gradient(2px 2px at 760px 400px, rgba(167,139,250,0.8), transparent);
    pointer-events: none;
  }

  /* Outer ambient ring */
  .ambient-ring {
    position: absolute;
    width: 860px;
    height: 860px;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    border: 1px solid rgba(139, 92, 246, 0.12);
    box-shadow: 0 0 60px rgba(139, 92, 246, 0.08);
    pointer-events: none;
  }

  /* Main Wrapper */
  .wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 10;
    margin-top: -24px;
  }

  /* Circular Badge */
  .badge-frame {
    position: relative;
    width: 450px;
    height: 450px;
    border-radius: 50%;
    background: linear-gradient(135deg, #a78bfa 0%, #d946ef 50%, #fbbf24 100%);
    padding: 3.5px;
    box-shadow: 
      0 0 100px -10px rgba(139, 92, 246, 0.65),
      0 30px 80px -10px rgba(0, 0, 0, 0.85),
      inset 0 2px 3px rgba(255, 255, 255, 0.7);
  }

  .badge-surface {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #581c87 0%, #3b0764 45%, #17052e 80%, #090214 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    box-shadow: 
      inset 0 20px 45px rgba(196, 181, 253, 0.2),
      inset 0 -20px 45px rgba(0, 0, 0, 0.7);
  }

  /* Concentric inner ring */
  .inner-ring {
    position: absolute;
    width: 320px;
    height: 320px;
    border-radius: 50%;
    border: 1.5px solid rgba(196, 181, 253, 0.28);
    pointer-events: none;
  }

  /* SVG Curved Circular Text */
  .curved-svg {
    position: absolute;
    width: 443px;
    height: 443px;
    top: 0;
    left: 0;
    pointer-events: none;
  }
  .curved-svg text {
    fill: #ffffff;
    font-size: 19px;
    font-weight: 800;
    letter-spacing: 6px;
    text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
  }

  /* Central Monogram */
  .monogram-core {
    width: 290px;
    height: 290px;
    border-radius: 50%;
    background: radial-gradient(circle at 40% 35%, #7c3aed 0%, #5b21b6 55%, #3b0764 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 
      0 15px 40px rgba(0, 0, 0, 0.65),
      inset 0 2px 4px rgba(255, 255, 255, 0.45),
      0 0 35px rgba(139, 92, 246, 0.5);
    border: 2px solid rgba(255, 255, 255, 0.28);
    position: relative;
    z-index: 5;
  }

  .monogram-svg {
    width: 190px;
    height: 190px;
    overflow: visible;
  }

  /* Brand Typography beneath */
  .brand-lockup {
    margin-top: 54px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .brand-title {
    font-size: 52px;
    font-weight: 900;
    letter-spacing: 8px;
    color: #ffffff;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    justify-content: center;
    text-shadow: 0 4px 30px rgba(139, 92, 246, 0.6);
  }

  .brand-title .highlight {
    background: linear-gradient(110deg, #c4b5fd 0%, #f472b6 50%, #fbbf24 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 900;
  }

  .brand-subtitle {
    margin-top: 15px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 11px;
    color: #c4b5fd;
    text-transform: uppercase;
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .brand-subtitle .dot {
    color: #fbbf24;
    font-size: 11px;
  }

  .contact-pill {
    margin-top: 22px;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 9px 24px;
    border-radius: 99px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(196, 181, 253, 0.25);
    font-size: 13.5px;
    font-weight: 600;
    letter-spacing: 3px;
    color: #e9d5ff;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.4);
  }

  .contact-pill i {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #34d399;
    box-shadow: 0 0 10px #34d399;
  }
</style>
</head>
<body>
  <div class="glow-center"></div>
  <div class="glow-accent"></div>
  <div class="grid-bg"></div>
  <div class="sparkles"></div>
  <div class="ambient-ring"></div>

  <div class="wrapper">
    <!-- Signature Circular Badge -->
    <div class="badge-frame">
      <div class="badge-surface">
        <div class="inner-ring"></div>
        
        <!-- SVG Curved Circular Text (Top: INSIGHT NOVATECH, Bottom: INNOVATION & TECH right-side up) -->
        <svg class="curved-svg" viewBox="0 0 443 443">
          <defs>
            <!-- Top curve (clockwise from 200° to 340°) -->
            <path id="top-path" d="M 45,221.5 A 176.5,176.5 0 1,1 398,221.5" fill="none" />
            <!-- Bottom curve (clockwise from left to right along bottom so text is upright!) -->
            <path id="bottom-path" d="M 52,221.5 A 170,170 0 0,0 391,221.5" fill="none" />
          </defs>
          <text>
            <textPath href="#top-path" startOffset="50%" text-anchor="middle">
              INSIGHT NOVATECH
            </textPath>
          </text>
          <text style="font-size: 16px; letter-spacing: 8px; fill: rgba(245,243,255,0.85);">
            <textPath href="#bottom-path" startOffset="50%" text-anchor="middle">
              ✦ INNOVATION & TECH ✦
            </textPath>
          </text>
        </svg>

        <!-- Central 3D Monogram -->
        <div class="monogram-core">
          <svg class="monogram-svg" viewBox="0 0 100 100">
            <defs>
              <linearGradient id="coregrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="100%" stop-color="#f5f3ff"/>
              </linearGradient>
              <filter id="coreshadow" x="-30%" y="-30%" width="160%" height="160%">
                <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.5"/>
                <feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="#c4b5fd" flood-opacity="0.6"/>
              </filter>
            </defs>
            <!-- Dot for 'i' -->
            <circle cx="24" cy="20" r="8.5" fill="url(#coregrad)" filter="url(#coreshadow)"/>
            <!-- Monogram Path -->
            <path d="M24 38V62a14 14 0 0 0 28 0V38l24 30V30" fill="none" stroke="url(#coregrad)" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" filter="url(#coreshadow)"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- Brand Typography Beneath -->
    <div class="brand-lockup">
      <h1 class="brand-title">
        <span>INSIGHT</span><span class="highlight">NOVATECH</span>
      </h1>
      <div class="brand-subtitle">
        IDEAS <span class="dot">✦</span> CODE <span class="dot">✦</span> IMPACT
      </div>
      <div class="contact-pill">
        <i></i> www.insightnovatech.com
      </div>
    </div>
  </div>
</body>
</html>'''

# 2. DP Minimalist 3D Monogram Style (Clean luxury icon)
dp_modern_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1080px;
    height: 1080px;
    background: #06050f;
    font-family: 'Montserrat', sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    position: relative;
  }
  
  .glow-main {
    position: absolute;
    width: 800px;
    height: 800px;
    top: 46%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.35) 0%, rgba(217, 70, 239, 0.18) 45%, transparent 70%);
    filter: blur(50px);
    pointer-events: none;
  }

  .grid-pattern {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(rgba(196, 181, 253, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(196, 181, 253, 0.04) 1px, transparent 1px);
    background-size: 44px 44px;
    pointer-events: none;
  }

  .wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 10;
    margin-top: -20px;
  }

  /* 3D Glassmorphism Icon Squircle */
  .icon-card {
    position: relative;
    width: 440px;
    height: 440px;
    border-radius: 110px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.14) 0%, rgba(255, 255, 255, 0.02) 60%, rgba(217, 70, 239, 0.12) 100%);
    padding: 3px;
    box-shadow: 
      0 0 90px -10px rgba(139, 92, 246, 0.7),
      0 35px 80px -15px rgba(0, 0, 0, 0.9),
      inset 0 1px 2px rgba(255, 255, 255, 0.5);
  }

  .icon-inner {
    width: 100%;
    height: 100%;
    border-radius: 107px;
    background: radial-gradient(circle at 30% 25%, #4c1d95 0%, #2e1065 50%, #110526 85%, #080214 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    box-shadow: 
      inset 0 20px 40px rgba(196, 181, 253, 0.22),
      inset 0 -20px 40px rgba(0, 0, 0, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.12);
  }

  .monogram-svg {
    width: 250px;
    height: 250px;
    overflow: visible;
  }

  .brand-lockup {
    margin-top: 56px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .brand-title {
    font-size: 54px;
    font-weight: 900;
    letter-spacing: 9px;
    color: #ffffff;
    text-transform: uppercase;
    text-shadow: 0 4px 30px rgba(139, 92, 246, 0.65);
  }

  .brand-title .grad {
    background: linear-gradient(110deg, #c4b5fd 0%, #e879f9 55%, #fde047 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .brand-tagline {
    margin-top: 14px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 12px;
    color: #c4b5fd;
    text-transform: uppercase;
  }

  .brand-badge {
    margin-top: 24px;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 9px 26px;
    border-radius: 99px;
    background: rgba(139, 92, 246, 0.1);
    border: 1px solid rgba(167, 139, 250, 0.3);
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 3.5px;
    color: #f5f3ff;
  }
  .brand-badge i {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #34d399;
    box-shadow: 0 0 10px #34d399;
  }
</style>
</head>
<body>
  <div class="glow-main"></div>
  <div class="grid-pattern"></div>

  <div class="wrapper">
    <div class="icon-card">
      <div class="icon-inner">
        <svg class="monogram-svg" viewBox="0 0 100 100">
          <defs>
            <linearGradient id="mgrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#ffffff"/>
              <stop offset="100%" stop-color="#f3e8ff"/>
            </linearGradient>
            <filter id="mshadow" x="-30%" y="-30%" width="160%" height="160%">
              <feDropShadow dx="0" dy="10" stdDeviation="8" flood-color="#000000" flood-opacity="0.55"/>
              <feDropShadow dx="0" dy="0" stdDeviation="15" flood-color="#a78bfa" flood-opacity="0.6"/>
            </filter>
          </defs>
          <circle cx="24" cy="20" r="8.5" fill="url(#mgrad)" filter="url(#mshadow)"/>
          <path d="M24 38V62a14 14 0 0 0 28 0V38l24 30V30" fill="none" stroke="url(#mgrad)" stroke-width="13" stroke-linecap="round" stroke-linejoin="round" filter="url(#mshadow)"/>
        </svg>
      </div>
    </div>

    <div class="brand-lockup">
      <h1 class="brand-title">
        <span>INSIGHT</span><span class="grad">NOVATECH</span>
      </h1>
      <div class="brand-tagline">
        IDEAS · CODE · IMPACT
      </div>
      <div class="brand-badge">
        <i></i> DIGITAL AGENCY
      </div>
    </div>
  </div>
</body>
</html>'''

# Write HTML files
with open(os.path.join(base_dir, 'render_dp_badge.html'), 'w', encoding='utf-8') as f:
    f.write(dp_badge_html)

with open(os.path.join(base_dir, 'render_dp_modern.html'), 'w', encoding='utf-8') as f:
    f.write(dp_modern_html)

# Render to PNG
subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    f'--screenshot={os.path.join(base_dir, "logo_dp_badge.png")}',
    '--window-size=1080,1080', '--default-background-color=00000000',
    f'file:///{base_dir.replace("\\\\", "/")}/render_dp_badge.html'
], check=True)

subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    f'--screenshot={os.path.join(base_dir, "logo_dp_modern.png")}',
    '--window-size=1080,1080', '--default-background-color=00000000',
    f'file:///{base_dir.replace("\\\\", "/")}/render_dp_modern.html'
], check=True)

print("Both DP styles rendered successfully!")
