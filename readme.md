**Steps to setup the project:**
0. Recommended: create first a virtual environment for python
In the command-line of your choice:

I. Create a virtual env:
>python -m venv demo

or

>python3 -m venv demo 
 
where "demo" is the name of the virtual environment.

The above command creates a new folder in the current path, named "demo", containing all the python standard
library packages.
ii. Activate the virtual env: 
>demo\Scripts\activate

You should see that your command-line prompt is now prefixed with (demo):(demo) c:\...\...\>
1. Install the project dependencies from requirements.txt file, using pip:
>pip install -r requirements.txt
2. Run the DB migrations: (Make sure you change your path first: >cd blog - your path should end with
......\django-blog\blog>)
>python manage.py migrate
3. Configure your django superuser for your local server setup:
>python manage.py createsuperuser
 
You will be prompted to provide the username, email address and a password.
4. Start the local django server:
 >python manage.py runserver 8000
 
Or add a new run configuration in PyCharm.

You will see the server will print out the url for your local project: Starting development server at
http://127.0.0.1:8000/
Copy the url and paste it in any browser. Access the Django Admin at the url: http://127.0.0.1:8000/admin/ and
login using the credentials you setup on step 3
Admin login: http://127.0.0.1:8000/admin/login/