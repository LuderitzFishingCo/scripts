#This script will eventually remove everything unnecessary in episode files and just leave the S00E00 format
import re, os
episodeformat = re.compile('S\d\dE\d\d')
seriesaddress = r"C:\Users\ndesh\Downloads\Film and Television\SeriesAddress"
series = os.listdir(r"C:\Users\ndesh\Downloads\Film and Television\SeriesAddress")

def fix_series(files):
    filetype = files[-4:]
    filename = files[:-4]
    new = filename.upper()
    capitalname = (f'{seriesaddress}\{new}{filetype}')
    normalname = (f'{seriesaddress}\{filename}{filetype}')
    os.rename(f'{normalname}',f'{capitalname}')
    mo = episodeformat.search(filename)
    final = mo.group()
    newname = (f'{seriesaddress}\{final}{filetype}')
    oldname = (f'{seriesaddress}\{filename}{filetype}')
    os.rename(f'{oldname}',f'{newname}')
    return newname

for files in series:
    if(files.endswith('.mkv') or files.endswith('.mp4')):
        series_file = fix_series(files)
        print(series_file)

