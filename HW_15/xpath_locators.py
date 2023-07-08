"""
XPath locators are prepared for Url: https://www.saucedemo.com/ and inheritage pages
"""
# 1. Website Logo "Swag Labs"
website_logo = "//div[contains(@class, 'login_logo')]"

# 2. Username input field
username_input = "//*[@placeholder='Username']"

# 3. Password input field
password_input = "//*[@placeholder='Password']"

# 4. Login button
login_button = "//input[@type='submit']"

# 5. Label 'Accepted usernames are:'
label_usernames = "//*[@class='login_credentials']/br/parent::node()/h4"

# 6. Label 'Password for all users':
label_password = "//*[@class='login_password']/h4"

# 7. Error message for locked_out_user
error_message = "//*[@data-test='error']"

# When login with standard user and redirected to https://www.saucedemo.com/inventory.html
# 8. App Logo "Swag Labs"
app_logo = "//*[@class='app_logo']"

# 9. "Open Menu" burger button
open_menu_button = "//img[contains(@alt, 'Open Menu')]/parent::node()/button"

# 10. "All Items" link in opened sidebar menu
all_items_link = "//*[@class='bm-item menu-item'][contains(text(), 'All Items')]"

# 11. "About" link in opened sidebar menu
about_link = "//*[@class='bm-item menu-item'][contains(text(), 'About')]"

# 12. "About" link in opened sidebar menu
logout_link = "//*[@class='bm-item menu-item'][contains(text(), 'Logout')]"

# 13. "About" link in opened sidebar menu
reset_app_state_link = "//*[@class='bm-item menu-item'][contains(text(), 'Reset App State')]"

# 14. Close opened sidebar menu button
close_open_menu_button = "//button[contains(text(), 'Close Menu')]"

# 15. Shopping cart button
shopping_cart_link = "//*[@class='shopping_cart_link']"

# 16. Filtering button
filtering_button = "//span/select"

# 17. All product prices
product_prices = "//*[@class='inventory_item_price']"

# 18. Specific product price
specific_product_price = "//button[@name='add-to-cart-sauce-labs-backpack']/parent::node()/div"

# 19. Add to cart button of "Sauce Labs Bike Light"
specific_add_to_cart = "//*[@name='add-to-cart-sauce-labs-bike-light']"

# 20. Image of "Sauce Labs Backpack"
specific_item_image = "//img[@alt='Sauce Labs Backpack']"

# 21. Shopping cart badge after adding item
shopping_cart_badge = "//a/span"

# When go to the cart and redirected to https://www.saucedemo.com/cart.html
# 22. Label "Your Cart"
your_cart_label = "//div/span"

# 23. Quantity label
quantity_label = "//div[contains(text(), 'QTY')]"

# 24. Description label
quantity_label = "//div[contains(text(), 'QTY')]"

# 25. "Continue Shopping" button
continue_shopping_button = "//button[@name='continue-shopping']"

# 26. "Continue Checkout" button
checkout_button = "//button[@name='checkout']"

# 27. All "Remove" button
remove_buttons = "//button[contains(text(), 'Remove')]"

# When proceed with Checkout in cart and redirected to https://www.saucedemo.com/checkout-step-one.html
# 28. Checkout: Your Information label
checkout_label = "//span[@class='title']"

# 29. First Name input
first_name_input = "//*[@placeholder='First Name']"

# 230. Last Name input
last_name_input = "//*[@placeholder='Last Name']"

# 31. Zip/Postal Code input
postal_code_input = "//*[@name='postalCode']"
