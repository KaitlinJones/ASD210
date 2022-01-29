

def partition(start, end, lyst):
    i = start               # set the pivot index to start
    pivot = lyst[i]

    while start < end:                                      # This loop runs till start pointer crosses
                                                            # end pointer, and when it does we swap the
                                                            # pivot with element on end pointer
        while start < len(lyst) and lyst[start] <= pivot:
            start += 1                      # increment the start until it finds an element > pivot
        while lyst[end] > pivot:
            end -= 1                        # decrement the end until it finds an element < pivot
        if(start < end):
            lyst[start], lyst[end] = lyst[end], lyst[start] # swap the elements on start and end 
                                                            # if they have not crossed each other
    
    lyst[end], lyst[i] = lyst[i], lyst[end]         # swap the end element with the pivot element; this 
                                                    # puts the pivot element in its correct position
    
    return end      # Returning end pointer to divide the array into 2

def quickSort(start, end, lyst): # utilizes partition and calls itself to recursively complete the sort

    if start < end:
        p = partition(start, end, lyst)     # p is partitioning index, array[p] is at right place
        quickSort(start, p - 1, lyst)       # sort elements before partition 
        quickSort(p + 1, end, lyst)         # sort elements after the partition
    
def main():
    animals = ["aardvark", "zebra", "giraffe","baboon","penguin","puppy" ,"rhinosaurus","elephant","gorilla","lion","tiger","bear"]
    quickSort(0, len(animals) - 1, animals)
    print("The sorted list is:", animals)

if __name__ == "__main__":
    main()
