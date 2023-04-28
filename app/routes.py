from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        orbital_period=request_body["orbital_period"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()

    for planet in planets:
        planets_response.append(planet.make_planet_dict())

    return jsonify(planets_response)