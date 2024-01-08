from flask import Flask
from flask_smorest import Api


from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app=Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"



api = Api(app)      #Connects flask smorest extension to the flask app.



api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)




# @app.route("/store")  # get_stores = app.get("/store")(get_stores)            # THis is same as the below decorator.
# def get_stores():
#     return {"Warehouse" : stores}

# @app.get("/store")  # get_stores = app.get("/store")(get_stores)
# def get_stores():
#     return {"Warehouse" : list(stores.values())}



# @app.post("/store")
# def create_store():
#     store_data = request.get_json()         # store_data is received in a dictionary form
    
#     if "Name" not in store_data:
#         abort(400, message = "Bad Request. Ensure 'Name' is included in the JSON payload.")

#     for i in stores.values():
#         if store_data["Name"] == i["Name"]:
#             abort(400, f"Store already exists")

#     store_id = uuid.uuid4().hex
#     new_store = {**store_data , "id" : store_id}
#     stores[store_id]=new_store
#     return new_store , 201

# @app.post("/item")
# def create_item():                          # Item consists of Price, Name and item id
#     item_data = request.get_json()

#     if ("Price" not in item_data or "store_id" not in item_data or "Name" not in item_data):
#         abort(404, message="Bad Request. Ensure 'Price', 'store_id' and 'Name' is included in JSON Payload")

#     for i in items.values():
#         if item_data["Name"] == i["Name"] and item_data["store_id"] == i["store_id"]:
#             abort(400, message="Item already present")           

#     if item_data["store_id"] not in stores:
#         abort(404, message= "Store not found")
#     item_id = uuid.uuid4().hex
#     new_item = {**item_data, "id" : item_id}
#     items[item_id] = new_item
#     return new_item, 201

# @app.get("/item")
# def get_item():
#     return {"Items" : list(items.values())}
    
# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort (404,message = "Not Found")
    
# @app.get("/item/<string:item_id>")
# def get_item1(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort (404,message = "Not Found")

# @app.delete("/item/<string:item_id>")
# def delete(item_id):
#     try:
#         del items[item_id]
#         return {"Message" : "Item deleted"}
#     except KeyError:
#         abort(404,Message = "Item not present to be deleted")

# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data = request.get_json()
#     if "Price" not in item_data or "Name" not in item_data:
#         abort(400, message="Bad Request. Ensure 'Price' and 'Name' is included in JSON payload.")
#     # new_data ={"Name" : item_data["Name"], "Price" : item_data["Price"], "item_id" : item_id}
#     # items[item_id] = new_data
#     try:
#         copy_item = items[item_id]
#         copy_item |= item_data                      # This signs mean the dictionary is copied from item_data to copy_data.
#         return copy_item,201
#     except KeyError:
#         abort(404, message="Item not present.")

# @app.delete("/store/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"Message" : "Store deleted "}
#     except KeyError:
#         abort(404, message="Store not present to be deleted")
