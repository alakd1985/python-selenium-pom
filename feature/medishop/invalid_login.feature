Feature: MediShop invalid login

  Scenario: Login with invalid credentials
    Given the user is on the MediShop login page
    When the user enters invalid login credentials
    And the user clicks the Sign In button
    Then the login should not be successful