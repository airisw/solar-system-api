from app import db

class Planet(db.Model):
    id = db.column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    orbital_period = db.Column(db.Integer)

    def make_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            orbital_period=self.orbital_period
        )