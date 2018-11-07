"""
Filename: core/trader.py

Author: Santosh Purja Pun (punsantosh1991@outlook.com)

Description: The primary function of this class is to generate bids for the simulation. This class will not be executed
directly, rather extended by the sellers and buyers class.
"""

from core.bid import Bid
from options import opts
import random


class Trader:
    def __init__(self):
        self.traderID = ""
        self.traderType = ""
        self.profit = 0

    def generateBid(self):
        """
        function to generate bids
        returns a list of Bids object.
        """
        # empty list to hold individual bid information
        bids = []
        for b in range(0, opts['NUMBIDS']):
            bidID = b+1
            reservedPrice = round(random.uniform(opts['MINPRICE'], opts['MAXPRICE']), 2)
            price = 0.0

            # generate bid quantity
            quantity = random.randint(opts['MINQUANTITY'], opts['MAXQUANTITY'])

            """
            For SELLERS:
            if the randomly generated amount is less than the critical price point set for the seller,
            then sellers profit margin of the generated amount will be added to the generated amount and set as the 
            bid price. And the reserved price will be the randomly generated price. Otherwise bid price and the reserved
            price will be same.

            For BUYERS:
            if the randomly generated amount is greater than the critical price point set for the buyer,
            then the buyers profit margin of the generated amount will be deducted to the generated amount and set 
            as the bid price. Ann the reserved price will be the randomly generated price. Otherwise bid price and the
            reserved price will be same.
            """

            # generate bid price for each selling bid
            if self.traderType == opts['SELLERBIDCHAR']:
                if reservedPrice < opts['SELLERCRITICALPRICE']:
                    price = round(reservedPrice + reservedPrice * opts['SELLERSMARGIN'], 2)
                else:
                    price = reservedPrice
            # generate bid price for each buying bids
            elif self.traderType == opts['BUYERBIDCHAR']:
                if reservedPrice > opts['BUYERCRITICALPRICE']:
                    price = round(reservedPrice - reservedPrice * opts['BUYERSMARGIN'], 2)
                else:
                    price = reservedPrice

            # append generated bid into a list
            bids.append(Bid(bidID, self.traderID, self.traderType, quantity, price, reservedPrice))

        return bids

    def updateProfit(self, profit):
        self.profit = self.profit + profit

    def getProfit(self):
        return self.profit

    def getTraderID(self):
        return self.traderID
