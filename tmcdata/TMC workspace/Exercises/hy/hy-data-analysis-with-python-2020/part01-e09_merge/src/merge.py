#!/usr/bin/env python3

def merge(L1, L2):
    "Merge sorts two sorted lists L1 and L2"
    L3 = list()
    L1Iterator = 0
    L2Iterator = 0
    L1Len = len(L1)
    L2Len = len(L2)

    #Loop through and add the correct item from the list
    while(L1Iterator < L1Len and L2Iterator < L2Len):
        if(L1[L1Iterator] > L2[L2Iterator]):
            L3.append(L2[L2Iterator])
            L2Iterator += 1
        else:
            L3.append(L1[L1Iterator])
            L1Iterator += 1

    #Add the rest of whichever list isn't fully added yet
    while(L1Iterator < L1Len):
        L3.append(L1[L1Iterator])
        L1Iterator += 1

    while(L2Iterator < L2Len):
        L3.append(L2[L2Iterator])
        L2Iterator += 1

    return L3

def main():
    L1 = [1,3,5]
    L2 = [2,4,6]
    print(merge(L1, L2))

if __name__ == "__main__":
    main()
