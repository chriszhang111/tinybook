from flask_blog import db,uploaded_images
from datetime import datetime


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    admin = db.Column(db.Integer, db.ForeignKey('author.id'))
    #posts = db.relationship('Blog_Post',backref='blog',lazy='dynamic')
    
    def __init__(self,name,admin):
        self.name = name
        self.admin = admin
    
    def __repr__(self):
        return '<Blog %r>' % self.name
        


class Blog_Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    ##blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'))
    body = db.Column(db.Text)    
    image = db.Column(db.String(255))
    slug = db.Column(db.String(256),unique=True)
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)
    category = db.Column(db.String(70))
    comments = db.relationship('Comment',backref='blog__post',lazy='dynamic')
    
    __searchable__ = ['title','body']    
    
    
    @property
    def imgsrc(self):
        return uploaded_images.url(self.image)
    
    def __init__(self,title,author,body,image=None,slug=None,publish_date=None,live=True,category=None):
        self.title = title
        self.author_id = author.id
        ##self.blog_id = blog.id
        self.body = body
        self.image = image
        if publish_date == None:
            self.publish_date = datetime.utcnow()
        else:
            self.publish_date = publish_date
        
        self.live = live
        self.category = category
        
        
    def __repr__(self):
        return '<Blog article:%r>' % self.title
        
        

class Comment(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    
    
    body = db.Column(db.Text)
    ########
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blog__post.id'))
    publish_date = db.Column(db.DateTime)
    live = db.Column(db.Boolean)
    
    def __init__(self,body,author,blog,publish_date=None,live=True):
        self.body = body
        self.author_id = author.id
        self.blog_id = blog.id
        self.publish_date = datetime.utcnow()
        self.live = live
        
    def __repr__(self):
        return '<Comment:%r>' % self.id
        