Feature: MediShop Order Details

  Scenario: Track an order after checkout
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Cash on delivery
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    And the order ID should be displayed
    When the user clicks Track order status
    Then the order tracking section should be displayed

  Scenario: Trigger invoice printing from order details
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Cash on delivery
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    And the order ID should be displayed
    When the user clicks Track order status
    And the user clicks Print invoice
    Then the invoice print action should be triggered

  Scenario: Open the cancel order dialog
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Cash on delivery
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    When the user clicks Track order status
    And the user opens the cancel order dialog
    Then the cancel order dialog should be displayed

  Scenario: Keep an order after opening cancellation dialog
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Cash on delivery
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    When the user clicks Track order status
    And the user opens the cancel order dialog
    And the user chooses to keep the order
    Then the cancel order dialog should close

  Scenario: Cancel an order with a selected reason
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Cash on delivery
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    When the user clicks Track order status
    And the user opens the cancel order dialog
    And the user selects cancellation reason "Ordered by mistake"
    And the user confirms the cancellation
    Then the order should be cancelled

   Scenario Outline: Cancel an order with a selected reason
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Cash on delivery
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    When the user clicks Track order status
    And the user opens the cancel order dialog
    And the user selects cancellation reason "<reason>"
    And the user confirms the cancellation
    Then the order should be cancelled
    And the cancellation message should contain "<reason>"

    Examples:
      | reason                  |
      | Ordered by mistake      |
      | Found a better price    |
      | Delivery takes too long |
      | Other                   |