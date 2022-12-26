Feature: Test Timer

Scenario:Timer
 Given Go to the Timer html file
 When Do not set minute and second and then click the start button
 Then Please set the time alert prompt should be appeared
 Then Special character and alphabet input are not allowed in min and sec
 When I input 3 sec and click start button
 Then Start Button becomes disabled
 Then if time completed, Times up alert should be appeared
 Then Start button becomes enabled after time complete message
 When I input 10sec and then click start button
 When I paused at after 2 sec and it should be shown as 8 sec
 Then Stop Timer and it should be cleared or shown as 0
 Then Start button becomes enabled after stop timer
 When I input -2 min and 1001 sec
 Then Please set the time from 0 to 1000 alert prompt should be appeared