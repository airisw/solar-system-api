import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_planet(app):
    planet = Planet(
        name="Planet 1",
        description="description 1",
        orbital_period=10
    )
    db.session.add(planet)
    db.session.commit()
    return planet

@pytest.fixture
def two_planets(app):
    planet_1 = Planet(
        name="Planet 1",
        description="description 1",
        orbital_period=10
    )

    planet_2 = Planet(
        name="Planet 2",
        description="description 2",
        orbital_period=20
    )

    db.session.add_all([planet_1, planet_2])
    db.session.commit()
    return [{
                "name": planet_1.name,
                "description": planet_1.description,
                "orbital_period": planet_1.orbital_period
                },
             {
                "name": planet_2.name,
                "description": planet_2.description,
                "orbital_period": planet_2.orbital_period
             }]