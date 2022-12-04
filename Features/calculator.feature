Feature: Test Calculator Functionality

Scenario:Calculator
 Given Go to the Calculator html file
 Then There should be no answer (input text id= txtResult)
 When I input "2" and "3" to calculator to add
 Then I get addition result "5"
  Then I cleared the text
 When I input "5" and "3" to calculator to subtract
 Then I get subtraction result "2"
  Then I cleared the text
 When I input "2" and "4" to calculator to multiply
 Then I get multiply result "8"
  Then I cleared the text
 When I input "6.8" and "4" to calculator to divide
 Then I get division result "1.7"