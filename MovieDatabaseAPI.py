from flask import Flask, request, jsonify

app = Flask(__name__)

class Movie():
    def __init__(self, movieID, movieTitle, movieGenre, movieReleaseYear):
        self.movieID = movieID
        self.movieTitle = movieTitle
        self.movieGenre = movieGenre
        self.movieReleaseYear = movieReleaseYear
    
    def update_Movie(self, updatedMovie):
        self.movieID = updatedMovie.get("UpdatedMovieID", self.movieID)
        self.movieTitle = updatedMovie.get("UpdatedMovieTitle", self.movieTitle)
        self.movieGenre = updatedMovie.get("UpdatedMovieGenre", self.movieGenre)
        self.movieReleaseYear = updatedMovie.get("UpdatedMovieReleaseYear", self.movieReleaseYear)

    def __str__(self):
        return f"Title: {self.movieID} {self.movieTitle}, Genre: {self.movieGenre}, Release Year: {self.movieReleaseYear}"

movieList = []

@app.route('/movies', methods= ['POST'])
def addMovies():
    data = request.get_json()
    movieId = data.get("MovieID")
    movieTitle = data.get("MovieTitle")
    movieGenre = data.get("MovieGenre")
    movieReleaseYear = data.get("MovieReleaseYear")
    for movie in movieList:
        if movie.movieID == movieId:
            return f"This ID already exists, please choose a unique one."
    
    movie1 = Movie(movieID=movieId, movieTitle=movieTitle, movieGenre=movieGenre, movieReleaseYear=movieReleaseYear)
    movieList.append(movie1)
    return "Movie Added to the List"

@app.route('/movies', methods= ['GET'])
def getListOfMovies():
    movies_json = [movie.__dict__ for movie in movieList]
    return jsonify({'movies': movies_json})

@app.route('/movies/<int:movie_ID>', methods= ['GET'])
def getMovieByID(movie_ID):
    for movie in movieList:
        if movie.movieID == movie_ID:
            return f" Title: {movie.movieTitle}, Genre: {movie.movieGenre}, Release Year: {movie.movieReleaseYear}"
    return "This ID doesn't exist."

@app.route('/movies/<int:movie_ID>', methods= ['PUT'])
def updateMovie(movie_ID):
    data = request.get_json()
    for movie in movieList:
        if movie.movieID == movie_ID:
            movie.update_Movie(data)
            return f"Movie Updated"
    return f"Movie doesn't exist"

@app.route('/movies/<int:movie_ID>', methods = ['DELETE'])
def deleteMovie(movie_ID):
    for movie in movieList:
        if movie.movieID == movie_ID:
            movieList.remove(movie)
            return jsonify(movie.__dict__)
    return f"Movie Not Found"

class Actor():
    def __init__(self, actorID, actorName, dateOfBirth, otherDetails):
        self.actorID = actorID
        self.actorName = actorName
        self.dateOfBirth = dateOfBirth
        self.otherDetails = otherDetails

    def update_actor(self, updated_actor):
        self.actorName = updated_actor.get("UpdatedActorName", self.actorName)
        self.dateOfBirth = updated_actor.get("UpdatedDateOfBirth", self.dateOfBirth)
        self.otherDetails = updated_actor.get("UpdatedOtherDetails", self.otherDetails)

    def __str__(self):
        return f"ID: {self.actorID}, Name: {self.actorName}, Date of Birth: {self.dateOfBirth}, Other Details: {self.otherDetails}"
            
actorList = []

@app.route('/actors', methods = ['GET'])
def getListOfActors():
    actors_json = [actor.__dict__ for actor in actorList]
    return jsonify({'actors' : actors_json})

@app.route('/actors/<int:actor_ID>', methods = ['GET'])
def getActorByID(actor_ID):
    for actor in actorList:
        if actor.actorID == actor_ID:
            return f" Name: {actor.actorName}, Date of Birth: {actor.dateOfBirth}, Other Details: {actor.otherDetails}"
    return f"Actor hasn't been added."

@app.route('/actors', methods = ['POST'])
def addActor():
    data = request.get_json()
    actorID = data.get("ActorID")
    actorName  = data.get("ActorName")
    actorDOB = data.get("ActorDOB")
    actorDeets = data.get("ActorDetails")
    for actor in actorList:
        if actor.actorID == actorID:
            return f"This ActorID already exists, choose a unique one."
    actor1 = Actor(actorID=actorID, actorName=actorName, dateOfBirth=actorDOB, otherDetails=actorDeets)
    actorList.append(actor1)
    return f"Actor Added!"

@app.route('/actors/<int:actor_ID>', methods = ['PUT'])
def updateActor(actor_ID):
    data = request.get_json()
    for actor in actorList:
        if actor.actorID == actor_ID:
            actor.update_actor(data)
            return f"Actor Updated"
    return f"Actor ID is wrong."

@app.route('/actors/<int:actor_ID>', methods = ['DELETE'])
def deleteActor(actor_ID):
    for actor in actorList:
        if actor.actorID == actor_ID:
            actorList.remove(actor)
            return jsonify(actor.__dict__)
    return f"Actor Not Found"

if __name__ == "__main__":
    app.run(debug=True)
