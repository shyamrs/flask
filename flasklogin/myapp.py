from flask import Flask,render_template,flash,request,redirect,url_for,session,logging
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
import redis



app=Flask(__name__)






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


        
        
        
        # connection
        R = redis.StrictRedis( host='localhost', port=6379, password='1916')
        print 'set_username',R.set("username","shyamsr")
        print 'username:', R.get("username")
        print 'set_password',R.set("password","123456")
        print 'password:', R.get("password")

        
       
                       
    
             
                     
    
            



        if  R.StringField > 0:
            
            
        
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('loginpage'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
    
            
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)


    return render_template('login.html')


 








if __name__=='__main__':
    app.run(debug=True)