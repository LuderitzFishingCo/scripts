import os, re, shutil
from TorrentFixer import change_name
from RuntimeSearch import find_rating

final = 'Hello there'
for folderName, subfolders, filenames in os.walk(r'C:\Users\ndesh\Downloads\Film and Television'):
        filecounter = 0
        for subfolder in subfolders:
            x = 0
            if (subfolder == 'Subs'):
                subfoldercounter = 0            
        for filename in filenames:
            if(filename.endswith('.srt')):
                subfolder = f'C:\\Users\\ndesh\\Downloads\\Film and Television\\{final} Subs'
                subfoldercounter += 1
                print(f'Moving: {folderName}\{filename} to {subfolder}')
                if(subfoldercounter == 1):
                    os.mkdir(f'{subfolder}')
                shutil.move(f'{folderName}\{filename}',f'{subfolder}')
            if(filename.endswith('.mkv') or filename.endswith('.mp4')):
                filecounter += 1    
        if(filecounter == 1):
            filetype = filename[-4:]
            file = filename[:-4]
            if(filename.endswith('.mkv') or filename.endswith('.mp4')):
                final = change_name(file)
                newname = (f'{folderName}\{final} HD{filetype}')
                oldname = (f'{folderName}\{filename}')
                print(f'{oldname}',f'{newname}')
                os.rename(f'{oldname}',f'{newname}')
                shutil.move(f'{newname}','C:\\Users\\ndesh\\Downloads\\Film and Television')
        print('')
