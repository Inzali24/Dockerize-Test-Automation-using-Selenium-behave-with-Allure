from behave import given, when, then
import time


@given('the browser open html file with system defined width and height')
def step(context):
    # path = Path("answerfiles/windowresize.html")
    # filepath = os.path.join(path.parent.absolute(), 'windowresize.html')
    context.HelperFunc.open('http://localhost:5000/answerfiles/windowresize.html')
    time.sleep(2)


@then('the current width and height of the window is shown')
def test_no_input(context):
    width = context.HelperFunc.find_by_id('windowWidth').text
    height = context.HelperFunc.find_by_id('windowHeight').text
    print(width, height)
    if width == "780" and height == "480":
        pass
    else:
       assert False, "Window Width and height is wrong"


@when('browser is maximized, the changed size of the window width and height is shown.')
def test_input_click(context):
    context.HelperFunc.set_window_size()
    width = context.HelperFunc.find_by_id('windowWidth').text
    height = context.HelperFunc.find_by_id('windowHeight').text
    print(width, height)
    if width == "1536" and height == "714":
        pass
    else:
         assert False, "Maximized Window Width and height is wrong"
