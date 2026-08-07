import re

filename = 'corporate-bookings.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<section class="subpage-hero">.*?</section>', 
'''<section class="subpage-hero">
                <span class="hero-badge">🎟️ Exclusive Access</span>
                <h1>Invite Only Participation</h1>
                <p>Experience Pune's most premium Navratri celebration. A curated business & social community event for select entrepreneurs, professionals, families & distinguished guests.</p>
            </section>''', content, flags=re.DOTALL)

content = re.sub(r'Corporate Dandiya Night Pune 2026', 'Invite-Only Dandiya Night Pune 2026', content)
content = re.sub(r'Corporate Outing & Team VIP Lounges', 'Exclusive Networking & VIP Lounges', content)
content = re.sub(r'Employee Appreciation & Rewards', 'Curated Networking & Celebration', content)
content = re.sub(r'Tailored employee pass packages.*?Magarpatta.', 'Exclusive networking opportunities for the elite community of Pune.', content)
content = re.sub(r'Corporate & IT Bulk Bookings', 'Exclusive Guest Access', content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated invite-only page")