import pandas as pd
import time


def checkFiles():
    dataframes = {}
    excelFile = pd.ExcelFile("Z:/Jim/MOI/PSMS/UploadData.xlsx")
    sheetNames = excelFile.sheet_names
    for sheetName in sheetNames:
        dataframes[sheetName] = pd.read_excel(excelFile, sheet_name=sheetName)
    work = dataframes["MasterBC"]
    ap = dataframes["001"]
    al = dataframes["002"]
    ms = dataframes["003"]

    # pd.ExcelFile("UploadData.xlsx").sheet_names - Check Sheetnames

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

        print("Extracting Files... \n")
        time.sleep(3)
        print(f"Total Items : {totalLine} ")

        validate = input("Save File? Y/N: ")
        if "y" in validate:
            try:
                with pd.ExcelWriter(
                    "Z:/Jim/MOI/PSMS/SalesLog.xlsx", engine="openpyxl"
                ) as writer:
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
