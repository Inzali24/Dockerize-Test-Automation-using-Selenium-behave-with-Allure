from behave import given, when, then
import time
from pathlib import Path
import os


@given('the browser open html file')
def test_open_html(context):  
    # path = Path("answerfiles/circle_area.html")
    # filepath = os.path.join(path.parent.absolute(), 'circle_area.html')
    # f = open(filepath, "r")
    # print(f.read())
    context.HelperFunc.open('http://localhost:5000/answerfiles/circle_area.html')    
    context.HelperFunc.maximize()
    time.sleep(1)


@then('initial radius input should be cleared')
def test_no_input(context):
    radius = context.HelperFunc.find_by_id('inRadius').get_attribute('value')
    if len(radius) == 0:
        pass
    else:
        raise Exception("Initial display should be empty")


@when('fill the radius 8 and click the calculate button')
def test_input_click(context):
    context.HelperFunc.find_by_id('inRadius').send_keys("")
    context.HelperFunc.find_by_id('inRadius').send_keys("8")
    time.sleep(1)
    context.HelperFunc.find_by_id('btnCalculate').click()
    time.sleep(1)


@then('result of area of a circle should be 201.0619 appeared on the area output with 4 decimal places')
def test_answer(context):
    area = context.HelperFunc.find_by_id('inArea').get_attribute('value')
    if area == '201.0619':
        pass
    else:
        assert False, 'Area of Circle Calculation is wrong'
