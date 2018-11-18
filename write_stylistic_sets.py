# Search for glyphs with "ss" in their suffix, create stylistic
# sets feature code for them, and copy it to clipboard.

import mojo
from AppKit import NSPasteboard, NSArray

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

if features != "":
    p = NSPasteboard.generalPasteboard()
    p.clearContents()
    a = NSArray.arrayWithObject_(features)
    p.writeObjects_(a)
    mojo.UI.Message('Stylistic sets features copied to your clipboard')

if features == "":
    mojo.UI.Message("Could not find properly named glyphs.")