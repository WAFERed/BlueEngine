# Libraries
import modules.interpreter as interpreter
import modules.interface as interface
import modules.log as log

OP_ACTION = {
        'help':     interface.PrintManual,
        'version':  interface.PrintVersion,
    }

def OperationMapper(action):

    # Call appropriate function for action code
    if action in OP_ACTION:

        # Call and log the action
        OP_ACTION[action]()
        log.Action(61, action)

    else:

        # Throw and log appropriate errors
        log.Error(11)
