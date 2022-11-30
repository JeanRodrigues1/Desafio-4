from flask import Flask, url_for, render_template
from .database import create_database, create_table_contact

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mulinhas'

    from .routes import routes
    app.register_blueprint(routes, url_prefix='/')

    try: create_database()
    except: pass
    
    try: create_table_contact()
    except: pass 

    return app