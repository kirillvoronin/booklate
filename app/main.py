import time
import json

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/usr/local/bin/chromedriver")

browser.get("https://bookmate.com/books/AAWMSh89/impressions")

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 0

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns -= 1

emodjidata = []

cards = browser.find_elements_by_class_name("card_default")
counter = 1
for each in cards:

    author = each.find_elements_by_xpath("./div[1]/span[1]/a[1]")
    emojies = each.find_elements_by_xpath("./div[2]/div[1]/div")
    text = each.find_elements_by_xpath("./div[2]//p")

    emoji_list = []

    for k in emojies:
        emoji_list.append(k.text)

    data = {
        "id": counter,
        "author": author[0].text,
        "emojies": emoji_list,
        "text": text[0].text
    }
    counter += 1

    emodjidata.append(data)

print(json.dumps(emodjidata, sort_keys=True, indent=4, ensure_ascii=False))
