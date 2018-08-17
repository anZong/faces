import os
import time

def rename(path):
	dirlist = os.listdir(path)
	i=0
	for d in dirlist:
		if not os.path.isdir(d):
			continue
		newpath = os.path.join(path,d)
		filelist = os.listdir(newpath)
		for f in filelist:
			i+=1
			filepath = os.path.join(newpath,f)
			filetype = os.path.splitext(filepath)[1]	
			newfile = os.path.join(path,str(i)+filetype)
			os.rename(filepath,newfile)

if __name__ == '__main__':
	rename(os.getcwd())