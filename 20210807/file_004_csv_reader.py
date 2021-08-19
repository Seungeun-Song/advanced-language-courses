import csv
import pandas as pd


def display_csv_reader():
    with open("example/monsters.csv", encoding="UTF-8") as f:
        reader = csv.reader(f, delimiter=",") # tsv : tab separated values(돈의 표시일때, ex, 100,000)  # delimiter = 구분자
        for row in reader:
            print(row[1])

def display_csv_reader_dict():
    with open("example/monsters.csv", encoding="UTF-8") as f:
        dictReader = csv.DictReader(f, delimiter =",")
        for row in dictReader:
            # print(type(row))   # <class 'dict'>
            print(row["monsterName"] + "의 값은" + row['price'])

def display_csv_pandas():
    df = pd.read_csv("example/monsters.csv")    
    print(df)
    print(df.shape)

if __name__ =="__main__":
    # display_csv_reader()
    # display_csv_reader_dict()
    display_csv_pandas()