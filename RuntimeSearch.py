#Python script to look at the films on my Hard Drive, google their titles and then return the runtime and IMDB score to a dictionary
import requests, random, re, sys, bs4, os, shutil
from bs4 import BeautifulSoup
from googlesearch import search 

def find_rating(filmtitle):
    film_rating = 'NA'
    runtime = 'NA'
    linkcounter = 0
    ratingcounter = 0
    for j in search(f'{filmtitle} film imdb', tld='com', lang='en', num=10, start=0, stop=10, pause=2.0):
        linkcounter += 1
        if(linkcounter == 1):
            print(j)
            firstresult = j
    print(f'______________________________________________________________________________________________\nFirst Result: {firstresult}')

    response = requests.get(
        url=firstresult,
    )
    counter = 0
    soup = BeautifulSoup(response.content, 'html.parser')
    for page_list in soup.find_all('ul'):
        for list_item in page_list.find_all('li'):
            counter += 1
            if(counter == 4):
                runtime = list_item.string
                # print(runtime) 
    for rating_wrapper in soup.find_all('div', class_='AggregateRatingButton__Rating-sc-1ll29m0-2 bmbYRW'):
        for rating in rating_wrapper.find_all('span'):
            if(rating.string):
                ratingcounter += 1
                if(ratingcounter == 1):
                    film_rating = rating.string
                    # print(film_rating)
    
    myFilm = {'Runtime': runtime,'Rating':film_rating}
    return myFilm
