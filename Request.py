import requests

url = 'https://ows.rasdaman.org/rasdaman/ows'

class requestWCPS():
    def __init__(self,query):
        self.query = query
        self.url = url
    
    def processRequest(query):
        response = requests.post(url, data= {'query':query})
        return response