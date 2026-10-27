
Feature: Prescription management

  Background:
    Given the user is on the MediShop login page
    When the user logs in with valid demo credentials

  Scenario: Upload a prescription successfully
    Given Salbutamol is in the shopping cart
    When the user clicks Secure checkout
    And the user uploads a prescription successfully
    Then the prescription should be uploaded successfully

  Scenario: Filter medicines requiring a prescription
    When the user opens prescription-only medicines
    Then prescription-required medicines should be displayed

  Scenario: Add a prescription-required medicine to the cart
    Given the user opens prescription-only medicines
    When the user adds Salbutamol to the cart
    And the user clicks the shopping cart
    Then Salbutamol should be present in the cart

  Scenario: Attempt checkout without uploading a prescription
    Given Salbutamol is in the shopping cart
    When the user clicks Secure checkout
    Then the checkout page should be displayed

  Scenario: Open checkout with a prescription-required medicine
    Given Salbutamol is in the shopping cart
    When the user clicks Secure checkout
    Then the checkout page should be displayed
