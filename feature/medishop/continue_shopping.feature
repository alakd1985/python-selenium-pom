Feature: MediShop continue shopping

  Scenario: Continue shopping from the shopping cart
    Given the user has Aspirin in the shopping cart
    When the user continues shopping
    Then the MediShop product page should be displayed

  Scenario: Preserve the cart product after continuing shopping
    Given the user has Aspirin in the shopping cart
    When the user continues shopping
    And the user opens the shopping cart
    Then the shopping cart should contain "Aspirin"

  Scenario: Preserve cart quantity after continuing shopping
    Given the user has two Aspirin in the shopping cart
    When the user continues shopping
    Then the MediShop product page should be displayed
    When the user opens the shopping cart
    Then the product quantity should be "2"