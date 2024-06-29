Feature: File upload

  Scenario: User uploads a file
    Given the user navigates to the upload page
    When the user selects a file to upload
    And the user submits the form
    Then the file should be successfully uploaded
