from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from resources import PARENT_LIST, SQUARES_LIST
import time


class GameBot:
     
    def __init__(self,driver = webdriver.Firefox()):
        self.driver = driver
    def get_to_site(self):
        self.driver.get('https://hczhcz.github.io/2048/20ez/')

    @classmethod
    def get_driver(cls):
        return cls()

'''
class Tile(GameBot):

    def get_title(self):
        self.title = self.driver.find_element_by_css_selector('h1.title').text
        print(self.title)
'''

Game = GameBot()
Game.get_to_site()
MAX = -1

while(True):
    GAME_BOARD = {'position-1-1':{'value':None,'col':1,'row':1},
    'position-1-2':{'value':None,'col':1,'row':2},
    'position-1-3':{'value':None,'col':1,'row':3},
    'position-1-4':{'value':None,'col':1,'row':4},
    'position-2-1':{'value':None,'col':2,'row':1},
    'position-2-2':{'value':None,'col':2,'row':2},
    'position-2-3':{'value':None,'col':2,'row':3},
    'position-2-4':{'value':None,'col':2,'row':4},
    'position-3-1':{'value':None,'col':3,'row':1},
    'position-3-2':{'value':None,'col':3,'row':2},
    'position-3-3':{'value':None,'col':3,'row':3},
    'position-3-4':{'value':None,'col':3,'row':4},
    'position-4-1':{'value':None,'col':4,'row':1},
    'position-4-2':{'value':None,'col':4,'row':2},
    'position-4-3':{'value':None,'col':4,'row':3},
    'position-4-4':{'value':None,'col':4,'row':4} }
    SQUARES_LIST = Game.driver.find_elements_by_css_selector('div.tile-inner')
    body = Game.driver.find_element_by_css_selector('body')
    for item in SQUARES_LIST:
        classname = item.find_element_by_xpath('..').get_attribute('class')
        value = item.text
        position = classname[(17+len(str(value))-1):(29+len(str(value))-1)]
        #col = classname[26]
        #SQUARES_LIST[position]['col'] = col
    # row = classname[28]
    # SQUARES_LIST[position]['row'] = row
        GAME_BOARD.update({position : {'value':int(value)}})
        MAX = max(MAX,int(value)) 
    if GAME_BOARD['position-4-4']['value'] == None :
        for index in range (1,4):
            if GAME_BOARD['position-4-{}'.format(str(index))]['value'] == MAX :
                print('down')
                body.send_keys(Keys.DOWN)
            elif GAME_BOARD['position-{}-4'.format(str(index))]['value'] == MAX :
                print('right')
                body.send_keys(Keys.RIGHT)
            else:
                body.send_keys(Keys.RIGHT)
                body.send_keys(Keys.DOWN)


    else:
        body.send_keys(Keys.RIGHT)
        body.send_keys(Keys.DOWN)
        
            




