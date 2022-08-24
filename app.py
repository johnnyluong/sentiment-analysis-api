from flask import Flask
from flask_restful import Api

from resources.run_vader import runVader

app = Flask(__name__)
api = Api(app)

api.add_resource(runVader, "/vader/<string:content>")

if __name__ == "__main__":
  app.run()