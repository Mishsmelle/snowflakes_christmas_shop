# Snowflakes Christmas Shop

[View the live project here.](https://snowflakes-christmas-shop.herokuapp.com/)

![Responsive image preview](/docs/testing_images/am-i-responsive-image.png)

Snowflakes Christmas Shop is an online Christmas decoration store. Customers can browse collections, view products, purchase online as well as read the site blog and contact the store through the contact form.  This website is intended for educational purposes only. 


## User Experience (UX)


### User stories

# New Users
1. As a new user, I want a clear layout so I can easily navigate the site on all platforms.
2. As a new user, I would like to view all products for sale without having to register for an account.
3. As a new user, I would like to be easily able to find products for their intended purpose.
4. As a new user, I would like the ability to search the store either by product title or keyword. 
5. As a new user, I would like to be able to add items to a shopping bag
6. As a new user, I would like to be able to update items that are already in my shopping bag.
7. As a new user, I would like to clearly see the total cost of my order including any shipping costs.

# Registered Users
1. As a registered user, I would like to see my previous orders or the status of current orders.
2. As a registered user, I would like to add comments to the blog posts. 
3. As a registered user, I would like the option to save my delivery details so I don't need to keep entering them.
4. As a registered user, I would like the ability to edit or delete a previous comment that I have left for a particular blog. 
5. As a registered user, I would like the ability to edit or delete my profile/account.

# Returning Users
1. As a returning user, I would like to easily see what new products have been added to the site.
2. As a returning user, I would like to follow the store on their social media channels so I can stay updated on any upcoming product releases or promotions. 
3. As a returning user, I would like to have the ability to contact the store if I have any questions or queries regarding a product or order.

# Store Owner / Administrator
1. As the store owner / admin, I would like the ability to add new products to the site
2. As the store owner / admin, I would like the ability to edit existing products.
3. As the store owner / admin, I would like the ability to delete existing products.
4. As the store owner / admin, I would like the ability to add blog posts to the site. 
5. As the store owner / admin, I would like the ability to read messages from my customers. 
6. As the store owner / admin, I would like the ability to edit or delete blog  comments that breach the stores policies. 
 
## Design

### Colour Scheme

The backgrounds are a nice clean white with black text. The colors introduced through the logo and buttons are red and green, traditional Christmas colours in keeping with the theme. 

### Typography

The Quicksand font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Quicksand is both easy to read and fun. 

### Imagery

Imagery is important. The hero image is designed to be striking and catch the user's attention. It also has a classic Christmas feel and compliments the site's colour scheme. 

### Wireframes

Home Page Wireframe - [View](/docs/wireframes/Homepage_wireframe_desktop.png)
Mobile Wireframe - [View](/docs/wireframes/homepage_wireframe_mobile.png))
Contact Us Page Wireframe - [View](/docs/wireframes/wireframe_contact_page.png))

### Features

    * Responsive on all device sizes
    * Interactive elements
    * Header 
    * Footer
    * Homepage
    * Product Page
    * Checkout
    * Blogs 
    * Contact Us page with form
    * Django Administrator page
    * Product management 


## Technologies Used


### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Javascript](https://www.javascript.com/)
* [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

* [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    Bootstrap was used to assist with the responsiveness and styling of the website.
* [Google Fonts:](https://fonts.google.com/)
    Google fonts were used to import the 'Quicksand' font into the style.css file which is used on all pages throughout the project.
* [Font Awesome:](https://fontawesome.com/)
    Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
* [jQuery:](https://jquery.com/)
    jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
* [Git](https://git-scm.com/)
    Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/)
    GitHub is used to store the projects code after being pushed from Git.
* [Canva:](https://www.canva.com/)
    Canva was used to create the logo, resizing images and editing photos for the website.
* [Balsamiq:](https://balsamiq.com/)
    Balsamiq was used to create the wireframes during the design process.
* [Django:](https://www.djangoproject.com/)
    A Python based framework for developing secure and maintainable websites - the core of this project.
* [Amazon Web Services (AWS):](https://aws.amazon.com/)
    AWS was used to host all static and media files using the S3 and IAM services.
* [Stripe:](https://stripe.com/ie)
    an API framework for processing secure payments.
* [Postgres:](https://www.postgresql.org/)
    Relational database, hosted and deployed via Heroku.
 

## Testing

See [Testing.md](https://github.com/Mishsmelle/snowflakes_christmas_shop/blob/main/testing.md) for full testing details 


## Deployment


This project was developed using [GitPod](https://gitpod.io/) and the latest version of the code base can be found in the master branch of this repository. No other branches were created during the development of this project.

### Cloning the Repository

To clone [this repository](https://github.com/Mishsmelle/snowflakes_christmas_shop) follow the instructions below:
1. Navigate to the repository.
2. Click on the Code button and copy the URL from the Clone>>HTTPS section.
3. Inside your development environment/IDE open a command terminal.
4. Create / navigate to the directory you would like the cloned copy to be made.
5. Type in the following command using the URL copied from step 2 and press Enter. This will create a cloned copy of the repository.
```git clone https://github.com/mishsmelle/snowflakes-christmas-shop```

### Deploying to Heroku from Gitpod

1. Open [Heroku](https://heroku.com/) in the browser and login, creating a new account if required.
2. On the Heroku Dashboard, click New->Create New App.
3. Give the app a new name and choose a region closest to you. Click the Create App button.
4. On the resource tab, provision a new Postgres database selecting the free Hobby Dev plan.
5. To use Postgres in the application two packages are required - these are dj-database-url and psycopg2. To install these in Gitpod type the following commands:

```
pip3 install dj_database_url
pip3 install psycopg2-binary
```

6. Freeze the requirements in Gitpod by typing ```pip3 freeze > requirements.txt.``` Heroku will use the requirements.txt file to install these packages during deployment.
7. Open the settings.py file and import the dj_database_url package by adding ```import dj_database_url``` at the top of the file underneath import os.
8. In the database section comment out the default configuration and replace it with the code below. The DATABASE_URL can be found under the settings tab in Heroku in the Config Vars section.
   
```
DATABASES = {
    'default': dj_database_url.parse('DATABASE_URL')
}
```

9. As a new database has been connected the migrations will need to run again to setup the database. Type in the following commands in Gitpod to run the migrations.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

10. The database can be populated using the fixtures and JSON files. Run the following commands to load the data into the Postgres database:

```
python3 manage.py loaddata categories
python3 manage.py loaddata products
```

11. Create a superuser account for the Django Administrator Panel using command ```python3 manage.py createsuperuser.``` When prompted, enter a username, email address and password.
12. To ensure the database URL doesn't end up in version control, replace the database configuration as set up in step 8 with the code below. When running on Heroku the DATABSE_URL will be defined in the Config Vars and the correct URL will be parsed by dj_database_url. Otherwise the sqlite database will be used when running in the Gitpod development environment.

    ```
   if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
    	   }
    ```

13. For the app to run, the Gunicorn web server package is required. To install this package run command ```pip3 install gunicorn.```
14. Freeze the requirements by running command ```pip3 freeze > requirements.txt.```
15. In the root directory of the project, create a Procfile by running the command ```touch Procfile.``` The Procfile is used to tell Heroku to create a web dyno to run gunicorn and serve in our Django app.
16. Open the Procfile copy in the following text, ensuring there is no blank line at the end of the file.
   ```web: gunicorn vinylrack.wsgi:application```
17. Login to Heroku using the ```heroku login -i``` command.
18. As AWS will be used to host the static files we need to prevent Heroku from collecting static files during deployment. This can be done by setting DISABLE_COLLECTSTATIC to 1. Enter the following command to set DISABLE_COLLECTSTATIC:
```heroku config:set DISABLE_COLLECTSTATIC=1 --app app-name```
19. In the settings.py file add the Heroku app to the list of allowed hosts. Also add in localhost to ensure the app still works in Gitpod.
ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']
20. Edit the .gitignore file (or create a new one if it doesn't exist) and add the following if required: 
    * core.Microsoft*
    * core.mongo*
    * core.python*
    * env.py
    * __pycache__/
    * *.py[cod]
    * node_modules/
    * .github/
    * *.sqlite3
    * *.pyc

21. Commit the changes to the main Github repository using the following commands:
    * git add .
    * git commit -m "Add commit message here"
    * git push
22. Initialise the Heroku repository using command ``` heroku git:remote -a app-name.```
23. To deploy the app to Heroku push the changes to the remove Heroku repository using command ```git push heroku main.``` This will deploy the site without any static files.
24. To automatically deploy when any changes are committed to Github, click in the Deploy tab in Heroku and set the Deployment method to Github.
25. In the Connect to GitHub section, search for the repository and click connect when the correct one is found.
26. In the Automatic Deploys section click on the Automatic Deploy button. This ensures that every time we push any changes to Github the code will be automatically deployed to heroku as well.
27. Create a new Django secret key using the Django Secret Key Generator website.
28. In Heroku, under the Settings tab, create a new Config Var with a key name of SECRET_KEY with the value set to the key generated in the previous step.
29. To ensure the Heroku app picks up this key add the following to the settings.py file:
SECRET_KEY = os.environ.get('SECRET_KEY', '')
30. Commit the changes to Github. Heroku should pickup the changes from Github and deploy the site to app-name.herokuapp.com.

### AWS S3 Configuration

The AWS S3 service will be used to host all static files and images.
1. Open [AWS](https://aws.amazon.com/) in the browser and login, creating a new account if required.
2. Open the AWS Management Console and search for the S3 service using the search box if it isn't listed in your recently accessed services.
3. Click 'Create New Bucket' to create a new bucket. It is recommended to give the bucket the same name as your Heroku app.
4. Select the region closest to you.
5. Uncheck 'Block all public access' and use the tick box below to acknowledge that the bucket will be public. Click 'Create bucket'.
6. Select your bucket from the bucket list. In the properties tab, turn on static website hosting and set the following default values then click save.
    * Index document: index.html
    * Error document: error.html
7. In the Permissions tab, paste in the following CORS configuration then click save.

    ```
   [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
    ```

8. In the Permissions tab go to the Bucket policy section and click the Edit button. Click the Policy Generator button to create a new security policy. Select/enter the following:
    * Policy Type: S3 Bucket Policy
    * Principal: *
    * Actions: GetObject
    * ARN: Copy the ARN from the Bucket Policy tab and paste here.
    * Click Add Statement then Generate Policy.
    * Copy the new policy and paste it into the Bucket Policy editor.
    * To allow access to all resources add a "/*" onto the end of the Resource key value.
    * Save the new policy.
9. In the Permissions tab go to the Access Control section and click the Edit button. On the "Everyone (public access)" line check the List checkbox and click Save changes.
10. Go back to the services and select Identity and Access Management (IAM) to add a new user. Use the search bar if IAM isn't listed. IAM will be used to create a new group, create an access policy giving the group access to the S3 bucket and to assign a user to the group so they can use the policy to access the files in the S3 bucket.
11. Under User Groups click the Create Group button. Enter a group name then scroll to the bottom and click Create group.
12. Under Policies click the Create Policy button. Follow the steps below:
    * Go to the JSON tab and select Import managed policy.
    * Search for the AmazonS3FullAccess policy and Import this.
From the S3 Bucket Policy page copy the ARN and paste this twice into the Resource key as shown below:

```
   "Resource": [
        "arn:aws:s3:::s3-bucket-name",
        "arn:aws:s3:::s3--bucket-name/*"
    ]
```

13. Click the Review Policy button giving the policy a name and description. Click the Create Policy button to save all changes.
14. Under User Groups, select the group that was created above. On the Permissions tab, select Attach Policies from the Add permissions dropdown menu. Search for the policy that was created above, select it and click the Add permissions button.
15. Under Users, click the Add Users button and give the user a name. Check the Access Key - Programmatic access option and click next. On the next page add the user to the new group that was created above. Click through to the end then click Create User.
16. Download the CSV file - this contains the user access key and secret access key which will be used by the Django app for authentication. Save the file in a secure location as this cannot be downloaded again once the user has been created.
17. To connect Django to the new S3 Bucket two new packages are required: boto3 and django-storages. In Gitpod type the following commands to install the packages:

```
pip3 install boto3
pip3 install django-storages
```

18. Freeze the requirements by running command ```pip3 freeze > requirements.txt.```
19. In the settings.py file add 'storages' to the INSTALLED_APPS list.
20. Add the following configuration to the settings.py file. As the S3 Bucket is only required when using Heroku, an if statement is used to check if the variable USE_AWS exists.

    ```
    if 'USE_AWS' in os.environ:
        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'bucket-name'
        AWS_S3_REGION_NAME = 'eu-west-2'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    ```

21. In Heroku at the following Config Vars to the app. The AWS keys can be found in the csv file that was downloaded when creating the S3 user. The ```DISABLE_COLLECTSTATIC``` can also be removed as Heroku will get the static files from AWS for any future deploys.

```
AWS_ACCESS_KEY_ID : From the csv file
AWS_SECRET_ACCESS_KEY : From the csv file
USE_AWS : True
```

Remove variable ```DISABLE_COLLECTSTATIC```
22. In the settings.py file add the following inside the ```USE_AWS``` if statement to tell Django where the static files will be sourced from in production.

```
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```

23. The next step is to configure Django to use S3 to store our static files whenever someone runs ```collectstatic``` and to also store any uploaded images in the S3 bucket.
24. In the root folder create a file by running ```touch custom_storages.py.```
25. Copy the following configuration into the file and save:

    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage
    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION
    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
 
26. In the settings.py file add the following inside the USE_AWS if statement to configure Django to use our custom storage class for static file storage and to override the static and media URLs in production.

    ```
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
 
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

27. In the settings.py add the following lines to the top of the USE_AWS if statement. These will configure the browser to cache static files for a long time as they don't change often.

```
   AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }
```

28. At this point all the changes can be committed to Github, triggering Heroku to deploy the app. Confirm all the static files have been uploaded to the S3 bucket.
29. To add the media files to the S3 bucket go to AWS S3, select the bucket and click on the Create folder. Create a folder called media.
30. Inside the media folder click Upload to upload all the media files to the S3 bucket. Under Permissions, set the Predefined ACL to Grant public-read access.
31. The superuser email address for the Postgres database needs to be confirmed to allow the user to login to the application. To do this, login to the Django admin panel and confirm the email address for the superuser by checking the Verified box. 

## Stripe Configuration

1. Login to Stripe and in the Developers section click on API Keys. In Heroku add the publishable and secret keys as the following config variables.

```
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
```

2. Click on the Webhooks link in the Developers section. Click on Add Endpoint to configure the following:
EndPoint URL: ```https://app-name.herokuapp.com/checkout/wh/```
Click receive all events in the Events to send section and click Add Endpoint.
3. On the webhook screen, reveal the Signing Secret and copy this into Heroku as a config variable named ```STRIPE_WH_SECRET.```
4. To confirm the webhook is working, send a test webhook from Stripe to ensure the listener is working. 

## Email Configuration

The following process assumes that GMail will be used for sending and receiving emails.
1. Open GMail in the browser and login, creating a new account if required.
2. Open the account settings, select Accounts and Import and then other Google account settings.
3. Click on the Security tab and turn on 2-Step Verification under Signing in to Google.
4. Click Get Started and enter your Gmail password and then follow the 2-Step Verification as instructed.
5. Once the 2-Step Verification has completed go back to the Security tab and select App passwords under Signing in to Google.
6. On the App passwords screen select Mail for the app and other for the device giving it the name Django. Click Generate to complete.
7. Copy the password and create a new config variable in Heroku called ```EMAIL_HOST_PASS``` pasting in the password as the value.
8. Also create another config variable in Heroku called ```EMAIL_HOST_USER``` and set this to the Gmail account.
9. In settings.py add the following:

   ```
   if 'DEVELOPMENT' in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = 'app-name@example.com'
        EMAIL_SUBJECT_PREFIX = '[App-Name]'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')
        DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
        EMAIL_SUBJECT_PREFIX = '[App-Name]'
    ```


10. Confirm the email is functioning correctly by registering a new user and checking that the email confirmation is received.


## Credits

### Code
* [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

### Content
The majority of the data for the products listed on this site was taken from [Arnotts](https://www.arnotts.ie) and [Christmas-Decorations.com](https://www.christmas-decorations.com/) websites 
The Hero image was from [Canva] with inspiration from the [Christmas Decorations](https://www.christmas-decorations.com/) homepage.

### Acknowledgements
I would like to thank my mentor,  Caleb Mbakwe for his guidance throughout this project. 
The tutors at Code Support for their assistance with issues that occurred during the design of the site. 
I would also like to thank my peers on Slack who helped by answering any questions I had with this project.
 
