import os
import shutil
import time

def main():
    path = "folder1"
    days = 30
    deletedFiles = 0
    deletedFolder = 0
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds>=get_age(rootFolder):
                removeFolder(path)
                deletedFolder = deletedFolder+1 
                break

            else : 
                for folder in folders:
                    folderPath = os.path.join(rootFolder, folder)
                    if seconds>=get_age(folderPath):
                        removeFolder(path)
                        deletedFolder = deletedFolder+1 
                for file in files:
                    filePath = os.path.join(rootFolder, file)
                    if seconds>=get_age(filePath):
                        removeFile(path)
                        deletedFiles = deletedFiles+1

        else : 
            if seconds>=get_age(filePath):
                removeFile(path)
                deletedFiles = deletedFiles+1


    else : 
        print("Path Does Not Exist")
        print("Deleted Files = "+ deletedFiles + 1)

    print("Deleted Folders" + str(deletedFolder))
    print("Deleted Files" + str(deletedFiles))

def removeFolder(path):
    if not shutil.rmtree(path):
        print("Folder Removed Successfully")

    else : 
        print("Unable To Delete The Folder")

def removeFile(path):
    if not os.remove(path):
        print("File Removed Successfully")

    else : 
        print("Unable To Delete The File")

def get_age(path):
    cTime = os.stat(path).st_ctime
    return cTime

main()



