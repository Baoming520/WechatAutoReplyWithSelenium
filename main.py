#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import json
import time

def main(argv=None):
  # Read config file
  with open('./config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

  # Load Chrome drive
  wd = webdriver.Chrome(config['web_drive_path'])
  wd.get('https://wx.qq.com/')

  contacts = wd.find_elements_by_xpath('//div[@ng-repeat="chatContact in chatList track by chatContact.UserName"]/div[@class="chat_item slide-left ng-scope top"]')
  nk_names = wd.find_elements_by_xpath('//div[@ng-repeat="chatContact in chatList track by chatContact.UserName"]/div[@class="chat_item slide-left ng-scope top"]/div[@class="info"]/h3[@class="nickname"]')
  index = 0
  for nk_n in nk_names:
    if nk_n.text == config['senders'][1]['nickname']:
      contacts[index].click()
      break

    index += 1
  
  # Process the specified sender's message.
  # loop = 5
  while True:
    u_elems = wd.find_elements_by_xpath('//div[@class="message ng-scope you"]/img[@class="avatar"]')
    m_elems = wd.find_elements_by_xpath('//div[@class="message ng-scope you"]/div[@class="content"]/div[@class="bubble js_message_bubble ng-scope bubble_default left"]/div[@class="bubble_cont ng-scope"]/div[@class="plain"]')
    if len(u_elems) > 0:
      uname = u_elems[len(u_elems) - 1].get_attribute('title')
      messg = m_elems[len(m_elems) - 1].text
      print('{}: {}'.format(uname, messg))

    time.sleep(3)
    # loop -= 1

  wd.execute_script('window.alert("Enjoy to use Selenium to do everything!")')
  
if __name__ == '__main__':
  main()
