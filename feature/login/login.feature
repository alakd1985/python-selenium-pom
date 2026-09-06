Feature: OrangeHRM Login

  As an OrangeHRM user
  I want to log in with valid or invalid credentials
  So that I can verify the login functionality


  Background:
    Given the user is on the OrangeHRM login page


  @smoke @positive
  Scenario: Successful login with valid credentials
    When the user logs in with valid credentials
    Then the Dashboard should be displayed


  @negative
  Scenario Outline: Login with invalid credentials

    When the user logs in with username "<username>" and password "<password>"
    Then the invalid credentials message should be displayed

    Examples:
      | username | password  |
      | Admin1   | admin123  |
      | Admin    | admin1234 |
      | Admin1   | admin1234 |


  @validation
  Scenario: Login with empty username and password
    When the user clicks the Login button without entering credentials
    Then the required field message should be displayed