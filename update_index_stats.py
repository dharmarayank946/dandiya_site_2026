import re

filename = 'index.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="stat-number">50\+</div>\s*<div class="stat-label">Premium Dining</div>', 
'''<div class="stat-number">Lavish</div>
                                    <div class="stat-label">Festive Menu</div>''', content)

content = re.sub(r'<div class="stat-number">Select Invite-Only</div>\s*<div class="stat-label">Daily Dancers</div>',
'''<div class="stat-number">Exclusive</div>
                                    <div class="stat-label">Invite-Only Attendees</div>''', content)

content = re.sub(r'Non-Stop Garba', 'Premium Garba', content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index stats")