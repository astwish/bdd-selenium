#! /usr/bin/env python
# _*_ coding: utf-8 _*_


from behave import *


@given('I am on home page')
def step_i_am_on_home_page(context):
    context.driver.get("http://demo.magentocommerce.com/")

@when(u'I search for {text}')
def step_i_search_for(context, text):
    search.field = context.driver.find_element_by_name("q")
    search.field.clear()

    # enter search keyword and submit
    search.field.send_keys(text)
    search.field.submit()

@then('I should see list of matching products in search results')
def step_i_should_see_list(context):
    products = context.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
    # check results
    assert len(products) > 0
