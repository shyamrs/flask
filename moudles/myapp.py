from flask import Flask,render_template,flash,request,redirect,url_for,session,logging
from wtforms import Form,StringField,TextAreaField,PasswordField,validators,SubmitField
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import inflect
import redis
from flask_sqlalchemy  import SQLAlchemy
from flask_wtf import FlaskForm 


login_manger=LoginManager()
bcrypt=Bcrypt()
p = inflect.engine()




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///data.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    words = db.Column(db.String(15))
    pluralwords = db.Column(db.String(50))




@app.route('/')
def index():
     return render_template('home.html')
     
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contacts.html')


class RegisterForm(Form):
        name=StringField('Name',[validators.Length(min=1,max=50)])
        username=StringField('Username',[validators.Length(min=4,max=25)])
        email=StringField('Email',[validators.Length(min=6,max=50)])
        password=PasswordField('Password',[
            validators.DataRequired(),
            validators.EqualTo('confirm',message='Passwords do not match')])
        confirm=PasswordField('Confirm Password')


@app.route('/register',methods=['GET','POST'])
def register():
        form = RegisterForm(request.form)
        
        
        

        if request.method=='POST' and form.validate():


              
                           
            


            return render_template('registerpage.html',form=form)

        return render_template('register.html',form=form)

@app.route('/login', methods=['GET', 'POST'])
              
            
            
            
                  
                    
def login():



    
    
    if request.method == 'POST':

         # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']
        hashed_password=bcrypt.generate_password_hash(password_candidate)



         #connection
        
        R = redis.StrictRedis(host='localhost',port=6379,db=0)
            
        result=R.get("username")

            
        
        password=R.get("password")
        
        
    
             

       

        
        if  result==username:
            
            
        
            

            #Compare Passwords
            if bcrypt.check_password_hash(hashed_password,password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return render_template('loginpage.html')
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
    
            
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)


    return render_template('login.html')

class module(Form):

        words =StringField('Enter the words')
        display =SubmitField('submit')
        

@app.route('/module1', methods=['GET', 'POST'])
def module1():
    words=None
    pluralwords=None

    form=module(request.form)

    if request.method == 'POST':
        words=request.form['words']
        pluralwords=p.plural(words)
    return render_template('module1.html',form=form,words=words,pluralwords=pluralwords)

    
if __name__=='__main__':
    app.secret_key = 'super secret key'

    app.run(debug=True)