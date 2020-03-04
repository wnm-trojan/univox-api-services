"""
    @author - Nadeen Gamage
    @email - nadeengamage@gmail.com
    @web - www.nadeengamage.com
    @project - UnivoX

    Description - Application users.
"""

from app import app, db

class User(db.Model):
    __tablename__ = 'tbl_users'

    id = db.Column(db.Integer, primary_key=True)
    x_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    role_id = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    created_by = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
