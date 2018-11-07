"""
Filename: core/match.py

Author: Santosh Purja Pun (punsantosh1991@outlook.com)

Description: This is match class. The function of this class is to receive two match bids and return the profit for
auctioneer, seller and buyers.
"""

from options import opts

class Match:
    def __init__(self, askBid, buyBid):
        self.askBid = askBid
        self.buyBid = buyBid
        self.clearningQuantity = 0

        self.clearingPrice = 0.0
        self.bidfee = opts['BIDFEE']
        self.clearingfee = opts['CLEARINGFEE']
        self.profitfee = opts['PROFITFEE']

        self.FeesForBuyer = 0.0
        self.FeesForSeller = 0.0

        self.calculateClearningPrice()
        self.calculateClearingQuantity()
        self.calculateFees()

    def matchedBids(self):
        return self.askBid.getBidInfo(hideReservePrice=True) + '<---->' + self.buyBid.getBidInfo(hideReservePrice=True) + ' with clearing price: ' +\
               opts['CURRENCY'] + str(self.clearingPrice)

    def calculateClearningPrice(self):
        self.clearingPrice = round((self.askBid.getBidAmount() + self.buyBid.getBidAmount()) / 2, 2)

    def calculateClearingQuantity(self):
        if self.askBid.getQuantity() > self.buyBid.getQuantity():
            self.clearningQuantity = self.buyBid.getQuantity()

        elif self.askBid.getQuantity() < self.buyBid.getQuantity():
            self.clearningQuantity = self.askBid.getQuantity()

        elif self.askBid.getQuantity() == self.buyBid.getQuantity():
            self.clearningQuantity = self.buyBid.getQuantity()

    def calculateFees(self):
        """
        calculates the profit for the auctioneer from the current matched bids
        profit_from_seller = bidfee + clearingfee + profitfee * (clearingPrice - bidPrice) * clearingQuantity
        profit_buyer = bidfee + clearingfee + profitfee * (bidPrice - clearningPrice) * clearingQuantity
        :return:
        """

        self.FeesForSeller = self.bidfee + self.clearingfee + self.profitfee * (
                    self.clearingPrice - self.askBid.getBidAmount()) * self.clearningQuantity

        self.FeesForBuyer = self.bidfee + self.clearingfee + self.profitfee * (
                    self.buyBid.getBidAmount() - self.clearingPrice) * self.clearningQuantity


    def getAuctioneerProfit(self):
        profit = self.FeesForSeller + self.FeesForBuyer
        return profit

    def getSellersProfit(self):
        """
        calculates the profit for seller from the current matched bid
        profit = (clearingPrice - reservedPrice) * clearingQuantity

        :return: profit
        """
        profit = (self.clearingPrice - self.askBid.getReservedPrice())*self.clearningQuantity - self.FeesForSeller
        return profit

    def getBuyersProfit(self):
        """
        calculates the profit for seller from the current matched bid
        profit = (reservedPrice - clearingPrice) * clearingQuantity

        :return: profit
        """
        profit = (self.buyBid.getReservedPrice() - self.clearingPrice) * self.clearningQuantity - self.FeesForBuyer
        return profit
