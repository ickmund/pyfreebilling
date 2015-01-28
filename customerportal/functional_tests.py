from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'PyFreeBilling' in browser.title

vdisplay.stop()