Feature: MediShop cart quantity management

  Scenario: Increase product quantity in the shopping cart
    Given the user has Aspirin in the shopping cart
    When the user increases the product quantity
    Then the product quantity should be "2"

  Scenario: Decrease product quantity in the shopping cart
    Given the user has two Aspirin in the shopping cart
    When the user decreases the product quantity
    Then the product quantity should be "1"
