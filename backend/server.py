# # # # backend/server.py
# # # import tornado.ioloop
# # # import tornado.web
# # # import pymongo
# # # import json
# # # from bson import ObjectId
# # # from tornado_cors import CorsMixin

# # # # MongoDB connection
# # # client = pymongo.MongoClient("mongodb://localhost:27017/")
# # # db = client["contract_management"]
# # # users_collection = db["users"]
# # # contracts_collection = db["contracts"]

# # # # JSON encoder for MongoDB ObjectId
# # # class JSONEncoder(json.JSONEncoder):
# # #     def default(self, o):
# # #         if isinstance(o, ObjectId):
# # #             return str(o)
# # #         return super().default(o)

# # # # Login handler
# # # class LoginHandler(CorsMixin, tornado.web.RequestHandler):
# # #     CORS_ORIGIN = '*'  # Allow all origins (for development only)
# # #     CORS_METHODS = ['POST']  # Allow POST requests
# # #     CORS_HEADERS = ['Content-Type']  # Allow Content-Type header

# # #     def post(self):
# # #         data = json.loads(self.request.body)
# # #         username = data.get("username")
# # #         password = data.get("password")

# # #         user = users_collection.find_one({"username": username, "password": password})
# # #         if user:
# # #             self.write({"message": "Login successful", "user": user})
# # #         else:
# # #             self.set_status(401)  # Unauthorized
# # #             self.write({"message": "Invalid credentials"})

# # # # Contracts handler
# # # class ContractsHandler(CorsMixin, tornado.web.RequestHandler):
# # #     CORS_ORIGIN = '*'  # Allow all origins (for development only)
# # #     CORS_METHODS = ['GET']  # Allow GET requests
# # #     CORS_HEADERS = ['Content-Type']  # Allow Content-Type header

# # #     def get(self):
# # #         contracts = list(contracts_collection.find())
# # #         self.write(json.dumps(contracts, cls=JSONEncoder))

# # # # Application setup
# # # def make_app():
# # #     return tornado.web.Application([
# # #         (r"/api/auth/login", LoginHandler),
# # #         (r"/api/contracts", ContractsHandler),
# # #     ])

# # # # Start the server
# # # if __name__ == "__main__":
# # #     app = make_app()
# # #     app.listen(8888)
# # #     print("Server running on http://localhost:8888")
# # #     tornado.ioloop.IOLoop.current().start()







# # # backend/server.py
# # import tornado.ioloop
# # import tornado.web
# # import pymongo
# # import json
# # from bson import ObjectId
# # from tornado_cors import CorsMixin

# # # MongoDB Atlas connection
# # #connection_string = "mongodb+srv://techie1589:techie1589@cluster.e2akc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
# # connection_string  = "mongodb+srv://kartik:kartik@cluster.e2akc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"
# # client = pymongo.MongoClient(connection_string)
# # db = client["contract_management"]  # Use your database name
# # users_collection = db["users"]
# # contracts_collection = db["contracts"]

# # # JSON encoder for MongoDB ObjectId
# # class JSONEncoder(json.JSONEncoder):
# #     def default(self, o):
# #         if isinstance(o, ObjectId):
# #             return str(o)
# #         return super().default(o)

# # # Login handler
# # class LoginHandler(CorsMixin, tornado.web.RequestHandler):
# #     CORS_ORIGIN = '*'  # Allow all origins (for development only)
# #     CORS_METHODS = ['POST']  # Allow POST requests
# #     CORS_HEADERS = ['Content-Type']  # Allow Content-Type header

# #     def post(self):
# #         data = json.loads(self.request.body)
# #         username = data.get("username")
# #         password = data.get("password")

# #         user = users_collection.find_one({"username": username, "password": password})
# #         if user:
# #             self.write({"message": "Login successful", "user": user})
# #         else:
# #             self.set_status(401)  # Unauthorized
# #             self.write({"message": "Invalid credentials"})

# # # Contracts handler
# # class ContractsHandler(CorsMixin, tornado.web.RequestHandler):
# #     CORS_ORIGIN = '*'  # Allow all origins (for development only)
# #     CORS_METHODS = ['GET']  # Allow GET requests
# #     CORS_HEADERS = ['Content-Type']  # Allow Content-Type header

