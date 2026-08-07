import os
import re

directory = '.'

replacements = [
    (r'Dandiya Connect 2026(\s*-\s*Pune)?', r'Dandiya Connect Pune 2026'),
    (r'Pune Navratri & Dandiya Portal 2026', r'Dandiya Connect Pune 2026 Portal'),
    (r'Navratri & Dandiya Festival 2026[^a-zA-Z0-9]*Pune', r'Dandiya Connect Pune 2026'),
    (r'Pune Navratri & Dandiya Festival', r'Dandiya Connect Pune 2026'),
    (r'9-night Garba celebration', r'premium one-day Garba celebration'),
    (r'9 Nights Non-Stop Garba', r'1 Night Exclusive Garba'),
    (r'9 Nights', r'1 Night'),
    (r'Oct 1[^a-zA-Z0-9]*Oct 9 \(9 Nights\)', r'15 October 2026'),
    (r'Oct 1[^a-zA-Z0-9]*Oct 9', r'15 October 2026'),
    (r'October 1[^a-zA-Z0-9]*October 9', r'15 October 2026'),
    (r'Navratri 2026', r'15 October 2026'),
    (r'9 magical nights', r'an exclusive magical night'),
    (r'10,000\+\s*Daily Dancers', r'Exclusive Audience'),
    (r'10,000\+\s*Audience', r'Exclusive Audience'),
    (r'10,000\+\s*expected audience', r'curated elite audience'),
    (r'10,000\+', r'Select Invite-Only'),
    (r'mass audience gathering', r'curated elite audience gathering'),
    (r'Large public festival', r'Premium, exclusive, invite-only experience'),
    (r'Premium Arena, Pune', r'Minimum 4-Star Property Banquet Hall, Pune'),
    (r'Large Ground', r'Large Premium Banquet Hall'),
    (r'50\+\s*Food Stalls', r'Premium Dinner Included'),
    (r'Food Stalls', r'Premium Dining'),
    (r'Food stalls', r'Premium dining'),
    (r'food stalls', r'premium dinner'),
    (r'Food Court', r'Premium Dining'),
    (r'food court', r'premium dining'),
    (r'Delicious Premium Dining', r'Premium Vegetarian Dinner Included'),
    (r'gourmet premium dining', r'lavish pure vegetarian dinner'),
    (r'Corporate Groups', r'Invite-Only Participation'),
    (r'Corporate Bookings', r'Invite-Only Participation'),
    (r'corporate groups', r'invite-only guests'),
    (r'Corporate Passes', r'Invite-Only Passes'),
    (r'Corporate Packages', r'Invite-Only Packages'),
    (r'Corporate Dandiya Night Pune', r'Invite-Only Dandiya Night Pune'),
    (r'>Corporate<', r'>Invite-Only<'),
    (r'>Corporate', r'>Invite-Only'),
    (r'RANKINGS 2026', r'AWARDS 2026'),
    (r'Top Events Ranking', r'Awards & Recognition'),
    (r'Best Events Ranking', r'Awards & Recognition'),
]

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        for old, new in replacements:
            content = re.sub(old, new, content)
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)

print("Done basic string replacements.")
