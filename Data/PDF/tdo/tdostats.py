import pdfplumber
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

pdf = pdfplumber.open("tdo.pdf")

loc_columns = ["Month_Year", "Total_Events"]


def get_total(doc):
    total_rows = []
    year_counter = 2014
    select_pages = [1, 2, 3, 4, 5, 7, 10, 13]
    doc_pages = list(doc.pages[i] for i in select_pages)
    for page in doc_pages:
        tab_first_half = page.extract_table()[-13:-7]
        tab_second_half = page.extract_table()[-7:-1]
        if year_counter < 2016:
            for row in tab_first_half:
                total_rows.append([row[0] + " " + str(year_counter), row[6]])
            for row in tab_second_half:
                total_rows.append([row[0] + " " + str(year_counter + 1), row[6]])
        else:
            for row in tab_first_half:
                total_rows.append([row[0] + " " + str(year_counter), row[7]])
            for row in tab_second_half:
                total_rows.append([row[0] + " " + str(year_counter + 1), row[7]])
        year_counter += 1
    return total_rows

test = get_total(pdf)
print(test)
