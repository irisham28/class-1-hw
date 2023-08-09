class Movies():
 #constructer
    def __init__(self,time,genre,name,director,language):
        self.time = time
        self.genre = genre
        self.name = name
        self.director = director
        self.language = language

    def movie_details(self):
        print("the entered movie details are: ")
        print(self.time)
        print(self.genre)
        print(self.name)
        print(self.director)
        print(self.language)

    def movie_cost(self):
        print("the movie cost is: ",self.time*1.5)


#first object

movie1 = Movies(130,"romance","lust love","emily ross","english")
movie1.movie_details()
movie1.movie_cost()

#second object
movie2 = Movies(40,"horror","RAWR","evelyn BOSS","spanish")


movie2.movie_details()
movie2.movie_cost()

#third object
movie3 = Movies(80,"historical fiction","the war","bobby rome","german")


movie3.movie_details()
movie3.movie_cost()
