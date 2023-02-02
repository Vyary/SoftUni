import sys

number_of_movies = int(input())

total_of_ratings = 0
highest_rating_movie = ''
highest_rating = - sys.maxsize
lowest_rating_movie = ''
lowest_rating = sys.maxsize

for movie in range(number_of_movies):
    movie_title = input()
    movie_rating = float(input())

    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_rating_movie = movie_title
        total_of_ratings += movie_rating
    elif movie_rating < lowest_rating:
        lowest_rating = movie_rating
        lowest_rating_movie = movie_title
        total_of_ratings += movie_rating
    else:
        total_of_ratings += movie_rating

average_score = total_of_ratings / number_of_movies

print(f"{highest_rating_movie} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_score:.1f}")
