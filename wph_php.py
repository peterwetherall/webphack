import subprocess, wph_error

#Check whether PHP is installed
def init():
	try:
		phpVersion = subprocess.check_output(["php", "-v"])
	except:
		wph_error.init("PHP not installed.\nDownload available at [https://www.php.net/downloads.php]")
	print("PHP version " + str(phpVersion).split()[1] + " is installed.")
	
#Convert PHP page to HTML
def page(path):
    try:
        raw = subprocess.check_output(["php", path])
        #Strip junk whitespace
        HTML = raw.decode().replace("\r", "").replace("\n", "").replace("\t", "")
    except Exception as e:
        wph_error.init("Failed to process [" + path + "]\n" + str(e))
    return HTML