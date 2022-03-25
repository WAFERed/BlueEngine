# IMPORTS
import sys

import modules.interpreter as interpreter
import modules.controller as controller

# MAIN FUNCTION
def main():
    
    # There must be some arguements to interpret
    if (len(sys.argv) > 1):

        # Iterating arguement list & seperating flags and actions
        ActionsFlags = interpreter.InterpretActionsFlags(sys.argv)

        # Actions
        for action in ActionsFlags[0]:
            controller.OperationMapper(action)
        
    else:

        # Manual on how to use the tool
        controller.OperationMapper('help')

if __name__ == "__main__":
    main()
