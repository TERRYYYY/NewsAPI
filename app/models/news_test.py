import unnitest
from models import news
News = news.News

class NewsTest(unnitest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def SetUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1,'Citizen','Corona virus cases rises to 400','2020-04-24T14:37','Jeff Koinange','https://cdn.mos.cms.futurecdn.net/bfTp9yFjG7PTBKTMifd28m-1200-80.jpg','https://www.tomsguide.com/news/hurry-amazing-iphone-se-deal-is-just-dollar184-right-now')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

    if __name__ == '__main__':
        unnitest.main()