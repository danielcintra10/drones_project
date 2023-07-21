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

### Extra Comments about the Project
 
The best practice is to manage sensitive project information through a configuration 
file or through environment variables, so that there are no security vulnerabilities 
in this regard. In this simple project, the management of this sensitive information
was not taken into account to facilitate as much as possible the deployment and review 
of the project by the company once it was completed. I am fully aware that if this 
project goes into production like this it would be a total disaster.

On the other hand, the Database Management System used is SQLite, 
similar to what was said above, it was chosen this way for its simplicity, 
for being portable and facilitating the deployment of the project with the 
required information already in the DB.

One suggestion that I do want to make is on the subject of drones, their models 
and the maximum weight they can carry. In the project they specify that the maximum 
weight that a drone can carry is 500g but it is not taken into account that if the 
drone models are based on their Lightweight, Middleweight weight... not everyone can
carry 500g as the maximum weight, so I established a weight limit of 500g for the 
Heavyweight model but for the previous ones I established a range of weights with 
which they can work.
Likewise, the issue of the state changes of the drones is not handled, when they are 
in each one of them, but I understand that due to the simplicity of the test, this issue 
is not dealt with.
***
***

