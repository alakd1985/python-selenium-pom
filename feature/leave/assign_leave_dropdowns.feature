Feature: Assign Leave Dropdowns

  Scenario: Print and select Leave Type

    Given the user is on the OrangeHRM login page
    When the user logs in with valid credentials
    Then the Dashboard should be displayed

    When the user navigates to the Leave page
    And the user navigates to Assign Leave
    And the user selects employee "Ranga Akunuri"
    And the user prints the Assign Leave dropdown options
    And the user selects leave type "US - Vacation"