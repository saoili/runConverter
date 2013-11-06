from selenium import webdriver

browser = webdriver.Firefox()

# Anita recently ran with some friends and was told that
# she ran 'a ten minute mile pace'. She normally thinks
# in kilometers per hour and wants to convert. Sorcha
# had told her about an app she was writing that did just that
# so she opened the app in a browser
browser.get('http://localhost:8000')

# she notices that the title of the webpage talks about running
# and converting
assert 'run' in browser.title
assert 'converter' in browser.title

# she sees a place to put in the minute mile value

# she enters the minute mile value and clicks a button or hits enter

# the website tells her how many kilometers per hour she ran