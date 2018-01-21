from flask_wtf import Form
from wtforms import validators,StringField, PasswordField,TextAreaField
from wtforms.fields.html5 import EmailField
from author.form import RegisterForm
from flask_wtf.file import FileField, FileAllowed


class SetupForm(RegisterForm):
    name = StringField('Blog name',[
        validators.Required(),
        validators.Length(max=80)
        
        ])
class ArticleForm(Form):
    title = StringField('Title',[
        validators.Required(),
        validators.Length(max=80)])
    
    body = TextAreaField('Context',[
        validators.Required()])
    
    image = FileField('Image', validators=[
        
        FileAllowed(['jpg','png','jpeg','gif'],'image only')
        ])
        
class CommentForm(Form):
    body = TextAreaField('Comment',[validators.Required(),validators.Length(max=140)])
    
class SearchForm(Form):
  search = TextAreaField('search', validators = [validators.Required()])    
    
      