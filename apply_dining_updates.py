import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Update all footers
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update the footer link from Food Stall to Premium Dining
    content = content.replace('Food Stall Dandiya Event Pune', 'Premium Dining Menu')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Fix food-stalls-vendors.html specifically
with open('food-stalls-vendors.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Fix Title and Meta
content = re.sub(r'<title>.*?</title>', '<title>Premium Dining at Dandiya Connect Pune 2026 | Exclusive Menu</title>', content)
content = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Discover the Pure Vegetarian Premium Dinner menu at Dandiya Connect Pune 2026. A lavish festive menu included in all passes for an elite Garba experience.">', content)

# Fix Breadcrumb
content = content.replace('<span>Food Stall Dandiya Event Pune</span>', '<span>Premium Dining Menu</span>')

# Fix broken HTML comment and remove JS for stalls
content = content.replace('<!-- Cross-Link<!-- Master Footer -->', '</div>\n    </div>\n    <!-- Master Footer -->')

js_to_remove = '''        function handleStallSubmit(e) {
            e.preventDefault();
            alert("Stall booking request received! Our stall allocation team will reach out with availability and layout pricing.");
        }

        function setStallCategory(cat) {
            var hidden = document.getElementById('stallTypeInput');
            var trigger = document.getElementById('stallTrigger');
            if (hidden && trigger) {
                hidden.value = cat;
                trigger.textContent = cat;
                trigger.classList.add('has-value');
            }
        }'''

# Also need to remove the event listeners for stallDropdown in JS
js_dropdown = '''        (function() {
            var wrap = document.getElementById('stallDropdown');
            if (!wrap) return;
            var trigger = wrap.querySelector('.custom-select-trigger');
            var options = wrap.querySelectorAll('.custom-option');
            var hiddenInput = document.getElementById('stallTypeInput');

            trigger.addEventListener('click', function(e) {
                e.stopPropagation();
                wrap.classList.toggle('open');
            });

            options.forEach(function(opt) {
                opt.addEventListener('click', function(e) {
                    e.stopPropagation();
                    var val = this.getAttribute('data-value');
                    hiddenInput.value = val;
                    trigger.textContent = this.textContent;
                    trigger.classList.add('has-value');

                    options.forEach(function(o) { o.classList.remove('selected'); });
                    this.classList.add('selected');

                    wrap.classList.remove('open');
                });
            });

            document.addEventListener('click', function() {
                wrap.classList.remove('open');
            });
        })();'''

content = content.replace(js_to_remove, '')
content = content.replace(js_dropdown, '')

with open('food-stalls-vendors.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Food dining updates applied!")
