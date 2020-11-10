import os, shutil, wph_error

#Ensure the folder in and folder out paths are valid
def check(folderIn, folderOut):	
	#Check whether the paths are valid directories
	if os.path.isdir(folderIn):
		print("Valid input directory [" + folderIn + "]")
	else:
		wph_error.init("Invalid input directory [" + folderIn + "]")
	if os.path.isdir(folderOut):
		print("Valid output directory [" + folderOut + "]")
	else:
		wph_error.init("Invalid output directory [" + folderOut + "]")

#Clean (empty) the specified directory
def clean(path):
	for filename in os.listdir(path):
		file_path = os.path.join(path, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				shutil.rmtree(file_path)
		except Exception as e:
			wph_error.init("Failed to delete " + file_path + " [" + e + "]")

#Map the input directory
def buildTree(path, relativePath, ignore, tree):
	for filename in os.listdir(path):
		file_path = os.path.join(path, filename)
		relativeFile_path = os.path.join(relativePath, filename);
		if filename in ignore:
			print("Ignoring [" + file_path + "]")
		else:
			try:
				if os.path.isfile(file_path) or os.path.islink(file_path):
					tree.append(relativeFile_path)
				elif os.path.isdir(file_path):
					tree = buildTree(file_path, relativeFile_path, ignore, tree)
			except Exception as e:
				wph_error.init("Failed to access [" + file_path + "]\n" + str(e))
	return tree
	
#Copy file
def copyFile(folderIn, folderOut, item):
    try:
        shutil.copyfile(
            os.path.join(folderIn, item),
            os.path.join(folderOut, item)
        )
    except:
        directory = item.split("\\")
        directory.pop()
        directory = "\\".join(directory)
        shutil.copytree(os.path.join(folderIn, directory), os.path.join(folderOut, directory))
        print("Creating directory [" + directory + "]")
        try:
            shutil.copyfile(os.path.join(folderIn, item), os.path.join(folderOut, item))
        except Exception as e:
            print("Couldn't copy file [" + item + "]")
            print(e)

#Write file
def writeFile(folderIn, folderOut, item, content):
    try:
        with open(os.path.join(folderOut, item), "w") as f:
            f.write(content)
    except:
        directory = item.split("\\")
        directory.pop()
        directory = "\\".join(directory)
        shutil.copytree(
            os.path.join(folderIn, directory),
            os.path.join(folderOut, directory)
        )
        print("Creating directory [" + directory + "]")
        with open(os.path.join(folderOut, item), "w") as f:
            f.write(content)