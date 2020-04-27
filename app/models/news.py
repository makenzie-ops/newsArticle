class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,id,title,overview,destcription ,poster,published_at,content):
        self.id = id
        self.title = title
        self.destcription  = destcription 
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.published_at = published_at
        self.content = content