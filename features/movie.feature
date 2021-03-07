Feature: Movie
""" 
Confirm that we can browse the movie information related pages on our site
"""

Scenario: success for visiting movie genres and genres details pages
    Given I navigate to the movie home pages
    When I click on the link to movie genres
    Then I should see the order for that all kind of same genres

