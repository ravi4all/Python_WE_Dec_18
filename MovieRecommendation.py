movies = [
    {
    'action' : ['hulk','ironman','batman','superman',
                'aquaman','thor','baahubali','bang bang','avengers'],
    'comedy' : [],
    'horror' : []
        }
    ]

user_1 = {'hulk','ironman','batman','superman','aquaman','thor',
          'bang bang','sanju','ms dhoni','baahubali'}
user_2 = {'baahubali','sanju','thor','hulk','batman','avengers',
          'zero','robot','ring','saw'}

similarMovies = user_1.intersection(user_2)
print(similarMovies)

intersection = len(user_1.intersection(user_2))
union = len(user_1.union(user_2))
f = intersection / union
print("Similarity Score",round(f*100,2),'%')
