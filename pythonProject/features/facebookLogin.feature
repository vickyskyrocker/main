Feature: Validate Facebook

  Scenario: validate facebook login
    Given User opens facebook login page
    When Enter Username and Password in login page
    Then Click on login button
    Then validate the button is clicked