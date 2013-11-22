from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_convert_from_one_to_another(self):
        # Anita recently ran with some friends and was told that
        # she ran 'a ten minute mile pace'. She normally thinks
        # in kilometers per hour and wants to convert. Sorcha
        # had told her about an app she was writing that did just that
        # so she opened the app in a browser
        self.browser.get('http://localhost:8000/runConverterApp')

        # she notices that the title of the webpage talks about running
        # and converting
        self.assertIn ('run', self.browser.title)
        self.assertIn ('convert', self.browser.title)
        self.fail('Finish the test!')
        
        # she sees a place to put in the minute mile value

        # she enters the minute mile value and clicks a button or hits enter

        # the website tells her how many kilometers per hour she ran
        
if __name__ == '__main__':
    unittest.main()