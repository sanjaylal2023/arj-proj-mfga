import os
import shutil

def delfile():
    longpath = os.path=('C:\Sumit_2022\del_file_folders')
    os.chdir(longpath)
    x=os.listdir()
    print (longpath)
    print('list of files ', x)
    for i in x:
        print('filename is : ', i)
        shutil.copy(i, www.txt)
        '''with open(i) as mytext:
            for i in mytext:
                print(i) 
        '''
    close(i)
delfile()