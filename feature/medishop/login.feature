Feature: MediShop Login

  Scenario: Login with valid demo credentials

    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
