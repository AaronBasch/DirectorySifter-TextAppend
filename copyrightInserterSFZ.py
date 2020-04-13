'''
Simply run.
'''

import os


def siftDirectories(directory):
    '''sifts through directory, adding copyright 2020 to all sfz files'''
    for f in os.listdir(directory):
        if 'sfz' in f:
            for sfzFile in os.listdir(directory):
    
                file = sfzFile.replace('sfz', 'txt')
                
                os.rename(directory + '/' + sfzFile, directory + '/' + file) 
                
                oldFile = open(directory + '/' + file, 'r')
                newText = oldFile.read()
                if 'copyright 2020' in newText:
                    os.rename(directory + '/' + file, directory + '/' + file.replace('txt', 'sfz') )
                    continue
                oldFile.close()
                newFile = open(directory + '/' + file, 'w')
                newFile.write(newText[:20] + ' copyright 2020\n' + newText[20:])
                newFile.close()

                os.rename(directory + '/' + file, directory + '/' + file.replace('txt', 'sfz') )
        elif os.path.isdir(directory + '/' + f):
            siftDirectories(directory + '/' + f)


parentDirectory = input('enter path name of parent directory: ')
siftDirectories(parentDirectory)
print('copyright 2020 added to all .sfz files')
