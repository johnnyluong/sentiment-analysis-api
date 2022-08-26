from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from resources.vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, required=True, help='Content required.',location='form')

class SentimentAnalysis(Resource):
    def post(self):
        args = parser.parse_args()
        text = args['text']
        analyzer = SentimentIntensityAnalyzer()
        vs = analyzer.polarity_scores(text)
        if vs['neu'] > 0.85:
          #content was approved -> post to database
          return vs, 200
        else:
          #content rejected -> inform user
          return "does not meet neutrality requirement", 404

api.add_resource(SentimentAnalysis, "/api/v1/")

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5444 ,debug=True)
  # app.run()


