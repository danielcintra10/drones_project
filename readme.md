# Medical Drones

## Getting started

### Clone repository
First you will need to clone down the repository.

1) Create a new directory on your computer. This will be the 'root directory'.

2) Open a terminal and cd into the root directory.

3) You can now clone the project from GitHub. You can do this a few different ways.
I use HTTPS.
```
- git clone https://github.com/danielcintra10/medical_drones.git .
```
### Virtual environment
Create a virtual environment to run the project.
1) Inside the root directory open a terminal and use the following command 
to create a virtual environment.

```
python -m venv venv
```
2) Now activate the virtual environment with the following command.
#### windows machine
```
venv\Scripts\activate.bat
```

#### mac/linux
```
source venv/bin/activate
```

You will know your virtual environment is active when your terminal displays the following:
```
(venv) path\to\project\
```

### Project Requirements 
Let's go ahead and install the project requirements. 
Add the following code to you terminal.
```
pip install -r requirements.txt
```

### Secrets and Environment Variables
It is good practice to separate sensitive information from your project. 
I have installed a package called 'python-dotenv' that helps me manage secrets easily. 
Let's go ahead and create an env file to store information that is specific to our working environment. 
Use the following command in your terminal.

#### windows machine
```
copy env.template .env
```
#### mac/linux
```
cp env.template .env
```
You can use the .env file to store API keys, secret_keys, app_passwords, db_secret_info,
and you will gain access to these in the Django app.
Use the .env.template file to guide you


### Fixtures 
Before start the project create database tables, use the following command:

~~~~
python manage.py migrate
~~~~

Now we need to load some data in the models that the application needs to run,
to do that use the following command:

~~~~
python manage.py loaddata fixtures/my_data.json
~~~~

### Create superuser
You need a user with administrator permissions specially to access to the admin site,
you can run the following command and follow the instructions to create a superuser

~~~~
python manage.py createsuperuser
~~~~

### Run the project
Now you can run the server:

~~~
python manage.py runserver
~~~

***
***

