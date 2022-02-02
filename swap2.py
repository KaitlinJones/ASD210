           
def reverse(lyst):
    for i in range (len(lyst) // 2):
        lyst[i], lyst[-1 - i] = lyst [-1 -i], lyst[i]

def main():
    lyst1 = [9,0,3,5,7,6,8]
    reverse(lyst1)
    print(lyst1)
    

if __name__ == "__main__":
    main()