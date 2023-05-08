from app import db 

class Galaxy(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    planets = db.relationship("Planet", back_populates="galaxy")