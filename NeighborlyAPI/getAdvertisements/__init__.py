import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

	try:
		url = os.environ["MyMongoDbConnectionString"]  # TODO: Update with appropriate MongoDB connection information --> DONE
		client = pymongo.MongoClient(url)
		database = client['mongodb'] # TODO: Change the MongoDB name --> DONE
		collection = database['advertisements'] # TODO: Change the collection name --> DONE


		result = collection.find({})
		result = dumps(result)

		return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
	except:
		print("could not connect to mongodb")
		return func.HttpResponse("could not connect to mongodb",
								 status_code=400)

