<h1>Django-React-Image-DL-App</h1>



<h3>Prerequisites</h3>


<h3>For React</h3>

Install Node JS
Refer to https://nodejs.org/en/ to install nodejs

Cloning and Running the Application in local
Clone the project into local

<code>git clone ..</code>

Install all the npm packages. Go into the react folder and type the following command to install all npm packages

<code>npm install</code>

In order to run the application Type the following command

<code>npm start</code>

The Application Runs on localhost:3000

<hr>

<h3>For Django</h3>

Go to Django folder

For installing required packages, execute the following command in terminal:

<code>$pip install -r requirements.txt</code>

After successful installation execute the following commands:

<code>$python manage.py migrate</code>
<code>$python manage.py runserver</code>

HTTP client 

axios library is used to make HTTP Calls from react app to upload image for classification and to get classification result

Used tensorflow for predictions model
