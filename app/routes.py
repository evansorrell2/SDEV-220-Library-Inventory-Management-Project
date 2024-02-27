#Routing and view functions
from app import app


@app.route('/')
def home():
    return 'Welcome to the library management system!'