import requests

# Set the base URL
BASE_URL = "http://localhost:5002"
s = requests.Session()


# Method that sends http get request
def send_get(url, headers=None, params=None):
    r = requests.get(url=BASE_URL + url, headers=headers, params=params)
    print("Get request status code: ",  r.status_code)
    print("Get request status url: ",  r.url)
    print("Get request json: ", r.json)
    print("Get request Text: " + r.text)


#  Method that sends http post request
def send_post(url, data, headers=None, params=None, ):
    print(data)
    r = requests.post(url=BASE_URL + url, json=data, headers=headers, params=params)
    print("Post request status code: ",  r.status_code)
    print("Post request status url: ",  r.url)
    print("Post request json: ", r.json)
    print("Post request Text: " + r.text)


# Method that sends http get request using sessions
def send_session_get(url, headers=None, params=None):    
    r = s.get(url=url, headers=headers, params=params)
    print("Get request status code: ",  r.status_code)
    print("Get request status url: ",  r.url)
    print("Get request status headers: ",  r.headers)
    print("Get request json: ", r.json)
    print("Get request Text: " + r.text)


# Set header and send get request
headers = {'user-agent': 'my-app', 'Content-Type': 'application/json'}
send_get("/headers", headers)


# Set query parameters and send get request
params = {'key1': 'params_value1', 'key2': 'params_value2'}
send_get("/query", headers, params)


# Set body content and send post request
data = {'data': 'data_value', 'data2': 'data_value2'}
send_post("/body", data)


# Set header and send get request
for i in range(10):
    send_session_get("https://example.com", headers)
    # send_get("/headers", headers)
