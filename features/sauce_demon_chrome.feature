Feature: Sauce Demo Automation Chrome

  Scenario: Log in, sort items, add to cart, and verify checkout process
    Given the user is on the Sauce Demo login page in Chrome
    When the user logs in with username "standard_user" and password "secret_sauce"
    Then the user should be redirected to the products page
    When the user sorts items by price from low to high
    And the user adds the first 3 cheapest items to the cart
    Then the user navigates to the cart page
    And the user should see 3 items in the cart
    And the user proceeds to checkout