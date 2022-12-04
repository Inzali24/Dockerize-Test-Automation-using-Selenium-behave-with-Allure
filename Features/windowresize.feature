Feature: Window Resizing
Scenario: Window width and height
  Given the browser open html file with system defined width and height
  Then the current width and height of the window is shown
  When browser is maximized, the changed size of the window width and height is shown.