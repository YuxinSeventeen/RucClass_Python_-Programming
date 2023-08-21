# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 22:35:21 2023

@author: yuxin17
"""

f=open("./data/movie_rating.txt",encoding=("utf-8"))
line  = f.readlines()
movie_rating={}
for word in line:
    x = word.split(',')
    if len(x) == 1:
        current_movie = word.strip(":\n")
        movie_rating[current_movie]=[]
    else:
        movie_rating[current_movie].append(int(x[1]))
f.close()

# 输出结果
for movie in movie_rating.items():
    name = movie[0]
    rating = round(sum(movie[1])/len(movie[1]),2)
    print('{}:{}'.format(name, rating))

with open('./data/average_rating.txt', 'w') as f:
    for movie in movie_rating.items():
        name = movie[0]
        rating = round(sum(movie[1])/len(movie[1]),2)
        f.write('{}\t{}\n'.format(name, rating))