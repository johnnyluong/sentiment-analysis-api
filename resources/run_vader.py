from flask_restful import Resource

class runVader(Resource):
    def get(self, content):
        if content is not None:
            return "Content Posted ...", 200
        return "Content was invalid ...", 404