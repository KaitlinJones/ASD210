def isSorted(lyst):     # define isSorted function
    """Returns true if list is sorted/False otherwise"""
    if len(lyst) >= 0 and len(lyst) < 2:        # checks for multiple values 
        return True                             # True if there are NOT multiple values 
    else:
        for i in range(len(lyst)-1):            # if there are multiple values check sorting 
            if lyst[i] > lyst [i + 1]:
                return False
        return True

def main():                                     # print results 
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))
if __name__=="__main__":
    main()