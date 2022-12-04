Feature: Test image

Scenario: image
  Given Go to the image html file
  When Click Capture button
  Then Image Should be appeared on the right Canvas
  When Click Flip button
  Then Right Canvas image should be flipped horizontally
  When Click zoom in button, image should be zoomed in
  When Click zoom out button,image should be zoomed out


