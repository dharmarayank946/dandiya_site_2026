import re

filename = 'sponsorship.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Sponsorship Grid
new_sponsor_grid = '''<div class="pricing-grid" style="margin-bottom: 40px;">
                <!-- Title Sponsor -->
                <div class="pricing-card vip reveal">
                    <h3 class="price-title">Title Sponsor</h3>
                    <div class="price-val">₹11,00,000</div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-star"></i> 1 Exclusive Slot</li>
                        <li><i class="fa-solid fa-circle-check"></i> Highest Brand Visibility</li>
                        <li><i class="fa-solid fa-circle-check"></i> Main Stage Branding</li>
                        <li><i class="fa-solid fa-circle-check"></i> Premium VIP Lounge Access</li>
                    </ul>
                    <a href="#sponsorFormSection" class="btn-festive" style="background: linear-gradient(135deg, var(--festive-gold), var(--festive-gold-dark));">Inquire Now</a>
                </div>

                <!-- Co-Sponsor -->
                <div class="pricing-card featured reveal reveal-d1">
                    <span class="popular-badge">PREMIUM ROI</span>
                    <h3 class="price-title">Co-Sponsor</h3>
                    <div class="price-val">₹6,00,000</div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-star"></i> 3 Slots Available</li>
                        <li><i class="fa-solid fa-circle-check"></i> Extensive Ground Branding</li>
                        <li><i class="fa-solid fa-circle-check"></i> Digital Campaign Inclusion</li>
                        <li><i class="fa-solid fa-circle-check"></i> VIP Hospitality Passes</li>
                    </ul>
                    <a href="#sponsorFormSection" class="btn-festive">Inquire Now</a>
                </div>

                <!-- Associate Sponsor -->
                <div class="pricing-card reveal reveal-d2">
                    <h3 class="price-title">Associate Sponsor</h3>
                    <div class="price-val">₹3,00,000</div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-star"></i> 5 Slots Available</li>
                        <li><i class="fa-solid fa-circle-check"></i> Strategic Brand Placement</li>
                        <li><i class="fa-solid fa-circle-check"></i> Experiential Kiosk Space</li>
                    </ul>
                    <a href="#sponsorFormSection" class="btn-festive">Inquire Now</a>
                </div>

                <!-- Branding Partner -->
                <div class="pricing-card reveal reveal-d3">
                    <h3 class="price-title">Branding Partner</h3>
                    <div class="price-val">₹50,000</div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-star"></i> 10 Slots Available</li>
                        <li><i class="fa-solid fa-circle-check"></i> Banner Displays</li>
                        <li><i class="fa-solid fa-circle-check"></i> Logo on Partner Wall</li>
                    </ul>
                    <a href="#sponsorFormSection" class="btn-festive">Inquire Now</a>
                </div>
            </div>
            
            <div class="dandiya-card reveal" style="text-align:center; padding: 20px; background: linear-gradient(135deg, rgba(223,178,59,0.1), rgba(156,21,56,0.05)); margin-bottom:40px;">
                <h4 style="color:var(--festive-crimson); margin-bottom:10px;"><i class="fa-solid fa-handshake"></i> Partnership Opportunities</h4>
                <p style="color:var(--text-muted); font-size:1.05rem;">Barter collaborations available! We are open to exploring mutual value-exchange partnerships. Details to be discussed on a case-by-case basis.</p>
            </div>'''

# We will just replace everything between <h3 style="font-family:'Playfair Display'... ">Sponsorship Tiers... and the start of the form section.
content = re.sub(r'<div class="pricing-grid">.*?</div>', new_sponsor_grid, content, count=1, flags=re.DOTALL)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print('sponsorship.html updated')