Feature: Facebook Login

  Scenario Outline: Login to Facebook with valid credentials
    Given User opens facebook login page
    When I enter username "<username>" and password "<password>"
    Then Click on login button

    Examples:
      | username          | password     |
      | user1             | password123  |
      | user2             | password456  |
      | user3             | password23   |
