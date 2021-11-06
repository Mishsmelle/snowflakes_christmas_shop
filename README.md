# Snowflakes Christmas Shop


## Contents


1. User Experience (UX)
2. Features
3. Technologies Used
4. Testing
5. Deployment
6. Credits

[View the live project here.]()

Snowflakes Christmas Shop is an online shopping site for Christmas goods. The website signposts options, provides status and feedback to users at all stages of the shopping process. It is designed for and tested on a range of devices including desktop PCs, tablets and mobile phones.


## User Experience (UX)


### User stories

[View User Stories here.]()


## Design


The header was originally taken from the Boutique Ado project. The page title was replaced with a business logo and icons updated to be more in keeping with the modern tone of the site. A footer was added to the bottom of all pages, which includes links to the website social media pages, a newsletter sign up section and a Contact us link. 

On the landing page, the hero image was chosen to bring in colour to the landing page and grab the attention of the user. Underneath the hero image, 3 products have been added to highlight the businesses best sellers and product links were added to easily navigate to the product page. 
The products page keeps the header and footer in place and shows a picture and key details such as the title, and category. When logged in as a superuser, options to edit/delete as shown on the main products page. 
The product details page shows a much larger image of the product on the left and a detailed product description on the right. A quantity selector under the product description makes it easy for users to select multiple items and a large add to cart button. 

### Colour Scheme
The template was kept simple with a white background and black text. The products stand out well against the plain white background. The text is easy to read as it is dark on a light background. 

### Typography
The font chosen was Google’s Quicksand. This was again chosen for a nice clean look and to be as user friendly as possible. 

### Buttons
Buttons are coloured red and green in keeping with the Christmas theme. 
The search box and profile/product management button is in grey to match the other navbar links.

### Imagery
Product images are all in the jpeg format to reduce the load speed of the site. All product images are sourced from third party ecommerce sites, Arnotts.ie and therange.ie. The main page hero image was sourced from Canva.com and the text added in canva by the developer. 

### Icons
Font Awesome Icons were used for all site icons such as User account and shopping cart.

### Wireframes
The wireframes for Desktop, Tablet and Mobile versions are here.
These wireframes were created at the start of the project and although very similar to the resulting website includes some features that were not implemented:
* Wish List
* Change password


## Database model


The database model uses a relational structure with tables for Product, ProductReview, Order, OrderLineItem, User, UserProfile and Categories.

The database schema is here.                                            [Go to Contents ⏫]()


## Features


The Bootstrap toolkit was used throughout including:
* Grid
* Navbar
* Modal
* Cards
* Carousel
* Forms
* Buttons
* Toasts
* Django-multiselectfield

In order for the site owner to add in size availability according to stock levels, the Django Multiselectfield was used. This provides checkboxes for each size option that can be purchased.

### Notifications
Bootstrap toasts were used to give feedback to the user on success, informational and error purposes.

### Sale
A site owner can select whether a product is on sale with a checkbox and set the percentage discount.
The product will then be included with other sale products from the Sale link on the navbar.
Each product on sale will have a Sale badge, original price with a strike through and sales price in the product card.

### Cart/Checkout/Checkout success
The site has separate pages for cart, checkout and checkout success corresponding to each stage of the purchase process. The customer is able to alter the quantity in the cart between 1 and 99. The price for individual products, sub-total of quantity for each product size, overall cart total and order total after shipping cost is shown.

### Checkout
Name, email, phone, address and card details are required on the checkout page.
A checkbox provides an option to save the contact and address details back to the profile.

### Free shipping
A shipping fee over €7 is added to all orders under €50.
Free shipping is automatically applied for users who spend over €50. 

### Profile
Customer’s contact details and order history are saved in their profile.
Contact details can be updated on the profile or check out pages.
Security is in place to ensure only the customer who submitted the order can see the order history.

### Add/Edit products
A site owner can create new product for the Product Management link on the navbar. Existing products can be updated via the Edit and Delete links on each item in the product views.

### Search box
Full search capability on product titles and description.

### Defensive programming
* Confirm Deletion
* HTML validity
* Non-public pages protected from unauthorised access.
* Admin pages protected from non-admin access
* Errors 404 and 500 handled by pages within the site.
* Comprehensive user notifications
* CRUD
* Site owners have full CRUD capability for products.
* Crispy forms
* Used to improve function and style of forms.
* AWS S3 hosting
* Static and media files hosted on AWS S3.
* Responsive on all device sizes tested

The use of the Bootstrap grid system and additional media queries enables the site to display effectively on a broad range of desktop, tablet and mobile screen sizes.


## Future development


Features not implemented from Wireframes:
* Wish List
* Change password
* Filter on products page
* Calculations for VAT & postage in different countries
* Notification if no product stock.
* Cart products saved to profile
* Magnification on product images
* Contact form                                                                  [Go to Contents ⏫]()


## Technologies Used


### Languages Used

* HTML5
* CSS3
* Javascript
* Python
* Frameworks
* Bootstrap 5.1
Bootstrap layout, content, components and utilities were used to structure the site and make it responsive.
* Django
Django was used to structure the site.

### Libraries
* **jQuery**
* jQuery has been used to launch toast messages, enable increment/decrement functionality in the cart, processing Stripe payments and checking country fields at checkout.
* **Fontawesome Icons**
Fontawesome Icons were used for all site icons.

