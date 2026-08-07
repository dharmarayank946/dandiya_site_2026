import re

filename = 'tickets.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Pricing Grid properly
new_pricing_grid = '''<div class="pricing-grid">
                <!-- Solo Pass -->
                <div class="pricing-card reveal">
                    <h3 class="price-title">Solo Pass</h3>
                    <div class="price-val">₹1,999 <span>/ person</span></div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-circle-check"></i> Single Entry Pass</li>
                        <li><i class="fa-solid fa-circle-check"></i> Pure Vegetarian Premium Dinner Included</li>
                    </ul>
                    <a href="#bookSection" class="btn-festive" onclick="setPassType('Solo Pass (₹1,999)', 1999)">Select Solo Pass</a>
                </div>

                <!-- Couple Pass (Featured) -->
                <div class="pricing-card featured reveal reveal-d1">
                    <span class="popular-badge">COUPLES CHOICE</span>
                    <h3 class="price-title">Couple Pass</h3>
                    <div class="price-val">₹3,499 <span>/ couple</span></div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-circle-check"></i> Entry for 2 (Couple)</li>
                        <li><i class="fa-solid fa-circle-check"></i> Pure Vegetarian Premium Dinner Included</li>
                        <li><i class="fa-solid fa-circle-check"></i> Express Entry Lane</li>
                    </ul>
                    <a href="#bookSection" class="btn-festive" onclick="setPassType('Couple Pass (₹3,499)', 3499)">Select Couple Pass</a>
                </div>

                <!-- Family Pass -->
                <div class="pricing-card reveal reveal-d2">
                    <h3 class="price-title">Family Pass</h3>
                    <div class="price-val">₹1,999 <span>/ adult</span></div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-circle-check"></i> ₹999 per Child</li>
                        <li><i class="fa-solid fa-circle-check"></i> Pure Vegetarian Premium Dinner Included</li>
                        <li><i class="fa-solid fa-circle-check"></i> Dedicated Family Seating Area</li>
                    </ul>
                    <a href="#bookSection" class="btn-festive" onclick="setPassType('Family Pass', 1999)">Select Family Pass</a>
                </div>

                <!-- Group Booking -->
                <div class="pricing-card vip reveal reveal-d3">
                    <h3 class="price-title">Group Booking</h3>
                    <div class="price-val">₹1,799 <span>/ adult</span></div>
                    <ul class="price-features">
                        <li><i class="fa-solid fa-star"></i> Applicable for 5 or more adults</li>
                        <li><i class="fa-solid fa-star"></i> Pure Vegetarian Premium Dinner Included</li>
                        <li><i class="fa-solid fa-star"></i> Reserved Group Table</li>
                    </ul>
                    <a href="#bookSection" class="btn-festive" style="background: linear-gradient(135deg, var(--festive-gold), var(--festive-gold-dark));" onclick="setPassType('Group Booking (₹1,799/adult)', 1799)">Select Group Pass</a>
                </div>
            </div>'''

content = re.sub(r'<div class="pricing-grid">.*?</div>\s*<!-- What\'s Included Section -->', new_pricing_grid + r'\n\n            <!-- What\'s Included Section -->', content, flags=re.DOTALL)

# Replace Dropdown options
new_dropdown = '''<div class="custom-select-options">
                                <div class="custom-option" data-value="Solo Pass (₹1,999)" data-price="1999">Solo Pass (₹1,999)</div>
                                <div class="custom-option" data-value="Couple Pass (₹3,499)" data-price="3499">Couple Pass (₹3,499)</div>
                                <div class="custom-option" data-value="Family Pass (Adults & Children)" data-price="1999">Family Pass (Details later)</div>
                                <div class="custom-option" data-value="Group Booking (₹1,799/adult)" data-price="1799">Group Booking (5+ Adults)</div>
                            </div>'''

content = re.sub(r'<div class="custom-select-options">.*?</div>\s*</div>', new_dropdown + r'\n                        </div>', content, flags=re.DOTALL)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)

print('tickets.html updated correctly')