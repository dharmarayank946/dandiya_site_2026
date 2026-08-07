import re

filename = 'food-stalls-vendors.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hero and content
content = re.sub(r'<section class="subpage-hero">.*?</section>', 
'''<section class="subpage-hero">
                <span class="hero-badge">🍽️ Premium Dining Experience</span>
                <h1>Pure Vegetarian Premium Dinner</h1>
                <p>Enjoy a lavish festive menu specially curated for our high-end Garba & Dandiya night. Dinner is included in all passes, ensuring a seamless and premium experience for all our curated elite audience.</p>
            </section>''', content, flags=re.DOTALL)

content = re.sub(r'<div class="subpage-poster-wrapper.*?</div>\s*</div>', 
'''<div class="subpage-poster-wrapper reveal">
                <img src="images/food_vendors_poster.png" alt="Premium Vegetarian Dinner at Dandiya Connect Pune" class="subpage-poster-img">
                <div class="subpage-poster-overlay">
                    <h3 class="subpage-poster-title">🍽️ Lavish Festive Menu</h3>
                    <p class="subpage-poster-subtitle">Specially curated for a high-end Garba & Dandiya experience.</p>
                </div>
            </div>''', content, flags=re.DOTALL, count=1)

menu_content = '''<div class="dandiya-card reveal" style="margin-top: 40px;">
                <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); text-align:center; margin-bottom: 25px;">Sample Menu Sections</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-martini-glass-citrus"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Welcome Drinks</h6></div>
                    </div>
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-bowl-food"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Chaat Counter</h6></div>
                    </div>
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-utensils"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Live Snacks Counter</h6></div>
                    </div>
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-plate-wheat"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Gujarati Specialties</h6></div>
                    </div>
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-bowl-rice"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Punjabi Main Course</h6></div>
                    </div>
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-bread-slice"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Indian Breads</h6></div>
                    </div>
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-seedling"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Rice Preparations & Salads</h6></div>
                    </div>
                    <div class="feature-item highlight-item">
                        <div class="pill-icon"><i class="fa-solid fa-ice-cream"></i></div>
                        <div><h6 class="mb-0 fw-bold highlight-title">Desserts & Live Ice Cream</h6></div>
                    </div>
                </div>
            </div>'''

# Replace whatever is below the poster up to the footer
content = re.sub(r'<!-- Vendor Perks & Amenities -->.*?(?=<!-- Master Footer -->|<!-- Cross-Link)', menu_content + r'\n\n            <!-- Cross-Link', content, flags=re.DOTALL)

# Let's just fix it by locating the end
with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated dining page")