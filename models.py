import json

class item:
    def __init__(self, title, genre, releaseDate):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        
    def __str__(self):
        return f"{self.title}({self.genre})({self.releaseDate})"
    
    def getTitle(self):
        return self.title
    
    def getGenre(self):
        return self.genre
    
    def getReleaseDate(self):
        return self.releaseDate

    
class book(item):
    def __init__(self, title, genre, releaseDate, author, publisher):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.author = author
        self.publisher = publisher
        
    def __str__(self):
        return f"{self.title}({self.genre})({self.releaseDate})({self.getAuthor()})({self.getPublisher()})"
        
    def getAuthor(self):
        return self.author
    
    def getPublisher(self):
        return self.publisher
    
class comic(book):
    def __init__(self, title, genre, releaseDate, author, publisher, artist):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.author = author
        self.publisher = publisher
        self.artist = artist
    
    def __str__(self):
        return f"{self.title}({self.genre})({self.releaseDate})({self.getAuthor()})({self.getPublisher()})({self.getArtist()})"

    def __repr__(self):
        return f"{self.title}({self.genre})({self.releaseDate})({self.getAuthor()})({self.getPublisher()})({self.getArtist()})"
    
    def getArtist(self):
        return self.artist
    
class movie(item):
    def __init__(self, title, genre, releaseDate, runtime, maturityRating, qualityRating, cast, director, producer):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.runtime = runtime
        self.maturityRating = maturityRating
        self.qualityRating = qualityRating
        self.cast = cast
        self.director = director
        self.producer = producer
        
    def getRuntime(self):
        return self.runtime
    def getMaturityRating(self):
        return self.maturityRating
    def getQualityRating(self):
        return self.qualityRating
    def getCast(self):
        return self.cast
    def getDirector(self):
        return self.director
    def getProducer(self):
        return self.producer
    
class show(movie):
    def __init__(self, title, genre, releaseDate, runtime, maturityRating, qualityRating, cast, director, producer, season, numEpisodes):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.runtime = runtime
        self.maturityRating = maturityRating
        self.qualityRating = qualityRating
        self.cast = cast
        self.director = director
        self.producer = producer
        self.season = season
        self.numEpisodes = numEpisodes
        
    def getSeason(self):
        return self.season
    def getNumEpisodes(self):
        return self.numEpisodes
    
class game(item):
    def __init__(self, title, genre, releaseDate, numPlayers, playingTime, publisher):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.numPlayers = numPlayers
        self.playingTime = playingTime
        self.publisher = publisher
        
    def getNumPlayers(self):
        return self.numPlayers
    def getPlayingTime(self):
        return self.playingTime
    def getPublisher(self):
        return self.publisher
    
class videoGame(game):
    def __init__(self, title, genre, releaseDate, numPlayers, playingTime, publisher, gameType, platform, esrbRating, qualityRating, cast, developer):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.numPlayers = numPlayers
        self.playingTime = playingTime
        self.publisher = publisher
        self.gameType = gameType
        self.platform = platform
        self.esrbRating = esrbRating
        self.qualityRating = qualityRating
        self.cast = cast
        self.developer = developer
        
    def getGameType(self):
        return self.gameType
    def getPlatform(self):
        return self.platform
    def getEsrbRating(self):
        return self.esrbRating
    def getQualityRating(self):
        return self.qualityRating
    def getCast(self):
        return self.cast
    def getDeveloper(self):
        return self.developer
    
class boardGame(game):
    def __init__(self, title, genre, releaseDate, numPlayers, playingTime, publisher, gameFormat, designer, artist):
        self.title = title
        self.genre = genre
        self.releaseDate = releaseDate
        self.numPlayers = numPlayers
        self.playingTime = playingTime
        self.publisher = publisher
        self.gameFormat = gameFormat
        self.designer = designer
        self.artist = artist

    def __str__(self):
        return f"{self.title}({self.genre})({self.releaseDate})({self.getNumPlayers()})({self.getPlayingTime()})({self.getPublisher()})({self.getGameFormat()})({self.getDesigner()})({self.getArtist()})"
        
    def getGameFormat(self):
        return self.gameFormat
    def getDesigner(self):
        return self.designer
    def getArtist(self):
        return self.artist
