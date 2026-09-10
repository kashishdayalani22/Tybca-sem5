import numpy as np

sales = np.array([
    [1200, 1500, 1800, 1600, 2000],   
    [900, 1100, 1000, 1200, 1300],   
    [2500, 2700, 2600, 3000, 3200],   
    [700, 800, 750, 900, 950]      
])

categories = np.array(["Grocery", "Clothing", "Electronics", "Stationery"])
days = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])


print("1. Complete Sales Array:")
print(sales)


print("\n2. Number of rows and columns:")
print(sales.shape)


print("\n3. Dimension of sales array:")
print(sales.ndim)


print("\n4. Sales of Electronics:")
print(sales[2])


print("\n5. Sales made on Monday:")
print(sales[:, 0])


print("\n6. Grocery sales from Monday to Wednesday:")
print(sales[0, 0:3])



print("\n7. Sales of Clothing and Electronics:")
print(sales[1:3])


category_total = np.sum(sales, axis=1)

print("\n8. Total sales of each product category:")
for i in range(len(categories)):
    print(categories[i], "=", category_total[i])


day_total = np.sum(sales, axis=0)

print("\n9. Total sales for each day:")
for i in range(len(days)):
    print(days[i], "=", day_total[i])



category_average = np.mean(sales, axis=1)

print("\n10. Average daily sales of each product category:")
for i in range(len(categories)):
    print(categories[i], "=", category_average[i])



category_max = np.max(sales, axis=1)

print("\n11. Maximum sales for each product category:")
for i in range(len(categories)):
    print(categories[i], "=", category_max[i])


category_min = np.min(sales, axis=1)

print("\n12. Minimum sales for each product category:")
for i in range(len(categories)):
    print(categories[i], "=", category_min[i])

overall_total = np.sum(sales)

print("\n13. Overall total sales:")
print(overall_total)


overall_average = np.mean(sales)

print("\n14. Overall average sales:")
print(overall_average)


print("\n15. Total sales category-wise (axis=1):")
print(np.sum(sales, axis=1))


print("\n16. Total sales day-wise (axis=0):")
print(np.sum(sales, axis=0))

highest_category_index = np.argmax(category_total)

print("\n17. Category having the highest total sales:")
print(categories[highest_category_index])


lowest_category_index = np.argmin(category_total)

print("\n18. Category having the lowest total sales:")
print(categories[lowest_category_index])


highest_day_index = np.argmax(day_total)

print("\n19. Day having the highest total sales:")
print(days[highest_day_index])


lowest_day_index = np.argmin(day_total)

print("\n20. Day having the lowest total sales:")
print(days[lowest_day_index])


highest_sale = np.max(sales)

print("\n21. Highest individual sales value:")
print(highest_sale)


lowest_sale = np.min(sales)

print("\n22. Lowest individual sales value:")
print(lowest_sale)

print("Category corresponding to highest total sales:")
print(categories[highest_category_index])


greater_2000 = sales[sales > 2000]

print("\n23. Sales values greater than ₹2,000:")
print(greater_2000)


less_1000 = sales[sales < 1000]

print("\n24. Sales values less than ₹1,000:")
print(less_1000)



count_greater_2000 = np.sum(sales > 2000)

print("\n25. Number of sales greater than ₹2,000:")
print(count_greater_2000)


count_less_1000 = np.sum(sales < 1000)

print("\n26. Number of sales less than ₹1,000:")
print(count_less_1000)


between_1000_2000 = sales[(sales >= 1000) & (sales <= 2000)]

print("\n27. Sales values between ₹1,000 and ₹2,000:")
print(between_1000_2000)


classification = np.where(sales >= 2000, "High", "Normal")

print("\n28. Sales classification:")
print(classification)

greater_2500 = np.where(sales > 2500, sales, 0)

print("\n29. Sales values greater than ₹2,500:")
print(greater_2500)


sales_replaced = np.where(sales < 1000, 1000, sales)

print("\n30. Sales after replacing values below ₹1,000:")
print(sales_replaced)

sorted_sales = np.sort(sales.flatten())

print("\n31. All sales values in ascending order:")
print(sorted_sales)

sorted_electronics = np.sort(sales[2])

print("\n32. Electronics sales in ascending order:")
print(sorted_electronics)

unique_sales = np.unique(sales)

print("\n33. Unique sales values:")
print(unique_sales)

unique_values, frequencies = np.unique(sales, return_counts=True)

print("\n34. Unique sales values and their frequencies:")
for value, frequency in zip(unique_values, frequencies):
    print(value, "=", frequency)

most_frequent_index = np.argmax(frequencies)
most_frequent_value = unique_values[most_frequent_index]

print("\n35. Sales amount occurring most frequently:")
print(most_frequent_value)

print("Frequency:")
print(frequencies[most_frequent_index])


new_sales = sales * 1.10

print("\n36. Sales increased by 10%:")
print(new_sales)


print("\n37. New sales data:")
print(new_sales)


new_total = np.sum(new_sales)

print("\n38. New total sales:")
print(new_total)


difference = new_total - overall_total

print("\n39. Difference between old and new total sales:")
print(difference)