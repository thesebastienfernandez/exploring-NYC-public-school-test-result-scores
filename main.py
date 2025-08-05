import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# get dataframe 
df_schools = pd.DataFrame(schools)

# sort schools by average math score
math_schools = df_schools[["school_name", "average_math"]]
sorted_math_schools = math_schools.sort_values("average_math", ascending=False)
# select the best results (80% of 800 for math score)
best_math_schools = sorted_math_schools[sorted_math_schools["average_math"] > (800 *0.8)]
print(best_math_schools) 

# new column total_SAT, it's the sum of math's score, reading's score and writing's score
df_schools["total_SAT"] = df_schools["average_math"] + df_schools["average_reading"] + df_schools["average_writing"]

# get top 10 schools with best total SAT score
new_df_schools = df_schools[["school_name", "total_SAT"]]
top_10_schools = new_df_schools.sort_values("total_SAT", ascending=False)[0:10]
print(top_10_schools)