from flask_sqlalchemy import SQLAlchemy
from server import *
db = SQLAlchemy(server)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database5.sqlite3'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
server.config['SECRET_KEY'] = "random string"

class Page_index(db.Model):
    __tablename__='ProductTShirt'
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Colimn(db.String(999)) 
    description  = db.Colimn(db.String(999)) 
    prix         = db.Colimn(db.String(999))
    filename     = db.Column(db.String(999))
    img          = db.Column(db.BLOB)
    def __init__(self,img,filename,title,description,prix):
        self.img        = img
        self.filename   = filename
        self.title      = title
        self.description= description
        self.prix       = prix
