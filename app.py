from flask import Flask
from flask_restful import Api
from resources.product import Products, Product

app = Flask(__name__)
api = Api(app)

api.add_resource(Products,'/products')
api.add_resource(Product,'/products/<int:codigo>')

if __name__ == '__main__':
    app.run(debug=True)