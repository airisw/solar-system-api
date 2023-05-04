from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"],
                   description=data_dict["description"],
                   orbital_period=data_dict["orbital_period"])