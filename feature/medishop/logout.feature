Feature: MediShop logout

  Scenario: Logout from MediShop
    Given the user is logged into MediShop
    When the user logs out
    Then the user should be returned to the login page