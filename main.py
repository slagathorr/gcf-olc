import functions_framework
import json
from openlocationcode import openlocationcode as olc

@functions_framework.http
def encode_olc(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    request_json = request.get_json(silent=True)
    request_args = request.args

    calls = request_json['calls']
    return_value = []

    # This code assumes the input data comes as (latitude,longitude) pairs.
    # This code does not do error checking on input.
    for call in calls:
        latitude = call[0]
        longitude = call[1]
        return_value.append(olc.encode(latitude,longitude,10))
    return_json = json.dumps( { "replies" : return_value } )
    return return_json