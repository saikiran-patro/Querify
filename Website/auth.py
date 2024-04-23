import re
from flask import Blueprint, render_template,  request
from .models import User
from . import db   
def is_valid_email(email):
 

  # Common email address regex pattern
  pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$)"

  # Check if the email matches the pattern
  if re.match(pattern, email):
    return True
  else:
    return False
  
def is_valid_password(password):
  """
  This function checks if a given string is a valid password using regular expressions.

  Args:
      password: The password string to validate.

  Returns:
      True if the password is valid, False otherwise.
  """

  # Password complexity requirements (adjust as needed)
  # - At least 8 characters long
  # - Contains at least one uppercase letter, lowercase letter, number, and special character
  pattern = r"(^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,}$))"

  # Check if the password matches the pattern
  if re.match(pattern, password):
    return True
  else:
    return False


auth=Blueprint('auth',__name__)





def is_valid_password(password):
 
  # Password complexity requirements (adjust as needed)
  # - At least 8 characters long
  # - Contains at least one uppercase letter, lowercase letter, number, and special character
  pattern = r"(^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,}$))"

  # Check if the password matches the pattern
  if re.match(pattern, password):
    return True
  else:
    return False


@auth.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':

        data = request.form


        emailAddress=data.get('email')
        password=data.get('password')
        user=User.query.filter_by(emailAddress=emailAddress).first()
        if user:
           
            print("User: " ,user.emailAddress)
            print("user password", user.password)
        
           
    return render_template('Login.html')


@auth.route('/logout')

def logout():
    return '<p>Logout</p>'
@auth.route('/signup',methods=['GET', 'POST'])

def signup():
    if request.method == 'POST':
       data= request.form
       firstName=data.get('firstName')
       lastName=data.get('lastName')
       emailAddress=data.get('email')
       password1=data.get('password1')
       password2=data.get('password2')


       if(len(firstName)<2) :
          return render_template('Signup.html', message="First name must be at least 2 characters" , category=False)
       elif(is_valid_email(emailAddress)==False):
          return render_template('Signup.html', message="Invalid Email Address", category=False)
       elif (password1!=password2):
          return render_template('Signup.html', message="Confirm Password doesn't match", category=False)
       elif(is_valid_password(password1)==False):
            return render_template('Signup.html', message="Password requires at least 8 characters long and contains at least one uppercase letter, lowercase letter, number, and special character ", category=False)
       else:
          new_user= User(emailAddress=emailAddress, firstName=firstName, lastName=lastName, password=password1)
          db.session.add(new_user)
          db.session.commit()
          return render_template('Signup.html', message="Account created successfully!", category=True )
       
    return render_template('Signup.html', text="testing")