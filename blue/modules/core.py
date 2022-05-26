# Imports
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from PIL import Image
import pandas
import time
import os

# Function to calculate the pixel values from coordinates
def coordinates2Pixels(coordValX, coordValY, areaVal):

    # Calculating coordinate pixel location 1' coordVal = 24 pixels)
    pixelValX           = int(round( ((180 * 24) + (coordValX * 24)), 0) )
    pixelValY           = int(round( ((90 * 24) - (coordValY * 24)), 0)  )

    # Using area to calculate a box
    radius              = int(round((areaVal * 24), 0))
    heightWidth         = radius * 2
    pixelStartX         = pixelValX - radius
    pixelStartY         = pixelValY - radius

    return (pixelStartX, pixelStartY, heightWidth)

# Copping tif files
def cropTif(input, output, long, lat, area, batchproc, batchsize):
    if batchproc == True:
        pass
    else:
        inputPath = input
        outputPath = output
        inputFileNames = []
        outputFileNames = []
        pixelCord = coordinates2Pixels(long, lat, area)

        # Maing list of files
        _, _, fileNames = next(os.walk(inputPath))
        fileCount = len(fileNames)
        #fileNames = fileNames.sort()

        # Making filepaths
        for i in range(0, fileCount):
            inputFileNames.append(inputPath + '/' + str(fileNames[i]))
            outputFileNames.append(outputPath + '/' + str(fileNames[i]))

        for i in range(0, fileCount):
            CurrentImage = Image.open(inputFileNames[i])
            CroppedImage = CurrentImage.crop((pixelCord[0],pixelCord[1],pixelCord[0] + pixelCord[2],pixelCord[1] + pixelCord[2]))
            CroppedImage.save(outputFileNames[i])
            print('Cropped :', outputFileNames[i])

# Normalize dataframe
def normalize(input, output):
    df = pandas.read_csv(input, output)
    result = df.copy()
    for feature_name in df.columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    result.to_csv(output, index=False)
    
# Benchmark performance of different NeuralNetworks
def genNN(input, activator, optimizer, showTime, modelEpochs, modelMetric):
    print('Imports done successfully')

    # Get the start time
    st = time.time()

    # Benchmark
    fileName        = input
    dataframe       = pandas.read_csv(fileName)
    dfCol           = len(dataframe.columns)
    dataset         = dataframe.values
    lossCalc        = modelMetric
    metricsList     = []
    metricsList.append(modelMetric)

    # Calculating number of neurons
    inDim           = dfCol - 1
    nNeuron         = dfCol * 2

    model = Sequential()
    model.add(Dense(nNeuron, input_dim = inDim, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(nNeuron, kernel_initializer = 'normal', activation = activator))
    model.add(Dense(1, kernel_initializer = 'normal'))
    
    # compile model
    model.compile(loss = lossCalc,
                optimizer=optimizer,
                metrics = metricsList)
    print('Model generated successfully')

    # Creating X and Y
    X = dataframe.drop(dataframe.columns[[-1]], axis=1)
    X = X.values
    Y = dataframe['WET_Fixed']
    Y = Y.values
    Y = Y.reshape(-1,1)
    print('X and Y seperated successfully')

    # Split into input (X) and output (Y) variables
    n_test = int(len(X)/2)

    to_drop = range(0,n_test)
    to_keep = range(n_test, len(X))
    trainX = pandas.DataFrame(X)
    trainX = trainX.drop(to_drop)
    testX = pandas.DataFrame(X)
    testX = testX.drop(to_keep)
    trainY = pandas.DataFrame(Y)
    trainY = trainY.drop(to_drop)
    testY = pandas.DataFrame(Y)
    testY = testY.drop(to_keep)
    print('Data split successfully (trainX, trainY, testX, testY)')

    modelCounter = 0

    # Fitting
    history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=modelEpochs, verbose=1)
    _, train = model.evaluate(trainX, trainY, verbose=0)
    # Evaluation
    _, test = model.evaluate(testX, testY, verbose=0)

    print(f'{modelCounter} - Model -> {activator}, {optimizer} || train:{train} , test:{test}')

    # Get the end time
    et = time.time()
    
    # get the execution time
    if showTime == True:
        elapsed_time = et - st
        print('Benchmark time:', elapsed_time, 'seconds')
