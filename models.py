
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
        super().__init__(title, genre, releaseDate)
        self.author = author
        self.publisher = publisher
        
    def getAuthor(self):
        return self.author
    
    def getPublisher(self):
        return self.publisher
    

    
class comic(book):
    def __init__(self, title, genre, releaseDate, author, publisher, artist):
        super().__init__(title, genre, releaseDate, author, publisher)
        self.artist = artist
        
    def getArtist(self):
        return self.artist
    
'''
class movie(item):
    def __init__(self, title, genre, releaseDate, runtime, maturityRating, qualityRating, cast, director, producer):
        super().__init__(title, genre, releaseDate)
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
        super().__init__(title, genre, releaseDate, runtime, maturityRating, qualityRating, cast, director, producer)
        self.season = season
        self.numEpisodes = numEpisodes
        
    def getSeason(self):
        return self.season
    def getNumEpisodes(self):
        return self.numEpisodes
    
class game(item):
    def __init__(self, title, genre, releaseDate, numPlayers, playingTime, publisher):
        super().__init__(title, genre, releaseDate)
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
        super().__init__(title, genre, releaseDate, numPlayers, playingTime, publisher)
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
        super().__init__(title, genre, releaseDate, numPlayers, playingTime, publisher)
        self.gameFormat = gameFormat
        self.designer = designer
        self.artist = artist
        
    def getGameFormat(self):
        return self.gameFormat
    def getDesigner(self):
        return self.designer
    def getArtist(self):
        return self.artist

'''