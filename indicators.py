from pycoingecko import CoinGeckoAPI
import time
cg = CoinGeckoAPI()

class Indicators:

    @staticmethod
    def getHistorical(coin: str, d: int):
        ''' get d days of a coin, coin's price'''
        return cg.get_coin_market_chart_by_id(
            id=coin, 
            vs_currency='usd', 
            days=d, 
            interval='daily')['prices']

    @staticmethod
    def getSMA(coin: str, n: int):
        ''' get the n'th Simple MA '''
        # Get price action over n last days for a coin, id
        pa = Indicators.getHistorical(coin, n)
        # Data is [[unix1, price1], [unix2, price2]]
        s = sum(x[1] for x in pa)
        # Return SMA, avergae of price over n days
        return s / n
        
    @staticmethod
    def getBB(coin: str, d: int):
        pass

    @staticmethod
    def getRSI(coin: str):
        ''' get RSI of a given coin '''
        # Get price action and define +/- lists
        pa = Indicators.getHistorical(coin, 14)
        p = list()
        n = list()
        # Get RSI of last 14 days
        for i in range(0, 14):
            # Difference in price between days
            d = pa[i][1] - pa[i+1][1]
            # Sort by +/-, append |diff|
            if d < 0:
                n.append(abs(d))
            else:
                p.append(abs(d))
        # Average gain / Average loss
        rs = (sum(p) / 14) / (sum(n) / 14)
        # Comupte and return RSI 
        return 100 - (100 / (1 + rs))
