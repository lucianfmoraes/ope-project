import pymongo
from flask import Flask, jsonify
app = Flask(__name__)


app.config.from_pyfile('../settings.py')


class Database:

    def __init__(self, collection):
        client = pymongo.MongoClient(
            "mongodb+srv://{}:{}@cluster-01.iozzj.mongodb.net/Cluster-01?retryWrites=true&w=majority".format(app.config.get("DB_USER"), app.config.get("DB_PASS")))
        self.db = client['ope-db']
        self.col = client['ope-db'].collection

    def get_all(self, col):
        data = []
        res = self.db[col].find(projection={'_id': False})
        for i in res:
            data.append(i)
        return jsonify(data)

    def get_user(self, user):
        res = jsonify(self.db.users.find_one(user, projection={"_id": False}))
        return res

    def create_user(self, user):
        res = str(self.db.users.insert_one(user).inserted_id)
        return res