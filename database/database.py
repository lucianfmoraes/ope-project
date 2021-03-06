import pymongo
from flask import jsonify


class Database:

    def __init__(self, collection):
        conex = "mongodb+srv://admin:rootadmin@cluster-01.iozzj.mongodb.net/Cluster-01?retryWrites=true&w=majority"
        client = pymongo.MongoClient(conex)
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
