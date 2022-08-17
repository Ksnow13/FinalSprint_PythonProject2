# preparing option 6 for HAB Taxi service Main Menu
# Author: Kyle Snow
# Date: 2022-08-09

import datetime
import FormatValues as FV

def OptionSix():

   # Gathering and validating dates

    while True:
        while True:
            try:
                StartDate = input("Enter the listing start date (MM-DD-YY): ")
                StartDate = datetime.datetime.strptime(StartDate, "%m-%d-%y")
            except:
                print(" Error - Invalid format. Please try again")
            else:
                break

        while True:
            try:
                EndDate = input("Enter the listing end date (MM-DD-YY): ")
                EndDate = datetime.datetime.strptime(EndDate, "%m-%d-%y")
            except:
                print(" Error - Invalid format. Please try again ")
            else:
                break

        # Getting the constants from the defaults file

        CurrentDate = datetime.datetime.now()

        DefaultsData = open("Defaults.dat", "r")

        TransactionNum = int(DefaultsData.readline())
        DriverNum = int(DefaultsData.readline())
        MonthlyStandFees = float(DefaultsData.readline())
        DailyRentalFees = float(DefaultsData.readline())
        WeeklyRentalFees = float(DefaultsData.readline())
        HST_RATE = float(DefaultsData.readline())
        InvoiceNum = int(DefaultsData.readline())

        DefaultsData.close()

        # Creating the titles and headings

        print()
        print("__________________________________________________________________________________________")
        print("HAB TAXI SERVICES                                                 CURRENT DATE: {}".format(FV.FDateMedium(CurrentDate)))
        print()
        print("PROFIT REPORT BETWEEN ENTERED DATES")
        print()
        print()
        print("REVENUE LISTING BETWEEN {} & {}".format(FV.FDateMedium(StartDate),FV.FDateMedium(EndDate)))
        print()
        print("TRANSACTION  TRANSACTION                      DRIVER                             ")
        print("    ID          DATE            TYPE          NUMBER      SUBTOTAL      HST       TOTAL")
        print("========================================================================================")

        # Creating counters and accumulators

        TransactionCtr = 0
        SubTotalAcc = 0
        HSTAcc = 0
        TotalAcc = 0
        MontlyStandFeeCtr = 0
        DailyRentalFeeCtr = 0
        WeeklyRentalFeeCtr = 0
        MonthlyStandAcc = 0
        DailyRentalAcc = 0
        WeeklyRentalAcc = 0


        # Opening the data files and assigning values

        f = open("Revenues.dat", "r")

        for RevenueRecord in f:

            RevenueLine = RevenueRecord.split(",")

            TransNum = RevenueLine[0].strip()
            TransDate = RevenueLine[1].strip()
            TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
            RevenueStatus = RevenueLine[2].strip()
            DriverNumber = RevenueLine[3].strip()
            SubTotal = float(RevenueLine[4].strip())
            HST = float(RevenueLine[5].strip())
            Total = float(RevenueLine[6].strip())

            # Statement to determine what info gets printed
            # Adding values to counters and accumulators

            if TransDate <= EndDate and TransDate >= StartDate:

                TransactionCtr += 1
                SubTotalAcc += SubTotal
                HSTAcc += HST
                TotalAcc += Total

                if RevenueStatus == "Monthly Stand Fees":
                    MontlyStandFeeCtr += 1
                    MonthlyStandAcc += Total
                if RevenueStatus == "Daily Rental Fees":
                    DailyRentalFeeCtr += 1
                    DailyRentalAcc += Total
                if RevenueStatus == "Weekly Rental Fees":
                    WeeklyRentalFeeCtr += 1
                    WeeklyRentalAcc += Total


                print("    {:<3s}      {:<10s}   {:<18s}   {:>4s}       {:>7s}     {:>6s}     {:>7s}".format(TransNum, FV.FDateMedium(TransDate), RevenueStatus, DriverNumber, FV.FDollar2(SubTotal), FV.FDollar2(HST), FV.FDollar2(Total)))

        if TransactionCtr == 0:
            print(" No files on record between these dates.")

        print("========================================================================================")
        print("TOTAL LISTINGS: {:<3d}                                     {:>9s}    {:>7s}   {}".format(TransactionCtr, FV.FDollar2(SubTotalAcc), FV.FDollar2(HSTAcc), FV.FDollar2(TotalAcc)))

        f.close()


        print()
        print("                      -------------------------------------")

        # Creating title and headers for the second list

        print()
        print("EXPENSE LISTING BETWEEN {} & {}".format(FV.FDateMedium(StartDate), FV.FDateMedium(EndDate)))
        print()
        print("   INVOICE        INVOICE      DRIVER                                          ")
        print("   NUMBER          DATE        NUMBER     TYPE        SUBTOTAL      HST         TOTAL")
        print("======================================================================================")

        # creating counters and accumulators for the second list

        InvoiceCtr = 0
        EXSubtotalAcc = 0
        EX_HSTAcc = 0
        EXTotalAcc = 0
        RepairCtr = 0
        SuppliesCtr = 0
        RepairAcc = 0
        SuppliesAcc = 0

        # Opening the data file and assigning values

        f = open("Expenses.dat", "r")

        for ExpenseRecord in f:

            ExpenseLine = ExpenseRecord.split(",")

            InvNum = ExpenseLine[0].strip()
            InvDate = ExpenseLine[1].strip()
            InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
            DriverNum = ExpenseLine[2].strip()
            InvStatus = ExpenseLine[3].strip()
            EXSubtotal = float(ExpenseLine[7].strip())
            EX_HST = float(ExpenseLine[8].strip())
            EXTotal = float(ExpenseLine[9].strip())

            # Statement to determine what gets printed
            # Adding to the counters and accumulators

            if InvDate <= EndDate and InvDate >= StartDate:
                InvoiceCtr += 1
                EXSubtotalAcc += EXSubtotal
                EX_HSTAcc += EX_HST
                EXTotalAcc += EXTotal

                if InvStatus == "Repair":
                    RepairCtr += 1
                    RepairAcc += EXTotal
                if InvStatus == "Supplies":
                    SuppliesCtr += 1
                    SuppliesAcc += EXTotal


                print("     {:<3s}        {:<10s}      {:<4s}     {:<8s}     {:>7s}      {:>6s}      {:>7s}".format(InvNum, FV.FDateMedium(InvDate), DriverNum, InvStatus, FV.FDollar2(EXSubtotal), FV.FDollar2(EX_HST), FV.FDollar2(EXTotal)))

        if InvoiceCtr == 0:
            print(" No files on record between these dates.")

        print("======================================================================================")
        print("TOTAL LISTINGS: {:<3d}                                 {:>9s}     {:>7s}    {:>9s}".format(InvoiceCtr, FV.FDollar2(EXSubtotalAcc), FV.FDollar2(EX_HSTAcc),FV.FDollar2(EXTotalAcc)))

        f.close()

        # Creating additional analytical data by listing and adding counters/accumulators

        ProfitLoss = TotalAcc - EXTotalAcc

        print()
        print()
        print("ADDITIONAL ANALYTICAL DATA")
        print()
        print("MONTHLY STAND FEES: {:<2d}  -- REVENUE:  {:>9s}".format(MontlyStandFeeCtr, FV.FDollar2(MonthlyStandAcc)))
        print("DAILY RENTAL FEES:  {:<2d}  -- REVENUE:  {:>9s}      TOTAL REPAIRS:  {:<2d} -- SPENT: {:>7s}".format(DailyRentalFeeCtr, FV.FDollar2(DailyRentalAcc), RepairCtr, FV.FDollar2(RepairAcc)))
        print("WEEKLY RENTAL FEES: {:<2d}  -- REVENUE:  {:>9s}      TOTAL SUPPLIES: {:<2d} -- SPENT: {:>7s}".format(WeeklyRentalFeeCtr, FV.FDollar2(WeeklyRentalAcc), SuppliesCtr, FV.FDollar2(SuppliesAcc)))
        print()
        print()
        print("PROFIT DETAILS BASED ON THE REVENUE LIST & EXPENSES LIST ABOVE")
        print()
        print("REVENUE SUBTOTAL: {:>9s}   EXPENSES SUBTOTAL: {:>9s}   PROFIT LOSS:    {}".format(FV.FDollar2(SubTotalAcc), FV.FDollar2(EXSubtotalAcc), FV.FDollar2(TotalAcc)))
        print("REVENUE HST:        {:>7s}   EXPENSES HST:        {:>7s}                 - {}".format(FV.FDollar2(HSTAcc), FV.FDollar2(EX_HSTAcc), FV.FDollar2(EXTotalAcc)))
        print("REVENUE TOTAL:    {:>9s}   EXPENSES TOTAL:    {:>9s}                 ----------- ".format(FV.FDollar2(TotalAcc), FV.FDollar2(EXTotalAcc)))
        print("                                                                  PROFIT:    {}".format(FV.FDollar2(ProfitLoss)))
        print("__________________________________________________________________________________________")

        BackToMenu = input("Scroll up to see revenue listings and expense listing, press enter to leave. ")

        break