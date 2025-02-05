from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Set up SQLite URI (you can change the database location if needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications for performance

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Menu model (equivalent to the table in the database)
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    Item = db.Column(db.String(100), nullable=False)  # Item name
    Price = db.Column(db.Float, nullable=False)  # Price of the item

    def __repr__(self):
        return f"<MenuItem {self.Item}>"

# Create the database tables (run once to initialize the database)
with app.app_context():
    db.create_all()

# Initialize the API
api = Api(app)

# Define the resource class for the menu
class MENU(Resource):
    def get(self):
        # Get all menu items from the database
        items = MenuItem.query.all()
        menu_list = [{'Item': item.Item, 'Price': item.Price} for item in items]
        return {"Items": menu_list}

    def post(self):
        data = request.get_json()
        Item = data.get('Item')
        Price = data.get('Price')

        # Create a new menu item and add it to the database
        new_item = MenuItem(Item=Item, Price=Price)
        db.session.add(new_item)
        db.session.commit()
        return {"message": f"Item {Item} with price {Price} added successfully!"}, 201

    def delete(self):
        data = request.get_json()
        Item = data.get('Item')

        # Find the item in the database and remove it
        item_to_remove = MenuItem.query.filter_by(Item=Item).first()
        if item_to_remove:
            db.session.delete(item_to_remove)
            db.session.commit()
            return {"message": f"Item {Item} removed successfully!"}, 200
        return {"message": f"Item {Item} not found!"}, 404

# Add the resource to the API
api.add_resource(MENU, '/menu')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
