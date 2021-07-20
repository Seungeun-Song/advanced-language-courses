import sweetviz as sv
import pandas as pd

df_train = pd.read_csv("train.csv")

my_report = sv.analyze(df_train)
my_report.show_html()