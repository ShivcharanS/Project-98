from os import read


"Welcome To File Swapper Name Your Files As file1 And Second As file2"

def swapper():

    fileInput = input("Enter Your File Name1 To Swap :- ")
    fileInput2 = input("Enter Your File Name2 To Swap :- ")

    file = open("file1.txt")
    file0 = open("file2.txt")

    file1 = file.read()
    file2 = file0.read()

    if(fileInput == "file1"):
        print(file2)
    
    if(fileInput2 == "file2"):
        print(file1)
    
    if(fileInput == "file2"):
        print(file1)
    
    if(fileInput2 == "file1"):
        print(file2)
    

swapper()