# TODO: Add logs to the logs.txt file in the same directory as the script
# TODO: Polish the code and add more features

"""
RELEASE 1.0.0 Open Source Downloader

AuthorNote: Please make issues and pull requests on GitHub if you find any bugs or have any suggestions
this is a good first contribution to open source. Also, I would like to try to run the files through Virustotal API
for added security so if you have any suggestions on how to do that please let me know.
"""

# Accessibility
ALLCAPS = False
debug = False

# Start Menu
print("Start Menu - Enter to continue")
initInput = input(":")
if initInput == "install":
	import os

	print("Installing...")
	os.system("pip install -r requirements.txt")
	print("     Done!      ")

if initInput == "config":
	print("1. Dev-Logs (ON/OFF)")
	# Dev-Logs are debug messages
	print("2. CAPS (ON/OFF)")
	# CAPS is text printed in all caps
	print("3. Leave")
	configInput = input(":")
	if configInput == "1":
		print("Dev-Logs are currently: " + str(debug))
		print("1. ON")
		print("2. OFF")
		configInput = input(":")
		if configInput == "1":
			debug = True
			print("Dev-Logs are now: " + str(debug))
		if configInput == "2":
			debug = False
			print("Dev-Logs are now: " + str(debug))

	if configInput == "2":
		print("CAPS is currently: " + str(ALLCAPS))
		print("1. ON")
		print("2. OFF")
		configInput = input(":")
		if configInput == "1":
			ALLCAPS = True
			print("CAPS is now: " + str(ALLCAPS))
		if configInput == "2":
			ALLCAPS = False
			print("CAPS is now: " + str(ALLCAPS))

# Package handling
try:
	import requests
except ImportError:
	print("Error: Requests Module not found use 'pip install requests' to install it")
try:
	from colorama import Fore, Style
except ImportError:
	print("Error: Colorama Module not found use 'pip install colorama' to install it")
try:
	import time
except ImportError:
	print("Error: Time Module not found use 'pip install time' to install it")
try:
	import os
except ImportError:
	print("Error: OS Module threw an error while importing")

# Functions
CC = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


# Main
def main():
	CC()
	print('''

                                           |--->  Downloader.py  <---|
                                          |->  Created by: itzCozi  <-|

    ''')
	time.sleep(0.1)
	Destination = input("Desired directory: ")

	# Check if the directory exists
	if os.path.exists(Destination):
		DwnldPath = Destination
		if debug:
			print(Fore.BLUE + "Destination set to: " + DwnldPath + Style.RESET_ALL)
	else:
		print(Fore.RED + "ERROR: Directory does not exist." + Style.RESET_ALL)
		if debug:
			print(Fore.RED + "ERROR1: Executing patch")
		os.mkdir(Destination)
		time.sleep(3)
		quit()

	# Name change
	NewName = input("New Name: ")
	if debug:
		print("New name set to: " + str(NewName) + Style.RESET_ALL)

	URL = input("Download URL: ")
	FileExt = URL[-4:]

	# Download and write to file
	file_content = requests.get(URL)
	open(Destination + '/' + NewName + FileExt, "wb").write(file_content.content)
	if debug:
		print(Fore.GREEN + "Downloaded file to: " + Destination + Style.RESET_ALL)


# Accessibility option
def CAPSmain():
	CC()
	print(Style.BRIGHT + '''

                                           |--->  DOWNLOADER.PY  <---|
                                          |->  CREATED BY: itzCozi  <-|

    ''')
	time.sleep(0.1)
	Destination = input("DESIRED DIRECTORY: ")

	# Check if the directory exists
	if os.path.exists(Destination):
		DwnldPath = Destination
		if debug:
			print.upper(Fore.BLUE + "Destination set to: " + DwnldPath + Style.RESET_ALL)
	else:
		print.upper(Fore.RED + "ERROR: Directory does not exist." + Style.RESET_ALL)
		if debug:
			print.upper(Fore.RED + "ERROR1: Executing patch")
		os.mkdir(Destination)
		time.sleep(3)
		quit()

	# Name change
	NewName = input("NEW NAME: ")
	if debug:
		print.upper("New name set to: " + str(NewName) + Style.RESET_ALL)

	URL = input("DOWNLOAD URL: ")
	FileExt = URL[-4:]

	# Download and write to file
	file_content = requests.get(URL)
	open(Destination + '/' + NewName + FileExt, "wb").write(file_content.content)
	if debug:
		print.upper(Fore.GREEN + "Downloaded file to: " + Destination + Style.RESET_ALL)


# Run
if ALLCAPS == True:
	CAPSmain()
else:
	main()
