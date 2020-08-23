def swapFileData():
    savedData = fileTwoData
    fileOneData = open("sample1.txt", "r+")
    fileTwoData = open("sample2.txt", "r+")
    for line in fileOneData :
        savedData = fileTwoData
    for line in savedData : 
        fileOneData = fileOneData

swapFileData()
