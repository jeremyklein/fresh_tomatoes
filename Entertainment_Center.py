import Media
import fresh_tomatoes

#Create an empty array of movies
movies=[]
# create a new instance of Movie 
toy_story = Media.Movie("Toy Story",
                        "Toys come to life",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg"
                        )
#add new movie object tothe list
movies.append(toy_story)
#call the open_movies_page method passing the movies array
fresh_tomatoes.open_movies_page(movies)
