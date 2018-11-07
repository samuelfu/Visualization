import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress

file = 'data.xlsx'
spreadsheet = pd.ExcelFile(file)
df = spreadsheet.parse(spreadsheet.sheet_names[0])
target = spreadsheet.parse(spreadsheet.sheet_names[1])

regressor = LinearRegression()
regressor.fit(df,target)

# plot
fig = plt.figure()

plt.plot(df['beauty'], target['course_eval'], linestyle='none', marker='o')
result = []
for index, row in df.iterrows():
    result.append((regressor.intercept_ + regressor.coef_[0][0]* row['minority'] \
                  + regressor.coef_[0][1] * row['age'] \
                  + regressor.coef_[0][2] * row['female'] \
                  + regressor.coef_[0][3] * row['onecredit'] \
                  + regressor.coef_[0][4] * row['beauty'] \
                  + regressor.coef_[0][5] * row['intro'] \
                  + regressor.coef_[0][6] * row['nnenglish']).tolist())
result = sum(result,[])

plt.plot( df['beauty'], pd.DataFrame(result,columns=['course_eval']) )

fig.suptitle('Beauty of Teacher and Course Ratings', fontsize=20)
plt.xlabel('Beauty', fontsize=18)
plt.ylabel('Course Evaluation', fontsize=16)

plt.show()
