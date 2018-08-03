from app import app, db
from app.models import User, Post

app.run(host='0.0.0.0')

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}