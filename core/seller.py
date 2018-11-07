"""
Filename: core/buyer.py

Author: Santosh Purja Pun (punsantosh1991@outlook.com)

Description: This is seller class which extends the trader class.
"""

from core.trader import Trader
from options import opts

class Seller(Trader):
    def __init__(self, sellerID):
        self.traderID = sellerID
        self.traderType = opts['SELLERBIDCHAR']
        self.profit = opts['PROFITAMT']
