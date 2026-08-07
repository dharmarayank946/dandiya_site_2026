import os
import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Update tickets.html
update_file('tickets.html', [
    ('Planning Corporate Group Booking', 'Planning for Invite-Only Participation')
])

# 2. Update sponsorship.html
update_file('sponsorship.html', [
    ('Corporate Sponsorship', 'Elite Sponsorship'),
    ('Corporate Sponsor Showcase', 'Elite Sponsor Showcase')
])

# 3. Update corporate-bookings.html
corporate_replacements = [
    # Meta and Title
    ('Bulk Employee Passes & Packages', 'Curated Business & Social Community'),
    ('Book corporate Dandiya night passes in Pune for your employees & teams. Exclusive bulk discounts, GST invoicing, reserved group bays for Hinjewadi, Kharadi & Magarpatta IT parks.', 'Book invite-only participation passes for Dandiya Connect Pune 2026. Join a curated business & social community of select entrepreneurs, professionals, families & guests.'),
    
    # Hero text
    ('Corporate Poster Showcase', 'Community Poster Showcase'),
    
    # IT Parks section -> Community section
    ("Serving Pune's Elite Professionals", 'A Curated Business & Social Community'),
    ('Special employee desk delivery & bulk invoicing available for organizations in:', 'Join a select gathering comprising:'),
    ('Hinjewadi IT Park', 'Entrepreneurs & Founders'),
    ('Kharadi EON Free Zone', 'Business Owners'),
    ('Magarpatta Cybercity', 'Working Professionals'),
    ('Baner High Street', 'Families & Select Guests'),
    
    # Packages
    ('Team Outing Pass', 'Community Group Pass'),
    ('Department Celebration', 'Professional Network Pass'),
    ('Enterprise / Townhall', 'Exclusive VIP Pass'),
    ('Inquire Team Package', 'Inquire Group Package'),
    ('Inquire Department Package', 'Inquire Network Package'),
    ('Inquire Enterprise Package', 'Inquire VIP Package'),
    ('10-25 Passes', '10-25 Guests'),
    ('25-50 Passes', '25-50 Guests'),
    ('50+ Passes', '50+ Guests'),
    ('Team Outing (10-25 Passes)', 'Community Group (10-25 Guests)'),
    ('Department Package (25-50 Passes)', 'Professional Network (25-50 Guests)'),
    ('Enterprise Tier (50+ Passes)', 'Exclusive VIP (50+ Guests)'),
    ('50+ Custom Employee Passes', '50+ Custom Guest Passes'),
    
    # Form
    ('Company / IT Organization', 'Organization / Community Name'),
    ('e.g. Infosys, TCS, Wipro, Amdocs...', 'e.g. Rotary Club, Business Network...'),
    ('Work Email ID', 'Email Address'),
    ('Corporate inquiry received', 'Participation inquiry received'),
    ('Get Pass Quotation & GST Invoice', 'Request Invite & Quotation')
]
update_file('corporate-bookings.html', corporate_replacements)

print("Participation updates applied!")
