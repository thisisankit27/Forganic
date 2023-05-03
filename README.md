# Forganic

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ https://github.com/thisisankit27/Forganic.git
    $ cd Forganic
    
Activate the virtualenv for your project.

    $ mkvirtualenv forganicEnv
    $ workon forganicEnv
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ cd mainProject
    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
