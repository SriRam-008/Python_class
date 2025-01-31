from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/home')
def wel():
    return "I'm Home!"

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    data = None 
    if request.method == 'POST':
        data = request.json
        return {"message": "Data received", "data": data}
    
    
    return {"message": "Send a POST request with JSON data"}

@app.route('/update/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    return {"message": f"Item {item_id} updated"}
@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return {"message": f"Item {item_id} deleted"}

if __name__ == '__main__':
    app.run(debug=True)
