# Driver Financial Report
# Author: Jacob Thomas
# Date: 08/9/22

import datetime
import pandas

def option7():

    # Date Inputs Need to validate
    while True:
        try:
            StartDate = input("Enter the start date for listing (MM-DD-YY): ")
            StartDate = datetime.datetime.strptime(StartDate, "%m-%d-%y")
        except:
            print("Invalid Date Format. Try again.")
        else:
            break

    StartDateFormat = datetime.datetime.strftime(StartDate, "%m-%d-%y")

    while True:
        try:
            EndDate = input("Enter the end date for listing (MM-DD-YY): ")
            EndDate = datetime.datetime.strptime(EndDate, "%m-%d-%y")
        except:
            print("Invalid Date Format. Try again.")
        else:
            break

    EndDateFormat = datetime.datetime.strftime(EndDate, "%m-%d-%y")

    # Start of listing
    print()
    print("HAB Taxi Services")
    print(f"Driver Financial Listing from {StartDateFormat} to {EndDateFormat}")
    print()
    print("Driver    Transaction   Transaction          Transaction                Transaction")
    print("Number       Date       Description            Amount          HST         Total")
    print("===================================================================================")

    # Open Revenue.dat File
    R = open("Revenues.dat", "r")

    # Accumulators and Counters
    TransCtr = 0
    TransAmtAcc = 0
    HSTAcc = 0
    TransTotalAcc = 0

    # Getting Data into a list
    for rev_data in R:
        data = rev_data.split(",")

        TransDate = data[1].strip()
        TransDesc = data[2].strip()
        DriverNum = data[3].strip()
        TransAmt = float(data[4].strip())
        HST = float(data[5].strip())
        TotalAmt = float(data[6].strip())

        # Formatting Detail line variables
        TransAmtFormat = "${:.2f}".format(TransAmt)
        HSTFormat = "${:.2f}".format(HST)
        TotalAmtFormat = "${:.2f}".format(TotalAmt)

        DateList = pandas.date_range(StartDate, EndDate - datetime.timedelta(days=1), freq='d')

        if TransDate in DateList:
            print(f"{DriverNum}      {TransDate}    {TransDesc:<20s} {TransAmtFormat:>7s}        {HSTFormat:>7s}         {TotalAmtFormat:>7s}")
            TransCtr += 1
            TransAmtAcc += TransAmt
            HSTAcc += HST
            TransTotalAcc += TotalAmt

    print("===================================================================================")

    # Formatting Accumulators and counters
    TransAmtAccFormat = "${:.2f}".format(TransAmtAcc)
    HSTAccFormat = "${:.2f}".format(HSTAcc)
    TransTotalAccFormat = "${:.2f}".format(TransTotalAcc)

    print(f"Total Number of Transaction: {TransCtr:>2d}            {TransAmtAccFormat:>9s}        {HSTAccFormat:>7s}       {TransTotalAccFormat:>9s}")
    print()

    backtomenu = input("Press enter to return to main menu. ")