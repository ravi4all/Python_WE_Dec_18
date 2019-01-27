movies = {
    'action' : ['hulk','ironman','batman','superman','robot'
                'aquaman','thor','baahubali','bang bang','avengers'],
    'comedy' : ['sanju','dhamaal','fukrey','zero'],
    'horror' : ['saw','ring','ring 2','nun'],
    'biopic' : ['sanju','ms dhoni']
        }

user_1 = {'hulk','ironman','batman','superman','aquaman','thor',
          'bang bang','sanju','ms dhoni','baahubali'}
user_2 = {'baahubali','sanju','thor','hulk','batman','avengers',
          'zero','robot','ring','saw'}

similarMovies = user_1.intersection(user_2)
print(similarMovies)

intersection = len(user_1.intersection(user_2))
union = len(user_1.union(user_2))

#Jaccard Distance
f = intersection / union
print("Similarity Score",round(f*100,2),'%')

action = 0
comedy = 0
horror = 0
biopic = 0

for m in similarMovies:
    if m in movies['action']:
        action += 1
    elif m in movies['comedy']:
        comedy += 1
    elif m in movies['horror']:
        horror += 1
    elif m in movies['biopic']:
        biopic += 1

print("""
Action : {}
Comedy : {}
Horror : {}
Biopic : {}
""".format(action, comedy, horror, biopic)
)
