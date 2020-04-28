class Source:
    def __init__(self , id , name , description , pubishedAt, author, urlToImage, url):
        
        self.id = id
        self.name = name
        self.description = description
        self.pubishedAt = pubishedAt
        self.author = author
        self.urlToImage = urlToImage
        self.url = url


class Article:
    def __init__(self,id,title,content,name,url):
        self.id = id
        self.title = title
        self.content = content
        self.name = name
        self.url = url