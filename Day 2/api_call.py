import requests 
import json

# creating a get request
url = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'
response = requests.get(url)

code = response.status_code

# if url is valid then do the operations
if code == 200:
    # converting json data to python object(dictionary)
    obj = json.loads(response.text)

    # keys in present data
    print(obj.keys())

    # total years data
    data = obj['data']
    total_years = len(data)
    print('Total years:', total_years)

    # attributes of each record
    print('Attributes of each record:',data[0].keys())

    # rendering population of USA year-wise
    for i in range(total_years):
        year = data[i]['ID Year']
        population = data[i]['Population']
        print('Year %d - Population %d'%(year, population))

else:
    print('Invalid URL!')
