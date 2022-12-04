from behave import given, when, then
import time
import imagehash
from PIL import Image, ImageOps
from pathlib import Path
import os


def save_photo(driver, photoname):
    with open('{0}.png'.format(photoname), 'wb') as file:
        photo = driver.HelperFunc.find_by_id('CANVAS')
        # write file
        file.write(photo.screenshot_as_png)


@given('Go to the image html file')
def step(context):
    # path = Path("answerfiles/captureimage.html")
    # filepath = os.path.join(path.parent.absolute(), 'captureimage.html')
    context.HelperFunc.open('http://localhost:5000/answerfiles/captureimage.html')
    context.HelperFunc.maximize()


@when('Click Capture button')
def test_capture(context):
    time.sleep(2)
    context.HelperFunc.find_by_id("btnIdCapture").click()
    time.sleep(2)


@then('Image Should be appeared on the right Canvas')
def test_capture_image(context):
    save_photo(context, 'BeforeMirror')  # 反転する前に写真を保存
    time.sleep(2)


@when('Click Flip button')
def test_flip_button(context):
    context.HelperFunc.find_by_id("btnIdMirror").click()
    time.sleep(2)


@then('Right Canvas image should be flipped horizontally')
def test_flipped_image(context):
    save_photo(context, 'AfterMirror')  # 反転する後に写真を保存
    time.sleep(2)
    img = Image.open('AfterMirror.png')
    img_before_match = ImageOps.mirror(img)
    img_before_match.save('Img_Before_Mirror.png')
    hash0 = imagehash.average_hash(Image.open('BeforeMirror.png'))
    hash1 = imagehash.average_hash(Image.open('Img_Before_Mirror.png'))
    cutoff = 10  # maximum bits that could be different between the hashes.
    print(hash0)
    print(hash1)
    print(hash0-hash1)
    if hash0 - hash1 < cutoff:
        print('images are similar')
        pass
    else:
        raise Exception('images are not similar')


@when('Click zoom in button, image should be zoomed in')
def test_zoom_in(context):
    canvas_width1 = context.HelperFunc.execute_script('return arguments[0].width', 'CANVAS')
    print('CanvasWidth1 : ', canvas_width1)
    context.HelperFunc.find_by_id('btnIdZin').click()
    time.sleep(3)
    canvas_width2 = context.HelperFunc.execute_script('return arguments[0].style.width', 'CANVAS')
    zoomed_canvas = int(canvas_width2[0:3])
    print('ZoomWidth2 : ', zoomed_canvas)
    if zoomed_canvas > canvas_width1:
        pass
    else:
        raise Exception('Zoom in does not work')


@when('Click zoom out button,image should be zoomed out')
def test_zoom_out(context):
    canvas_width1 = context.HelperFunc.execute_script('return arguments[0].style.width', 'CANVAS')
    zoomed_canvas1 = int(canvas_width1[0:3])
    print('cCanvasWidth1 : ', canvas_width1)
    context.HelperFunc.find_by_id('btnIdZout').click()
    time.sleep(3)
    canvas_width2 = context.HelperFunc.execute_script('return arguments[0].style.width', 'CANVAS')
    zoomed_canvas2 = int(canvas_width2[0:3])
    print('ZoomWidth2 : ', zoomed_canvas2)
    if zoomed_canvas2 < zoomed_canvas1:
        pass
    else:
        raise Exception('Zoom out does not work')
