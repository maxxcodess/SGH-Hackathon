api_response = {'msg': 'Client with requested id: https://outpost.mapmyindia.com/api/security/oauth/check_token?token= does not exists', 'responsecode': '403', 'error_description': 'Services for the client have been suspended due to daily/hourly transactions limit. Please contact MapmyIndia support at apisupport@mapmyindia.com', 'error_code': 'DAILY_LIMIT_EXHAUSTED', 'error': 'Daily Limit Expired'}
import json

# localvarJson = json.loads(api_response)
if 'error' in api_response.keys() :
    print("error")
    pass