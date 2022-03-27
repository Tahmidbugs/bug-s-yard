

import csv
with open("fake_data_list.csv") as f:
  file=csv.reader(f)
  file=list(file)[1:]
