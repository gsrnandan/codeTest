input = [1,-2,[3,4],[5,[6,7],8],9,[10,20,[30,40],[50,[60,70],80]],1,2,[3,4],[5,[6,7],8],9,[10,20,[30,40],[50,[60,70],80]]]


def flattenList(nestedList):
    """ Method to flatten an array of arbitrarily nested arrays of integers into a flat array of integers.
            
        This method reads the input list and puts them into a flat list of integers after validation.
                
        Args:
            nestedList (list): The nested list of integers that are to be flattened
                
        Return:
            (list): Returns a flat list of integers
         
    """
    outputList = []
    for i in nestedList:
        if isinstance(i,int):
            outputList.append(i)
        elif isinstance(i,list):
            outputList.extend(flattenList(i))
        else:
            raise TypeError("Element {0} has unsupported type ({1})".format(i,type(i).__name__))
    return outputList


print flattenList(input)
