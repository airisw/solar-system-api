from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, make_response, request, abort

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_planets():
    query_params = request.args.get("name")

    planet_query = Planet.query

    if query_params:
        planet_query = Planet.query.filter_by(name=query_params)

    planets_response = []

    for planet in planet_query:
        planets_response.append(planet.make_planet_dict())

    return jsonify(planets_response)


#GET ONE ENDPOINT
@bp.route("/<id>", methods = ["GET"])
def handle_planet(id):
    planet = validate_model(Planet, id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "orbital_period": planet.orbital_period
    }


#UPDATE ONE ENDPOINT
@bp.route("/<id>", methods = ["PUT"])

def update_planet(id):
    planet = validate_model(Planet, id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.orbital_period = request_body["orbital_period"]
    
    db.session.commit()

    return make_response(f"Planet {planet.name} was successfully updated", 200)


#DELETE ONE ENDPOINT
@bp.route("/<id>", methods = ["DELETE"])
def delete_planet(id):
    planet = validate_model(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.name} successfully deleted", 200)

#HELPER FUNCTION
def validate_model(cls, id):
    try:
        id = int(id)
    except:
        abort(make_response({"message": f"{id} was invalid"}, 400))
    
    model = cls.query.get(id)

    if not model:
        abort(make_response({"message": f"{cls.__name__} with id {id} was not found"}, 404))

    return model
