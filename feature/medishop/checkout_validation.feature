Feature: MediShop checkout validation

  Background:
    Given the user is logged into MediShop
    When the user searches for "Aspirin"
    And the user adds the product to the cart
    And the user opens the shopping cart
    And the user proceeds to checkout

  Scenario: Checkout without customer name
    When the user leaves the customer name empty
    And the user submits the checkout form
    Then the checkout form should show a validation error

  Scenario: Checkout without mobile number
    When the user leaves the mobile number empty
    And the user submits the checkout form
    Then the checkout form should show a validation error

  Scenario: Checkout without house address
    When the user leaves the house address empty
    And the user submits the checkout form
    Then the checkout form should show a validation error

  Scenario: Checkout without city
    When the user leaves the city empty
    And the user submits the checkout form
    Then the checkout form should show a validation error

  Scenario: Checkout without pincode
    When the user leaves the pincode empty
    And the user submits the checkout form
    Then the checkout form should show a validation error