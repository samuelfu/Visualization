'''
Course_eval : “Course overall” teaching evaluation score, on a scale of 1 (very unsatisfactory) to 5 (excellent)
Beauty: Rating of instructor physical appearance by a panel of six students,
    averaged across the six panelists, shifted to have mean zero
'''

import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

file = 'data.xlsx'
spreadsheet = pd.ExcelFile(file)
dataframe = spreadsheet.parse(spreadsheet.sheet_names[0])
dataframe = pd.concat([dataframe,spreadsheet.parse(spreadsheet.sheet_names[1])], axis=1)
# plot
fig = plt.figure()
stats = linregress(dataframe['beauty'], dataframe['course_eval'])

plt.plot('beauty', 'course_eval', data=dataframe, linestyle='none', marker='o')
plt.plot(dataframe['beauty'], stats.slope * dataframe['beauty']+stats.intercept)

fig.suptitle('Beauty of Teacher and Course Ratings', fontsize=20)
plt.xlabel('Beauty', fontsize=18)
plt.ylabel('Course Evaluation', fontsize=16)

plt.show()

