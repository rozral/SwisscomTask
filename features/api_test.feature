Feature: Testing NASA API
  Scenario: I send a request to retrieve the Astronomy Picture of the Day for yesterday or a specific date
    # Date format: "YYYY-MM-DD" OR "YESTERDAY"
    Given I create a request to NASA API for APoD of date "YESTERDAY"
      When I should receive an OK (200) response
      Then Response should contain following keys: "title, explanation, url, media_type, date"
      Then Media type (media_type) should be either image or video