# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 08:14:17 2021

@author: ndesh
"""
#Import
import os, shutil
from hurry.filesize import size
import pandas as pd
from RuntimeSearch import find_rating

linkcounter = 0
myFilms = []
titles = []
for folderName, subfolders, filenames in os.walk(r'E:\Film and Television\Films'):
        folder = folderName[29:]
        for subfolder in subfolders:
            x = 0
        for filename in filenames:
            filesize = os.path.getsize(f'{folderName}\{filename}')
            filesize = size(filesize)
            if(filename.endswith('HD.mkv') or filename.endswith('HD.mp4') or filename.endswith('HD.avi')):
                film_find = find_rating(filename[:-4])
                myFilm = {'Title': filename[:-4],'Size':filesize, 'Runtime': film_find['Runtime'],'IMDB_Rating':film_find['Rating']}
                film = myFilm['Title']
                print(myFilm)
                myFilms += [myFilm]
            elif(filename.endswith('.mkv') or filename.endswith('.mp4') or filename.endswith('.avi')):
                film_find = find_rating(filename[:-4])
                myFilm = {'Title': filename[:-4],'Size':filesize, 'Runtime': film_find['Runtime'],'IMDB_Rating':film_find['Rating']}
                print(myFilm)
                myFilms += [myFilm]
        print(len(myFilms))

harddrive_df = pd.DataFrame(myFilms)
harddrive_df.to_excel('HardDriveFilms.xlsx')
shutil.move(r'C:\Users\ndesh\Scripts\HardDriveFilms.xlsx',r'C:\Users\ndesh\Videos')