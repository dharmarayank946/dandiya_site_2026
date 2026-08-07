import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Event name & dates
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update event name across all pages
    content = re.sub(r'Dandiya Connect 2026', 'Dandiya Connect Pune 2026', content)
    content = re.sub(r'Pune Navratri & Dandiya Portal 2026', 'Dandiya Connect Pune 2026', content)
    content = re.sub(r'Navratri & Dandiya Festival 2026 – Pune', 'Dandiya Connect Pune 2026', content)
    content = re.sub(r'Pune Navratri & Dandiya Festival', 'Dandiya Connect Pune 2026', content)
    
    # 2. Update event date to 15 October 2026
    content = re.sub(r'9-night Garba celebration', 'One-day exclusive Garba celebration', content)
    content = re.sub(r'9 Nights Non-Stop Garba', '1 Night Exclusive Garba', content)
    content = re.sub(r'9 Nights', '1 Night', content)
    content = re.sub(r'Oct 1 – Oct 9', '15 October 2026', content)
    content = re.sub(r'October 1 - October 9', '15 October 2026', content)
    content = re.sub(r'Navratri 2026', '15 October 2026', content)
    content = re.sub(r'9 magical nights', 'an exclusive magical night', content)
    
    # 3 & 4. Positioning and audience
    content = re.sub(r'10,000\+\s*Daily Dancers', 'Premium, Exclusive Invitees', content)
    content = re.sub(r'10,000\+\s*Audience', 'Curated Elite Audience', content)
    content = re.sub(r'10,000\+', 'Select Invite-Only', content)
    
    # 5. Venue
    content = re.sub(r'Premium Arena, Pune', 'Minimum 4-Star Property Banquet Hall, Pune', content)
    
    # 6. Food court removal
    content = re.sub(r'50\+\s*Food Stalls', 'Premium Dinner Included', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Done basic replace')