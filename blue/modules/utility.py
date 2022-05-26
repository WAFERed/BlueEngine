# Imports
from PIL import Image
import numpy
import pandas
import os
import glob
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# File check
def fileCheck(path, detailed, rec):
    _, _, fileNames = next(os.walk(path))
    fileCount = len(fileNames)
    if (detailed == True):
        print(fileNames)
        print('File Count:', fileCount)
    else:
        print('File Count:', fileCount)

# File detail
def fileDetail(path):
    print('file size:', os.path.getsize(path))
    print('file modification time:', os.path.getmtime(path))
    print('file creation time:', os.path.getctime(path))
    print('full statistics:', os.stat(path))

# File detail
def tifDetail(path):
    try:
        img = Image.open(path)
    except:
        # throw error
        return
    npImg = numpy.array(img)
    numpy.info(npImg)

# File detail
def dfDetail(path):
    try:
        df = pandas.read_csv(path)
    except:
        return
    print(df.head(5))
    print(df.info())
    print(df.describe())

# File detail
def checkNaN(path):
    try:
        df = pandas.read_csv(path)
    except:
        return
    # Any NaN values in df
    print('NaN values exist:', df.isnull().values.any())
    # Count of NaN values in df
    print('NaN values count:', df.isnull().sum().sum())

# Rank neural network
def rankNN(path, rankUsing, count):
    df = pandas.read_csv(path)
    df = df.sort_values(by=rankUsing)
    print(df.head(count))
    print(df.tail(count))

# Get list of
def getList(listOf):
    optimizerList   = ['adadelta',
                        'adagrad',
                        'adam',
                        'adamax',
                        'ftrl',
                        'nadam',
                        'rmsprop',
                        'sgd']
    activatorList   = ['relu',
                        'elu',
                        'exponential',
                        'gelu',
                        'hard_sigmoid',
                        'linear',
                        'relu',
                        'selu',
                        'sigmoid',
                        'softmax',
                        'softplus',
                        'softsign',
                        'swish',
                        'tanh']
    listDict        = {
        'optimizer' : optimizerList,
        'activator' : activatorList
    }
    try:
        print(listDict[listOf])
    except:
        return