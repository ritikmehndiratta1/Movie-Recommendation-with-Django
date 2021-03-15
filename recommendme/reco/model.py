import numpy as np
import pandas as pd

def movie_reco(movie_name):
    
    # initialize column names for u.data
    column_names=['user_id','item_id','rating','timestamp']
    
    # read file u.data
    df=pd.read_csv('movie_files\\u.data',sep='\t',names=column_names)
    
    # read file Movie_Id_Titiles
    movie_titles= pd.read_csv('movie_files\\Movie_Id_Titles')
    
    # merge the two data frames on the column item_id
    df=pd.merge(df,movie_titles,on='item_id')

    # group the movies with the same title calculate the mean reviews and put them in descending order
    df.groupby('title')['rating'].mean().sort_values(ascending=False)
    ratings=pd.DataFrame(df.groupby('title')['rating'].mean())
    
    # adding column for number of ratings in the data frame of ratings 
    ratings['num of ratings']=pd.DataFrame(df.groupby('title')['rating'].count())
    moviemat=df.pivot_table(index='user_id',columns='title',values='rating')
    
    # sort the values in rating in descending order based on number of reatings
    ratings.sort_values('num of ratings',ascending=False).head(10)

    # fetching the movie ratings for the inputted movie name in form_page.html
    movies_user_ratings=moviemat[movie_name]

    # finding the movie similar to the given movie with the use of correlation function in pandas
    similar_to_movies=moviemat.corrwith(movies_user_ratings)

    # fetching the column of correlation from data frame similar_to_movies and dropping the null values
    corr_movies=pd.DataFrame(similar_to_movies,columns=['Correlation'])
    corr_movies.dropna(inplace=True)
    
    # join the corr_movies with number of ratings from the ratings dataframe
    corr_movies=corr_movies.join(ratings['num of ratings'])

    # storing the final 6 results with hightest correlation and number of ratings greater than 80
    final_reco=corr_movies[corr_movies['num of ratings']>80].sort_values('Correlation',ascending=False).head(6)
    
    # fetching the name of the movies and adding that as a column and setting the index column as serial number 
    indexstuff=[x for x in final_reco.index]
    sno=[int(x) for x in range(1,7)]
    final_reco['S.No.']=sno
    final_reco.set_index('S.No.',inplace=True)
    final_reco['title']=indexstuff

    # printing the final result which would only be visible on the server-side
    print(final_reco)

    # making a dictionary to return the resulting items to views.py
    dit={ 'title1':final_reco.at[2,'title'],
    'title2':final_reco.at[3,'title'],
    'title3':final_reco.at[4,'title'],
    'title4':final_reco.at[5,'title'],
    'title5':final_reco.at[6,'title'] }
    return dit