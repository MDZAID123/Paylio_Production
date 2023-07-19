# Paylio_Production
Section1  Course introduction




Welcome
Complete project demo
Goal of the course -advance fintech application banking app security and autogeneration from scratch to deployment
Tools and requirements
Vs code
Google chrome browser
Github account 
Python


What is django-dynamic and interactive websites
Consist of various components  such as 
1)database interface
2)url routing system
3)user  authentication
4)django models- for structuring database tables
5) django views-for writing logics
Views helps us to define the logic behind every webpage
6)django templates for visual representation
7)django urls for connecting accessing views and templates
8)django authentication and security
Django has build in security feature to protect our application from common web vulnerabilities
Super admin interface
Fully functional adminpanel to manage you applications
Download all the source code and instruction for future reference



Section 2 Project and  workspace setup
Virtual environmenet highly recommended while creating projects
Manage.py file will be inside the root of the django project 
Install new apps in setting.py 
Then  configure templates
Now configure static and media files in setting and urls .py
Now create a new vies template urls and then run the server
Now we need to configure inheritance and partials
We want to specifically put titles for different pages
We can use multiple block content


ADMIN PANEL CUSTOMISATION USING JAZZMIN LIBRARY
Configure admin page super user and jazzmin


Custom django admin


Install jazzmin
Add jazzmin to installed apps
Add jazzmin config code in settings.py
Create superuser 
Login to admin section



Section 3 creating custom user models in django
To login using email instead of username
We need to create a  auth user model


When we create  a new login model instead of the default one we require  to create the super user for that login type again
Superuser
email-zaidiiit123@gmail.com
Username-zaid
Password-meowcoder123
From the admin we should be able to see all the users that get into our database 


Session 4 
User Authentication system
User registration feature
Creating forms and views and mapping urls
How to override fields and add placeholders IDS 


We DONT want our input to be reflected in our url 

Cause that will be a very big security leak to us
Method post -grab and and send it to the server
Django needs a new token when it whenever its going to create a form
Request.post will grab all the things that you type in here 


Whenever someone sign-up i want them to automatically log in



Now we will configure the template


We already have build it templates for the frontend just use them and them code backend well
Close the preloader if you dont want to reload the page every time


Logout Authentication and deleting sessions
Login authentication and then 
We will working on with alerts
For signin we are using data from normal rawinput fields in django here 



Creating the bank account model
To save user money and sensitive information like pin number 
Make sure to register the every new app created in settings.py
We need to create a file where user can upload their images


We need to register our models in the app specific admin.py file


Creating a bank account using Django Signals 
Automatically creates a bank account for usrs when they create an account

KYC MODEL USING DJANGO
Form for kyc
One user should have only one kyc
 

KYC Forms using Django Forms
It is a better pratice to make your code more readability



Creating Kyc Views in Django 
This will allow uswr to submit their kyc from the frontend
Get saved in the database and we can able to view it in our admin section
On the admin verify the account and make it active 


It is a good practice to keep the app specific templates in a separate folder 


Ctrl+shift +p for doing auto django for static files
Kyc-regform.html page extends from dashboard-base.html  page
To look kyc form much better 
Populate fields in html tags one by one


Message  Alerts using Django  Messages
Configuring the DashBoard



When we are logged in we should get rid of the login button from the webpage
Bank account dashboard
Using django views and urls

Displaying user account information on the account dashboard page
To grab and display currently logged in user details we will fetch them from userauths
Note that we have linked the image to the user kyc till now 
//and not directly to the account model of the user 


Our logic is that if a user is not logged in he should have access to account page 
Redirect them to some other while doing so



Set up logic for your website  and then code accordingly for it 
Whenever we log in it should redirect them to the accounts page



Section 10
Transfer payment Mian banking logic
First we will be searching user based on account number or account id


To load the profile picture in other page we need to import the same views that we rendered on the accounts page
Now when we search we need to fetch users on this page 

We should also give users the ability to search other users by their email address


Now we will allow user to enter amount to be paid then perform basic processing using Django
Processing amount to be paid from backend and frontend using JS

We need to send the account number to which we want to send money to as  a parameter in url
And then decode it from redirectintg url



You need to handle account does not exist on the search account page in a professional manner 
Instead of user getting an error on the webpage
We need to configure the choose buttom on the search account page


For backend payment transfer logic we will be using javascript

Section 11 Creating a Transaction Model
Creating transaction model to keep track of transfer payments and  deposits





Section-12 Transfer Payment Main Banking Logic
VERIFY and process payment to be sent to the backend




User should be able to put a description of every transaction that he might be making



TRANSFER PAYMENT CONFIRMATION
THIS PAGE WILL LET THE USER COFIRM THE PAYMENT THEY ARE ABOUT TO Make


We can also set some fees for every transaction that our webapp is doing

Final process of transfer

Authenticate transfer process using pin number


Users should enter their pin  number for unique transaction

Transfer successful page and details of the complete transaction



SECTION13 Payment transaction history

Listing payment transaction history-stored in the database model


In our system there are different type of transactions 
Transaction Detail 
To display more information about a transaction 


Section -14 payment request logic using Django
 Search users tgo request money from 
Using account number or email



Get And checking the amount  the user want to request 


Processing the amount to be requested by the user



Payment request confirmation Page


Process the request and Display the confirm success page 
Process and confirm payment request and redirect to success page



Section 15 setting received paymentr requests 
1)settle users payment request using django-accept and pay request 


We want to separate the transactions on different tabs


In our system we should be able to delete a payment request that we made till now


2)Confirm settlement request made  by  users
Confirming the settlement request made  by the users 

3) Confirming the Payment request and release money to user’s bank account
Release  requested amount to user account and re calculate account balance 



Logic is that the once settled payment request should be settled again



4)Delete payment request by  users 
In case the user in not interested in the payment request any longer 


WSGIR REQUEST   simply a web development error

Section 16 Credit card feature using django

Creating credit card model to store user credit card in  Database 
Adding the Credit Card Form to the frontend using Django
List View list all credit card from database to frontend
We will be showing user’s credit card in its dashboard
Credit card detail page to display all the details and history of a card
Fund Cash to Credit Card from account balance
Withdraw cash from credit card
Delete credit card from user account system and Database 




SECTION 17 hosting and deployment 
1)hosting website on railways
Deploy app top railway -manage static and server files
So far we have runned our application on our localhost that is our development server
Start pushing our application on live server
Live server applications


We need requirements.txt
We need runtime.txt
We wont be using django sqlite on our live server

Working and using Env files


2)LIVE DATABASE SETUP
Database Hosting using Postgresql On railway Databases
Provisioning a Database for our live website


3) Modify live server database
Add delete update field and logic to live database
Here we will modify and make changes to live website that is already hosted online
Make sure that whatever new fields you are creating inj your model you are already making null =True to that 


4)Hosting Static and Media Files on  Live ON AWS S3 bucket 
The next time you are trying to make your git repository and railway updates the sites that  all the images are going to be deleted 
How to push our files to AWS
Before using aws download boto3 and django-storages


