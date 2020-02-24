import logging
import logstash
import sys

host = '18.209.173.73'
# im going to change some ports which 

test_logger = logging.getLogger('python-logstash-logger111')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler(host, 5959,version=1))
# test_logger.addHandler(logstash.TCPLogstashHandler(host, 5959, version=1))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

# add extra field to logstash message
extra = {
    'test_string': 'python version: ' + repr(sys.version_info),
    'test_boolean': True,
    'test_dict': {'a': 1, 'b': 'c'},
    'test_float': 1.23,
    'test_integer': 123,
    'test_list': [1, 2, '3'],
}
test_logger.info('python-logstash: test extra fields', extra=extra),


class StockHolding:
    def __init__( self, symbol, sharesPurchased, price  ):
        self.symbol = symbol
        self.sharesPurchased = sharesPurchased
        self.price = price

        test_logger.info('Created StockHolding: {} - {}, ${}'.format(self.symbol, self.sharesPurchased, self.price))
        
    def getSymbol(self):
        return self.symbol
    
    def getNumOfShares(self):
        return self.sharesPurchased
    
    def getTotalCost(self):
        return self.price * self.sharesPurchased
    
    def estimateProfit(self, numOfSharesCouldSell, currentPricePerShares):
        return (currentPricePerShares * numOfSharesCouldSell ) - (self.price * numOfSharesCouldSell)
    
    def sellShares(self, numOfSharesToSell):
        if self.sharesPurchased < numOfSharesToSell:
    	    raise ValueError("Insufficient share: ")
        self.sharesPurchased -= numOfSharesToSell
        
def main():
    testStockHolding = StockHolding("MARY", 100, 2.50)
    logging.debug(testStockHolding.getSymbol())
    logging.error(testStockHolding.getNumOfShares())
    logging.warning(testStockHolding.getTotalCost())

    profit  = 50
    if profit == testStockHolding.estimateProfit(100, 3.00) :
        print("I make a profit! ")
 
    sharesRemaining = 5
    testStockHolding.sellShares(95)
    if sharesRemaining == testStockHolding.getNumOfShares():
        print("The number of shares after selling is the value expected. ")
        
    try:
        testStockHolding.sellShares(95)
        print("Shares Sold!")
    except ValueError as e:
        print(str(e),"remaining share: ",testStockHolding.getNumOfShares())

main()


