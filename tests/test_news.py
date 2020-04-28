import unittest
from  app.models import Source


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.new_news = Source(1,'CNN','Corona virus cases rises to 400','2020-04-24T14:37','William Sportsman','https://cdn.mos.cms.futurecdn.net/bfTp9yFjG7PTBKTMifd28m-1200-80.jpg','https://www.tomsguide.com/news/hurry-amazing-iphone-se-deal-is-just-dollar184-right-now')
    
