with open(r'd:\Workspace\dashboard-map\batam.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the old eko-section-5 block: start ~line 716, end ~line 874
start_line = None
end_line = None

for i, line in enumerate(lines):
    if 'class="eko-section-5" id="section-kemiskinan-gini"' in line and start_line is None:
        # Walk back to find the comment start
        for j in range(i, max(0, i-5), -1):
            if 'SECTION 5: KEMISKINAN' in lines[j]:
                start_line = j - 1  # include blank line before comment
                break
        if start_line is None:
            start_line = i - 2

for i, line in enumerate(lines):
    if start_line is not None and i > start_line + 5:
        # After the Kemiskinan section ends, find next "<!-- " comment that introduces style-129 or next section
        if '<!-- <div class="style-129">' in line or (i > start_line + 100 and '</div>' in line and 'eko-section-5' not in line):
            # Check if previous lines close the eko-section-5 div
            # The section ends at the </div>    </div> near line 874
            pass

# More reliable: find the character positions
with open(r'd:\Workspace\dashboard-map\batam.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_start = content.find('<!-- ========================================================\n         SECTION 5: KEMISKINAN')
if old_start == -1:
    old_start = content.find('<!--\n         SECTION 5: KEMISKINAN')
if old_start == -1:
    # Try with \r\n
    old_start = content.find('<!-- ========================================================\r\n         SECTION 5: KEMISKINAN')

print(f'old_start={old_start}')

# Find where the old section ends - it's followed by the inline style commented block
old_end_marker = '<!-- <div class="style-129">'
old_end = content.find(old_end_marker, old_start if old_start >= 0 else 0)
print(f'old_end={old_end}')

if old_start >= 0 and old_end >= 0:
    # Remove the old section
    removed = content[old_start:old_end]
    print(f'Removing {len(removed)} chars ({removed.count(chr(10))} lines)')
    new_content = content[:old_start] + content[old_end:]
    with open(r'd:\Workspace\dashboard-map\batam.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Success! Old eko-section-5 removed.')
else:
    print('ERROR: Could not find markers. Checking content...')
    # Show relevant area
    idx = content.find('SECTION 5:')
    print(f'SECTION 5: found at {idx}')
    if idx >= 0:
        print(repr(content[idx-50:idx+200]))
