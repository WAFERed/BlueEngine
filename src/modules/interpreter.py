def InterpretActionsFlags(arguements):

    # List of actions and flags
    actions = []
    flags = []

    # Iterating over each individual 'space' seperated statement
    for i in range(1, len(arguements)):
        arguement = arguements[i]
        arguement_length = len(arguement)
        
        # If argement starts with '-' it is to be further evaluated
        if (arguement[0] == '-'):

            # Check to ensure there are no '-' with no operations
            if(arguement_length > 2):

                # Incase of another '-' i.e. '--', it is an action
                if (arguement[1] == '-'):

                    # Split arguement string after '--' and append it to action list
                    actions.append(arguement[2:])

                else:

                    # Split arguement string after '-' and append it to flag list
                    flagstring = arguement[1:]
                    for i in range(0, len(flagstring)):
                        flags.append(flagstring[i])
            else:

                # Split arguement string after '-' and append it to flag list
                flagstring = arguement[1:]

                # Iterate over flags one by one and seperate them into a list
                for i in range(0, len(flagstring)):
                    flags.append(flagstring[i])
        else:

            # If arguement doesn't start with '-', continue to next arguement
            continue
    
    # Return the generated actiion and flag list
    return (actions, flags)