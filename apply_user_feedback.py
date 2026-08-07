import re

def update_sponsorship():
    with open('sponsorship.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_tier_grid = '''<div class="tier-grid">
                
                <!-- Title Sponsor -->
                <div class="tier-card featured reveal">
                    <span class="badge-festive" style="align-self: flex-start; margin-bottom: 12px; font-size: 0.75rem;">PRIME EXCLUSIVITY</span>
                    <h3 class="tier-title">Title Sponsor</h3>
                    <p class="tier-tagline">Complete event co-branding as "[Brand Name] Dandiya Connect Pune 2026".</p>
                    <ul class="tier-features">
                        <li><i class="fa-solid fa-star"></i> Title Branding on Main Gate Arch & Tickets</li>
                        <li><i class="fa-solid fa-star"></i> Main Stage Branding & Continuous LED Loop</li>
                        <li><i class="fa-solid fa-star"></i> Prime Experiential Booth Slot (20x20 ft)</li>
                        <li><i class="fa-solid fa-star"></i> 50 VIP Passes + VIP Lounge Access</li>
                        <li><i class="fa-solid fa-star"></i> Dedicated Social Media Reels & PR Release</li>
                    </ul>
                    <a href="#sponsorInquiry" class="btn-festive" onclick="selectTier('Title Sponsor')">Inquire Title Tier</a>
                </div>

                <!-- Co-Sponsors -->
                <div class="tier-card reveal reveal-d1">
                    <h3 class="tier-title">Co-Sponsors</h3>
                    <p class="tier-tagline">High impact brand presence on stage & digital campaigns.</p>
                    <ul class="tier-features">
                        <li><i class="fa-solid fa-check"></i> "Co-Sponsor" logo credit on main entrance arch</li>
                        <li><i class="fa-solid fa-check"></i> Secondary LED Screen video loops</li>
                        <li><i class="fa-solid fa-check"></i> Brand Stall Space (10x10 ft)</li>
                        <li><i class="fa-solid fa-check"></i> 25 VIP Passes for clients/executives</li>
                        <li><i class="fa-solid fa-check"></i> Dedicated Instagram Story & Carousel</li>
                    </ul>
                    <a href="#sponsorInquiry" class="btn-festive" onclick="selectTier('Co-Sponsors')">Inquire Co-Sponsor Tier</a>
                </div>

                <!-- Associate Sponsors -->
                <div class="tier-card reveal reveal-d2">
                    <h3 class="tier-title">Associate Sponsors</h3>
                    <p class="tier-tagline">Exclusive rights for Food, Banking, Telecom, or Fashion categories.</p>
                    <ul class="tier-features">
                        <li><i class="fa-solid fa-check"></i> Category Rights (e.g. Official Food / Bank Partner)</li>
                        <li><i class="fa-solid fa-check"></i> Banner placement around premium dinner / arena</li>
                        <li><i class="fa-solid fa-check"></i> Promotional product sampling rights</li>
                        <li><i class="fa-solid fa-check"></i> 10 VIP Passes</li>
                        <li><i class="fa-solid fa-check"></i> Logo feature on official website & ticket emails</li>
                    </ul>
                    <a href="#sponsorInquiry" class="btn-festive" onclick="selectTier('Associate Sponsors')">Inquire Associate Tier</a>
                </div>
                
                <!-- Branding Partners -->
                <div class="tier-card reveal reveal-d3">
                    <h3 class="tier-title">Branding Partners</h3>
                    <p class="tier-tagline">Brand visibility across the venue and digital platforms.</p>
                    <ul class="tier-features">
                        <li><i class="fa-solid fa-check"></i> Standee and Banner Displays at venue</li>
                        <li><i class="fa-solid fa-check"></i> Logo on Partner Wall</li>
                        <li><i class="fa-solid fa-check"></i> Digital mentions on social media</li>
                        <li><i class="fa-solid fa-check"></i> 5 VIP Passes</li>
                        <li><i class="fa-solid fa-check"></i> Networking opportunities with other sponsors</li>
                    </ul>
                    <a href="#sponsorInquiry" class="btn-festive" onclick="selectTier('Branding Partners')">Inquire Branding Tier</a>
                </div>

            </div>'''
    
    html = re.sub(r'<div class="tier-grid">.*?</div>\s*<!-- Deliverables Comparison Matrix Table -->', 
                  new_tier_grid + '\n\n            <!-- Deliverables Comparison Matrix Table -->', html, flags=re.DOTALL)
    
    new_matrix = '''<div class="matrix-table-wrap">
                    <table class="matrix-table">
                        <thead>
                            <tr>
                                <th>Deliverables & Privileges</th>
                                <th>Title Sponsor</th>
                                <th>Co-Sponsors</th>
                                <th>Associate Sponsors</th>
                                <th>Branding Partners</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Co-Branded Event Title Name</strong></td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> Yes (Exclusive)</td>
                                <td><span class="dash-icon">—</span></td>
                                <td><span class="dash-icon">—</span></td>
                                <td><span class="dash-icon">—</span></td>
                            </tr>
                            <tr>
                                <td><strong>Main Entrance Arch Logo</strong></td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> Prime Top Center</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> Co-Sponsor Position</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> Banner Standee</td>
                                <td><span class="dash-icon">—</span></td>
                            </tr>
                            <tr>
                                <td><strong>Stage LED Video Ads (Every Hour)</strong></td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 60 Secs Loop</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 30 Secs Loop</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 15 Secs Loop</td>
                                <td><span class="dash-icon">—</span></td>
                            </tr>
                            <tr>
                                <td><strong>Brand Experience Stall Area</strong></td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 20 x 20 ft</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 10 x 10 ft</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 6 x 6 ft</td>
                                <td><span class="dash-icon">—</span></td>
                            </tr>
                            <tr>
                                <td><strong>VIP Passes & Lounge Access</strong></td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 50 VIP Passes</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 25 VIP Passes</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 10 VIP Passes</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 5 VIP Passes</td>
                            </tr>
                            <tr>
                                <td><strong>Dedicated Instagram Reel & Post</strong></td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 3 Dedicated Reels</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> 1 Dedicated Reel</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> Group Post Tag</td>
                                <td><i class="fa-solid fa-circle-check check-icon"></i> Group Post Tag</td>
                            </tr>
                        </tbody>
                    </table>
                </div>'''

    html = re.sub(r'<div class="matrix-table-wrap">.*?</div>', new_matrix, html, flags=re.DOTALL)
    
    new_options = '''<div class="custom-select-options">
                                <div class="custom-option" data-value="Title Sponsor">Title Sponsor</div>
                                <div class="custom-option" data-value="Co-Sponsors">Co-Sponsors</div>
                                <div class="custom-option" data-value="Associate Sponsors">Associate Sponsors</div>
                                <div class="custom-option" data-value="Branding Partners">Branding Partners</div>
                            </div>'''
    html = re.sub(r'<div class="custom-select-options">.*?</div>', new_options, html, flags=re.DOTALL)
    
    with open('sponsorship.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated sponsorship.html")

def update_navratri():
    with open('navratri-events-pune.html', 'r', encoding='utf-8') as f:
        html = f.read()

    awards_content = '''<div class="guide-section reveal">
                <h2 style="font-family: 'Playfair Display', serif; color: var(--festive-crimson); margin-top: 0; margin-bottom: 30px;">Awards & Recognition</h2>
                
                <div class="guide-grid" style="grid-template-columns: repeat(2, 1fr);">
                    <div class="guide-card">
                        <div class="pill-icon" style="background: linear-gradient(135deg, var(--festive-red), var(--festive-crimson)); color: white; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 50%;"><i class="fa-solid fa-trophy"></i></div>
                        <h4>Best Dressed Female</h4>
                        <p style="color: var(--text-muted); font-size: 0.9rem;">Awarded to the most elegant and authentically dressed female participant.</p>
                    </div>

                    <div class="guide-card">
                        <div class="pill-icon" style="background: linear-gradient(135deg, var(--festive-red), var(--festive-crimson)); color: white; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 50%;"><i class="fa-solid fa-trophy"></i></div>
                        <h4>Best Dressed Male</h4>
                        <p style="color: var(--text-muted); font-size: 0.9rem;">Celebrating the best traditional attire among male attendees.</p>
                    </div>

                    <div class="guide-card">
                        <div class="pill-icon" style="background: linear-gradient(135deg, var(--festive-red), var(--festive-crimson)); color: white; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 50%;"><i class="fa-solid fa-trophy"></i></div>
                        <h4>Best Couple</h4>
                        <p style="color: var(--text-muted); font-size: 0.9rem;">Recognizing the most coordinated and graceful couple on the dance floor.</p>
                    </div>

                    <div class="guide-card">
                        <div class="pill-icon" style="background: linear-gradient(135deg, var(--festive-red), var(--festive-crimson)); color: white; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; border-radius: 50%;"><i class="fa-solid fa-trophy"></i></div>
                        <h4>Best Family</h4>
                        <p style="color: var(--text-muted); font-size: 0.9rem;">Awarded to the family that embodies the festive spirit together.</p>
                    </div>
                </div>
            </div>'''
    
    html = re.sub(r'(<!-- FAQs Accordion Section -->)', awards_content + r'\n\n            \1', html)
    
    with open('navratri-events-pune.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated navratri-events-pune.html")

update_sponsorship()
update_navratri()
