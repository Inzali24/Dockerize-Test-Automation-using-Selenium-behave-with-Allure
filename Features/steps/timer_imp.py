from behave import given, when, then
import time
from pathlib import Path
import os
from selenium.common.exceptions import TimeoutException


@given('Go to the Timer html file')
def step(context):
    # path = Path("answerfiles/timer.html")
    # filepath = os.path.join(path.parent.absolute(), 'timer.html')
    context.HelperFunc.open('http://localhost:5000/answerfiles/timer.html')
    context.HelperFunc.maximize()


@when('Do not set minute and second and then click the start button')
def test_no_input(context):
    context.HelperFunc.find_by_id('min').send_keys("")
    context.HelperFunc.find_by_id('sec').send_keys("")
    context.HelperFunc.find_by_id('btnStart').click()


@then('Please set the time alert prompt should be appeared')
def test_no_input_alert(context):
    try:
        context.HelperFunc.wait_until()
        alert = context.HelperFunc.switch_to()
        alert.accept()
    except TimeoutException:
        raise Exception("There is no input error alert!")


@then('Special character and alphabet input are not allowed in min and sec')
def test_number_only(context):
    l = context.HelperFunc.find_by_id('min')
    l.send_keys('Abc@#&')
    typedValue = l.get_attribute('value')
    if typedValue.isnumeric():
        pass
    else:
        raise Exception("Alphabets are not allowed")


@when('I input 3 sec and click start button')
def test_input_timer(context):
    context.HelperFunc.find_by_id('sec').send_keys('3')
    context.HelperFunc.find_by_id('btnStart').click()


@then('Start Button becomes disabled')
def test_disable_button(context):
    time.sleep(1)
    startTestDisEnable = context.HelperFunc.find_by_id('btnStart')
    if startTestDisEnable.get_property('disabled'):
        pass
    else:
        raise Exception("Start Button should be disabled")


@then('if time completed, Times up alert should be appeared')
def test_finished_alert(context):
    try:
        time.sleep(3)
        context.HelperFunc.wait_until()
        alert = context.HelperFunc.switch_to()
        alert.accept()                
    except TimeoutException:
        raise Exception('There is no finished timer alert Message!')


@then('Start button becomes enabled after time complete message')
def test_enable_button1(context):    
    startTestEnable = context.HelperFunc.find_by_id('btnStart')
    time.sleep(1)    
    if startTestEnable.get_property('disabled'): 
        raise Exception("Start Button should be enabled") 


@when('I input 10sec and then click start button')
def test_input_timer(context):
    time.sleep(1)
    context.HelperFunc.find_by_id('sec').send_keys('10')
    context.HelperFunc.find_by_id('btnStart').click()


@when('I paused at after 2 sec and it should be shown as 8 sec')
def test_paused_button(context):
    time.sleep(2)
    context.HelperFunc.find_by_id('btnPause').click()
    sec = context.HelperFunc.find_by_id('sec').get_attribute('value')
    if sec == '8':
        pass
    else:
        raise Exception("Timer Counting Error.")


@then('Stop Timer and it should be cleared or shown as 0')
def test_stop_button(context):
    time.sleep(2)
    context.HelperFunc.find_by_id('btnStop').click()
    sec = context.HelperFunc.find_by_id('sec').get_attribute('value')
    if sec == '' or sec == '0':
        pass
    else:
        raise Exception("Timer Counting Error.")


@then('Start button becomes enabled after stop timer')
def test_enable_button(context):    
    startTestEnable = context.HelperFunc.find_by_id('btnStart')
    time.sleep(1)    
    if startTestEnable.get_property('disabled'): 
        raise Exception("Start Button should be enabled")


@when('I input -2 min and 1001 sec')
def test_time_interval(context):
    context.HelperFunc.find_by_id('min').send_keys('-2')
    context.HelperFunc.find_by_id('sec').send_keys('1001')
    context.HelperFunc.find_by_id('btnStart').click()


@then('Please set the time from 0 to 1000 alert prompt should be appeared')
def test_time_range_alert(context):
    try:
        time.sleep(2)
        context.HelperFunc.wait_until()
        alert = context.HelperFunc.switch_to()
        alert.accept()
        pass
    except TimeoutException:
        print("No time range alert Error")
