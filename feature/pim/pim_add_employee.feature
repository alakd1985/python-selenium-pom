Feature: PIM Employee Management

  @pim
  @add
  Scenario: Add a new employee

    Given the user is on the OrangeHRM login page
    When the user logs in with valid credentials
    Then the Dashboard should be displayed

    When the user navigates to the PIM page
    And the user clicks the Add Employee button
    And the user enters employee details
      | first_name | last_name |
      | Alak       | Dutta       |
    And the user saves the employee record
    Then the employee should be added successfully