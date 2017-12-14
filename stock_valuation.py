import urllib.request
import matplotlib.pyplot as plt

dates = []
closeprices = []
minPrices = []
maxPrices = []

def MostVolatility():
    maxV = 0    
    dateOccured = ""
    
    for i in range(len(dates)):
        d = dates[i]
        minP = minPrices[i]
        maxP = maxPrices[i]
        vol = maxP - minP
        if vol > maxV:
            dateOccured = d
            maxV = vol
    
    print ("Max vol. " + str(maxV) + " occured on " + dateOccured)
    

def LoadStockData():
    stock = str(input("Enter Ticker:"))
    url = "http://ichart.finance.yahoo.com/table.csv?s=" + stock 
    response = urllib.request.urlopen(url)
    content = response.read().decode("utf-8") 
    records = content.split("\n")
    del records[0]
    
    for record in records:   
        if record == "" :
            break
            
        columns = record.split(",")
        closeprices.append(float(columns[4]))
        dates.append(columns[0])
        minPrices.append(float(columns[3]))
        maxPrices.append(float(columns[2]))

def MinMaxAvg(prices):
    print ("Min Price: " + str(min(prices)))
    print ("Max Price: " + str(max(prices)))
    print ("Avg Price: " + str(sum(prices) / len(prices)))
    
prices = []

while(True):
    print("1- Load Stock Data")    
    print("2- Min/Max/Average")    
    print("3- Historic Volatility")    
    print("4- Daily Volatility")    
    print("0- Exit")    
    choice = int(input("What would you like to do?"))    
    
    if choice == 1:
        LoadStockData()
    elif choice == 2:
        MinMaxAvg(closeprices)
    #elif choice == 3:    
    
    elif choice == 4:
        MostVolatility()

    elif choice == 0:    
        break 

