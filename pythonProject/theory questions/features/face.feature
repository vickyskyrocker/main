Feature: Validate Facebook

  Scenario Outline: validate facebook login
    Given User opens facebook login page
    When Enter username "<Username>" and password "<Password>" in login page
    Then Click on login button
    Examples:
      | Username  | Password |
      | admin     | admin123 |
      | admin123  | admin345 |
      | admin345  | admin567 |
      | admin567  | admin    |