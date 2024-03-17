# Created by iryna at 3/13/2024
Feature: Tests for pagination on Secondary deals page


  Scenario: User can open the Secondary deals page and go through the pagination
    Given Open Reelly.io
    And Log in to the main page
    When Click on Secondary option at the left side menu
    Then Verify the right page opens
    And Verify user can go to the final page using the pagination button
    And Verify user can go back to the first page using the pagination button
