"""
Filename: core/auctioneer.py

Author: Santosh Purja Pun (punsantosh1991@outlook.com)

Description: This is auctioneer class. It receives all bid information and matches them.
"""

from options import opts
from core.match import Match


class Auctioneer:
    def __init__(self):
        self.askBids = []
        self.buyBids = []
        self.buyers = []
        self.sellers = []
        self.profit = opts['PROFITAMT']

        self.matchedBidsInfo = []

    def matchBids(self):
        flag = False
        while self.askBids[0].getBidAmount() <= self.buyBids[0].getBidAmount() and flag == False:
            match = Match(self.askBids[0], self.buyBids[0])

            # print the matched bids
            self.matchedBidsInfo.append(match.matchedBids())

            # update the profit for the auctioneer after each matched bid
            self.profit = self.profit + match.getAuctioneerProfit()

            flag = True

            # get the corresponding Traders for the current bid
            seller = next(filter(lambda seller: seller.traderID == self.askBids[0].getTraderID(), self.sellers))
            buyer = next(filter(lambda buyer: buyer.traderID == self.buyBids[0].getTraderID(), self.buyers))

            # update the profit for each of the trader
            seller.updateProfit(match.getSellersProfit())
            buyer.updateProfit(match.getBuyersProfit())

            # update the bids
            if self.askBids[0].getQuantity() > self.buyBids[0].getQuantity():
                tempQuantity = self.askBids[0].getQuantity() - self.buyBids[0].getQuantity()

                # update the bid quantity
                self.askBids[0].updateQuantity(tempQuantity)
                self.buyBids.pop(0)
                flag = False

            elif self.askBids[0].getQuantity() < self.buyBids[0].getQuantity():
                tempQuantity = self.buyBids[0].getQuantity() - self.askBids[0].getQuantity()

                # update the bid quantity
                self.buyBids[0].updateQuantity(tempQuantity)
                self.askBids.pop(0)
                flag = False

            elif self.askBids[0].getQuantity() == self.buyBids[0].getQuantity():
                # update the bid quantity
                self.buyBids.pop(0)
                self.askBids.pop(0)
                flag = False

        return self.matchedBidsInfo

    def setBids(self, askBids, buyBids):
        self.askBids = askBids
        self.buyBids = buyBids

    def setTraders(self, sellers, buyers):
        self.sellers = sellers
        self.buyers = buyers

    def getProfit(self):
        return self.profit
