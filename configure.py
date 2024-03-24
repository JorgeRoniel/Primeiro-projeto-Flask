from routes.home import home_routes
from routes.clientes import clientes_routes
from database.database import db
from database.models.clientes import Cliente

def configureAll(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(home_routes)
    app.register_blueprint(clientes_routes, url_prefix='/clientes')

def configure_db():
    db.connect()
    db.create_tables([Cliente])