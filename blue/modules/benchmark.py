# Imports
import os
from pickle import DEFAULT_PROTOCOL
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas
import time

# Benchmark batch processing
def benchBatch(showtime):
    # Get the start time
    st = time.time()

    # Benchmark

    # Get the end time
    et = time.time()
    # get the execution time
    if showtime == True:
        elapsed_time = et - st
        print('Benchmark time:', elapsed_time, 'seconds')

# Benchmark performance of different NeuralNetworks
def benchNN(input, output, showtime, modelEpochs, modelMetric):

    print('Imports done successfully')

    # Get the start time
    st = time.time()

    # Benchmark
    fileName        = input
    resultPath      = output
    dataframe       = pandas.read_csv(fileName)
    dfCol           = len(dataframe.columns)
    dataset         = dataframe.values
    lossCalc        = modelMetric
    metricsList     = []
    metricsList.append(modelMetric)

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
    
    # Other
    modelCounter    = 0
    modelNames      = []
    modelList       = []
    resultDF        = pandas.DataFrame()
    accList         = []
    print('Parameters set successfully')

    # Calculating number of neurons
    inDim           = dfCol - 1
    nNeuron         = dfCol * 2

    # Generating Model List
    for activator in activatorList:
        for optimizer in optimizerList:
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
            modelList.append(model)

            # Display
            modelName = (str(activator), str(optimizer))
            print(f'{modelCounter} - Model compiled successfully for: {modelName[0], modelName[1]}')
            modelNames.append(modelName)

            modelCounter = modelCounter + 1

    print('All models generated successfully')

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

    # Model Fitting
    for i in range(0, len(modelNames)):

        # Fitting
        history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=modelEpochs, verbose=0)
        _, train_acc = model.evaluate(trainX, trainY, verbose=0)
        # Evaluation
        _, test_acc = model.evaluate(testX, testY, verbose=0)
        #print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))

        print(f'{modelCounter} - Model -> {modelNames[i]} || train:{train_acc} , test:{test_acc}')
        accList.append((train_acc, test_acc))
        
        modelCounter = modelCounter + 1

    # Get the end time
    et = time.time()
    
    # Extraction
    lOpt = []
    lActv = []
    lTrAcc = []
    lTeAcc = []
    for i in range(0, len(modelNames)):
        lActv.append(modelNames[i][0])
        lOpt.append(modelNames[i][1])
        lTrAcc.append(accList[i][0])
        lTeAcc.append(accList[i][1])

    # To dataframe
    resultDF['optimizer'] = lOpt
    resultDF['activator'] = lActv
    resultDF['train'] = lTrAcc
    resultDF['test'] = lTeAcc

    # Export
    resultDF.to_csv(resultPath, index=False)

    
    # get the execution time
    if showtime == True:
        elapsed_time = et - st
        print('Benchmark time:', elapsed_time, 'seconds')
    