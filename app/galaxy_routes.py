from flask import Blueprint, jsonify, make_response, request, abort
from app.models.galaxy import Galaxy
from app.models.planet import Planet
from app import db
from .routes import validate_model

bp = Blueprint("galaxy", __name__, url_prefix="/galaxy")


# CREATE ENDPOINT
@bp.route("", methods=["POST"])
def create_galaxy():
  request_body = request.get_json()
  new_galaxy = Galaxy(name=request_body["name"])

  db.session.add(new_galaxy)
  db.session.commit()

  return make_response(f"galaxy {new_galaxy.name} successfully created", 201)


# GET ONE ENDPOINT
@bp.route("/<galaxy_id>", methods=["GET"])
def handle_one_galaxy(galaxy_id):
  galaxy = validate_model(Galaxy, galaxy_id)
  galaxy = Galaxy.query.get(galaxy_id)
  galaxy_dict = {"id": galaxy.id, "name": galaxy.name}

  return jsonify(galaxy_dict), 200


@bp.route("/<galaxy_id>/planets", methods=["POST"])
def create_planet(galaxy_id):
    galaxy = validate_model(Galaxy, galaxy_id)
    galaxy = Galaxy.query.get(galaxy_id)
    request_body = request.get_json()

    new_planet = Planet.from_dict(request_body, galaxy)
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created with Galaxy {galaxy.name}", 201)


#GET ALL PLANETS BY GALAXY ENDPOINT
@bp.route("/<galaxy_id>/planets", methods=["GET"])
def handle_planets_from_galaxy(galaxy_id):
    galaxy = validate_model(Galaxy, galaxy_id)
    # galaxy = Galaxy.query.get(galaxy_id)

    planets_response = []
    for planet in galaxy.planets:
        planets_response.append(planet.make_planet_dict())

    return jsonify(planets_response), 200


    




