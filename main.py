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

# group by borough
group_std_dev = df_schools.groupby("borough")["total_SAT"]
# aggregate num_schools, average_SAT and std_SAT
agg_std_dev = group_std_dev.agg(num_schools="count", average_SAT="mean", std_SAT="std").reset_index()
# round values to two decimal places 
rounded_std_dev = agg_std_dev.round(2)

# create dataframe with only one row with the largest standard deviation
largest_std_dev = pd.DataFrame([rounded_std_dev.loc[rounded_std_dev["std_SAT"].idxmax()]])
print(largest_std_dev)
