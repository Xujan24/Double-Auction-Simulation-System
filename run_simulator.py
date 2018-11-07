"""
Filename: run_simulator.py

Author: Santosh Purja Pun (punsantosh1991@outlook.com)

Description: This is the main file which is used to run the simulation. This file creates buyers and sellers objects,
generates all the asking and buying bids and sort them. The sorted bids and the traders objects are then passed to the
auctioneer class to perform the matching. Finally, prints the results and create a text file containing all the simulation
results.
"""

from core.auctioneer import Auctioneer
from core.buyer import Buyer
from core.seller import Seller
from options import opts
import itertools

if __name__ == '__main__':
    # creating buyers and sellers
    buyers = list(map(lambda id: Buyer(id+1), range(0, opts['NUMBUYERS'])))
    sellers = list(map(lambda id: Seller(id+1), range(0, opts['NUMSELLERS'])))


    # generating bids
    # Since each trader gives a list of bids, so flattening the list of lists into a single list of bids
    askBids = itertools.chain.from_iterable(map(lambda seller: seller.generateBid(), sellers))
    buyBids = itertools.chain.from_iterable(map(lambda buyer: buyer.generateBid(), buyers))

    # sorting the bids in increasing order according to their bid price
    askBids = sorted(askBids, key=lambda bid: bid.getBidAmount(), reverse=False)
    buyBids = sorted(buyBids, key=lambda bid: bid.getBidAmount(), reverse=True)



    # print all generated bids
    print ("All Generated Bids")
    print ('(Note: Bid format (bidID, traderID, traderType, Quantity, Price, ReservedPrice)')
    print('-----------------------------------------')
    print('All Asking Bids:')
    for bid in askBids: print(bid.getBidInfo())

    print('All Buying Bids:')
    for bid in buyBids: print(bid.getBidInfo())

    # write the generated bids into the file
    with open(opts['OUTPUTFILE'], 'w') as f:
        f.write("All the Generated Bids:\n")
        f.write("(Note: Bid format (bidID, traderID, traderType, Quantity, Price, ReservedPrice)\n")
        f.write("------------------------------------------------------------\n")
        f.write("Asking Bids:\n")
        for bid in askBids: f.write(bid.getBidInfo() + '\n')
        f.write('\n')
        f.write("Buying Bids:\n")
        for bid in buyBids: f.write(bid.getBidInfo() + '\n')
        f.write('\n')

    # create the auctioneer and pass all the generated bids and traders
    auctioneer1 = Auctioneer()
    auctioneer1.setBids(askBids, buyBids)
    auctioneer1.setTraders(sellers, buyers)



    # get all the matched batches and print the result
    print("All Matching Bids")
    print("(Note: Bid Format (bidID, traderID, traderType, Quantity, Price)")
    print('-----------------------------------------')
    matchedBids = auctioneer1.matchBids()
    for match in matchedBids: print(match)



    # print all the unmatched bids
    print('All Unmatched bids:')
    print('(Note: Bid Format (bidID, traderID, traderType, Quantity, Price)')
    print('-----------------------------------------')
    print("All unmatched Asking Bids:")
    for bid in askBids: print(bid.getBidInfo(hideReservePrice=True))

    print("All unmatched Buying Bids:")
    for bid in buyBids: print(bid.getBidInfo(hideReservePrice=True))



    # print the profit for the auctioneer and each of the traders
    print('Total Profit for Auctioneer: ', opts['CURRENCY'],  round(auctioneer1.getProfit(), 2))
    for seller in sellers: print('Profit for SELLER', seller.getTraderID(), ': ', opts['CURRENCY'], round(seller.getProfit(),2))
    for buyer in buyers: print('Profit for BUYER', buyer.getTraderID(), ': ', opts['CURRENCY'], round(buyer.getProfit(),2))


    # write the results from the simulation to the the file.
    with open(opts['OUTPUTFILE'], 'a') as f:
        f.write("All the Matched Bids:\n")
        f.write("(Note: Bid Format (bidID, traderID, traderType, Quantity, Price)\n")
        f.write("------------------------------------------------------------\n")
        for match in matchedBids: f.write("%s\n" % match)
        f.write('\n')

        f.write("Unmatched Bids:\n")
        f.write("(Note: Bid Format (bidID, traderID, traderType, Quantity, Price)\n")
        f.write("------------------------------------------------------------\n")
        f.write("All unmatched asking Bids:\n")
        for bid in askBids: f.write(bid.getBidInfo(hideReservePrice=True) + '\n')
        f.write('\n')
        f.write("All unmatched buying Bids:\n")
        for bid in buyBids: f.write(bid.getBidInfo(hideReservePrice=True) + '\n')
        f.write('\n')

        f.write("Profits for Auctioneers and Each of the Traders:\n")
        f.write("------------------------------------------------------------\n")
        f.write('Total Profit for Auctioneer: ' + opts['CURRENCY'] + str(round(auctioneer1.getProfit(), 2)) + '\n\n')
        f.write("Profit for Sellers:\n")
        for seller in sellers: f.write('Profit for SELLER' + str(seller.getTraderID()) + ': ' + opts['CURRENCY'] +
                                       str(round(seller.getProfit(), 2)) + '\n')
        f.write("\nProfit for Buyers:\n")
        for buyer in buyers: f.write('Profit for BUYER' + str(buyer.getTraderID()) + ': ' + opts['CURRENCY'] +
                                     str(round(buyer.getProfit(), 2)) + '\n')