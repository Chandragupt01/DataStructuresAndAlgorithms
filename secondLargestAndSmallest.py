def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    smallest=float("inf")
    secondSmallest=float("inf")
    largest=float("-inf")
    secondLargest=float("-inf")

    for i in range(n):
        if a[i]<smallest:
            secondSmallest=smallest
            smallest=a[i]
        elif a[i]<secondSmallest and a[i]!=smallest:
            secondSmallest=a[i]
        if a[i]>largest:
            secondLargest=largest
            largest=a[i]
        elif a[i]>secondLargest and a[i]!=largest:
            secondLargest=a[i]

    return [secondLargest,secondSmallest]