# #     def get(self):
# #         contracts = list(contracts_collection.find())
# #         self.write(json.dumps(contracts, cls=JSONEncoder))

# # # Application setup
# # def make_app():
# #     return tornado.web.Application([
# #         (r"/api/auth/login", LoginHandler),
# #         (r"/api/contracts", ContractsHandler),
# #     ])

# # # Start the server
# # if __name__ == "__main__":
# #     app = make_app()
# #     app.listen(8888)
# #     print("Server running on http://localhost:8888")
# #     tornado.ioloop.IOLoop.current().start()














# # backend/server.py
# import tornado.ioloop
# import tornado.web
# import pymongo
# import json
# from bson import ObjectId

# # MongoDB Atlas connection
# connection_string  = "mongodb+srv://kartik:kartik@cluster.e2akc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster"

# client = pymongo.MongoClient(connection_string)
# db = client["python-tornado"]  # Use your database name
# users_collection = db["users"]
# contracts_collection = db["contracts"]

# # JSON encoder for MongoDB ObjectId
# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return super().default(o)

# # Base handler to handle CORS
# class BaseHandler(tornado.web.RequestHandler):
#     def set_default_headers(self):
#         self.set_header("Access-Control-Allow-Origin", "*")
#         self.set_header("Access-Control-Allow-Headers", "Content-Type")
#         self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

#     def options(self):
#         # No body for OPTIONS requests
#         self.set_status(204)
#         self.finish()

# # Login handler
# class LoginHandler(BaseHandler):
#     def post(self):
#         data = json.loads(self.request.body)
#         username = data.get("username")
#         password = data.get("password")

#         user = users_collection.find_one({"username": username, "password": password})
#         if user:
#             self.write({"message": "Login successful", "user": user})
#         else:
#             self.set_status(401)  # Unauthorized
#             self.write({"message": "Invalid credentials"})

# # Contracts handler
# class ContractsHandler(BaseHandler):
#     def get(self):
#         contracts = list(contracts_collection.find())
#         self.write(json.dumps(contracts, cls=JSONEncoder))

# # Application setup
# def make_app():
#     return tornado.web.Application([
#         (r"/api/auth/login", LoginHandler),
#         (r"/api/contracts", ContractsHandler),
#     ])

# # Start the server
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8888)
#     print("Server running on http://localhost:8888")
#     tornado.ioloop.IOLoop.current().start()











# backend/server.py
import tornado.ioloop
import tornado.web
import pymongo
import json
from bson import ObjectId
from bson.json_util import dumps  # Use bson's dumps for MongoDB-specific types

# MongoDB Atlas connection
connection_string  = "mongodb+srv://kartik:kartik@python-tornado.e2akc.mongodb.net/?retryWrites=true&w=majority&appName=python-tornado"

# Function to check MongoDB connection
def check_mongodb_connection():
    try:
        # Attempt to connect to MongoDB
        client = pymongo.MongoClient(connection_string)
        # Ping the database to check if the connection is successful
        client.admin.command('ping')
        print("Database connected successfully!")
        return client
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        exit(1)  # Exit the application if the connection fails

# Check MongoDB connection and get the client
client = check_mongodb_connection()
db = client["python-tornado"]  # Use your database name
users_collection = db["users"]
contracts_collection = db["contracts"]

# Base handler to handle CORS
class BaseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
        self.set_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")

    def options(self):
        # No body for OPTIONS requests
        self.set_status(204)
        self.finish()

# Login handler
class LoginHandler(BaseHandler):
    def post(self):
        data = json.loads(self.request.body)
        username = data.get("username")
        password = data.get("password")

        user = users_collection.find_one({"username": username, "password": password})
        if user:
            # Convert ObjectId to string for JSON serialization
            user["_id"] = str(user["_id"])
            self.write({"message": "Login successful", "user": user})
        else:
            self.set_status(401)  # Unauthorized
            self.write({"message": "Invalid credentials"})

# Contracts handler
class ContractsHandler(BaseHandler):
    def get(self):
        contracts = list(contracts_collection.find())
        # Use bson's dumps to handle MongoDB-specific types
        self.write(dumps(contracts))

# Application setup
def make_app():
    return tornado.web.Application([
        (r"/api/auth/login", LoginHandler),
        (r"/api/contracts", ContractsHandler),
    ])

# Start the server
if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()