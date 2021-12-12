## **Testing**

### Table of Contents

1.Approach
2.Responsive Testing
3.User Story Testing
4.Features Testing
5.Code Validation
6.Bugs / Issues

## Approach

[Chrome DevTools](https://developer.chrome.com/docs/devtools/) will be used to test responsiveness of the site. Ensuring the site is usable on different devices and screen sizes.

Every feature noted in the README has been tested to ensure the site is fully operational.

All the code used (HTML/CSS/JS/Python) was also tested using online validation tools as per the requirements.

* [*W3C Markup Validation Service](https://validator.w3.org/).
*  [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
*  [JS Hint](https://jshint.com/).
*  [PEP8 Online](http://pep8online.com/).

I have also used Google Lighthouse and [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) to check the Performance, Accessibility, Best Practices and Search Engine Optimisation of the website.


# Responsive Testing

### Desktop

The responsiveness of the site on desktop devices was tested using Chrome, Firefox and Safari browsers. The following screen widths were tested: 1024 pixels, 1280 pixels, 1440 pixels, 1600 pixels and 1920 pixels. The site was responsive across all devices and screen sizes.

### Mobile and Tablet

The mobile and tablet responsiveness of the site was tested using the Device Mode in [Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly).

For mobile devices the minimum screen width the site was tested at was 320 pixels (iPhone SE) in [Chrome DevTools](https://developer.chrome.com/docs/devtools/). The site was also tested using [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) and passed all tests (see image below).

![](Mobile-Friendly Test - Google Search Console 2021-12-11 21-37-46.png)

The responsiveness was also tested on an iPhone X Max. The site was consistently responsive across all devices and screen sizes.


# User Story Testing

### New Users

1. **As a new user, I want a clear layout so I can easily navigate the site on all platforms.** 

The website has been developed to work on different browsers across all platforms. Extensive testing has been performed (see Functional/Features Testing below).

2. **As a new user, I would like to view all products for sale without having to register for an account.**

Users can browse and purchase products without registering for an account.

3. **As a new user, I would like to be easily able to find products for their intended purpose.** 

Users can browse by category by clicking on the indoor and outdoor decorations links in the main navigation.

4. **As a new user, I would like the ability to search the store either by product title or keyword.**

Users can search the website using the search bar at the top of the screen by the product names and categories.

5. **As a new user, I would like to be able to add items to a shopping bag.**

When viewing the detail of any products users can add the item to their shopping bag.

6. **As a new user, I would like to be able to update items that are already in my shopping bag.**

Users can edit / delete items in their shopping back before completing the checkout process.

7. **As a new user, I would like to clearly see the total cost of my order including any shipping costs.**

Users are prompted in the toast message how much more they would need to spend to avail of a free shipping option. In the checkout then users will see the shipping cost displayed before completing their order.

### Registered Users

1. **As a registered user, I would like to see my previous orders or the status of current orders.** 

Registered users can view their order history and order status on their &quot;My Profile&quot; page.

2. **As a registered user, I would like to add comments to the blog posts.** 

Registered users will have the option to add a comment to a Blog post. Unregistered users will be prompted to sign up.

3. **As a registered user, I would like the option to save my delivery details so I don&#39;t need to keep entering them.**

Registered users will see a tick box at checkout to save their delivery details for future purchases.

4. **As a registered user, I would like the ability to edit or delete a previous comment that I have left for a particular blog.** 

Registered users will see options to edit and delete their comments on the particular blog post.

5. **As a registered user, I would like the ability to edit or delete my profile/account.**

Registered users can edit their profile in the my profile page. Currently registered users cannot delete their own profile. This is something I would look at adding in the future.

### Returning Users

1. **As a returning user, I would like to read blogs or any new content the site has for recommendations.**

A link to the blog is included in the main nav for returning users to visit and stay up to date on promotions and styling tips.

2. **As a returning user, I would like to follow the store on their social media channels so I can stay updated on any upcoming product releases or promotions.**

Social media links are listed in the footer - these are visible on all pages.

3. **As a returning user, I would like to have the ability to contact the store if I have any questions or queries regarding a product or order.**

A Contact Us link is available in the main nav. There is also an email address and phone number listed in the site footer which is visible from every page.

### Store Owner / Administrator

1. **As the store owner / admin, I would like the ability to add new products to the site.**

Products can be added to the site via the Product Management page. Once the user is logged in and has the correct permissions the Product Management page can be accessed via the My Account icon in the navigation bar.

2. **As the store owner / admin, I would like the ability to edit existing products.**

When logged in as an admin the edit option for a product will be visible on the products page and the product details page. Clicking on this link will open the edit product page.

4. **As the store owner / admin, I would like the ability to delete existing products.**

When logged in as an admin the delete option for a product will be visible on the products page and the product details page. Clicking on this link will open a modal for the to confirm delete of the item from the database.

5. **As the store owner / admin, I would like the ability to add blog posts to the site.**

Only site admin will see an option to "Add a Blog Post" in the blogs sections. Site admin can also add new blog posts via the Django admin console .

6. **As the store owner / admin, I would like the ability to read messages from my customers.**

Store administrators will be able to view messages from customers sent via the contact us form on the Django admin console. The owner of the site&#39;s admin email address will also receive an email immediately with the message contents.

7. **As the store owner / admin, I would like the ability to edit or delete blog comments that breach the store's policies.** 

Site administrators can edit or delete any comments via the Django admin console.

# Features Testing

### 1. Responsive on all device sizes

See Responsive testing section above.

### 2. Interactive Elements: Search Bar

Confirm that the user can interact with the site by searching for products using the search bar in the nav bar.

**TESTING STEPS:**

1.In the search bar enter a keyword such as "snowglobes"; and confirm that the correct number of products are returned and displayed correctly.
2.Repeat these steps using Firefox & Safari browsers.
3.Repeat these steps using a mobile device.

### RESULTS:

The correct products were found and displayed when searching by keyword. When there was more than one product matching the keyword then the correct number of products were shown.

## ![](searchbar_confirmation.png)

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

In future this feature could be improved by adding in the ability to search by category as well as product title.

### 3.Header

Test navigation bar links function correctly and that the correct links are displayed for admin and non admin users.

**TESTING STEPS:**

1. Check that the nav bar is fixed to the top of the browser window when scrolling down.
2. With the user logged out check that the following menu options appear in the My Account drop down menu: Register &amp; Login
3. Click each of the menu options listed above and confirm that you are taken to the correct page.
4. Login as a regular non admin user and check that the following menu options appear in My Account drop down menu: My Profile, Logout.
5. Click each of the menu options listed above and confirm that you are taken to the correct page. Clicking the Logout option should log you out of the website.
6. Login in using an administrator account and check that the following options appear in the nav bar: Product Management, My Profile, Logout,
7. Click each of the menu options listed above and confirm that you are taken to the correct page. Clicking the Logout option should open the sign out page to log you out of the website.
8. On desktop devices confirm that clicking on the Snowflakes logo in the top left returns the user to the home page.
9. Confirm that all the navigation links under the main nav menu function correctly. On mobile devices these will collapse into a hamburger icon.
10. Repeat these steps using Firefox & Safari browsers.
11. Repeat these steps using a mobile device.
12. Repeat the above tests with a screen size of <=992 pixels and check the menu options All Products, Indoor Decorations, Outdoor Decorations, Blogs and Contact Us into the hamburger icon. Also confirm that the Snowflakes icon is not rendered and that instead there is a Home link in the hamburger menu.
13. On mobile devices confirm that the Search, My Account and Shopping Bag icons are rendered at the top of the screen and function correctly.

### RESULTS:

All the navigation links function correctly for all users and link to the correct pages. For screen sizes <=992 pixels the correct navigation links collapse into the hamburger menu and function correctly. The nav bar also remains fixed to the top of the page on both desktop and mobile devices.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

### 4.Footer

Test footer links function correctly and that it scrolls with the page contents.

**TESTING STEPS:**

1. Check that the footer remains at the bottom of the screen on every page.
2. Check that the footer scrolls down when displaying a page with lots of content.
3. Click on the email address and confirm that it opens the user's mailbox and preloads the address into the 'to' bar.
4. Click on each social media link and verify it opens up the correct page in a new browser tab.
5. Repeat these steps using Firefox & Safari browsers.
6. Repeat these steps using a mobile device.

### RESULTS:

The footer is visible at the bottom of the screen when there is minimal content and scrolls down when viewing a page with lots of content.

The email is hyperlinked and the correct address appears in the user's mailbox to field. All social media links are working and link to the correct pages, opening in a new tab.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone XMax mobile device with no issues.

### 5: Home Page

## Test to check the Home Page is displaying the correct information, the images scales correctly and all the collections links are working correctly.

**TESTING STEPS:**

1. Confirm that the hero image is displaying correctly.
2. Confirm that the "Shop the Collections" section is displaying correctly.
3. Click on any of the images and confirm that the correct navigation is in place.
4. Repeat these steps using Firefox & Safari browsers.
5. Repeat these steps using a mobile device.

### RESULTS:

The hero image is displayed correctly on desktop and mobile devices. The Shop the Collections images move from a horizontal grid to vertical on mobile and all the links are working as expected.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone XMax mobile device with no issues.

### 6: User Account Registration

Test to confirm that the user registration process functions correctly.

**TESTING STEPS:**

1. Click on the Register link in the My Account dropdown menu.
2. Confirm that the form validation functions correctly. All fields are mandatory and the user should be prompted to complete all fields.
3. Complete the form and click the Sign Up button
4. Confirm that the user is redirected to the Verify Your Email Address page and that a message appears stating a confirmation email has been sent.
5. Confirm that a confirmation email has been received at the email address used above.
6. Click on the link in the confirmation email to activate the new account.
7. On the Confirm Email Address screen click on the Confirm button.
8. Sign into the site using the new user credentials.
9. Check that the correct links appear in the My Account dropdown for a logged in non-admin user.
10. Repeat these steps using Firefox & Safari browsers.
11. Repeat these steps using a mobile device.

### RESULTS:

The form validation functioned as expected prompting the user to complete all the fields with valid information. The user was redirected to the Verify Your Email page after clicking the Sign Up button with the correct success message being displayed.

![](verify_email_confirmation.png)

The confirmation was received at the specified email address. See below.

![](email_confirmation.png)

The link in the email redirected the user to the Confirm Email address page and clicking the Confirm button successfully verified the email address. Sign-in was successful using the new user credentials and the correct navigation links were displayed in the My Account dropdown menu.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone XMax mobile device with no issues.

### 6.2: User Authentication

Test to confirm that users can log in to the site and access the pages they have permissions to view.

**TESTING STEPS:**

1. Login to the site using a non-admin account.
2. Confirm that the user has access to the following pages and that the information presented is correct for the logged in user: My Profile and Log Out.
3. Logout of the site and login using an admin account.
4. Confirm that the user has access to the following pages and that the information presented is correct for the logged in user:My Profile, Product Management and Log Out.
5. Repeat these steps using Firefox & Safari browsers.
6. Repeat these steps using a mobile device.

### RESULTS:

Logging in as a non-admin and admin resulted in the correct links being displayed in the My Accounts dropdown and each page displaying the correct information for the logged in user.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone XMax mobile device with no issues.

### 6.3: User Sign-out

Test to confirm that a user can sign-out of the site and is redirected to the correct screen after sign-out.

**TESTING STEPS:**

1. Logout of the site by clicking on the Logout link in the My Account dropdown.
2. Confirm that the user is redirected to the Sign Out confirmation page.
3. Click the Sign Out button and confirm the user is redirected back to the home page.
4. Confirm the correct links are displayed in the My Account dropdown menu - these should be Register and Login.
5. Repeat these steps using Firefox & Safari browsers.
6. Repeat these steps using a mobile device.

### RESULTS: 

Clicking on the logout link in the My Account dropdown redirects the user to the correct Sign Out confirmation page. Clicking on the Sign Out button logs out the user redirecting them back to the home page. The links in the My Account dropdown are correct for a user who is not logged in to the site.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone XMax mobile device with no issues.

### 6.4: Password Reset

Confirm account owners are able to reset their password if they have forgotten theirs.

1. Open Chrome browser and navigate to: [https://snowflakes-christmas-shop.herokuapp.com/](https://vinyl-rack.herokuapp.com/).
2. Click login from the My Account drop down menu.
3. On the sign in page click forgot password:

![](sign_in_html.png)

1. Confirm the user is brought to the password reset page to enter their email address.
2. Enter your email address and click "reset my password".
3. Confirm an email is received at the given email address
4. Repeat the above steps using Firefox & Safari browsers.
5. Repeat the above steps using a mobile device.

Clicking the Forgot password button in the Login page successfully brings the user to the Password Reset page. I entered a non admin user email address and confirmed (image below) an email was received at this address. The email contained a link that brings the user to the Change Password page (see below) and I entered and confirmed my new password. After clicking Update Password I confirmed a success message was displayed. I then tried to log in using the new password and this was successful.

Tests performed using Chrome, Firefox & Safari desktop browsers. Repeated tests using an iPhone XMax with no issues.

![](password_reset.png)

![](password_reset_2.jpeg) ![](password_reset_3.jpeg) ![](password_reset_4.jpeg)

### 7: All Products Page 

Test to confirm all the products available on the site are listed on the products list page. Check that the image, title and price are clearly displayed. Confirm that the edit/delete links are displayed for each product when the use is logged in the admin access.

**TESTING STEPS:**

1. Click on the All Products link in the Catalogue dropdown menu. Confirm that all the products available on the site are listed on the page.
2. Confirm that the image, title and price are clearly displayed.
3. Click on any product and confirm the correct product details page is opened.
4. Navigate back to the All Products page and login as an administrator.
5. Confirm that the edit/delete links are present below each of the products.
6. Repeat these steps using Firefox & Safari browsers.
7. Repeat these steps using a mobile device.

### RESULTS:

Clicking on the All Products link in the Catalogue dropdown opens the correct page with all the available products listed. When logged out or logged in as a non-admin there are no edit/delete links displayed. When logged in as a site admin the edit/delete links are displayed below each of the products.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone XMax mobile device with no issues.

### 7.2: Product Details Page

Test to confirm that the correct information is displayed on the Product Details page for logged out users, logged in (non-admin) and logged in (admin).

**TESTING STEPS:**

1. On the home page click on any product to open the product details page. Confirm that the page displays the correct information for the product and that the edit/delete links are not visible above the product description.
2. Login to the site as a non admin and confirm that the edit/delete links are not visible next to the artist name.
3. Login to the site with admin access and confirm that the edit/delete links are present above the product description.
4. Click the Add To Bag button and confirm that the item has been added to your shopping bag.
5. Repeat these steps using Firefox & Safari browsers.
6. Repeat these steps using a mobile device.

### RESULTS:

The Product Details page displays the correct information for logged out, logged in (non admin) and logged in (admin) users.

![](product_detail_confirmation_desktop.png)


Clicking the Add To Bag button successfully adds the product to the shopping bag as can be seen in the two images below: ![](addtocart_toast_success.png) ![](shopping_bag.png)

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone XMax mobile device with no issues.

### 7.3: Search product database

Test to confirm the products can be browsed and sorted using the search bar and product sort tab.

**TESTING STEPS:**

1. Click on the By Price link in the All Products dropdown menu. Confirm that all the products are listed on the page by price.
2. Click on Indoor Decorations in the main nav and select one of the options, Trees, Ornaments or Snowglobes and confirm that the correct products are displayed for that particular category.
3. Use the product sort filter in the top right to sort the products by title A-Z and reversed, Z-A.
4. Repeat these steps using Firefox & Safari browsers.
5. Repeat these steps using a mobile device.

### RESULTS:

Clicking on the By Price link correctly displays all the products in ascending price order. When one of the Indoor Decorations options is selected, the correct products are displayed.

When using the product sort filter, to organize the products by title, the products are displayed in the correct order.

![](price_filter_confirmation.png)

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

## 8.1 Checkout - Shopping Bag. Adding, Editing and Removing products from Cart.

Test to confirm that users can add products to their shopping bag and edit their shopping bag before checkout.

**TESTING STEPS:**

1. Browse the store and via the product details page add a product to the shopping bag by clicking the Add to Bag button.
2. Confirm that the pop-up message displays the correct information confirming the product has been added to the bag.
3. Add a couple more different products to the shopping bag checking the correct information is displayed in the pop-up message.
4. Once all products have been added go to the shopping bag by clicking either the Go To Secure Checkout in the pop-up message of the shopping bag icon in the nav bar. Both should take you to the shopping bag page.
5. Confirm that the information displayed on the Shopping Bag page is correct.
6. Increase the quantity for one of the products and click the Update link to refresh the page. Confirm that the Subtotal for the product has been updated along with the Bag Total and Grand Total.
7. Remove a product from the bag by clicking on the remove button. Confirm the product has been removed from the shopping bag.
8. Remove products from the shopping back until the Bag Total is less than the free delivery threshold of €50.
9. Confirm that the Shopping Bag page is displaying the correct information and reminding the user how much more they need to spend before they qualify for free shipping.

### RESULTS:

When adding products to the shopping bag the correct information is displayed in the pop-up message window. Clicking the Go To Secure Checkout button in the pop-up window opens the Shopping Bag page. It was also confirmed that clicking the shopping bag icon in the nav bar takes the user to the same page. The information displayed on the Shopping Bag page was correct matching the items previously added to the Bag.

Item quantities could be adjusted using the +/- buttons and clicking on the Update link adjusted the subtotal and totals accordingly. When completing this round of testing an error was spotted where products could not be removed from the shopping bag. The button resulted in a 500 error where this had previously worked before.

When the Bag Total was below the free delivery threshold of €50 the correct information was displayed on the Shopping Bag page and the pop-up message. See images below.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

### 8.2: Checkout and Stripe Payment**

Test to confirm that the user can securely checkout using Stripe by entering their delivery details and credit card information. Confirm that the order is recorded correctly and appears in the users profile page under previous orders. Also checks that the confirmation email is sent to the user.

**TESTING STEPS:**

1. Add a couple of items to the shopping bag and navigate to the Shopping Bag page.
2. Click Secure Checkout to open the Checkout page. Confirm that the order summary is correct.
3. Complete the checkout form providing delivery details and credit card information. Use the following Stripe test card details:
    * Card Number: 4242 4242 4242 4242
    * Expiration: Any date in the future
    * CVC: Any 3 digit number
    * Postcode: Any 5 digit number 
4. Confirm that the form validation functions correctly prompting the user to complete all mandatory information.
5. Once the form is complete click the Complete Order button.
6. Confirm the order success pop-up message is displayed and that the user is redirected to the order confirmation and the information is correct.
7. Confirm receipt of the confirmation email and that all details are correct.
8. Login to the Django administration panel and confirm the order has been added to the Orders table.
9. Login to Stripe and confirm that the payment was created and charged.
10. Login to the site and repeat the steps 3 to 11 as detailed above.
11. Confirm that the order has been added to your profile by clicking on the My Profile link under the My Account dropdown.
12. Click on the order number and confirm the details are correct.


### RESULTS:

The checkout page order summary displayed the correct information. The form validation functioned correctly prompting the user to complete all mandatory fields with the correct information. 

![](checkout_prompt.png)

The order success message was displayed and the correct information was displayed on the Order Confirmation page. See below: 

![](checkout_confirmation_desktop.png)

The confirmation email was received and this contained the correct information. See below:

![](order_confirmation_email.png)

The orders table in the Django Administration panel had been updated to include the new order with all details being correct. 

![](admin_order_confirmation.png)

The payment was created and charged in Stripe (see image below).

![](stripe_order_confirmed.png)

The My Profile page listed the new order and clicking on the order number displayed the correct information:

![](profile_order_history_confirmation.png)

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

### 9: Blogs

Test to confirm that admin only can write a product blog post and that logged in users can add comments to blog posts. Ensure non-registered users can access and read blogs but not add comments. Also confirm that the form validation is functioning correctly.

**TESTING STEPS:**

1. Login to the site as an admin and click on blogs in the main navigation.
2. Confirm the option to "Add a Blog" is displayed at the top of the page.
3. Add a title, intro, body and attach an image.
4. Click Add Blog Post to confirm the blog is now visible on the blog main page.
5. Confirm the user is unable to submit empty fields.
6. From the list of blogs, choose one and click "Read More".
7. On the Blog post page, confirm the options to Edit and Delete are visible above the image.
8. Confirm the options to Edit and Delete a blog are also visible under the title on the main blogs page.
9. Click the Add Review button to add the review to the Product and confirm the user is redirected to the My Review page.
10. Click on Edit to ensure the user is navigated to the Edit Blog Post page.
11.Edit the blog title and click Edit Blog Post to confirm the edit function is working.
12. Click on Delete to confirm the blog post is deleted as expected.
13. Log into the site as a registered user (non admin) and confirm the edit and delete buttons are not visible on the blogs main page and blog post page.
14. Click Add a comment on the Blog post page to confirm registered users can add comments.
15. Login as a non -registered user to confirm you are able to view blogs, but when clicking on "Add a comment" are prompted to register for an account.
16. Repeat these steps using Firefox & Safari browsers.
17. Repeat these steps using a mobile device.

### RESULTS:

When visiting the site as a non-admin user, the blogs page is visible with a list of blog posts. ![](blogs_non_admin.png)

Clicking "Read more" on a blog post brings the user to the blog post page to read the full blog

When visiting as a registered user, blog posts can be read and also commented on:

![](registered_users_blog_comment.png)

Registered users can delete comments they post, but not edit them. This feature could be added in future iterations of the site.

When visiting the site as an admin, new blog posts can be added. Admin can also edit and delete existing posts via the website on the Django admin console.

![](edit_blogpost_frontend.png)

I then logged into the Django admin and confirmed the admin user is able to view and add blog posts from here.

![](admin_add_blogpost_superuser.png)

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

### 9: Contact Us

**TESTING STEPS:**

1. Navigate to the Contact Us page by clicking the Contact Us link in the main nav.
2. Confirm that the form validation is functioning as per the form validation requirements.
3. Once the form has been completed, click on the Submit button. Confirm that the success message is displayed.
4. Check that the user has received a confirmation email to the specified email address and that all the details are correct.
5. Repeat these steps using Firefox & Safari browsers.
6. Repeat these steps using a mobile device.

### RESULTS:

The form validation functions correctly prompting the user to complete all the required fields. Clicking the Submit button results in the correct success message being displayed stating that the message has been sent.

![](getintouch_toast.png)

The site admin will receive an email letting them know a customer has sent a message and the contents of the message:

![](admin_email_confirmation.png)

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

### 10: Profile Page

Test to confirm that users can update their information via the profile page and that delivery details are automatically added to the checkout form.

**TESTING STEPS:**

1. Navigate to the profile page by clicking on My Profile in the My Account dropdown.
2. If the default delivery information is empty then populate the form and click Update Information when complete.
3. Add some products to your bag and proceed to the checkout page.
4. Confirm that the form has been populated with the correct information from your profile.
5. Before completing the order modify the contents of the form and select the &#39;Save this delivery information to my profile&#39; checkbox.
6. Complete the order.
7. Return to the Profile page and confirm that the delivery details have been updated to those used during checkout.
8. Repeat these steps using Firefox & Safari browsers.
9. Repeat these steps using a mobile device.

### RESULTS: 

On the My Profile page the default delivery information was updated and successfully saved. During the checkout process the correct information from my profile was displayed in the checkout form. The information was changed in the form and the update profile checkbox selected. After completing the checkout it was confirmed that the default delivery information on the My Profile page had been updated with the new data.

### 12.1: Product Management, Add New Product

Test to check that admin users can add new products to the site and that the form validation is functioning correctly.

**TESTING STEPS:**

1. Login in as an admin user and navigate to the Product Management page.
2. Complete the form on the Product Management page checking the form validation is working as per the Product model validation requirements.
3. Once completed add the new Product to the site.
4. Confirm that the user is redirected to the Product Details page for the new product and that the details are correct.
5. Repeat these steps using Firefox & Safari browsers.
6. Repeat these steps using a mobile device.

### RESULTS:

The process of adding a product worked as expected. The form validation functioned correctly prompting the user to complete all mandatory fields. The new entries appeared in the dropdown lists on the Product Management page.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone Max X mobile device with no issues.

### 12.2: Product Management, Edit &amp; Delete Product

Test to check that admin users can edit and delete existing product on the site.

**TESTING STEPS:**

1. Login in as an admin user click on any product to open up the product details page.
2. Click in the edit link to open the edit product page.
3. Confirm that the form is populated with the correct information for the product being edited.
4. Once the product has been modified click the Update Product button to save the changes.
5. Confirm that the user is redirected to the product details page and that the changes are displayed.
6. Repeat these steps using Firefox & Safari browsers.
7. Repeat these steps using a mobile device.

### RESULTS:

Click the edit link in the product details page and open up the edit page with the correct information being displayed in the form. Product details can be changed by clicking on the corresponding button and updating the information in the form. The information was updated in the product page once saved and the edit page closed.

After making changes to the product and clicking the Update Product button the user was redirected to the product details page showing the updated information.

Tests performed using Chrome, Firefox and Safari desktop browsers. Repeated tests using an iPhone X Max mobile device with no issues.

# Code Validation

### Python Flake8 Validation

All python code was checked using Flake8. These results can be found [here](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/python-flake8-results.txt). A few of the errors relating to longer lines were not refactored as these were either auto generated files or determined to be of low importance.

[Java Script Linting Errors](https://jshint.com/)

Stripe Elements Java Script

No errors reported, two warnings: 'template literal syntax' is only available in ES6

![](jshint_stripe_js.png)

Country Field Java Script

No errors, one warning: 'let' is available in ES6 (use 'esversion:') or Mozilla JS extensions (use moz).

![](jshint_countryfield_js.png)

[W3C HTML Checker](https://validator.w3.org/nu/)

See screenshots of individual page checks below. No errors noted, some minor warnings.

**Homepage:**

![](html_validator_homepage.png)

**Products page:**

![](html_validator_all_products.png)

**Product detail Page:**

![](htmll_validator_one_warning_product_details.png)

**Blogs page:**

![](html_validator_blogs.png)

**Blog post page:**

![](html_validator_blog_post_page.png)

**Shopping bag page:**

![](html_validator_shopping_bag_2_warnings.png)

**Checkout:**

![](html_validator_checkout_one_warning.png)

**Contact us:**

[W3C CSS Checker](https://jigsaw.w3.org/css-validator/)

The CSS code was validated using the W3C CSS Checker - no errors were found.

![](W3C CSS Validator results for https:::snowflakes-christmas-shop.herokuapp.com: (CSS level 3 + SVG) 2021-12-12 21-34-13.png)

### Lighthouse Reports

The Google Lighthouse reports can be found at the links listed below. Minor changes were made to the website to improve accessibility.

MOBILE
* [Product Detail Page - Mobile](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/product_detail_lghthouse_mobile.pdf)
* [Products Page - Mobile](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/products_lighthouse_mobile.pdf)
* [Contact Us Page - Mobile](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/contactus_lighthouse_mobile.pdf)
* [Blogs Page - Mobile](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/blogs_mobile_lighthouse.pdf)
* [Profile Page - Mobile](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/profile_page_mobile_lighthouse.pdf)
* [Product Management - Mobile](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/product_management_mobile_lighthouse.pdf)
* [Admin Page - Mobile](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/admin_lighthouse_mobile.pdf)
* Home page - Mobile

DESKTOP

* [Product Detail Page - Desktop](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/Product_details_lighthouse_desktop.pdf)
* [Products Page - Desktop](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/products_desktop_lighthouse.pdf)
* [Contact Us Page - Desktop](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/contactus_lighthouse_desktop.pdf)
* [Blogs Page - Desktop](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/blogs_lighthouse_desktop.pdf)
* [Profile Page - Desktop](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/profile_page_desktop_lighthouse.pdf)
* [Product Management - Desktop](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/product_management_lighthouse_desktop.pdf)
* [Admin Page - Desktop](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/docs/Lighthouse_Reports/admin_desktop_lighthouse.pdf)
* Home page - Desktop

## Bugs/Issues/Unresolved Issues

When testing a few errors were found:

In the html validator for the contact us page, an error message indicates that a select element cannot have a placeholder but removing the placeholder causes a 404 error on the contact page.

When creating a order as a registered user the order history is not updating on the profile page.

On the Shopping bag page the remove button is not working.