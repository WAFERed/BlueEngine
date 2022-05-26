#####################################################################################################
# IMPORTS                                                                                           #
#####################################################################################################

# Main
from itertools import count
import click
import os

# Modules
import blue.modules.utility as utility
import blue.modules.benchmark as benchmark
import blue.modules.core as core
#import modules.visualization as visualization
#import modules.interface as interface
#import modules.interpreter as interpreter
import blue.modules.network as network
#import modules.logger as logger


#####################################################################################################
# CLICK GROUP                                                                                       #
# DESCRIPTION: A group allows application call to branch off to the appropriate function            #
#####################################################################################################

@click.group()
def cli():
    pass

#####################################################################################################
# FUNCTIONS                                                                                         #
# DESCRIPTION: Functions with specified arguements and options                                      #
#####################################################################################################

# (1) - Test hello function
@click.command(short_help='Says hello to given name')
@click.option('--count', default=10, help='Number of greetings')
@click.argument('name')
def sayHello(count, name):
    for x in range(count):
        print('Hello,', name)

# (2) - File check function
@click.command(short_help='Checks files and their count')
@click.option('--recursive', default=False, type=click.BOOL, help='Check files recursively')
@click.option('--detailed', default=False, type=click.BOOL, help='Verbosity of filecheck process')
@click.argument('path', default=os.getcwd(), type=click.Path(exists=True))
def fileCheck(path, recursive, detailed):
        utility.fileCheck(path, detailed, recursive)

# (3) - File detail function
@click.command(short_help='Shows file details')
@click.argument('filename', type=click.Path(exists=True))
def fileDetail(filename):
    utility.fileDetail(filename)

# (4) - Tif detail function
@click.command(short_help='Shows tif file details')
@click.argument('filename', type=click.Path(exists=True))
def tifDetail(filename):
    utility.tifDetail(filename)

# (5) - DataFrame detail function
@click.command(short_help='Shows DataFrame .csv file details')
@click.argument('filename', type=click.Path(exists=True))
def dfDetail(filename):
    utility.dfDetail(filename)

# (6) - NaN value checker
@click.command(short_help='Checks for NaN values and their count')
@click.argument('filename', type=click.Path(exists=True))
def checkNaN(filename):
    utility.checkNaN(filename)

# (7) - Rank benchmarked Neural Networks
@click.command(short_help='Ranks Neural Networks using a paramter')
@click.option('--count', default=5, type=click.INT, help='How many rows to show')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('rankUsing', type=click.STRING)
def rankNN(filename, rankusing, count):
    utility.rankNN(filename, rankusing, count)

# (8) - Remote data fetcher
@click.command(short_help='Fetches data from Internet using wget')
@click.option('--mode', default='single', type=click.STRING, help='Direct file(s) URL (space seperated) or URL .txt list')
@click.argument('dataurl', type=click.STRING)
@click.argument('output', type=click.Path(exists=True))
def fetchData(dataurl, mode, output):
    network.fetchData(dataurl, mode, output)

# (9) - Get list of things
@click.command(short_help='Shows list of items')
@click.argument('listof', type=click.STRING)
def getList(listof):
    utility.getList(listof)

# (10) - Benchmark batch processing
@click.command(short_help='Benchmarks and shows time to run it')
@click.option('--time', default=True, type=click.BOOL, help='Time how long it takes to benchmark batch processing operation')
def benchBatch(time):
    benchmark.benchBatch(time)

# (11) - Benchmark performance of different NeuralNetworks
@click.command(short_help='Runs all combination of Neural Networks')
@click.option('--time', default=True, type=click.BOOL, help='Time how long it takes to benchmark neural networks')
@click.option('--epochs', default=200, type=click.INT, help='Number of epochs each model will run')
@click.option('--metric', default='mean_absolute_error', type=click.STRING, help='Reported metric(s) for models')
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path(exists=True))
def benchNN(input, output, time, epochs, metric):
    benchmark.benchNN(input, output, time, epochs, metric)

