#!/usr/bin/env python
# _*_ coding: utf-8 _*_


from selenium import webdriver


# before feature
def before_all(context):
    context.driver = webdriver.Firefox()    

# after feature
def after_all(context):
    context.driver.quit()
