Feature: MediShop payment methods

  Scenario: Open Payment methods from Home
    Given the user is logged into MediShop
    When the user opens Payment methods
    Then the Payment methods page should be displayed

  Scenario: Open Add payment method modal
    Given the user is logged into MediShop
    When the user opens Payment methods
    And the user opens Add payment method
    Then the Add payment method modal should be displayed


  Scenario: Add a demo card payment method
    Given the user is logged into MediShop
    When the user opens Payment methods
    And the user opens Add payment method
    And the user selects "Credit / debit card" as the payment type
    And the user fills the demo card details
    And the user saves the payment method
    Then the saved payment method should be displayed


  Scenario: Add a demo card as the default payment method
    Given the user is logged into MediShop
    When the user opens Payment methods
    And the user opens Add payment method
    And the user selects "Credit / debit card" as the payment type
    And the user fills the demo card details
    And the user saves the payment method
    Then the saved payment method should be displayed
    And the saved payment method should be the default


  Scenario: Delete the saved payment method
    Given the user is logged into MediShop
    When the user opens Payment methods
    And the user opens Add payment method
    And the user selects "Credit / debit card" as the payment type
    And the user fills the demo card details
    And the user saves the payment method
    Then the saved payment method should be displayed
    When the user deletes the saved payment method
    Then the payment methods empty state should be displayed
