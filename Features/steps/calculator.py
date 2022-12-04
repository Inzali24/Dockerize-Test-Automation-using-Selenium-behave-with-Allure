from behave import given, when, then


@given('Go to the Calculator html file')
def step(context):    
    context.HelperFunc.open('http://localhost:5000/answerfiles/calculator.html')
    context.HelperFunc.maximize()


@then('There should be no answer (input text id= txtResult)')
def no_input_test(context):
    text = context.HelperFunc.find_by_id('txtResult').get_attribute('value')


@when('I input "2" and "3" to calculator to add')
def test_sum_input(context):
    context.HelperFunc.find_by_id('btn2').click()
    context.HelperFunc.find_by_id('btnPlus').click()
    context.HelperFunc.find_by_id('btn3').click()
    context.HelperFunc.find_by_id('btnEqual').click()


@then('I get addition result "{x}"')
def test_sum_output(context, x):
    ans = context.HelperFunc.find_by_id('txtResult').get_attribute('value')
    print("addition {}".format(ans))
    if ans == x:
        print('Then I get right result "{}", "{}"'.format(ans, x))
        pass
    else:
        raise Exception("Invalid sum result is returned.")


@then('I cleared the text')
def clear(context):
    context.HelperFunc.find_by_id('btnClr').click()


@when('I input "5" and "3" to calculator to subtract')
def test_subtract_input(context):
    context.HelperFunc.find_by_id('btn5').click()
    context.HelperFunc.find_by_id('btnMinus').click()
    context.HelperFunc.find_by_id('btn3').click()
    context.HelperFunc.find_by_id('btnEqual').click()


@then('I get subtraction result "{y}"')
def test_subtract_output(context, y):
    ans = context.HelperFunc.find_by_id('txtResult').get_attribute('value')
    print("subtraction {}".format(ans))
    if ans == y:
        print('Then I get right result "{}", "{}"'.format(ans, y))
        pass
    else:
        raise Exception("Invalid subtraction result is returned.")


@when('I input "2" and "4" to calculator to multiply')
def test_multiply_input(context):
    context.HelperFunc.find_by_id('btn2').click()
    context.HelperFunc.find_by_id('btnMultiply').click()
    context.HelperFunc.find_by_id('btn4').click()
    context.HelperFunc.find_by_id('btnEqual').click()


@then('I get multiply result "{y}"')
def test_multiply_output(context, y):
    ans = context.HelperFunc.find_by_id('txtResult').get_attribute('value')
    print("subtraction {}".format(ans))
    if ans == y:
        print('Then I get right result "{}", "{}"'.format(ans, y))
        pass
    else:
        raise Exception("Invalid multiplication result is returned.")


@when('I input "6.8" and "4" to calculator to divide')
def test_division_input(context):
    context.HelperFunc.find_by_id('btn6').click()
    context.HelperFunc.find_by_id('btnDot').click()
    context.HelperFunc.find_by_id('btn8').click()
    context.HelperFunc.find_by_id('btnDivide').click()
    context.HelperFunc.find_by_id('btn4').click()
    context.HelperFunc.find_by_id('btnEqual').click()


@then('I get division result "{y}"')
def test_division_output(context, y):
    ans = context.HelperFunc.find_by_id('txtResult').get_attribute('value')
    print("subtraction {}".format(ans))
    if ans == y:
        print('Then I get right result "{}", "{}"'.format(ans, y))
        pass
    else:
        raise Exception("Invalid division result is returned.")