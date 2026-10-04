Feature: MediShop clear shopping cart

  Scenario: Clear all products from the shopping cart
    Given the user has Aspirin in the shopping cart
    When the user clears the shopping cart
    Then the shopping cart should be empty
