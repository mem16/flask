from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

@app.route('/')
def home():
    return "hello world"

# returns all stores
@app.route('/stores')
def get_stores():
    """
    routing /stores
    returns stores
    """
    return jsonify({"stores":stores})

# adds store in stores
# takes in store
@app.route('/store',methods=['POST'])
def create_store():
    """
    routing /store , Method POST
    returns added store
    """
    request_data = request.get_json()
    for store in stores:
        if store['name']==request_data['store']:
            return jsonify("we already have a store with that name")
    new_store = {
            'name':request_data['store'],
            'items':[]
            }
    stores.append(new_store)
    return jsonify(new_store)

# fetches store from stores
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify ({'message': 'store not found'})

# store item in stores
# takes in store,name,price
@app.route('/store/item' , methods=['POST'])
def create_item_in_store():
    request_data = request.get_json()
    store_name = request_data['store']
    for store in stores:
        if store['name'] == store_name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify ({'message' :'store not found'})

# deletes the item from a store in stores
# takes in store,name
@app.route('/store/item/delete' , methods=['POST'])
def delete_item_in_store():
    request_data = request.get_json()
    store_name = request_data['store']
    for store in stores:
        if store['name'] == store_name:
            flag_deleted_item = 0
            for item in store['items']:
                if item['name']==request_data['name']:
                    flag_deleted_item = 1
                    store['items'].remove(item)
            if flag_deleted_item == 1:
                return jsonify("deleted item")
            else:
                return jsonify("item not found")
    return jsonify ({'message' :'store not found'})

# updates the price of an item in a store
# takes in store,name,price
@app.route('/store/item/update' , methods=['POST'])
def update_item_in_store():
    request_data = request.get_json()
    store_name = request_data['store']
    for store in stores:
        if store['name'] == store_name:
            flag_updated_item = 0
            for item in store['items']:
                if item['name']==request_data['name']:
                    flag_updated_item = 1
                    item['price']=request_data['price']
            if flag_updated_item == 1:
                return jsonify("updated item")
            else:
                return jsonify("item not found")
    return jsonify ({'message' :'store not found'})

if __name__ == "__main__":
    app.run(port=5001)
