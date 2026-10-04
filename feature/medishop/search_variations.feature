Feature: MediShop search variations

  Scenario: Search using a partial product name
    Given the user is logged into MediShop
    When the user searches for "Aspir"
    Then the search results should contain "Aspirin"

  Scenario: Search using different letter case
    Given the user is logged into MediShop
    When the user searches for "ASPIRIN"
    Then the search results should contain "Aspirin"
