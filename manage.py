from flask_script import Manager
from temper_app import bootstrap_app

app = bootstrap_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
