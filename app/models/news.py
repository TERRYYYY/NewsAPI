class News:
    '''
    News class to define News object
    '''
    def __init__(self,id,name,description,publishedAt,author,urlToImage,url):
        self.id=id
        self.name=name
        self.description=description
        self.publishedAt=publishedAt
        self.author=author
        self.urlToImage=urlToImage
        self.url=url