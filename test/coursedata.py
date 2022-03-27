

import csv
with open("Course_description.csv") as f:
  file2=csv.reader(f)
  file2=list(file2)[1:]
