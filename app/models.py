from datetime import datetime
from app import db

class TimestampMixin(object):
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Book(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    author = db.Column(db.String(100), nullable=False, index=True)
    category = db.Column(db.String(50), nullable=False, index=True)
    is_borrowed = db.Column(db.Boolean, default=False)
    return_date = db.Column(db.Date, nullable=True)

class Video(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    category = db.Column(db.String(50), nullable=False, index=True)
    director = db.Column(db.String(100), nullable=False, index=True)
    is_borrowed = db.Column(db.Boolean, default=False)
    return_date = db.Column(db.Date, nullable=True)

class Game(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, index=True)
    category = db.Column(db.String(50), nullable=False, index=True)
    platform = db.Column(db.String(50), nullable=False, index=True)
    is_borrowed = db.Column(db.Boolean, default=False)
    return_date = db.Column(db.Date, nullable=True)

class User(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))

class BorrowRecord(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_type = db.Column(db.String(50), nullable=False)  # "book", "video", "game"
    item_id = db.Column(db.Integer, nullable=False)
    borrow_date = db.Column(db.Date, nullable=False)
    expected_return_date = db.Column(db.Date, nullable=False)
    actual_return_date = db.Column(db.Date)
    
class Review(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_type = db.Column(db.String(50), nullable=False)  # "book", "video", "game"
    item_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
    
    def set_rating(self, rating):
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 1 and 5")
