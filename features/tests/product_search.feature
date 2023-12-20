Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  Scenario: User can filter the Secondary deals by Unit price range
    Given Open Log in page
    When Input bilgen.nazli@gmail.com and Taylanaz09
    When Click on Continue
    Then Verify main page opened
    When Click on Secondary option at the left side menu
    Then Verify the secondary page opened
    Then Click on Filters button
    Then Filter the products by price range from 1200000 to 2000000
    Then Click on Apply filter button
    Then Verify the price in all cards is inside the range (1200000 - 2000000)