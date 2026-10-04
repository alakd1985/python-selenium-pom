Feature: MediShop shopping cart

  Scenario: Add a product to the shopping cart
    Given the user is logged into MediShop
    When the user searches for "Aspirin"
    And the user adds the product to the cart
   Then the shopping cart should contain "Aspirin"

  Scenario: Remove a product from the shopping cart
    Given the user has Aspirin in the shopping cart
    When the user removes the product from the shopping cart
    Then the shopping cart should be empty