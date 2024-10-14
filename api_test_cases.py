API Documentation: 
Testing different API functionalities using Python `requests`.
 
Question 1: Retrieve Access Token from Login API
```python
import requests
import time
 
def get_access_token(email, password):
    start_time = time.time()
    response = requests.post("https://reqres.in/api/login", data={"email": email, "password": password})
    time_taken = time.time() - start_time
    if response.status_code == 200:
        return response.json()['token'], time_taken
    return None, time_taken
```
Comment: We retrieve the access token for further API usage. Time taken for the request is also recorded.
 
