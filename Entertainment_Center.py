import Media
import fresh_tomatoes

movies=[]
toy_story = Media.Movie("Toy Story", "Toys come to life", "https://www.youtube.com/watch?v=KYz2wyBy3kc", "http://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg")
movies.append(toy_story)
fresh_tomatoes.open_movies_page(movies)
