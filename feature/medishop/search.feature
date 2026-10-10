Feature: MediShop product search

  Scenario: Search for a valid product
    Given the user is logged into MediShop
    When the user searches for "Aspirin"
    Then the search results should contain "Aspirin"

  Scenario: Search for a product that does not exist
    Given the user is logged into MediShop
    When the user searches for "ProductThatDoesNotExist123"
    Then no matching product should be displayed

  Scenario: Search for a product using lowercase letters
    Given the user is logged into MediShop
    When the user searches for "aspirin"
    Then the search results should contain "Aspirin"