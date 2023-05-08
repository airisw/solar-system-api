from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    orbital_period = db.Column(db.Integer)
    galaxy_id = db.Column(db.Integer, db.ForeignKey('galaxy.id'))
    galaxy = db.relationship("Galaxy", back_populates="planets")

    def make_planet_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            orbital_period=self.orbital_period
        )
    
    @classmethod
    def from_dict(cls, data_dict, galaxy):
        return cls(name=data_dict["name"],
                   description=data_dict["description"],
                   orbital_period=data_dict["orbital_period"],
                   galaxy_id=data_dict["galaxy_id"],
                   galaxy=galaxy)