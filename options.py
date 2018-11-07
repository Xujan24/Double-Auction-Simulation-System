"""
Filename: options.py

Author: Santosh Purja Pun (punsantosh1991@outlook.com)

Description: This file contains the values for all the parameters required for the simulation, which include price range,
quantity, number of bids each trader has to produce, and so on. Changing any value will directly affect the simulation.
"""
from collections import OrderedDict

opts = OrderedDict()

opts['MAXQUANTITY'] = 30             # maximum no of quantity
opts['MINQUANTITY'] = 1              # minimum no of quantity

opts['CURRENCY'] = 'AU$'             # set the currency
opts['MAXPRICE'] = 150.0             # maximum price
opts['MINPRICE'] = 50.0              # minimum price

opts['SELLERCRITICALPRICE'] = 90.0   # critical price point for seller
opts['BUYERCRITICALPRICE'] = 140.0   # critical price point for buyer
opts['SELLERSMARGIN'] = 0.4          # profit margin for seller
opts['BUYERSMARGIN'] = 0.05          # profit margin for buyer

opts['NUMBIDS'] = 10                 # no of bids each trader should produce

opts['NUMBUYERS'] = 10               # no of buyers
opts['NUMSELLERS'] = 10              # no of sellers
opts['BUYERBIDCHAR'] = 'B'           # character to represent buyer bids
opts['SELLERBIDCHAR'] = 'A'          # character to represent seller bids

opts['PROFITAMT'] = 0.0              # initial profit amount for each traders and auctioneers
opts['BIDFEE'] = 1.0                 # bid fee for each bid charged by the auctioneer
opts['CLEARINGFEE'] = 3.0            # clearing fee for each bid charged by the auctioneer
opts['PROFITFEE'] = 0.2              # profit fee for each bid charged by the auctioneer

opts['OUTPUTFILE'] = './results.txt' # specifies the file to write the simulation results