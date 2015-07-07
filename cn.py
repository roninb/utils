# script written by Malik Butler to change the name of a bunch of files
# USAGE: python cn.py <prefix name of all files> <extension for all files>

# Example input: DCM001.jpg reginadancing.png img2003.JPEG img2004.JPEG
# Example usage: python cn.py Sum14- png
# Example output: Sum14-1.png Sum14-2.png Sum14-3.png Sum14-4.png

import subprocess
import sys

# checks amount of command line args
if len(sys.argv) is 1:
	# assigns defaults to variables for use later
	new_name = ""
	new_extension = "jpg"
elif len(sys.argv) is 3:
	# assigns command line args to variables for use later
	new_name = str(sys.argv[1])
	new_extension = str(sys.argv[2])
else:
	# prints error and closes program
	print "Invalid Usage: Try: "
	print "python cn.py <filename prefix> <file extension> or "
	print "python cn.py for default"
	sys.exit(1)

# assigns a bytestring of your current directory's contents, one item per line
old_names = subprocess.check_output(["ls", "-1"])

# converts the bytestring to a utf-8 string that python can handle
old_names = old_names.decode("utf-8")

# creates a dict of strings using 1 line/string (why we used the -1 arg before)
old_names = old_names.split("\n")

old_names.pop()

count = 1 # counter for loop

# loops, renaming each file in the current directory a number and the file 
# extension passed, skips this file
for name in old_names:
	if name == "cn.py":
		continue
	subprocess.call(["mv", name, "%s%d.%s" % (new_name, count, new_extension)])
	count = count + 1

# prints a list of the new file names to ensure proper running
subprocess.call("ls")