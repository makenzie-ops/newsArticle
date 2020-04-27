class Article:
      '''
    News class to define News Objects
    '''

def __init__(self,id,title,overview,description ,poster,published_at,content):
    self.id = id
    self.title = title
    self.description  = description 
    self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
    self.published_at = published_at
    self.content = content


class Source:

    all_sources = []

    def __init__(self,news_id,title,imageurl,source):
        self.news_id = news_id
        self.title = title
        self.imageurl = imageurl
        self.source = source


    def save_source(self):
        Source.all_sources.append(self)


    @classmethod
    def clear_sources(cls):
        Source.all_sources.clear()

    @classmethod
    def get_sources(cls,id):

        response = []

        for source in cls.all_sources:
            if source.news_id == id:
                response.append(source)

        return response