def reverse(lyst):
    left = 0 
    right = len(lyst) - 1
    while left < right:
        iterate(right, left, lyst)
        left += 1
        right -= 1
        
def iterate(right, left, lyst):
    lyst[left], lyst[right] = lyst[right], lyst[left]

def main():
    lyst1 = ["a","b","c","d",1,2,3,4]
    reverse(lyst1)
    print(lyst1)

if __name__ == "__main__":
    main()