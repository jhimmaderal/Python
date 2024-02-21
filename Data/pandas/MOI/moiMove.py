import pandas as pd
import time
import datetime as dt

def stockAdjustment():
    def checkFiles():
        dataframes = {}
        excelFile = pd.ExcelFile("Z:/Jim/MOI/PSMS/UploadData.xlsx")
        sheetNames = excelFile.sheet_names
        for sheetName in sheetNames:
            dataframes[sheetName] = pd.read_excel(excelFile, sheet_name=sheetName)
        work = dataframes["MasterBC"]
        try:
             
            branch = str(input('Enter Branch Code: '))
            match branch:
                case '001' | 'ap':               
                    branchFile = pd.read_csv("Z:/Jim/MOI/PSMS/001.csv")
                    branchCode = '001'
                case '002' | 'al':
                    branchFile = pd.read_csv("Z:/Jim/MOI/PSMS/002.csv")
                    branchCode = '002'
                case '003' | 'ms':
                    branchFile = pd.read_csv("Z:/Jim/MOI/PSMS/003.csv")
                    branchCode = '003'
                case _:
                    print('No Branch Found ! Select Branch Again.')
                    checkFiles()
        except:
                print('No Branch Found ! Select Branch Again.')
                checkFiles()

        # pd.ExcelFile("UploadData.xlsx").sheet_names - Check Sheetname.

        def mergeFiles():
            columns = [
                "trdate",
                "doc_type",
                "item_code",
                "barcode",
                "Your Company CR#",
                "loc_id",
                "qty",
                "price",
                "tr_no",
                "tr_no",
                "no_of_bills",
            ]
            try:
                df1 = work.merge(ap, left_on="barcode", right_on="barcode", how="left")
                df2 = work.merge(al, left_on="barcode", right_on="barcode", how="left")
                df3 = work.merge(ms, left_on="barcode", right_on="barcode", how="left")

                df1 = df1[columns].dropna()
                df2 = df2[columns].dropna()
                df3 = df3[columns].dropna()

                line1 = len(df1)
                line2 = len(df2)
                line3 = len(df3)
                totalLine = line1 + line2 + line3
            except:
                df1 = work.merge(branchFile, left_on="barcode", right_on="barcode", how="left")
                df1["no_of_bills"] = df1["no_of_bills"].fillna(0)
                df1["loc_id"] = "B"+branchCode
                df1["trdate"] = dt.date.today().strftime("%Y-%m-%d")
                df1 = df1[columns].dropna()
                df1.insert(5, "Other Entity CR# - رقم السجل التجارى للطرف الاخر", "")
                line1 = len(df1)
                totalLine = len(df1)

            print("Extracting Files... \n")
            time.sleep(3)
            print(f"Total Items : {totalLine} ")

            validate = input("Save File? Y/N: ")
            if "y" in validate:
                try:
                    with pd.ExcelWriter(
                        "Z:/Jim/MOI/PSMS/SalesLog.xlsx", engine="openpyxl"
                    ) as writer:
                        try:
                            df1.to_excel(writer, "SalesLog", index=False)
                            df2.to_excel(
                                writer,
                                "SalesLog",
                                startrow=(line1 + 1),
                                header=False,
                                index=False,
                            )
                            df3.to_excel(
                                writer,
                                "SalesLog",
                                startrow=(line1 + line2 + 1),
                                header=False,
                                index=False,
                            )
                        except:                         
                            count = 0
                            for header in list(df1):
                                count = count + 1
                
                                if count == 1:
                                    df1 = df1.rename(
                                        columns={header: "Transaction Date - تاريخ الحركة"}
                                    )
                                   
                                if count == 2:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Transaction Type Code - كود نوع الحركة"
                                        }
                                    )
                                elif count == 3:
                                    df1 = df1.rename(
                                        columns={header: "Item Code - كود الصنف"}
                                    )
                                elif count == 4:
                                    df1 = df1.rename(
                                        columns={header: "Item Barcode - باركود الصنف"}
                                    )
                                elif count == 5:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Your Company CR# - رقم السجل التجارى للشركة"
                                        }
                                    )
                                elif count == 6:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Other Entity CR# - رقم السجل التجارى للطرف الاخر"
                                        }
                                    )
                                elif count == 7:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Company Store/Inventory Code - رقم المخزن "
                                        }
                                    )
                                elif count == 8:
                                    df1 = df1.rename(columns={header: "Quantity - الكمية"})

                                elif count == 9:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Selling Price per unit - سعر البيع للوحدة"
                                        }
                                    )
                                elif count == 10:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Comon Referance No. -  رقم المرجع المشترك"
                                        }
                                    )
                                elif count == 11:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Internal Transfer Number/Code - رقم التحويل الداخلي"
                                        }
                                    )
                                elif count == 12:
                                    df1 = df1.rename(
                                        columns={
                                            header: "Number of Consumer Invoices - عدد فواتير البيع للمستهلك"
                                        }
                                    )    
                            df1.to_excel(writer, "SalesLog", index=False)

                    dateNow = dt.date.today().strftime("%Y%m%d")
                    df = pd.read_excel('Z:/Jim/MOI/PSMS/SalesLog.xlsx')
                    df.to_csv(f'Z:/Jim/MOI/PSMS/{branchCode}_19070_TransactionData_{dateNow}.csv', index=False, sep="|")                
                    time.sleep(2)
                    print("\nFile Saved Succesfully \n")
                except PermissionError:
                    print(
                        "Permission denied: SalesLog.xlsx. Please close the file before running the script again."
                    )
                runAgain = input("Run script again ? Y/N: ")
                if "y" in runAgain:
                    checkFiles()
                else:
                    runApp()
            else:
                runApp()

        mergeFiles()


    def runApp():
        startApp = input("Do you want to run the script? Y/N: ")
        if "y" in startApp:
            checkFiles()
        else:
            exit()

    runApp()

