from flask_blog import app,uploaded_images
from flask import flash,render_template,redirect,url_for,session,abort,request
from blog.form import *
from flask_blog import db
from author.models import Author
from blog.models import *
from author.decorators import login_required
import bcrypt

POST_PER_PAGE = app.config['POST_PER_PAGE']
COMMENT_PER_PAGE = 5



#####home page
@app.route('/')
@app.route('/index')
@app.route('/index/<int:page>')
def index(page=1):
    blogs = Blog_Post.query.filter_by(live=True).order_by(Blog_Post.publish_date.desc()).paginate(page,POST_PER_PAGE,False)  ##### all the blogs in descending order
    return render_template('blog/index.html',blogs=blogs)
    
    
@app.route('/search',methods=['GET','POST'])
def search():
    result = None
    keyword = ''
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        results = Blog_Post.query.msearch(keyword,fields=['title'],limit=20)
    return render_template('blog/search.html',results=results,keyword=keyword)
     

    
    
    
#####  personal page 
@app.route('/home/<username>')
@app.route('/home/<username>/<int:page>')
@login_required 
def home(username,page=1):
    list_of_blog = []
    mess = ''
    
    user = Author.query.filter_by(username=username).first()
    if user == None:
        return "There is no such user"
    List = Blog_Post.query.with_parent(user) 
    Blog_list = Blog_Post.query.with_parent(user).filter_by(live=True).order_by(Blog_Post.publish_date.desc()).paginate(page,POST_PER_PAGE,False)
    
    if List.count()  == 0:
        mess = '%s has no blogs yet'%username
    else:
        mess = '%s has %s blogs' % (username,str(List.count()))
        
    return render_template('blog/home.html',username=username,mess=mess,Blog_list=Blog_list)
    
    
###### perosnal articles page
@app.route('/article/<username>/<blog>',methods=['GET','POST'])
@app.route('/article/<username>/<blog>/<int:page>',methods=['GET','POST'])
def article(username,blog,page=1):
    ##page = request.args.get('page',1,type=int) 
    
    article_ = Blog_Post.query.filter_by(title=blog).first_or_404()
    author = Author.query.filter_by(username=session.get('username',None)).first()
    
    ##comment = Comment.query.with_parent(article_).order_by(Comment.publish_date.asc()).paginate(page,COMMENT_PER_PAGE,False)
    title = article_.title
    text = article_.body
    
    
    form = CommentForm()
    if form.validate_on_submit():
        if author!=None:
            new_comment = Comment(form.body.data,
                              author,
                              article_)
            db.session.add(new_comment)
            db.session.flush()
            
            if new_comment.id and author.id and article_.id:
                db.session.commit()
                flash("comment has been post")
                return redirect(url_for('article',username=article_.author.username,blog=article_.title,page= (article_.comments.count())//COMMENT_PER_PAGE  ))
        else:
            flash('You must log in')
    if page == -1:
        page = (article_.comments.count())//COMMENT_PER_PAGE        
    
    comments = Comment.query.with_parent(article_).order_by(Comment.publish_date.asc()).paginate(page,COMMENT_PER_PAGE,False)    
            
                          
        
    
    
    return render_template('/blog/article.html',username=username,article=article_,comments=comments,form=form)


##########write articles page    
@app.route('/write',methods=['GET','POST'])
@login_required
def write():
    message = ''
    error = ''
    user = Author.query.filter_by(username = session['username']).first()
    form = ArticleForm()
    if form.validate_on_submit():
        image = request.files.get('image')
        filename = None
        try:
            filename = uploaded_images.save(image)
        except:
            flash("Can not upload image")
            
        
        post = Blog_Post(
            form.title.data,
            user,
            form.body.data,
            filename
        )
        db.session.add(post)
        db.session.flush()
        
        if user.id and post.id:
            db.session.commit()
            flash("new blog created")
            return redirect(url_for('home',username=user.username))
            
        else:
            error = 'Error creating blog'
            db.session.rollback()
    return render_template('blog/write.html',username=user.username,form=form,error=error)        
            
    
    
    
@app.route('/delete/<int:post_id>')
def delete(post_id):
    post = Blog_Post.query.filter_by(id=post_id).first_or_404()
    user = post.author.username
    post.live = False
    db.session.commit()
    flash("article deleted")
    return redirect(url_for('home',username=user))
    
    


    


@app.route('/setup',methods=['GET','POST'])
def setup():
    error = ''
    form = SetupForm()
    if form.validate_on_submit():
        author =Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            form.password.data,
            True
            )
        db.session.add(author)
        db.session.flush()
        
        if author.id:
            blog = Blog(
                form.name.data,
                author.id)
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        if author.id and blog.id:
            db.session.commit()
            #######flash message in admin.html
            flash("Blog created")
            return redirect(url_for('admin'))
        else:
            db.session.rollback()
            error = "Error creating blog"
            
    
    
    return render_template('blog/setup.html',form=form,error=error)
    





