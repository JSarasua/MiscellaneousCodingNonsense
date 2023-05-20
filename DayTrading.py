import random

# Given a list of a stock prices per day. Find the best day to buy and then sell

def CreateRandomizedList(min:int, max:int, count:int):
    newList = random.sample(range(min, max), count)
    return newList

def FindBestMinMaxPairBruteForce(stockPriceList:list):
    minPrice = -1
    maxPrice = -1
    bestDiff = -1
    minIndex = -1
    maxIndex = -1

    dayCount = len(stockPriceList)
    for currentPriceIndex in range(0, dayCount):
        currentPrice = stockPriceList[currentPriceIndex]
        for futurePriceIndex in range(currentPriceIndex + 1, dayCount):
            futurePrice = stockPriceList[futurePriceIndex]
            currentDiff = futurePrice - currentPrice
            if currentDiff > bestDiff:
                minIndex = currentPriceIndex
                maxIndex = futurePriceIndex
                minPrice = currentPrice
                maxPrice = futurePrice
                bestDiff = currentDiff
    return (minPrice, maxPrice, minIndex, maxIndex, bestDiff)


def FindBestMinMaxPairSmart(stockPriceList:list):
    minPrice = -1
    minIndex = -1
    bestMinPrice = -1
    bestMinIndex = -1
    maxPrice = -1
    bestDiff = -1
    minIndex = -1
    maxIndex = -1

    dayCount = len(stockPriceList)
    for currentPriceIndex in range(0, dayCount):
        currentPrice = stockPriceList[currentPriceIndex]
        if minPrice == -1:
            minPrice = currentPrice
            minIndex = currentPriceIndex
            continue
        elif currentPrice < minPrice:
            minPrice = currentPrice
            minIndex = currentPriceIndex
            continue
        currentDiff = currentPrice - minPrice
        if currentDiff > bestDiff:
            bestMinPrice = minPrice
            maxPrice = currentPrice
            bestDiff = currentDiff
            bestMinIndex = minIndex
            maxIndex = currentPriceIndex
    return (bestMinPrice, maxPrice, bestMinIndex, maxIndex, bestDiff)


stockList = CreateRandomizedList(0, 10, 10)
bestPrice = FindBestMinMaxPairBruteForce(stockList)
print(stockList)
print("\nBrute force way")
print("MinPrice: " + str(bestPrice[0]))
print("MaxPrice: " + str(bestPrice[1]))
print("MinIndex: " + str(bestPrice[2]))
print("MaxIndex: " + str(bestPrice[3]))
print("Profit: " + str(bestPrice[4]))

bestPrice = FindBestMinMaxPairSmart(stockList)
print("\nSmart way")
print("MinPrice: " + str(bestPrice[0]))
print("MaxPrice: " + str(bestPrice[1]))
print("MinIndex: " + str(bestPrice[2]))
print("MaxIndex: " + str(bestPrice[3]))
print("Profit: " + str(bestPrice[4]))