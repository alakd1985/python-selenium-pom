Feature: MediShop continue shopping

  Scenario: Continue shopping from the shopping cart
    Given the user has Aspirin in the shopping cart
    When the user continues shopping
    Then the MediShop product page should be displayed
