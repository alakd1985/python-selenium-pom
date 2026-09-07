Feature: Add Employee in PIM

  As an OrangeHRM user
  I want to add a new employee from the PIM module
  So that the employee record is created successfully

  Background:
    Given the user is on the OrangeHRM login page
    When the user logs in with valid credentials

  @pim @add
  Scenario: Add a new employee
    When the user navigates to the PIM page
    And the user clicks the Add Employee button
    And the user enters employee details:
      | first_name | last_name |
      | John       | Doe       |
    And the user saves the employee record
#    Then the employee should be added successfully
