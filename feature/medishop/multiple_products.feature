Feature: MediShop multiple products in shopping cart

  Scenario: Add multiple products to the shopping cart
    Given the user is logged into MediShop
    When the user searches for "Aspirin"
    And the user adds the product to the cart
    And the user searches for "Vitamin C"
    And the user adds the product to the cart
    Then the shopping cart should contain "Aspirin"
    And the shopping cart should contain "Vitamin C"
