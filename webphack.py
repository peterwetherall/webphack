import sys

if len(sys.argv) < 3:
    print("\nUsage: webphack.py [input dir] [output dir] [...]\n")
    print("[input dir] - Full path to the input directory.")
    print("[output dir] - Full path to the output directory.")
    print("[...] - Optional comma-separated file and directory names to ignore.\n")
    print("Example: webphack.py C:\phpFolder C:\htmlFolder config,backend.php,.htaccess")
    exit()
else:
    folderIn = sys.argv[1]
    folderOut = sys.argv[2]
    if len(sys.argv) > 3:
        ignore = sys.argv[3].split(",")

#Check the folder in and folder out paths are valid
import wph_dir
wph_dir.check(folderIn, folderOut)
	
#Check whether PHP is installed
import wph_php
wph_php.init()

#Clean out the output directory
wph_dir.clean(folderOut)
print("Output directory cleaned.")

#Map the input directory
tree = wph_dir.buildTree(folderIn, "", ignore, [])
print("Input directory mapped.")

#Convert from dynamic to STATIC.
import os

for item in tree:
    if len(item.split(".")) > 1:
        ext = item.split(".")[1]
    else:
        ext = None
    if ext == "php":
        output = wph_php.page(os.path.join(folderIn, item))
        name = item.split(".")
        name.pop()
        name = ".".join(name)
        wph_dir.writeFile(folderIn, folderOut, name + ".html", output)
    else:
        wph_dir.copyFile(folderIn, folderOut, item)

print("\nwebphack complete!\n")
