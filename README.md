# projectfourecommerce

view website https://projectfourecommerce.herokuapp.com/

to enter the backend

-username: test
-password: test

To pay:

pay with details: 4242 4242 4242 4242
11/22   123

In order to see the orderhistory please note that the email whichyou registered with must be the same as the email you ordered with. 



#Intro
This is Code Institute Stream Four Project. As project four should be a fullstack webapplication with a buildin payment functionality I have decided to make webshop. The name of the webshop is "Made by Loni" is inspiration of my sister called "Lonneke Machielsen". In her freetime she is making bracelets. It was my fantasy to build a webshop with my sister as brand. 
Hence "Made by Loni" is about fashion and as my sister is making bracelets and likes to wear porsch dresses I decided that bracelets and dresses are the products of this webshop. The products have in common, that they are porsch and that women are the target group. 

Goal
The goal was to create a website for customers where my sister can sell her fashion. 

Therefore the website has been developed:
User friendly for desktop and mobile.
The website should have a state of the art design. 
A website wich can be managed by the owener. 



# Pages
The website has the following pages:

- Homepage
- Productlist with all products
- Productlist page for each category (bracelets and dresses)
- Product page
- Cart page/checkout page
- Thanks for order page
- Login and Register page
- Order history page
- Order detail page
- Wishlist page
- Blog page
- About page
- Contact page


# Design

UX and UI design ideas were taken online from https://drive.google.com/file/d/1ZcnGMBVTmVKyvBEkYT38ck_HfTg-KHri/view I saw a picture. Which gave me the inspiration to make the whole website. Further I have followed a course on Udemy: https://www.udemy.com/course/develop-a-shopping-cart-website-with-django-2-and-python-3/learn/lecture/9054068#overview this has gave me the knowledge to build the shop app, order and cart app. 

Shop logo was created using a fontawesome style.

The layout is made of bootstrap and crispy. The forms, such as the login, register and contactform are crispyforms the grid of the whole website is form bootstrapp. The footer is a bootsnip template with social media icons.

The website is made as responsive as possible using media queries and bootstrap.

