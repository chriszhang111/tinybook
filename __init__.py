from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flaskext.markdown import Markdown
from flask_uploads import UploadSet, configure_uploads,IMAGES
from flask_bootstrap import Bootstrap
from flask_msearch import Search
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('settings')
Bootstrap(app)
db = SQLAlchemy(app)
mail = Mail(app)

migrate = Migrate(app,db)
Markdown(app)
search = Search(db=db)
search.init_app(app)

uploaded_images = UploadSet('images',IMAGES)
configure_uploads(app,uploaded_images)




from blog import view
from author import view