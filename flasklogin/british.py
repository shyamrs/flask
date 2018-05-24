from flask import Flask,render_template,flash,request,redirect,url_for
from werkzeug import secure_filename
import inflect

p=inflect.engine()

app=Flask(__name__)



@app.route('/')
def index():
     return render_template('home.html')


@app.route('/module1_plu', methods=['GET','POST'])
def module1_plu():
    if request.method == 'POST':
      f = request.files['myfile']
      f.save(secure_filename(f.filename))
      
      
      file_content = f.readlines('')
      pluralwords=p.plural(file_content)

      return render_template('module1_plu.html',pluralwords=pluralwords)

    return render_template('module1_plu.html')  	

    

    
         


if __name__=='__main__':
    app.secret_key = 'super secret key'

    app.run(debug=True)
