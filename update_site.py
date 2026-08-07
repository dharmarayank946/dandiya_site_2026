import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

def replace_in_file(filename, old_str, new_str, regex=False):
    if not os.path.exists(filename): return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if regex:
        content = re.sub(old_str, new_str, content)
    else:
        content = content.replace(old_str, new_str)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Global Replacements
for f in html_files:
    # Navigation Links
    replace_in_file(f, '>Food Stalls<', '>Premium Dining<')
    replace_in_file(f, '>Corporate<', '>Invite-Only<')
    replace_in_file(f, '>Guide<', '>Awards<')
    replace_in_file(f, 'food-court', 'premium-dining')
    
    # 1. Event Name
    replace_in_file(f, 'Dandiya Connect Pune 2026 - Pune', 'Dandiya Connect Pune 2026')
    replace_in_file(f, 'Dandiya Connect 2026', 'Dandiya Connect Pune 2026')
    
    # 2. Date & Audience
    replace_in_file(f, r'10,000\+ expected audience', 'curated elite audience comprising entrepreneurs, business owners, professionals, community leaders, and select invitees', True)
    replace_in_file(f, r'10,000\+', 'Select', True)
    replace_in_file(f, 'mass audience gathering', 'curated elite audience')
    replace_in_file(f, 'Large public festival', 'Premium, Exclusive, Invite-Only Event')
    replace_in_file(f, 'Large Ground', 'Large Premium Banquet Hall')
    replace_in_file(f, 'Premium Arena, Pune', 'Minimum 4-Star Property Banquet Hall, Pune')
    replace_in_file(f, 'Food court/fair style event', 'Elegant fine dining included')
    replace_in_file(f, 'food court/fair style event', 'elegant fine dining included')
    replace_in_file(f, 'Food stalls', 'Premium dining')
    replace_in_file(f, 'food stalls', 'premium dinner')
    replace_in_file(f, 'Food Court', 'Premium Dinner')
    replace_in_file(f, 'food court', 'premium dinner')
    
    # 5. Audience
    replace_in_file(f, 'Corporate Groups', 'Invite Only Participation')
    replace_in_file(f, 'Corporate Bookings', 'Invite Only Participation')
    replace_in_file(f, 'Corporate Passes', 'Invite-Only Passes')
    replace_in_file(f, 'corporate groups', 'curated business & social community')
    
    # 6. Awards
    replace_in_file(f, 'RANKINGS 2026', 'AWARDS 2026')
    replace_in_file(f, 'Best Events Ranking', 'Awards & Recognition')
    replace_in_file(f, 'Top Events Ranking', 'Awards & Recognition')
    
    # Update some specific headings
    replace_in_file(f, 'Official Navratri Event & Passes', 'Premium Navratri Event & Passes')

print('Global replacements done.')