# Imports
import wget

def fetchData(dataurl, persistance, output):
    print(dataurl, persistance, output)
    try:
        data = wget.download(dataurl, output)
        print('worked')
    except:
        print('not worked')
        return