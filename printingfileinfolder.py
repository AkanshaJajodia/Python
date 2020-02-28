import os, glob

os.chdir("/Users/akanshajajodia/Desktop")
count = 0
for file in glob.glob("*.png"):
    print(file)
    count +=1
print("Total number of PNG files in this folder is ", count)