### Development & production platforms
* **GitPod**
GitPod was used for code editing, version control, committing and pushing to GitHub.
* **GitHub**
GitHub was used to store and manage project code pushed from GitPod.
* **Heroku**
Heroku was used for hosting the deployed web application.
* **AWS S3**
Hosting live static and media files.

### Other applications
* **Balsamiq**
Balsamiq was used for wireframes created during the design process.
* **Favicon.io**
This website provided the capability for Favicon generation.                    [Go to Contents ⏫]()


## Testing


See Test report here.                                                           [Go to Contents ⏫]()

## Making a Local Clone

1. Log into GitHub and locate the Snowflakes-Christmas-Shop
2. Under the repository name, click ‘Clone or download’.
3. To clone the repository using HTTPS, under ‘Clone with HTTPS’, copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in step 3.
    >$ git clone https://github.com/mishsmelle/snowflakes-christmas-shop
8. Click Enter. Your local clone will be created.
    >[Please see this link for a more detailed explanation.]()
9. Following Stripe documentation, create a Stripe account and in Developers on the API key tab find the public and secret key.
10. Also in Stripe create a Webhook and find the Webhook secret key.
11. Create an env.py file to contain the following environment variables.
    >os.environ.setdefault("SECRET_KEY", "<app secret key>")
    >os.environ.setdefault("DEVELOPMENT", "True")
    >os.environ.setdefault('STRIPE_PUBLIC_KEY', '<from Stripe>')
    >os.environ.setdefault('STRIPE_SECRET_KEY', '<from Stripe>')
    >os.environ.setdefault('STRIPE_WH_SECRET', '<from Stripe>')
12. Create a .gitignore file ensuring *.sqlite3, *.pyc and pycache are added.
13. Install all project requirements with pip install –r requirements.txt
14. Run database migrations
15. Load category and product fixtures in following order
16. Create a superuser
17. Run the app

### Deploy to Heroku

1. Login to Heroku
2. Create new app
3. Add name , choose closest region and click Create app
4. In Resources create a new Postgres database
5. Select Hobby Dev-Free plan and click Submit Order Form
6. In your IDE install dj_database_url and psycopg2
7. Import dj_database_url in settings.py
8. Replace default database with a call to dj_database_url.parse and give it the database URL from Heroku
    >DATABASES = {
    >'default': dj_database_url.parse('your-url-goes-here')
    >}

9. Run all migrations again for the Postgres database (see steps 11 to 13 in Making a Local Clone)
10. Install gunicorn to act as a web server
11. Freeze requirements
12. Create a Procfile to tell Heroku to create a web dyno to run gunicorn to serve the Django app. This should contain the following:
13. Login to Heroku from your IDE using your API key as the password
14. Temporarily disable collectstatic so Heroku will not collect static files when we deploy.
15. In Settings, create the following Config Vars
16. Add the Heroku hostname to ALLOWED_HOSTS in settings.py
17. Commit & push to GitHub
18. Initialise your IDE with Heroku and push to it.
19. In Heroku on the Deploy tab select GitHub as Deployment method
20. Search for repository and click Connect
21. Click Enable Automatic Deploys


#### Configuring S3
1. Create an AWS account
2. Create a bucket for S3
3. Uncheck Block all public access and acknowledge settings
4. Enable static website hosting & Save changes.
5. Add default values for index, error doc & click Save.
6. In Permissions on CORS paste the following:
7. Click Edit in Bucket policy to create a security policy
8. Click Policy Generator and for Principal enter * and actions add Get Object
9. Enter the ARN from step 7.
10. Click Add statement
11. Click Generate Policy
12. Copy Policy JSON Document
13. Paste into Bucket policy (with slash & asterisk at end of Resource for full access) & Save changes.
14. Click Edit in Access Control List, check box for List access for Everyone & Save changes.

### AWS IAM (Identity & Access Management)
1. In AWS navigate to IAM, User groups, Create user group
2. Enter a name and click Create group
3. In Policies, click Create Policy
4. On the JSON tab, click Import managed policy
5. Search for S3 and import the AmazonS3FullAccess policy
6. Add in the ARN from the AWS Policy Generator page
7. Click Next Tags and Review
8. Add a name, Description and click Create policy
9. Attach the policy to the group created.
10. In User Groups select your group
11. In Permissions, click Attach Policies
12. Select the policy created & click Add permissions
13. In Users, click Add users
14. Add username and Access Type as Programmatic access & click Next
15. Select to add user to our policy, click Next and Create User
16. Click Download.csv to get your access credentials.

### Connect Django to S3
1. Install boto3
2. Install Django Storages
3. Freeze requirements
4. Add the following settings for Django to connect to S3
5. In Heroku Config Vars add the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY and delete the DISABLE_COLLECTSTATIC variable
6. In settings.py tell Django where static files are located
7. Create a media folder on S3 and upload files
8. Select Grant Public Read Access to the objects                               [Go to Contents ⏫]()


## Credits


### Code
The site was based on the Code Institute Boutique Ado project.
Bootstrap 5.1 was used throughout the site so that it is responsive to different devices and viewport sizes.
Code was used from external sources in the following instances:

### Content
All content was written by the developer.

### Media
The images used were sourced as follows:
[Arnotts.com]()
[Canva.com]()
[Therange.com]()

### Acknowledgements

Caleb for his mentoring and advice.
Code Institute Tutors and peers for assistance with feature implementation and bug fixes.
Go to Contents ⏫

