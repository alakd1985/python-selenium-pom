Feature: MediShop Checkout

  Scenario: Select Credit / debit card as payment method
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user enters the checkout delivery information
    And the user selects Credit / debit card
    And the user enters the card number
    And the user enters the card expiry date
    And the user enters the card CVV
    And the user enters the name on card
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    And the order ID should be displayed
    And the payment method should be Credit / Debit Card

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
    And the user accepts the terms and conditions
    And the user clicks Place order
    Then the order confirmation should be displayed
    And the order ID should be displayed
    And the payment method should be Cash on Delivery

  Scenario: Select Express delivery
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user selects Express delivery

  Scenario: Select UPI app payment
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user searches for Aspirin
    And the user adds Aspirin to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user selects UPI app

