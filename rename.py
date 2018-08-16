import os
import time

curPath = os.getcwd()
print curPath
FILE_TYPES = ['.png','.jpg','.jpeg','.gif']
IGNORE = ['.git','.svn']

def rename(path):
	filelist = os.listdir(path)
	i = 0
	for item in filelist:
		oldpath = os.path.join(path,item)
		if os.path.isdir(oldpath) and item not in IGNORE:
			print 'start rename %s' % oldpath
			rename(oldpath)
			continue
		filename = os.path.splitext(oldpath)[0]
		filetype = os.path.splitext(oldpath)[1]	
		if filetype not in FILE_TYPES:
			continue
		i+=1
		newfile = os.path.join(path,str(i)+filetype)
		os.rename(oldpath,newfile)
		print oldpath + ' > ' + newfile
	print 'rename finished.'

def randstr():
	import string
	import random
	ran_str = ''.join(random.sample(string.ascii_letters+string.digits,10))
	return ran_str

if __name__ == '__main__':
	rename(curPath)