from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
import os

app = create_app(os.getenv('CONFIG', 'default'))
manager = Manager(app)
migrate = Migrate(app)

def make_shell_context():
    return dict(app=app, db=db)
    
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    '''
    Runs unit test
    '''
    from subprocess import call
    call(['nostests','-v',
         '--with-coverage', '--cover-package=app', '--cover-branches',
         '--cover-erase', '--cover-html', '--cover-html-dir=cover'])

if __name__ == '__main__':
    manager.run()
