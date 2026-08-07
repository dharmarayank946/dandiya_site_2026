import re

filename = 'venue.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hero and content
content = re.sub(r'Sprawling Open-Air Venue.*?Dance Floor', 'Large Premium Banquet Hall • Elegant Ambience', content, flags=re.DOTALL)
content = re.sub(r'Grand Festive Arena & Lawns', 'Premium 4-Star Banquet Hall', content)
content = re.sub(r'Massive Dance Floor', 'Elegant Dance Floor', content)
content = re.sub(r'Open-Air Arena', 'Banquet Hall', content)
content = re.sub(r'Spacious open lawns.*?air circulation', 'Air-conditioned premium indoor setup', content)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated venue page")