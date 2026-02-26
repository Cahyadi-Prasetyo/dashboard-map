import re

# Extract all CSS rule blocks from both files
def extract_rules(css):
    rules = {}
    # Match class selectors and their properties
    for m in re.finditer(r'(\.[a-zA-Z][\w-]*)\s*\{([^}]*)\}', css):
        selector = m.group(1)
        props = m.group(2).strip()
        if selector not in rules:
            rules[selector] = props
    return rules

lp = open('assets/css/landingpage.css', 'r', encoding='utf-8').read()
sh = open('assets/css/shared.css', 'r', encoding='utf-8').read()

lp_rules = extract_rules(lp)
sh_rules = extract_rules(sh)

diffs = []
for sel, lp_props in lp_rules.items():
    if sel in sh_rules:
        sh_props = sh_rules[sel]
        if lp_props.strip() != sh_props.strip():
            diffs.append(sel)

print(f"Rules with different values: {len(diffs)}")
for d in sorted(diffs):
    print(f"\n=== {d} ===")
    print(f"  LP: {lp_rules[d][:120]}")
    print(f"  SH: {sh_rules[d][:120]}")
