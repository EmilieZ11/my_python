from datetime import datetime
from re import findall
import os


def main(): print("--- File Handling ---")


def file_hello(): pass


# Create Text
demoFile = "demo.txt"
# try:
if not os.path.exists(demoFile):
    f = open(demoFile, "xt")
    # except FileExistsError:
    #    pass
    # else:
    f.close()

# Read Text
f = open(demoFile, "rt")
demoText = f.read()
thisTime = len(findall("\n", demoText))
f.close()

# Append Text
f = open(demoFile, "at")  # "w" => Write, "b" for Binary (e.g. Images)
f.write(str(thisTime + 1) + ". " + str(datetime.now()) + "\n")
f.close()

# Delete File
if os.path.exists("demo - Copy.txt"):
    os.remove("demo - Copy.txt")

# Delete Folder
try:
    os.rmdir("New Folder")
except FileNotFoundError:
    pass
except OSError:  # You can only remove empty folders.
    pass

main()
file_hello()
print()
