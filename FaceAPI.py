# Import modules
import requests
import json

# First, get a token

url = 'https://api.sirv.com/v2/token'

payload = {
  'clientId': 'Za363g1RB7ATSj6dGzy4Z0Jz5iV',
  'clientSecret': 'xrPg4gT+9/dEEj/Tqm1wnX+IQvplSvxRkSPwvYQvF7RfbO2L7ltvZ23RT4f4MKaMhBV09HT7p7ZTeFPsK+1VNA=='
}

headers = {'content-type': 'application/json'}

response = requests.request('POST', url, data=json.dumps(payload), headers=headers)

token = response.json()['token']

# Now upload a file

url = 'https://api.sirv.com/v2/files/upload'

querystring = {'filename':'/path/to/uploaded-image.jpg'}

payload = open('/path/to/local-image.jpg', 'rb')

headers = {
  'content-type': 'image/jpeg',
  'authorization': 'Bearer %s' % token
}

response = requests.request('POST', url, data=payload, headers=headers, params=querystring)

print(response)