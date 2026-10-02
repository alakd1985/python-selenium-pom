Feature: Assign Leave

  Background:
    Given the user is on the OrangeHRM login page

  @leave @assign
  Scenario: Assign leave to an employee

    When the user logs in with valid credentials
    Then the Dashboard should be displayed

    When the user navigates to the Leave page
    And the user navigates to Assign Leave
    And the user assigns leave with the following details
      | employee | leave_type    | from_date  | to_date    | comment         |
      | Alex Taylor | US - Vacation | 2026-10-15 | 2026-10-16 | Family vacation |
    And the user clicks the Assign button
    And the user confirms the leave assignment
    Then the leave should be assigned successfully