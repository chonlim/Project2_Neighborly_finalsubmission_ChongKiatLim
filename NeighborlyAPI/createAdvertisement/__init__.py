import azure.functions as func
import pymongo
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

	request = req.get_json()

	if request:
		try:
			url = os.environ["MyMongoDbConnectionString"]  # TODO: Update with appropriate MongoDB connection information --> DONE
			client = pymongo.MongoClient(url)
			database = client['mongodb'] # TODO: Change the MongoDB name --> DONE
			collection = database['advertisements'] # TODO: Change the collection name --> DONE

			rec_id1 = collection.insert_one(eval(request))

			return func.HttpResponse(req.get_body())

		except ValueError:
			print("could not connect to mongodb")
			return func.HttpResponse('Could not connect to mongodb', status_code=500)

	else:
		return func.HttpResponse(
			"Please pass name in the body",
			status_code=400
		)