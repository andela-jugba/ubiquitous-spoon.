from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import Book, Category
import os

app = create_app(os.getenv('CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, Book=Book, Category=Category)
    
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    '''
    Runs unit test
    '''
    from subprocess import call
    call(['nosetests','-v',
         '--with-coverage', '--cover-package=app', '--cover-branches',
         '--cover-erase', '--cover-html', '--cover-html-dir=cover'])

@manager.command
def deploy():
    from flask_migrate import upgrade
    
    upgrade()
    
    
if __name__ == '__main__':
    manager.run()
