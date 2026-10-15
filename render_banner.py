import subprocess
import os

chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
base_dir = r'c:\Users\dell\Downloads\insight222'

# 1. Wide Banner (1920 x 640) - Standard Social Media Cover (Twitter, LinkedIn, Facebook)
banner_wide_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    width: 1920px;
    height: 640px;
    background: #06050f;
    font-family: 'Montserrat', sans-serif;
    color: #ffffff;
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: center;
  }

  /* Deep space lighting */
  .glow-left {
    position: absolute;
    width: 700px;
    height: 700px;
    left: -150px;
    top: -100px;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.22) 0%, transparent 65%);
    filter: blur(50px);
    pointer-events: none;
  }
  .glow-right {
    position: absolute;
    width: 900px;
    height: 800px;
    right: -100px;
    top: -100px;
    background: radial-gradient(circle, rgba(217, 70, 239, 0.25) 0%, rgba(139, 92, 246, 0.20) 45%, transparent 70%);
    filter: blur(50px);
    pointer-events: none;
  }
  .glow-bottom {
    position: absolute;
    width: 600px;
    height: 400px;
    right: 250px;
    bottom: -150px;
    background: radial-gradient(circle, rgba(251, 191, 36, 0.12) 0%, transparent 60%);
    filter: blur(60px);
    pointer-events: none;
  }

  /* Modern Cyber Grid */
  .grid-bg {
    position: absolute;
    inset: 0;
    background-image: 
      linear-gradient(rgba(196, 181, 253, 0.035) 1px, transparent 1px),
      linear-gradient(90deg, rgba(196, 181, 253, 0.035) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
  }

  /* High-tech circuit / particle dots */
  .stars {
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(1.5px 1.5px at 120px 100px, rgba(255,255,255,0.7), transparent),
      radial-gradient(2px 2px at 450px 80px, rgba(167,139,250,0.8), transparent),
      radial-gradient(1.5px 1.5px at 980px 140px, rgba(217,70,239,0.7), transparent),
      radial-gradient(2px 2px at 1350px 70px, rgba(255,255,255,0.8), transparent),
      radial-gradient(1.5px 1.5px at 1750px 160px, rgba(251,191,36,0.6), transparent),
      radial-gradient(2px 2px at 800px 520px, rgba(139,92,246,0.7), transparent);
    pointer-events: none;
  }

  /* Content Container */
  .container {
    width: 100%;
    max-width: 1800px;
    margin: 0 auto;
    padding: 0 90px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    z-index: 10;
  }

  /* Left Side: Brand & Hero Copy */
  .hero-left {
    max-width: 960px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .top-pill {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 7px 18px;
    border-radius: 99px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(196, 181, 253, 0.25);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 3.5px;
    color: #c4b5fd;
    text-transform: uppercase;
    backdrop-filter: blur(12px);
    margin-bottom: 22px;
  }
  .top-pill i {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #34d399;
    box-shadow: 0 0 10px #34d399;
  }

  .banner-h1 {
    font-size: 64px;
    font-weight: 900;
    line-height: 1.06;
    letter-spacing: -2px;
    margin-bottom: 18px;
    text-transform: uppercase;
  }

  .banner-h1 .grad {
    background: linear-gradient(100deg, #a78bfa 0%, #d946ef 55%, #fbbf24 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    display: inline-block;
  }

  .hero-sub {
    font-size: 18px;
    font-weight: 500;
    color: #cbd5e1;
    line-height: 1.5;
    margin-bottom: 26px;
    max-width: 820px;
  }

  /* Service Tags */
  .service-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 34px;
  }

  .tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    border-radius: 99px;
    background: rgba(255, 255, 255, 0.045);
    border: 1px solid rgba(196, 181, 253, 0.18);
    font-size: 13.5px;
    font-weight: 600;
    color: #f1f5f9;
    backdrop-filter: blur(10px);
  }
  .tag span {
    color: #d946ef;
    font-size: 14px;
  }

  /* Contact Footer Bar */
  .contact-bar {
    display: flex;
    align-items: center;
    gap: 28px;
    padding-top: 18px;
    border-top: 1px solid rgba(196, 181, 253, 0.15);
  }

  .contact-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14.5px;
    font-weight: 600;
    color: #e2e8f0;
  }
  .contact-item i {
    color: #a78bfa;
    font-style: normal;
    font-size: 16px;
  }
  .contact-item .highlight {
    color: #fbbf24;
  }

  /* Right Side: Visual Showcase */
  .hero-right {
    position: relative;
    width: 620px;
    height: 520px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Ambient Halo behind badge */
  .badge-halo {
    position: absolute;
    width: 480px;
    height: 480px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(139, 92, 246, 0.35) 0%, rgba(217, 70, 239, 0.15) 50%, transparent 70%);
    filter: blur(40px);
  }

  /* 3D Glassmorphism Showcase Card */
  .showcase-card {
    position: relative;
    width: 520px;
    border-radius: 32px;
    background: rgba(14, 10, 40, 0.65);
    border: 1px solid rgba(196, 181, 253, 0.22);
    backdrop-filter: blur(24px) saturate(1.4);
    box-shadow: 
      0 30px 80px -15px rgba(0, 0, 0, 0.8),
      0 0 60px -10px rgba(139, 92, 246, 0.35),
      inset 0 1px 2px rgba(255, 255, 255, 0.35);
    padding: 32px 36px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  /* Top Card Header with Logo */
  .card-header {
    display: flex;
    align-items: center;
    gap: 18px;
    padding-bottom: 18px;
    border-bottom: 1px solid rgba(196, 181, 253, 0.14);
  }

  .card-logo-badge {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #7c3aed 0%, #4c1d95 60%, #1e0845 100%);
    border: 1.5px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 24px rgba(124, 58, 237, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  .card-logo-badge svg {
    width: 38px;
    height: 38px;
  }

  .card-header-text h3 {
    font-size: 20px;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
  }
  .card-header-text h3 span {
    background: linear-gradient(100deg, #c4b5fd, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  .card-header-text p {
    font-size: 12px;
    color: #a7a2cf;
    letter-spacing: 3px;
    text-transform: uppercase;
    font-weight: 600;
    margin-top: 3px;
  }

  /* Mini Metric Cards */
  .metrics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }

  .metric-box {
    background: rgba(255, 255, 255, 0.035);
    border: 1px solid rgba(196, 181, 253, 0.12);
    border-radius: 18px;
    padding: 16px 18px;
  }
  .metric-val {
    font-size: 24px;
    font-weight: 800;
    color: #ffffff;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .metric-val.green { color: #34d399; }
  .metric-val.purple { color: #c084fc; }
  .metric-label {
    font-size: 11.5px;
    font-weight: 600;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
  }

  /* Floating Status Pill */
  .status-pill {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: rgba(139, 92, 246, 0.12);
    border: 1px solid rgba(167, 139, 250, 0.28);
    border-radius: 14px;
    padding: 12px 18px;
    font-size: 13px;
    font-weight: 600;
  }
  .status-pill-left {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #e2e8f0;
  }
  .status-pill-left i {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #34d399;
    box-shadow: 0 0 10px #34d399;
  }
  .status-pill-right {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: #fbbf24;
    background: rgba(251, 191, 36, 0.12);
    padding: 3px 10px;
    border-radius: 6px;
  }
</style>
</head>
<body>
  <div class="glow-left"></div>
  <div class="glow-right"></div>
  <div class="glow-bottom"></div>
  <div class="grid-bg"></div>
  <div class="stars"></div>

  <div class="container">
    <!-- Left Hero -->
    <div class="hero-left">
      <div class="top-pill">
        <i></i> Digital Innovation & Software Studio
      </div>
      
      <h1 class="banner-h1">
        We Build Your<br>
        <span class="grad">Vision Into Reality</span>
      </h1>

      <p class="hero-sub">
        High-impact Web Platforms, Native iOS & Android Apps, Custom SaaS Architecture, and Intelligent AI Automation Systems.
      </p>

      <div class="service-tags">
        <div class="tag"><span>✦</span> Web Applications</div>
        <div class="tag"><span>✦</span> Mobile Apps</div>
        <div class="tag"><span>✦</span> AI & Automation</div>
        <div class="tag"><span>✦</span> Custom SaaS</div>
        <div class="tag"><span>✦</span> UI/UX Design</div>
      </div>

      <div class="contact-bar">
        <div class="contact-item">
          <i>📞</i> 08135971304
        </div>
        <div class="contact-item">
          <i>🌐</i> www.insightnovatech.com
        </div>
        <div class="contact-item">
          <span class="highlight">✦</span> Ready to Launch? Let's Talk!
        </div>
      </div>
    </div>

    <!-- Right Showcase Card -->
    <div class="hero-right">
      <div class="badge-halo"></div>
      
      <div class="showcase-card">
        <div class="card-header">
          <div class="card-logo-badge">
            <svg viewBox="0 0 100 100">
              <circle cx="24" cy="20" r="8" fill="white"/>
              <path d="M24 38V62a14 14 0 0 0 28 0V38l24 30V30" fill="none" stroke="white" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </div>
          <div class="card-header-text">
            <h3>INSIGHT<span>NOVATECH</span></h3>
            <p>Ideas · Code · Impact</p>
          </div>
        </div>

        <div class="metrics-grid">
          <div class="metric-box">
            <div class="metric-val green">100%</div>
            <div class="metric-label">Custom Architecture</div>
          </div>
          <div class="metric-box">
            <div class="metric-val purple">99.9%</div>
            <div class="metric-label">Reliability & Uptime</div>
          </div>
        </div>

        <div class="status-pill">
          <div class="status-pill-left">
            <i></i> Next-Gen Tech Stack
          </div>
          <div class="status-pill-right">PRODUCTION READY</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>'''

# Write Banner HTML
with open(os.path.join(base_dir, 'render_banner_wide.html'), 'w', encoding='utf-8') as f:
    f.write(banner_wide_html)

# Render Banner to PNG (1920 x 640)
subprocess.run([
    chrome_path, '--headless', '--disable-gpu',
    f'--screenshot={os.path.join(base_dir, "banner_social_wide.png")}',
    '--window-size=1920,640', '--default-background-color=00000000',
    f'file:///{base_dir.replace("\\\\", "/")}/render_banner_wide.html'
], check=True)

print("Social Media Wide Banner rendered successfully!")
