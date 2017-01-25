## Merge-sort on a deck of cards of only one suit, aces high
import math

## We will assign a number value to face cards so the computer can determine
##   which is higher or lower
J = 11
Q = 12
K = 13
A = 14

## Here is our shuffled deck
D = [4, 9, Q, 3, 10, 7, J, 5, A, 6, K, 8, 2]

## We define the mergeSort here; notice how it "recursively" calls itself
def mergeSort(deck, p, r):
    if p < r:
        q = (p + r)//2
        mergeSort(deck, p, q)
        mergeSort(deck, q + 1, r)
        merge(deck, p, q, r)
    return deck

## We now define the most important merge function
def merge(deck, p, q, r):
    
    ## the sizes of each sub-problem
    N_1 = q - p + 1
    N_2 = r - q
    
    ## create the left and right piles from the original deck
    L = []
    R = []
    for i in range(1, N_1):
        L[i] = deck[p + i - 1]
    for j in range(1, N_2):
        R[i] = deck[q + j]
        
    ## we will place a terminator card at the bottom of each pile so that
    ##   we know when we've reached the bottom of a comparison pile
    L[N_1 + 1] = math.inf
    R[N_2 + 1] = math.inf
    
    ## reset our counters
    i = 1
    j = 1
    
    ## compare and either put the left card back into the deck or the right one
    for k in range(p, r):
        if L[i] <= R[j]:
            deck[k] = L[i]
            i += 1
        else:
            deck[k] = R[j]
            j += 1
    return deck
    
