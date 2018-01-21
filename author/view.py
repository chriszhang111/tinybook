from flask_blog import app,db
from flask import render_template,redirect,url_for,session,request,flash
from author.form import RegisterForm,LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    error = None
    
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next',None)
    if form.validate_on_submit():
        author = Author.query.filter_by(username=form.username.data).first()
        if author != None:
            session['username'] = form.username.data
            if bcrypt.hashpw(form.password.data,author.password) == author.password:
            ##if author.password == form.password.data:
                if session.get('next')!=None:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:    
                    return redirect(url_for('home',username=session['username']))
            else:
                error = 'Wrong password'
        else:
            error = 'User does not exist'
    
    
    
    return render_template('author/login.html',form=form,error=error)
    
    
    
    

@app.route('/register',methods=['GET','POST'])
def register():
    error = ''
    form = RegisterForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data,salt)
        user = Author(
            '',
            form.email.data,
            form.username.data,
            hashed_password,
            True
            )
            
        if Author.query.filter_by(username=user.username).first() != None:
            error = 'User already exist'
        else:
            
          db.session.add(user)  
          db.session.flush()
          if user.id:
              db.session.commit()
              flash("registered successfully")
            #######flash message in admin.html
          else:
              flash("There is something w")
              
        
    return render_template('author/register.html',form=form,error=error)
    
@app.route('/success')
def success():
    return 'registered successfully'
    
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('index'))