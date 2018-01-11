from app import application, db
from app.models import User, Post

# can create a shell context to auto-import certain things when running flask shell


@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}