from PIL import Image as im 
import numpy as np
from io import BytesIO
import csv

class outputResponse():
    def __init__(self,reponse):
        self.response = reponse

    def retrieveResult(response, returntype):
        if (returntype == "image/png" or returntype == "image/jpeg"):
            img_arr = np.array(im.open(BytesIO(response.content)))
            data = im.fromarray(img_arr) 
            data.show() 

        elif (returntype == "text/csv"):
            response = response.content.decode('utf-8')
            my_list = response.split (",")
            with open ('x.csv', 'w') as file:
                writer = csv.writer(file, delimiter = ',')
                writer.writerow(my_list)

        elif (returntype == 1 or returntype == 0):
            print(response.content)

        else:
            response = response.content.decode('utf-8')
            print (response)