# (12) - TIF image cropper
@click.command(short_help='Crops .tif file(s) for given coordinates')
@click.option('--batchproc', default=False, type=click.BOOL, help='Enable batch processing of .tif files')
@click.option('--batchsize', default=12, help='Size of each batch of .tif files')
@click.argument('input', default=os.getcwd(), type=click.Path(exists=True))
@click.argument('output', default=os.getcwd(), type=click.Path(exists=True))
@click.argument('long', type=click.FLOAT)
@click.argument('lat', type=click.FLOAT)
@click.argument('area', type=click.FLOAT)
def cropTif(input, output, long, lat, area, batchproc, batchsize):
    core.cropTif(input, output, long, lat, area, batchproc, batchsize)
    
# (13) - Data normalizer
@click.command(short_help='Normalizes .csv DataFrame using min-max')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('output', type=click.Path(exists=True))
def normalize(filename, output):
    core.normalize(filename, output)

# (14) - Feature generator
@click.command(short_help='Generates features for data')
@click.argument('filename', type=click.Path(exists=True))
@click.argument('output', type=click.Path(exists=True))
def genFeatures(filename, output):
    core.genFeatures(filename, output)

# (15) - NeuralNetwork generator
@click.command(short_help='Compiles and Trains a Neural Network for given data')
@click.option('--time', default=True, type=click.BOOL, help='Time how long it takes to benchmark neural networks')
@click.option('--epochs', default=200, type=click.INT, help='Number of epochs each model will run')
@click.option('--metric', default='mean_absolute_error', type=click.STRING, help='Reported metric(s) for models')
@click.argument('input', type=click.Path(exists=True))
@click.argument('activator', type=click.STRING)
@click.argument('optimizer', type=click.STRING)
def genNN(input, activator, optimizer, time, epochs, metric):
    core.genNN(input, activator, optimizer, time, epochs, metric)

# (16) - Predictor using NeuralNetwork
@click.command(short_help='Predicts future data values using trained Neural Network')
@click.option('--time', default=True, type=click.BOOL, help='Time how long it takes to benchmark neural networks')
@click.option('--epochs', default=200, type=click.INT, help='Number of epochs each model will run')
@click.option('--metric', default='mean_absolute_error', type=click.STRING, help='Reported metric(s) for models')
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path(exists=True))
@click.argument('future', type=click.Path(exists=True))
@click.argument('activator', type=click.STRING)
@click.argument('optimizer', type=click.STRING)
def predictNN(input, output, future, activator, optimizer, time, epochs, metric):
    core.predictNN(input, output, future, activator, optimizer, time, epochs, metric)


#####################################################################################################
# CLICK GROUP ADD                                                                                   #
# DESCRIPTION: Adding functions to the click group so they are callable through python application  #
#####################################################################################################

# 1. Test
cli.add_command(sayHello)           # (1)

# 2. Utility
cli.add_command(fileCheck)          # (2)
cli.add_command(fileDetail)         # (3)
cli.add_command(tifDetail)          # (4)
cli.add_command(dfDetail)           # (5)
cli.add_command(checkNaN)           # (6)
cli.add_command(rankNN)             # (7)
cli.add_command(getList)            # (8)

# 3. Network
cli.add_command(fetchData)          # (9)

# 4. Tuning & Performance
cli.add_command(benchBatch)         # (10)
cli.add_command(benchNN)            # (11)

# 5. Core Functionality
cli.add_command(cropTif)            # (12)
cli.add_command(normalize)          # (13)
cli.add_command(genFeatures)        # (14)
cli.add_command(genNN)              # (15)

# 6. Prediction
cli.add_command(predictNN)          # (16)


#####################################################################################################
# MAIN FUNCTION                                                                                     #
# DESCRIPTION: Entry point of the python application that calls the click cli() function            #
#####################################################################################################

# Starting main function
if __name__ == '__main__':
    # The click group is called
    cli()
