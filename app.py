from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from controllers.items_controller import items_bp

app = Flask(__name__)

app.config['SECRET_KEY'] = 'root';
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(items_bp, url_prefix='/api')

db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(50))
	email = db.Column(db.String(120))
	
admin = Admin(app,name = 'Admin Interface')
admin.add_view(ModelView(User,db.session))

#@app.route('/')
#def home():
#	return "Hello, Flask on Lubuntu"

if __name__ == "__main__":
	with app.app_context():
		db.create_all()
		app.run(debug=True)
