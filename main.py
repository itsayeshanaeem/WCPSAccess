from Output import outputResponse
from Queries import coverageCondensor, coverageConstructor, coverageFiltering, coverageSubsetting, multiBand, inducedOperation
from Request import requestWCPS

url = 'https://ows.rasdaman.org/rasdaman/ows'

def main():
    str1 = input("Please enter the type of query you want: ")
    if ("coverage constructor" in str1):
        str2 = input("Please enter the Coverage name: ")
        a  = coverageConstructor(str2)
        query = a.getquery()
        print (query)
        response = requestWCPS.processRequest(query)
        print (response.content) 

    elif ("coverage condensor" in str1):
        str2 = input("Please enter the Coverage name: ")
        a = coverageCondensor(str2)
        query = a.getquery()
        print (query)
        returntype = a.returntypefunc()
        response = requestWCPS.processRequest(query)
        outputResponse.retrieveResult(response,returntype)

    elif ("coverage subsetting" in str1):
        str2 = input("Please enter the Coverage name: ")
        a = coverageSubsetting(str2)
        query = a.getquery()
        returntype = a.returntypefunc()
        print (query)
        response = requestWCPS.processRequest(query)
        outputResponse.retrieveResult(response,returntype)

    elif ("coverage filtering" in str1):
        str2 = input("Please enter the Coverage name: ")
        a = coverageFiltering(str2)
        query = a.getquery()
        returntype = a.returntypefunc()
        response = requestWCPS.processRequest(query)
        outputResponse.retrieveResult(response,returntype)

    elif ("induced operation" in str1):
        str2 = input("Please enter the Coverage name: ")
        a = inducedOperation(str2)
        query = a.getquery()
        returntype = a.returntypefunc()
        response = requestWCPS.processRequest(query)
        outputResponse.retrieveResult(response,returntype)

    elif ("multi-band" in str1):
        str2 = input("Please enter the first Coverage name: ")
        str3 = input("Please enter the second Coverage name: ")
        a = multiBand(str2,str3)
        query = a.getquery()
        returntype = a.returntypefunc()
        response = requestWCPS.processRequest(query)
        outputResponse.retrieveResult(response,returntype)
main()