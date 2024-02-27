#Application startup script
from app import app, db
from app.models import Book, Video, Game, User, BorrowRecord, Review  # make sure to import models before creating shell context

# Create shell context
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Book': Book, 'Video': Video, 'Game': Game, 'User': User, 'BorrowRecord': BorrowRecord, 'Review': Review}

if __name__ == '__main__':
    app.run(debug=True)
