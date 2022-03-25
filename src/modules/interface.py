def PrintManual():

    # Try Opening INFO.txt file with '/', otherwise use '\'
    try:
        manual = open("../INFO.txt", "r").read()
        print(manual)
    except:
        manual = open("..\\INFO.txt", "r").read()
        print(manual)

def PrintVersion():

    # Try Opening INFO.txt file with '/', otherwise use '\'
    try:
        version = open("../version.txt", "r").read()
        print(version)
    except:
        version = open("..\\version.txt", "r").read()
        print(version)