Feature: Prescription management

  Scenario: Upload a prescription successfully
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials
    Then the MediShop home page should be displayed
    When the user clicks Browse medicines
    And the user selects Prescription only
    And the user adds Salbutamol to the cart
    And the user clicks the shopping cart
    And the user clicks Secure checkout
    And the user clicks Upload a prescription
    And the user clicks Upload your first prescription
    And the user uploads the test prescription
    And the user accepts the prescription confirmation
    And the user saves the prescription
    When the user clicks the shopping cart
    And the user clicks Secure checkout