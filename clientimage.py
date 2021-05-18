import requests

resp = requests.post("http://localhost:5000/predict",
                     files={"file": open('C://olahcitra//chan.jpg','rb')})

print(resp.json())
#print(resp)
