from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, orbital_period):
        self.id = id
        self.name = name
        self.description = description
        self.orbital_period = orbital_period

    def generate_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "orbital_period": self.orbital_period
        }

planets = [
    Planet(1, "Mercury", "Mercury is the first planet from the Sun and the only one in the Solar System without a considerable atmosphere.", 88),
    Planet(2, "Venus", "Venus is the second planet from the Sun and the only terrestrial object in the Solar System other than Earth that has a substantial atmosphere and is almost as massive and large as Earth.", 225),
    Planet(3, "Earth", "Earth is the third planet from the Sun and the only place known in the universe where life has originated and found habitability.", 365),
    Planet(4, "Mars", "Mars is the fourth planet from the Sun and the third largest and massive terrestrial object in the Solar System.", 687),
    Planet(5, "Jupiter", "Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass more than two and a half times that of all the other planets in the Solar System combined, and slightly less than one one-thousandth the mass of the Sun.", 4380),
    Planet(6, "Saturn", "Saturn is the sixth planet from the Sun and the second-largest in the Solar System, after Jupiter. It is a gas giant with an average radius of about nine and a half times that of Earth.", 10585),
    Planet(7, "Uranus", "Uranus is the seventh planet from the Sun. Uranus has the third-largest planetary radius and fourth-largest planetary mass in the Solar System.", 30660),
    Planet(8, "Neptune", "Neptune is the eighth planet from the Sun and the farthest known planet in the Solar System. It is the fourth-largest planet in the Solar System by diameter, the third-most-massive planet, and the densest giant planet.", 60225)
]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("/<id>", methods= ["GET"])
def handle_planet(id):
    id = validate_id(id)

    for planet in planets:
        if planet.id == id:
            return planet.generate_dict()

    abort(make_response({"message": f"Planet with {id} was not found"}, 404))

def validate_id(id):
    try:
        id = int(id)
        return id
    except:
        abort(make_response({"message": f"{id} was invalid"}, 400))

@bp.route("", methods=["GET"])
def handle_planets():
    result_list = []

    for planet in planets:
        result_list.append(planet.generate_dict())

    return jsonify(result_list)