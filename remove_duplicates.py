with open(r'd:\Workspace\dashboard-map\batam.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first (duplicate) style-137 block and the first (duplicate) footer
# They appear between INDIKATOR 7 section and the second style-137 block

# The duplicate block starts with the first <div class="style-137"> 
# and ends right before the second <div class="style-137">

import re

# Find all occurrences of style-137
idx1 = content.find('<div class="style-137">')
idx2 = content.find('<div class="style-137">', idx1 + 1)

print(f'First style-137 at char: {idx1}')
print(f'Second style-137 at char: {idx2}')

if idx1 >= 0 and idx2 >= 0:
    # The duplicate is from idx1 to idx2 (the chunk between them is the first copy)
    # But we need to include the blank lines before idx2
    # Find any leading whitespace/newlines before idx2
    # Trim backwards to include the blank lines
    chunk_to_remove = content[idx1:idx2]
    print(f'Removing {len(chunk_to_remove)} chars ({chunk_to_remove.count(chr(10))} lines)')
    print('Preview of removed content start:', repr(chunk_to_remove[:100]))
    print('Preview of removed content end:', repr(chunk_to_remove[-100:]))
    
    new_content = content[:idx1] + content[idx2:]
    with open(r'd:\Workspace\dashboard-map\batam.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done!')
else:
    print('ERROR: Could not find both style-137 blocks')