Font Awesome Icons were used for different icons on the website (account, shopping bag, burger menu, social media, arrow icons etc.).





  # The homepage 

  Has a bootstrapp mobile responsive navbar.
  Fullscreen image with button to the shop

  a selection of newest arrivals
  a selection of most viewed items

  a blog section with the most recent post (will only show one post without an image)
  contact section with button which will lead to the contactpage.

  # Productlist with all products
  This product displays all the products which are posted in the shop. It includes pagination.

  # Productlist page for each category
  This type of pages will only show products which are asigned to one category. It includes pagination.

  # Productpage
  The productpage is displaying the product and information. It contains the product title, description picture and price. Further this     page provide two buttons:
  
  - add to wishlist  (once the product is saved in the wishlist the button will change into delete from wichlist. If you click on that          the product will be removed from the wishlished and the button will change into add to wishlist. 
  
  - add to cart. (this will add the product to the shopping cart)
    
    The productpage is different per category additional the productpages in the dresses catogory will show a drop down where customers 
    are able to select their size. 
   
   # Cart page
   the cart page is divided in two sections:
   1
   The cart page display which products are added to the cart. In the cart customers have the possibilty to increase or decrease the          quantity of each product. Further its possible to delete each product. 
   2
   In this section there are two buttons
     - continue shopping (they go to the general shopping list where all products of all categories are displayed)
     - payment button , pay with card (a pop up button will appear where to fill out their billing/shipping address
      once that is filled out a next pop up will appear to fill in the card details. 
   
   It is possible to order without an account!
   
   # Thanks page
   This page confirms the order and includes a button with continue shopping.
   
   # Registration page
   Contains a form in order to register. People need to fill their name and surname, username, email and password. Once that's than they 
   are redirected to the shoppinglist, but need to go to the loginpage in order to login.
   
   # Login
   The login page is to login for users which are registered. The can login via username and password.
   
   # Order history page
   This is a list of orders placed by the customer. Each rule in the list will lead to the order detailpage.
   
   # Order detail page 
   Order detailpage provides details of the order. Customer order and shipping/billing details. 
   
   # Wishlist page
   This is a page where people once logged in! Can see which items they put in the wishlist. Then the can click on the item, which will      lead to the productpage and are able to add the item in cart or delete it form the wishlist. 
   
   # Blog page
   This is a page where news and information can be posted by the administrator of the website. 
   
   # About page
   This is a page which tells something about the brand and the founder of Made by Loni. 
    
   # Contact page
   In this page visitors/customers of the website have three options to contact, namely whatsapp, email and the contactform. 
   the phone and email are hyperlinks which will open a whatsapp or email window on the screen.
   The contact form is a form which can be filled out, once it is filled out the a success message will appear on the screen.
   
   
   
# Functionality
Django project has the following apps/folders:


- Blog
- Cart
- Customer_service

- ecommerce (parent app)

- order
- search_app
- shop
- static (is a folder not a app)
- staticfiles (is a folder not a app)
- wishlist


# Blog app
Has a blog model and a view with one template where all the blogs are listed. 

# Cart app
The cart app has two model cart and cart items. Once a product is added to the cart the cart and cartitem models are used. 

# Shop app
Has a category product and productimages model. In order to create products, categories should be created first. 
Then after that products can by created and each product can be created with more images by the productimages

Accounts has customized user, UserRegistrationForm and a UserLoginForm form. It accepts email as a username and has fields first_name and last_name. Superuser must be created in the back-end using "python manage.py createsuperuser" command. And first_name and last_name fields are also required when creating a superuser. Superusers can be shop managers. However they are not supposed to shop on the website. It can be changed in the future though if necessary. Accounts app also has customized authenticate and get_user function for user. Vitor Freitas guide was followed to create customized users.

# Customer service
Has a contact model in order to deal with enquiries from customer via the contactform on the contactpage.

# ecommerce
ecommerce is the parent app where all other apps are subrelated. This app connects all apps with each other in order to create interaction on the website.

# order
Once the cartitems in cart are paid, the order will be created. This app has two models, namely order and orderitem. As each order has a customerdetails and billing and shipping address which are related to the cart model, each order will be different by its order_items. As with each order each order item is related to an order.

# search_app 

This is a special app with no model, but is made via the views.py ap. The search app is able to search products by name and description.

# Wishlist
This is created to store wished items. It has one model, wishitems. It has a foreign key to the product which the login user has added to the wishlist, therefore wishlist has also an foreign key to the user. 

# static 
This contains the css, javascripts and media folders in order to save all the static data. 

# staticfiles
This contains the css, javascripts and media folders in order to save all the static data from the static folder. So staticfiles are the blueprint of the static folder in order to pass the files over to AWS cloud.

# deployment
The deployment is via AWS cloud and HEROKU.


# Dilemma's

I have been working on this project with a lot of fun and passion, but I have also experienced dilemma's in building it. I have seen that a website is never finished and that the enimy of finished is perfect! So still I have quite a lot features I wanted to implement such as:

- social media login: although I have added an social media login with facebook in my third steam project, it's cost time and time to set up special accounts and to get them verified, so that's the reason why I decided to not implement it. 

- thumbnail carousel on the productpage: a thumbnail carousel on productpage provides visitors the opportunity to see more productphoto's. Although I have made the backend for this feature. It cost time to find the perfect jquery implementation. I surely want to that, but I decided that this feature will be outside the scope of this project. 

- Productphoto zoom: The productphoto zoom is a functionality that the photo zooms in when the cursor hovers over the product photo. I have decided that this only will make sence in combination with the thumbnail carousel. 

- product filtering: I have decided to not implement product filtering as this will not fit in my current layout. Further reason is, that I find it hard to find a solution to get this very mobile friendly. I miss the knowledge to make this functionality mobile friendly, but I have the knowledge to create filter functionality and I want to implement that after my education at code institute. 

- product sorting: product sorting is a feature which I decided to not implement as I will mess up my layout. And I sorting goes hand in hand with productfiltering. So I decided to do it or to do it not.

- product sharing: this is a feature which I decided to not implement as I am running out of time. I want to implement this feature after my study for code institute. 

- Better product management so stock per color and size: This is much harder to implement, so I decided to not implement this for this project as perfect is the enimy of finished. 

- implement ideal: this is also a feature which takes a lot of time, therefore I decided to not implement this. Ideal is a payment feature in the Netherlands (around 90 percent of all online transactions in the Netherlands are done with ideal). 

# Credentials 

I really want to thank udemy and the instructor on udemy who have made a course. I have implement all the features from the udemy course which results that the following apps (its backend and fronted are taken over from that udemy course):

- cart app
- search app
- order app
- shop app

The things which I have added to this project is:

- the landingpage
- blog app 
- customer service app 
- wishlist app
- the about page. 
-I have also done little changes in some front end stuff and I have changed the login. On the udemy course if the customer is registered it need to login again, I have changed that, now once the customer is registered it will automatically logged in. 

I also want to thank codeinstitute as this time has gave me the opportunity to learn frontend and django. I am happy that I can set up a blog and online shop on my own. Codeinstitute has also given me trust in coding as at the beginning of the course I had zero knowledge about coding! And now I have the confidence to build websites!


https://github.com/radlad7/PyShop

https://www.udemy.com/course/develop-a-shopping-cart-website-with-django-2-and-python-3/learn/lecture/9054068?start=300#overview
