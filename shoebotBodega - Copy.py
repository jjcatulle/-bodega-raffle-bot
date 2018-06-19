#Bodega raffle Bot
#by: Jean Catulle
#inspiration from cookgroup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#the script above import packages and the modules
# I'm using chrome browser
driver= webdriver.Chrome()

#opening bodegas website
driver.get('http://m.gvwy.io/?scale=0.5752&raflid=ed6d063a225&template=589a49826af78dce0b03dc33&previous_url=https%3A%2F%2Fshop.bdgastore.com%2Fblogs%2Fupcoming-releases%2F6-19-18-off-white-air-jordan-1-x-off-white-unc&referrer=https%3A%2F%2Fshop.bdgastore.com%2Fblogs%2Fupcoming-releases')

#adding a pause to let the page load
driver.implicitly_wait(10) # seconds

#locating 'use my email' button then clicking on it
signup_button = driver.find_element_by_link_text('Use Your Email')
signup_button.click()

#locate 'name' box
name_box = driver.find_element_by_name('Name')
# Send Name
name_box.send_keys('jean catulle') #add your
# Find 'email' box
email_box = driver.find_element_by_name('Email')
# Send Email
email_box.send_keys('catullej@wit.edu') #add your email
#find the login button and click it
login_box = driver.find_element_by_name('Login')
login_box.click()
#pick sizes
sizes_hover = driver.find_element_by_class('entry-option incomplete visible-parent')
sizes_hover.click()
size_us = driver.find_element_by_name('extra')
size_us.send_keys('8') #US sizes pick 7-14
#press the send entry
enter_draw =  driver.find_element_by_class('btn submit-link-custom')
eneter_draw.click()
#alright guys above we pick our size and enter 5 submition
#Part 2
#signup for news letter for extra entries
news_mail = diver.find_element_by_class('title entry-option-title-emlist')
news_mai.click()
confirm_button = driver.find_element_by_name('confirm')
confirm_button.click()
enter_button = driver.find_element_by_class('submit-link mode-emlist')
enter_button.click()
# above is another 5 entries
#To Do List
#create a loop
#REVIew each line
#make the code more efficient
#finish asap)

                    #SHOEBOTCHAT 2018 by Jean Catulle
