import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
base_dir = r'c:\Users\dell\Downloads\insight222'

# 1. Perfected DP Badge Style (1080x1080)
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
  
  .glow-center {
    position: absolute;
    width: 800px;
    height: 800px;
    top: 48%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.35) 0%, rgba(217, 70, 239, 0.18) 40%, transparent 72%);
    filter: blur(50px);
    pointer-events: none;
  }
  .glow-accent {
    position: absolute;
    width: 500px;
    height: 500px;
    top: 36%;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    background: radial-gradient(circle, rgba(217, 70, 239, 0.28) 0%, transparent 60%);
    filter: blur(40px);
    pointer-events: none;
  }

  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(rgba(139, 92, 246, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(139, 92, 246, 0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    mask-image: radial-gradient(circle at 50% 50%, black 45%, transparent 75%);
    -webkit-mask-image: radial-gradient(circle at 50% 50%, black 45%, transparent 75%);
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

  .wrapper {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    z-index: 10;
    margin-top: -20px;
  }

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

  .inner-ring {
    position: absolute;
    width: 320px;
    height: 320px;
    border-radius: 50%;
    border: 1.5px solid rgba(196, 181, 253, 0.28);
    pointer-events: none;
  }

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
    filter: drop-shadow(0 10px 18px rgba(0, 0, 0, 0.55)) drop-shadow(0 0 25px rgba(196, 181, 253, 0.6));
  }

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

  <div class="wrapper">
    <div class="badge-frame">
      <div class="badge-surface">
        <div class="inner-ring"></div>
        
        <svg class="curved-svg" viewBox="0 0 443 443">
          <defs>
            <path id="top-path" d="M 45,221.5 A 176.5,176.5 0 1,1 398,221.5" fill="none" />
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

        <div class="monogram-core">
          <svg class="monogram-svg" viewBox="0 0 100 100">
            <circle cx="24" cy="20" r="8.5" fill="white"/>
            <path d="M24 38V62a14 14 0 0 0 28 0V38l24 30V30" fill="none" stroke="white" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </div>
      </div>
    </div>

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

# 2. Perfected Modern Minimalist 3D Squircle DP (1080x1080)
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

  .icon-card {
    position: relative;
    width: 440px;
    height: 440px;
    border-radius: 110px;
    background: linear-gradient(145deg, rgba(255, 255, 255, 0.16) 0%, rgba(255, 255, 255, 0.02) 60%, rgba(217, 70, 239, 0.14) 100%);
    padding: 3.5px;
    box-shadow: 
      0 0 95px -10px rgba(139, 92, 246, 0.75),
      0 35px 80px -15px rgba(0, 0, 0, 0.9),
      inset 0 1px 2px rgba(255, 255, 255, 0.5);
  }

  .icon-inner {
    width: 100%;
    height: 100%;
    border-radius: 106px;
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
    filter: drop-shadow(0 14px 22px rgba(0,0,0,0.6)) drop-shadow(0 0 35px rgba(196, 181, 253, 0.65));
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
    background: rgba(139, 92, 246, 0.12);
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
          <circle cx="24" cy="20" r="8.5" fill="white"/>
          <path d="M24 38V62a14 14 0 0 0 28 0V38l24 30V30" fill="none" stroke="white" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
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
        <i></i> www.insightnovatech.com
      </div>
    </div>
  </div>
</body>
</html>'''

# 3. Full 16:9 Landscape Banner (1920x1080)
banner_16x9_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px;
    height: 1080px;
    background: #06050f;
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 70px 100px;
  }

  .glow-top-left {
    position: absolute;
    width: 800px;
    height: 800px;
    left: -200px;
    top: -200px;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.28) 0%, transparent 65%);
    filter: blur(60px);
    pointer-events: none;
  }
  .glow-center-right {
    position: absolute;
    width: 1000px;
    height: 900px;
    right: -150px;
    top: 50%;
    transform: translateY(-50%);
    background: radial-gradient(circle, rgba(217, 70, 239, 0.26) 0%, rgba(139, 92, 246, 0.2) 45%, transparent 70%);
    filter: blur(60px);
    pointer-events: none;
  }

  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(rgba(196, 181, 253, 0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(196, 181, 253, 0.035) 1px, transparent 1px);
    background-size: 50px 50px;
    pointer-events: none;
  }

  /* Top Navigation Bar */
  .top-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    z-index: 10;
  }

  .nav-brand {
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .nav-logo-badge {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #7c3aed, #4c1d95 60%, #1e0845 100%);
    border: 1.5px solid rgba(255, 255, 255, 0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 25px rgba(139, 92, 246, 0.5);
  }
  .nav-logo-badge svg {
    width: 30px;
    height: 30px;
  }

  .nav-title {
    font-size: 22px;
    font-weight: 800;
    letter-spacing: 2px;
  }
  .nav-title span {
    background: linear-gradient(100deg, #c4b5fd, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  .nav-tag {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 20px;
    border-radius: 99px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(196, 181, 253, 0.22);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    color: #c4b5fd;
    text-transform: uppercase;
  }
  .nav-tag i {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #34d399;
    box-shadow: 0 0 8px #34d399;
  }

  /* Center Main Area */
  .center-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 60px;
    position: relative;
    z-index: 10;
    margin: 40px 0;
  }

  .hero-left {
    max-width: 900px;
  }

  .hero-h1 {
    font-size: 76px;
    font-weight: 900;
    line-height: 1.05;
    letter-spacing: -2.5px;
    margin-bottom: 24px;
    text-transform: uppercase;
  }

  .hero-h1 .grad {
    background: linear-gradient(100deg, #a78bfa 0%, #d946ef 55%, #fbbf24 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }

  .hero-p {
    font-size: 21px;
    font-weight: 500;
    line-height: 1.5;
    color: #cbd5e1;
    margin-bottom: 34px;
    max-width: 780px;
  }

  .service-row {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    margin-bottom: 40px;
  }

  .serv-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 22px;
    border-radius: 99px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(196, 181, 253, 0.2);
    font-size: 15px;
    font-weight: 600;
    color: #f8fafc;
    backdrop-filter: blur(12px);
  }
  .serv-pill span {
    color: #d946ef;
    font-size: 16px;
  }

  .cta-group {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    padding: 16px 36px;
    border-radius: 99px;
    background: linear-gradient(100deg, #7c3aed, #c026d3);
    color: #ffffff;
    font-size: 16px;
    font-weight: 700;
    box-shadow: 0 14px 44px -8px rgba(168, 85, 247, 0.85);
  }

  .btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 15px 32px;
    border-radius: 99px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(196, 181, 253, 0.3);
    color: #e2e8f0;
    font-size: 15px;
    font-weight: 600;
  }

  /* Right Showcase UI Elements */
  .hero-right {
    position: relative;
    width: 660px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  .main-card {
    width: 580px;
    border-radius: 36px;
    background: rgba(14, 10, 40, 0.72);
    border: 1.5px solid rgba(196, 181, 253, 0.25);
    backdrop-filter: blur(28px) saturate(1.5);
    box-shadow: 
      0 40px 100px -20px rgba(0, 0, 0, 0.85),
      0 0 80px -10px rgba(139, 92, 246, 0.4),
      inset 0 1px 2px rgba(255, 255, 255, 0.4);
    padding: 38px 42px;
    display: flex;
    flex-direction: column;
    gap: 24px;
  }

  .card-top {
    display: flex;
    align-items: center;
    gap: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid rgba(196, 181, 253, 0.14);
  }

  .large-badge {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #7c3aed, #4c1d95 60%, #1e0845 100%);
    border: 2px solid rgba(255, 255, 255, 0.35);
    box-shadow: 0 10px 30px rgba(124, 58, 237, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .large-badge svg {
    width: 48px;
    height: 48px;
  }

  .card-top-info h2 {
    font-size: 24px;
    font-weight: 800;
    letter-spacing: 2px;
  }
  .card-top-info h2 span {
    background: linear-gradient(100deg, #c4b5fd, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .card-top-info p {
    font-size: 13px;
    letter-spacing: 4px;
    color: #a7a2cf;
    text-transform: uppercase;
    font-weight: 600;
    margin-top: 4px;
  }

  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }

  .stat-card {
    background: rgba(255, 255, 255, 0.035);
    border: 1px solid rgba(196, 181, 253, 0.14);
    border-radius: 20px;
    padding: 20px 22px;
  }
  .stat-num {
    font-size: 32px;
    font-weight: 900;
    color: #ffffff;
  }
  .stat-num.teal { color: #34d399; }
  .stat-num.pink { color: #f472b6; }
  .stat-label {
    font-size: 12.5px;
    font-weight: 600;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-top: 6px;
  }

  .live-status {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(139, 92, 246, 0.12);
    border: 1px solid rgba(167, 139, 250, 0.28);
    border-radius: 16px;
    padding: 14px 22px;
  }
  .live-status-left {
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: 14px;
    font-weight: 600;
  }
  .live-status-left i {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #34d399;
    box-shadow: 0 0 10px #34d399;
  }
  .live-status-right {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #fbbf24;
    background: rgba(251, 191, 36, 0.12);
    padding: 4px 12px;
    border-radius: 8px;
  }

  /* Bottom Bar */
  .bottom-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 24px;
    border-top: 1px solid rgba(196, 181, 253, 0.15);
    position: relative;
    z-index: 10;
  }

  .bottom-contacts {
    display: flex;
    align-items: center;
    gap: 36px;
  }

  .contact-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 15px;
    font-weight: 600;
    color: #e2e8f0;
  }
  .contact-item span { color: #a78bfa; font-size: 18px; }

  .bottom-motto {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 4px;
    color: #94a3b8;
    text-transform: uppercase;
  }
  .bottom-motto b { color: #fbbf24; }
</style>
</head>
<body>
  <div class="glow-top-left"></div>
  <div class="glow-center-right"></div>
  <div class="grid-bg"></div>

  <!-- Top Nav -->
  <div class="top-nav">
    <div class="nav-brand">
      <div class="nav-logo-badge">
        <svg viewBox="0 0 100 100">
          <circle cx="24" cy="20" r="8" fill="white"/>
          <path d="M24 38V62a14 14 0 0 0 28 0V38l24 30V30" fill="none" stroke="white" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <div class="nav-title">INSIGHT<span>NOVATECH</span></div>
    </div>
    <div class="nav-tag">
      <i></i> Global Engineering & Design Studio
    </div>
  </div>

  <!-- Center Content -->
  <div class="center-content">
    <div class="hero-left">
      <h1 class="hero-h1">
        We Build Your<br>
        <span class="grad">Vision Into Reality</span>
      </h1>
      <p class="hero-p">
        We design, engineer, and deploy high-converting websites, high-performance mobile apps, and autonomous AI systems built to scale.
      </p>

      <div class="service-row">
        <div class="serv-pill"><span>✦</span> Full-Stack Websites</div>
        <div class="serv-pill"><span>✦</span> iOS & Android Apps</div>
        <div class="serv-pill"><span>✦</span> AI & Workflow Automation</div>
        <div class="serv-pill"><span>✦</span> Custom SaaS Solutions</div>
      </div>

      <div class="cta-group">
        <div class="btn-primary">
          <span>Get Started Today</span> ➔
        </div>
        <div class="btn-outline">
          <span>08135971304</span>
        </div>
      </div>
    </div>

    <div class="hero-right">
      <div class="main-card">
        <div class="card-top">
          <div class="large-badge">
            <svg viewBox="0 0 100 100">
              <circle cx="24" cy="20" r="8" fill="white"/>
              <path d="M24 38V62a14 14 0 0 0 28 0V38l24 30V30" fill="none" stroke="white" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="card-top-info">
            <h2>INSIGHT<span>NOVATECH</span></h2>
            <p>Ideas · Code · Impact</p>
          </div>
        </div>

        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-num teal">100%</div>
            <div class="stat-label">Production Delivery</div>
          </div>
          <div class="stat-card">
            <div class="stat-num pink">99.9%</div>
            <div class="stat-label">Security & Uptime</div>
          </div>
        </div>

        <div class="live-status">
          <div class="live-status-left">
            <i></i> Modern Software Architecture
          </div>
          <div class="live-status-right">ACTIVE & READY</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Bottom Bar -->
  <div class="bottom-bar">
    <div class="bottom-contacts">
      <div class="contact-item">
        <span>📞</span> 08135971304
      </div>
      <div class="contact-item">
        <span>🌐</span> www.insightnovatech.com
      </div>
      <div class="contact-item">
        <span>📍</span> Lagos, Nigeria
      </div>
    </div>
    <div class="bottom-motto">
      ENGINEERING THE <b>FUTURE</b> OF DIGITAL
    </div>
  </div>
</body>
</html>'''

# Write HTML files
with open(os.path.join(base_dir, 'render_dp_badge.html'), 'w', encoding='utf-8') as f:
    f.write(dp_badge_html)

with open(os.path.join(base_dir, 'render_dp_modern.html'), 'w', encoding='utf-8') as f:
    f.write(dp_modern_html)

with open(os.path.join(base_dir, 'render_banner_16x9.html'), 'w', encoding='utf-8') as f:
    f.write(banner_16x9_html)

# Render DP Badge (1080x1080)
subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    f'--screenshot={os.path.join(base_dir, "logo_dp_badge.png")}',
    '--window-size=1080,1080', '--default-background-color=00000000',
    f'file:///{base_dir.replace("\\\\", "/")}/render_dp_badge.html'
], check=True)

# Render DP Modern (1080x1080)
subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    f'--screenshot={os.path.join(base_dir, "logo_dp_modern.png")}',
    '--window-size=1080,1080', '--default-background-color=00000000',
    f'file:///{base_dir.replace("\\\\", "/")}/render_dp_modern.html'
], check=True)

# Render 16:9 Banner (1920x1080)
subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    f'--screenshot={os.path.join(base_dir, "banner_social_16x9.png")}',
    '--window-size=1920,1080', '--default-background-color=00000000',
    f'file:///{base_dir.replace("\\\\", "/")}/render_banner_16x9.html'
], check=True)

print("All brand assets (DPs & Banners) rendered successfully!")
