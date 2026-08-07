import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Clean up "Corporate" references
    content = re.sub(r'Corporate Group Passes', 'Invite-Only Passes', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate Dandiya Night Pune', 'Invite-Only Dandiya Night Pune', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate Pass Quotation Inquiry', 'Invite-Only Quotation Inquiry', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate Lounge & Team Dandiya Experience', 'Exclusive Networking & VIP Lounge Experience', content, flags=re.IGNORECASE)
    content = re.sub(r'Serving Pune\'s Major IT & Corporate Parks', 'Serving Pune\'s Elite Professionals', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate Group Seating Bay', 'Premium Group Seating Bay', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate VIP Lounge', 'VIP Lounge', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate Relationship Manager', 'VIP Relationship Manager', content, flags=re.IGNORECASE)
    content = re.sub(r'HR / Corporate Contact Person', 'Primary Contact Person', content, flags=re.IGNORECASE)
    content = re.sub(r'Get Corporate Quotation', 'Get Pass Quotation', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate Email ID', 'Official Email ID', content, flags=re.IGNORECASE)
    content = re.sub(r'Corporate Employee Passes', 'Invite-Only Passes', content, flags=re.IGNORECASE)
    content = re.sub(r'corporate professionals', 'business professionals', content, flags=re.IGNORECASE)
    content = re.sub(r'corporate sales team', 'sales team', content, flags=re.IGNORECASE)
    content = re.sub(r'corporate group packages', 'exclusive group packages', content, flags=re.IGNORECASE)
    content = re.sub(r'corporate packages', 'invite-only packages', content, flags=re.IGNORECASE)
    content = re.sub(r'corporate bulk discounts', 'group booking discounts', content, flags=re.IGNORECASE)
    content = re.sub(r'VIP/Corporate', 'VIP/Group', content, flags=re.IGNORECASE)
    
    # Clean up IT parks text
    content = re.sub(r'customized bulk discounts for Pune IT companies & corporate teams', 'exclusive networking opportunities for elite communities', content, flags=re.IGNORECASE)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print('Clean up done')