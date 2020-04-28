class Source:
    def __init__(self , id , title , description , pubished_at, author, urlToImage, url):
        
        self.id = id
        self.title = title
        self.description = description
        self.pubished_at = pubished_at
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