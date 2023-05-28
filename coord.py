from posixpath import split
from pydoc import doc
import re
import string
import pyperclip


run = True
line = ""

print("Enter coordinates like so: \"00 00 00 n 000 00 00 w\"")
print("Enter nothing to copy line\n")

def setClipboard(stuff):
    Line = "\n\
            <Placemark>\n\
			    <name></name>\n\
			    <styleUrl>#area</styleUrl>\n\
			    <LineString>\n\
				    <tessellate>1</tessellate>\n\
				    <coordinates>\n\
					    {coord}\n\
				    </coordinates>\n\
			    </LineString>\n\
		    </Placemark>".format(coord=stuff)
    print(Line)
    pyperclip.copy(Line)

firstLine = ""
while run:
    text = input("").lower()
    if text == "":
        line += firstLine
        setClipboard(line)
        firstLine = ""
        line=""
        continue;

    words = text.split()
    long = int(words[0]) + int(words[1])/60 + int(words[2])/3600
#    if words[3] != "n":
#        long = 0 - long
    lat = 0 - (int(words[3]) + int(words[4])/60 + int(words[5])/3600)
#    if len(words) == 8:
#        if words[7] != "e":
#            lat = 0 - lat

    coords = "{lt:.10f},{lg:.10f},0 ".format(lt=lat,lg=long)

    if firstLine == "":
        firstLine = coords
    line += coords
    

