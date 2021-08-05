from os import name
import cv2
import dropbox
import time
import random

startTime=time.time()

def takeSnapshot():
    number=random.randint(0,100)
    videocapturobject=cv2.VideoCapture(0)
    result=True

    while(result):
        ret,frame=videocapturobject.read()
        imgname="img"+str(number)+".png"
        print(ret)

        cv2.imwrite(imgname,frame)
        startTime=time.time
        result=False
    
    return imgname
    print("Image Taken")
    
    videocapturobject.release()
    cv2.destroyAllWindows()

def uploadFile(imgname):
    accesstoken="tmvc6M65wNYAAAAAAAAAAY6mkvfEapFR0U-6rmvTvCyfkkr_lLii8oUyWlyq93cx"
    file=imgname
    filefrom=file
    fileto="/newfolder/"+imgname

    dbx=dropbox.Dropbox(accesstoken)
    with open(filefrom, "rb")as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")

def main():
    while(True):
        if ((time.time()-startTime)>=30):
            name=takeSnapshot()
            uploadFile(name)


main()