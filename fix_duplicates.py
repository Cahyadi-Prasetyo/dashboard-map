import glob
import re

files = glob.glob("*.html")

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Count occurrences of ROW 5
    count = content.count("<!-- ROW 5 -->")
    if count > 1:
        # Find the SECOND occurrence and remove everything from it to the closing </div> of that wrapper
        # Strategy: find second "<!-- ROW 5 -->" and remove from there to just before the next <script> tag
        first_idx = content.index("<!-- ROW 5 -->")
        second_idx = content.index("<!-- ROW 5 -->", first_idx + 1)
        
        # Find the end of the second ROW 5 block
        # The pattern is: <!-- ROW 5 --> ... </div>\n\n    <script
        # Find the next <script after the second ROW 5
        script_after = content.index("<script", second_idx)
        
        # Remove from second_idx to script_after
        content = content[:second_idx] + content[script_after:]
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed duplicate in {file}")
    else:
        print(f"OK: {file} has {count} ROW 5 block(s)")

print("Done.")
