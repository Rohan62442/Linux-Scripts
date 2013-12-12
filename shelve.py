#!/usr/bin/python3
import zipfile
import os
import sys

try:
    
    if sys.argv[1]=='-e':
        assert os.path.exists(sys.argv[2])
        zf=zipfile.ZipFile(sys.argv[2],'a',zipfile.ZIP_DEFLATED, allowZip64=True)
        for x in zf.namelist():
            zf.extract(x)
        zf.close()

    elif sys.argv[1]=='-l':
        assert os.path.exists(sys.argv[2])
        zf=zipfile.ZipFile(sys.argv[2],'a',zipfile.ZIP_DEFLATED, allowZip64=True)
        print("\nNAME\t\t\tFILE SIZE\t\tCOMPRESSED SIZE\n***************************************************************")
        for x in zf.namelist():
            print(str(zf.getinfo(x).filename)+"\t\t"+str(zf.getinfo(x).file_size)+"\t\t\t"+str(zf.getinfo(x).compress_size))
        zf.close()

    elif sys.argv[1]=='-a':
        if not sys.argv[2].endswith('.zip'):
            zf=zipfile.ZipFile(sys.argv[2]+'.zip','a',zipfile.ZIP_DEFLATED, allowZip64=True)
        else:
            zf=zipfile.ZipFile(sys.argv[2],'a',zipfile.ZIP_DEFLATED, allowZip64=True)
        fileList=[]
        directList=[]
        for i in range(3,len(sys.argv)):
            if os.path.isdir(sys.argv[i]):
                directList.append(sys.argv[i])
            else:
                fileList.append(sys.argv[i])
        for x in fileList:
            zf.write(x)
        for x in directList:
            for dirname, subdirs, files in os.walk(x):
                zf.write(dirname)
                for filename in files:
                    zf.write(os.path.join(dirname, filename))
        zf.close()

    elif sys.argv[1]=='-f':
        assert os.path.exists(sys.argv[2])
        zf=zipfile.ZipFile(sys.argv[2],'a',zipfile.ZIP_DEFLATED, allowZip64=True)
        fileList=[]
        for i in range(3,len(sys.argv)):
            if zf.namelist().count(sys.argv[i]+'/')!=0:
                temp=sys.argv[i]
                temp+='/'
                fileList.append(temp)
                for x in zf.namelist():
                    if temp==x[:len(temp)]:
                        fileList.append(x)
            else:
                fileList.append(sys.argv[i])
        for x in fileList:
            zf.extract(x)
        zf.close()

    else:
        print("Error: Incorrect options given.")
        
except AssertionError:
    print("The archive does not exist.")
except KeyError:
    print("Atleast one file/directory specified does not exist in the archive.")
except FileNotFoundError:
    print("Atleast one file/directory specified does not exist.")
    os.remove(sys.argv[2])
except zipfile.BadZipFile:
    print("Bad Zip File.")