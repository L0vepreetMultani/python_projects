# first import the numpy as np
import numpy as np
import urllib.request
# use url retrieve function of urllib.request url to add the data of that csv into the climate.txt file
urllib.request.urlretrieve(
    'https: // gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 'climate.txt')
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print(climate_data)
