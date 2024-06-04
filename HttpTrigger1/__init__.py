import logging
import json
import logging
import azure.functions as func
from src.services.prediction_pipeline import predictionPerform

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('id')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('id')

    if name:
       # Call predictionPerform function to get the result
        result = predictionPerform(name)

        # if isinstance(result, str):  # If predictionPerform returns a string (indicating an error)
        #     return func.HttpResponse(
        #         json.dumps({"error": result}),
        #         status_code=400,
        #         mimetype='application/json'
        #     )
        # else:  # If predictionPerform returns a dictionary (indicating successful prediction)
        #     return func.HttpResponse(
        #         json.dumps({"result":"okay"}),
        #         status_code=200,
        #         mimetype='application/json'
        #     )
        return func.HttpResponse(
                json.dumps({"result":"okay"}),
                status_code=200,
                mimetype='application/json'
            )
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


