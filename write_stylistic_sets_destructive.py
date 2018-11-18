# Search for glyphs with "ss" in their suffix, create stylistic sets feature
# code for them, and OVERWRITE ALL OF YOUR FEATURES WITH THESE NEW ONES

f = CurrentFont()

sets = []
features = ""

for g in f.keys():
    if "." in g:
        if "ss" in g.split(".")[1] and g.split(".")[1] not in sets:
            sets.append(g.split(".")[1])

sets.sort()

for set in sets:
    features += "feature %s {\n" % set
    for g in f:
        if set in g.name:
            base = g.name.split(".")[0]
            suffix = g.name.split(".")[1]
            features += "sub %s by %s;\n" % (base, g.name)
    features += "} %s;\n\n" % set

f.features.text = features