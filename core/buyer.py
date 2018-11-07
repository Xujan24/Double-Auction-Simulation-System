"""
Filename: core/buyer.py

Author: Santosh Purja Pun (punsantosh1991@outlook.com)

Description: This is buyer class which extends the trader class.
"""

from core.trader import Trader
from options import opts

class Buyer(Trader):
    def __init__(self, buyerID):
        self.traderID = buyerID
        self.traderType = opts['BUYERBIDCHAR']
        self.profit = opts['PROFITAMT']
