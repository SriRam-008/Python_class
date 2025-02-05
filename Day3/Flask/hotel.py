from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class MENU(Resource):
    list = []

    def get(self):
        return {"Items": MENU.list}

    def post(self):
        data = request.get_json()
        Item = data.get('Item')  
        Price = data.get('Price')  
        MENU.list.append({'Item': Item, 'Price': Price}) 
        return {"message": f"Item {Item} with price {Price} added successfully!"}, 201

    def delete(self):
        data = request.get_json()
        Item = data.get('Item')
       
        for menu_item in MENU.list:
            if menu_item['Item'] == Item:
                MENU.list.remove(menu_item)
                return {"message": f"Item {Item} removed successfully!"}, 200
        return {"message": f"Item {Item} not found!"}, 404


api.add_resource(MENU, '/menu')

if __name__ == '__main__':
    app.run(debug=True)
