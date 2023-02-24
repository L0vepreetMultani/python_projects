import numpy as np
import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv',
    'climate.txt')
climate_data = np.genfromtxt('climate.txt', deliminter=',', skip_header=1)
