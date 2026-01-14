import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
total_students = len(df["Names"])

df["Result"] = df["Marks"].apply(
    lambda x : "Pass" if x>65 else "Fail"
)
passed = df[df["Result"]=="Pass"]
failed = df[df["Result"]=="Fail"]
pass_percentage = (len(passed)/total_students)*100


sorted = df.sort_values(by="Marks",ascending=False)
top3 = sorted.head(3)
last2 = sorted.tail(2)


print("-----STUDENT PERFORMANCE ANALYZER-----")
print("Total Students        :",total_students)
print("Students Passed       :",len(passed))
print("Students Failed       :",len(failed))
print("Pass Percentage       :",pass_percentage) 

print("\n\nTop 3 Students :")
for index,row in top3.iterrows():
    print(row["Names"],row["Marks"])

print("\n\nStudents needing attention : ")
for index,row in last2.iterrows():
    print(row["Names"])

plt.bar(df["Names"],df["Marks"],label="Marks")
plt.legend()
plt.show()
df.to_csv("students_final.csv",index=False)