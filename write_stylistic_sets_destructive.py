# menuTitle : Write Stylistic Sets - Destructive

'''
Search for glyphs with "ss" or "alt" in their suffix, create ss** and salt feature
code for them, and OVERWRITE ALL OF YOUR EXISTING FEATURES WITH THESE NEW ONES
''' 

f = CurrentFont()

s_sets = []
s_alts = []
features = ""

for g in f:
    if "." in g.name and "ss" in g.name.split(".")[1] and g.name.split(".")[1] not in s_sets:
        s_sets.append(g.name.split(".")[1])

for s_set in s_sets:
    features += "feature %s {\n" % s_set
    for g in f:
        if s_set in g.name:
            base = g.name.split(".")[0]
            suffix = g.name.split(".")[1]
            features += "\tsub %s by %s;\n" % (base, g.name)
    features += "} %s;\n\n" % s_set
    
for g in f:
    if "." in g.name and "alt" in g.name.split(".")[1]:
        s_alts.append(g.name.split(".")[1])

for s_alt in s_alts:
    features += "feature salt {\n"
    for g in f:
        if s_alt in g.name:
            base = g.name.split(".")[0]
            suffix = g.name.split(".")[1]
            features += "\tsub %s by %s;\n" % (base, g.name)
    features += "} salt;\n\n"

f.features.text = features
