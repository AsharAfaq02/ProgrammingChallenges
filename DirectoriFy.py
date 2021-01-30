def my_directory(dirString):
    z = 0
    s = 0
    rpt = 0
    if dirString[len(dirString)-1] != "/":
        dirString = dirString + "/"

    if dirString[0] != "/":
        dirString = "/"+dirString


    for x in dirString:
        z = z + 1
        if x == "/":
            q = s+1
            s = z-1

            print(" "*rpt+dirString[q:s])
            rpt = rpt + 2




filePath = input("Enter Directory Path: ")
my_directory(filePath)