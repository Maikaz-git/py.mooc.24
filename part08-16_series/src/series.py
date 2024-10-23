# Write your solution here:
class Series:

    def __init__(self, name:str, seasons:int, genre:list):

        self.name = name
        self.seasons = seasons
        self.genre = genre
        self.rating = []
        self.title = name

        
    def rate(self, rating:int):
        self.rating.append(rating)

    
    
    def __str__(self):
        genre_str = ", ".join(self.genre)
        if len(self.rating) != 0:
            ratings = len(self.rating)
            average = sum(self.rating) / len(self.rating)
            return f" {self.name} ({self.seasons} seasons)\n genres: {genre_str} \n {ratings} ratings, average {average:.1f} points"

        else:
            return f" {self.name} ({self.seasons} seasons)\n genres: {genre_str} \n no ratings"

def minimum_grade(rating: float, series_list: list):
    lst = []
    for series in series_list:
        for rate in series.rating:
            if rating <= rate:
                lst.append(series) 
    return lst

def includes_genre(genre: str, series_list: list) :
    lst = []
    for series in series_list:
        for gen in series.genre:
            if gen == genre:
                lst.append(series)
    return lst

if __name__=="__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)