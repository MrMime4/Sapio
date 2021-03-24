# Sapio
Final Year Project

Requirements{

      pip install django mysqlclient
      pip install imutils
      pip install python-opencv
      django == 3.0.5
      python < 3.0.x

}

To Run The project on your local machine first download the relevent python version along with the "pip" utility to be esily able to download other requirement.

Then, install django in an envirement with following commands,

      pip install virtualenv
      mkdir myproject
      cd myproject
      virtualenv myprojectenv
      source myprojectenv/bin/activate
      
Now At this point you have created a virtual envirement for your project      

      pip install django==3.0.5
      pip install python-opencv
      pip install imutils
      pip install mysqlclient
      
      git clone https://github.com/MrMime4/Sapio.git
      
      cd Sapio
      cd stream
      python manage.py makemigrations
      python manage.py migrate
      python manage.py runserver
