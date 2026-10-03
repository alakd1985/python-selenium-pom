Feature: MediShop Checkout

  Scenario: Complete checkout using Cash on delivery

    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed

    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Cash on delivery
    Then the user clicks Place order