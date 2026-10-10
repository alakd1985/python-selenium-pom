Feature: MediShop payment methods

  Scenario: Open Payment methods from Home
    Given the user is logged into MediShop
    When the user opens Payment methods
    Then the Payment methods page should be displayed

  Scenario: Open Add payment method modal
    Given the user is logged into MediShop
    When the user opens Payment methods
    And the user opens Add payment method
    Then the Add payment method modal should be displayed
