#This script moves files from Downloads to appropriate folders
#For video files they are moved to films
#For document files they are moved to documents
import os, re, shutil
moduleRegex = re.compile(r'IN(F|L) ?(\d\d\d)')
downloadsaddress = r"C:\Users\ndesh\Downloads"
downloads = os.listdir(r"C:\Users\ndesh\Downloads")
for files in downloads:
    file = files
    mo = moduleRegex.search(file)
    if(mo):
        if(mo.group(1) == 'F' or mo.group(1) == 'f'):
            if(mo.group(2) == '324'):
                shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Documents\\Education\\3rd Year\\2nd Semester\\INF324')
            elif(mo.group(2) == '370'):
                shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Documents\\Education\\3rd Year\\2nd Semester\\INF370')
        elif(mo.group(1) == 'L' or mo.group(1) == 'l'):
            shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Documents\\Education\\3rd Year\\2nd Semester\\INL320')
    elif(files.endswith('HD.mkv') or files.endswith('HD.mp4')):
        shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Videos\\Films')
    elif(files.endswith('.mkv') or files.endswith('.mp4')):
        shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Videos')
    elif(files.endswith('.pdf') or files.endswith('.PDF') or files.endswith('.xlsx') or files.endswith('.docx') or files.endswith('.zip') or files.endswith('.doc') or files.endswith('.json') or files.endswith('.csv') or files.endswith('.xlx')):
        shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Documents')
    elif(files.endswith('.jpg') or files.endswith('.jpeg')or file.endswith('.png')or files.endswith('.PNG')):
        shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Pictures')
    elif (files.endswith('.exe')):
        shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Documents\\Progams')
    elif(files.endswith('.torrent')):
        shutil.move(f'C:\\Users\\ndesh\\Downloads\\{file}','C:\\Users\\ndesh\\Videos\\Torrents')