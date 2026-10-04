Feature: MediShop checkout validation

  Scenario: Checkout with missing required information
    Given the user has Aspirin in the shopping cart
    When the user opens the checkout page
    And the user attempts to place the order without delivery information
    Then the checkout should not be completed