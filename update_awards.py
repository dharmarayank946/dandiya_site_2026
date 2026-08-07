import re

filename = 'best-dandiya-events-pune-2026.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hero and content
content = re.sub(r'<section class="subpage-hero">.*?</section>', 
'''<section class="subpage-hero">
                <span class="hero-badge">🏆 Awards & Recognition</span>
                <h1>Awards & Recognition 2026</h1>
                <p>Join us in celebrating the true spirit of Navratri at Dandiya Connect Pune 2026! We will be honoring the most enthusiastic participants across various categories with special awards and recognition.</p>
            </section>''', content, flags=re.DOTALL)

content = re.sub(r'Top 10 Dandiya Night Rankings Pune 2026', 'Dandiya Connect Pune 2026 Awards', content)
content = re.sub(r'PUNE #1 DANDIYA RANKING POSTER', 'AWARDS & RECOGNITION POSTER', content)
content = re.sub(r'Best Dandiya Events Pune 2026 Ranking Poster', 'Awards Poster', content)

awards_content = '''<div style="margin-top:40px;">
                <h2 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); text-align:center; margin-bottom: 30px;">Award Categories</h2>
                
                <div class="ranking-card reveal">
                    <div class="ranking-num"><i class="fa-solid fa-trophy" style="font-size: 1.5rem;"></i></div>
                    <div>
                        <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); margin:0 0 10px;">Best Dressed Female</h3>
                        <p style="color:var(--text-muted); margin:0;">Awarded to the most elegant and authentically dressed female participant.</p>
                    </div>
                </div>

                <div class="ranking-card reveal reveal-d1">
                    <div class="ranking-num"><i class="fa-solid fa-trophy" style="font-size: 1.5rem;"></i></div>
                    <div>
                        <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); margin:0 0 10px;">Best Dressed Male</h3>
                        <p style="color:var(--text-muted); margin:0;">Celebrating the best traditional attire among male attendees.</p>
                    </div>
                </div>

                <div class="ranking-card reveal reveal-d2">
                    <div class="ranking-num"><i class="fa-solid fa-trophy" style="font-size: 1.5rem;"></i></div>
                    <div>
                        <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); margin:0 0 10px;">Best Couple</h3>
                        <p style="color:var(--text-muted); margin:0;">Recognizing the most coordinated and graceful couple on the dance floor.</p>
                    </div>
                </div>

                <div class="ranking-card reveal reveal-d3">
                    <div class="ranking-num"><i class="fa-solid fa-trophy" style="font-size: 1.5rem;"></i></div>
                    <div>
                        <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); margin:0 0 10px;">Best Family</h3>
                        <p style="color:var(--text-muted); margin:0;">Awarded to the family that embodies the festive spirit together.</p>
                    </div>
                </div>

                <div class="ranking-card reveal">
                    <div class="ranking-num"><i class="fa-solid fa-trophy" style="font-size: 1.5rem;"></i></div>
                    <div>
                        <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); margin:0 0 10px;">Best Garba Performer</h3>
                        <p style="color:var(--text-muted); margin:0;">Honoring outstanding Garba dance skills and energy.</p>
                    </div>
                </div>

                <div class="ranking-card reveal">
                    <div class="ranking-num"><i class="fa-solid fa-trophy" style="font-size: 1.5rem;"></i></div>
                    <div>
                        <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); margin:0 0 10px;">Best Dandiya Performer</h3>
                        <p style="color:var(--text-muted); margin:0;">Recognizing exceptional rhythm and style in Dandiya Raas.</p>
                    </div>
                </div>

                <div class="ranking-card reveal">
                    <div class="ranking-num"><i class="fa-solid fa-award" style="font-size: 1.5rem;"></i></div>
                    <div>
                        <h3 style="font-family:'Playfair Display', serif; color:var(--festive-crimson); margin:0 0 10px;">Special Recognition Awards</h3>
                        <p style="color:var(--text-muted); margin:0;">Surprise categories and special mentions throughout the exclusive evening.</p>
                    </div>
                </div>
            </div>'''

# Replace the ranking cards and comp table
content = re.sub(r'<div class="ranking-card reveal.*?</table>\s*</div>\s*</div>', awards_content, content, flags=re.DOTALL)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated awards page")