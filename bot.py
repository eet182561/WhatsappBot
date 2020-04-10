'''
This is a python whatsapp bot.
Will soon convert it into and API
'''

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Whatsapp:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://web.whatsapp.com')
        self.chat_open = False
        print('Please Scan the QR Code and press enter')
        input()
    

    def open_chat(self,name):
        chat = self.browser.find_element_by_xpath('//*[@title="'+name+'"]')
        self.chat_open = True
        chat.click()
    
    def send_message_with_open_chat(self,message):
        message_box = self.browser.find_element_by_xpath('//*[@data-tab="1"]')
        message_box.send_keys(message+'\n\r')

    def send_message(self,name=None,message=None):
        if name is None and self.chat_open==True:
            if message == None:
                self.send_message_with_open_chat("Hello")
            else:
                self.send_message_with_open_chat(message)
        elif not name==None:
            self.open_chat(name)
            if message == None:
                self.send_message_with_open_chat("Hello")
            else:
                self.send_message_with_open_chat(message)
        else:
            print('Please specify the sender. No chat open.')
