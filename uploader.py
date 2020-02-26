from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os, glob
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

##this will only work for files with some content in them 
##make sure files are in the same directory 
##drive folder id can be found in the url to drive folder
nameFragment = raw_input("type the fragment of the file name: ")
extension = raw_input("type the file extension type: ")
for f in glob.glob("{}*.{}".format(nameFragment, extension)):
            print f
            with open(f,"r") as f1:
                fn = os.path.basename(f1.name)
                file_drive = drive.CreateFile({'title': fn, 'parents':[{'id':'[INSERT FILE ID]'}]})  
                file_drive.SetContentFile(fn) 
                file_drive.Upload()
                print "The file: " + fn + " has been uploaded"