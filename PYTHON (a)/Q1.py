import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Kiran"],
    "Age": [20, 21, 19, 22, 20],
    "City": ["Ahmedabad", "Vadodara", "Surat", "Rajkot", "Ahmedabad"],
    "Marks": [75, 82, 68, 91, 79]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nColumn Names:")
print(df.columns)

print("\nIndex:")
print(df.index)

print("\nData Types:")
print(df.dtypes)

print("\nName Column:")
print(df["Name"])

print("\nMarks Column:")
print(df["Marks"])

print("\nName and City:")
print(df[["Name", "City"]])

print("\nName, Age and Marks:")
print(df[["Name", "Age", "Marks"]])

print("\nFirst Row:")
print(df.iloc[0])

print("\nThird Row:")
print(df.iloc[2])

print("\nFirst Three Rows:")
print(df.head(3))

print("\nLast Two Rows:")
print(df.tail(2))

print("\nFirst 3 Rows and First 2 Columns:")
print(df.iloc[:3, :2])

print("\nRows 2-4 and Name, Marks:")
print(df.loc[1:3, ["Name", "Marks"]])

print("\nName and Marks of First 3 Students:")
print(df.loc[:2, ["Name", "Marks"]])

print("\nNumber of Rows:")
print(df.shape[0])

print("\nNumber of Columns:")
print(df.shape[1])

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nBasic Statistical Information:")
print(df.describe())

df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail")

print("\nDataFrame after adding Result:")
print(df)

df["Percentage"] = df["Marks"]

print("\nDataFrame after adding Percentage:")
print(df)

print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

print("\nStudents from Vadodara:")
print(df[df["City"] == "Vadodara"])

print("\nMarks > 75 and Age <= 21:")
print(df[(df["Marks"] > 75) & (df["Age"] <= 21)])

print("\nMarks in Ascending Order:")
print(df.sort_values(by="Marks", ascending=True))

print("\nMarks in Descending Order:")
print(df.sort_values(by="Marks", ascending=False))

print("\nAverage Marks:")
print(df["Marks"].mean())

highest_marks = df["Marks"].max()
print("\nHighest Marks:")
print(highest_marks)

lowest_marks = df["Marks"].min()
print("\nLowest Marks:")
print(lowest_marks)

print("\nStudent with Highest Marks:")
print(df.loc[df["Marks"].idxmax()])

print("\nStudent with Lowest Marks:")
print(df.loc[df["Marks"].idxmin()])

print("\nTotal Number of Students:")
print(len(df))

print("\nStudents in Each City:")
print(df["City"].value_counts())

print("\nMissing Values:")
print(df.isnull().sum())