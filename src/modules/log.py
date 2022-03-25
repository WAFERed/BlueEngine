
# Imports
import datetime

# 0-10      - Generic Codes
# 11-60     - Error Codes
# 61-110    - Action Codes
LOG_CODES = {
    0   :   'OK',
    1   :   'ERROR',
    11  :   'incorrect action or action doesn\'t map to any function',
    61  :   'comand ran successfully'
}

# Update files for persistant records of logs
def UpdateLogFile(FilePath, Log):
    File = open(FilePath, "a")
    File.write(Log)
    File.close()

def Error(ERR_CODE):
    # Error string
    ERROR = '[' + str(datetime.datetime.now()) + ']' + ' ERR_CODE:(' + str(ERR_CODE) + ') : ' + LOG_CODES[ERR_CODE] + '\n'

    # Terminal Output
    print(ERROR)

    # File Logging
    UpdateLogFile('logs/errors.txt', ERROR)

def Action(ACTION_CODE, Command):
    # Action string
    ACTION = '[' + str(datetime.datetime.now()) + ']' + ' ACTION_CODE:(' + str(ACTION_CODE) + ' \'--' + Command + '\') : ' + LOG_CODES[ACTION_CODE] + '\n'

    # Terminal Output
    print(ACTION)

    # File Logging
    UpdateLogFile('logs/actions.txt', ACTION)