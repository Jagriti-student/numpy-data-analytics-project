import numpy as np
expenses = np.array([
    [500, 200, 150, 100],
    [600, 250, 100, 150],
    [450, 300, 200, 120],
    [700, 150, 250, 180],
    [550, 400, 180, 200],
    [800, 350, 300, 250],
    [650, 220, 150, 170]
])

#-----------------Level 1: Basic Array Understanding------------------------------

#Print the complete expense array.
print(expenses)

#Check array shape.
print("Shape of array is : ",expenses.shape)

#Check number of dimensions.
print("Dimension of array is : ",expenses.ndim)

#Check total number of elements.
print("Total number of elements / size is : ", expenses.size)

#Access expenses of a particular day.
print("Day 5 expense is : ",expenses[4:5,0:4])

#Access a particular category.
print("Category 3 elements are : ", expenses[:,2:3])

#Check datatype of expense
print("Data Type of expense is : ",expenses.dtype)

#--------------------Level 2: Daily Expense Analysis-----------------------------

#Calculate total expense for each day.
print("Day 1 total expense : ",np.sum(expenses[0:1,0:4]))
print("Day 2 total expense : ",np.sum(expenses[1:2,0:4]))
print("Day 3 total expense : ",np.sum(expenses[2:3,0:4]))
print("Day 4 total expense : ",np.sum(expenses[3:4,0:4]))
print("Day 5 total expense : ",np.sum(expenses[4:5,0:4]))
print("Day 6 total expense : ",np.sum(expenses[5:6,0:4]))
print("Day 7 total expense : ",np.sum(expenses[6:7,0:4]))


#Find average daily spending.
print("Day 1 average expense : ",np.mean(expenses[0:1,0:4]))
print("Day 2 average expense : ",np.mean(expenses[1:2,0:4]))
print("Day 3 average expense : ",np.mean(expenses[2:3,0:4]))
print("Day 4 average expense : ",np.mean(expenses[3:4,0:4]))
print("Day 5 average expense : ",np.mean(expenses[4:5,0:4]))
print("Day 6 average expense : ",np.mean(expenses[5:6,0:4]))
print("Day 7 average expense : ",np.mean(expenses[6:7,0:4]))


#Find the day with the highest total spending.
daily_total=expenses.sum(axis=1)
print(daily_total)
highest_day = np.argmax(daily_total)
print("The day with the highest total spending : ",highest_day+1)


#Find the day with the lowest total spending.
lowest_day = np.argmin(daily_total)
print("The day with the lowest total spending : ",lowest_day+1)


#Find days where total spending exceeded a given budget.
given_budget=1000
days=np.where(daily_total > given_budget)[0]+1
print("Day where total spending exceeded a given budget : ",days)


#Count how many days exceeded the budget.
count=np.sum(daily_total > given_budget)
print("Total days exceeded the budget : ",count)

#------------------------Level 3: Category-wise Analysis----------------------

#Calculate total spending on each category.
total_expense_category=expenses.sum(axis=0)
print("Category Wise total expense : ",total_expense_category)


#Find the category with highest spending.
highest_category=np.argmax(total_expense_category)
print("The category with the highest total spending : ",highest_category+1)


#Find the category with lowest spending.
lowest_category=np.argmin(total_expense_category)
print("The category with the lowest total spending : ",lowest_category+1)


#Calculate average spending for each category.
print("Average spending of each category : ",np.mean(total_expense_category))


#Compare spending between categories.
if(total_expense_category[0]>total_expense_category[1]):
    print("Food spending is greater than Travel")
else:
    print("Travel spending is greater than Food")

if(total_expense_category[1]>total_expense_category[2]):
    print("Travel spending is greater than Shopping")
else:
    print("Shopping spending is greater than Travel")

if(total_expense_category[2]>total_expense_category[3]):
    print("Shopping spending is greater than other")
else:
    print("Others spending is greater than Shopping")

#-----------------------Level 4: NumPy Indexing & Filtering Practice---------------

#Find all expenses greater than 300.
print("Expenses greater than 300 : ",expenses[expenses>300])


#Find days where Food expense exceeded 600.
print("Expenses greater than 600 : ",np.where(expenses[:,0:1]>600)[0]+1)


#Find days where Shopping expense was below 200.
print("Expenses below than 200 : ",np.where(expenses[:,2]<200)[0]+1)


#Replace expenses above a certain limit (practice array modification).
limit=500
new_expenses = expenses.copy()
new_expenses[new_expenses > limit] = limit
print("Replace expenses above a certain limit : ", new_expenses)


#Apply a discount percentage to a particular category.
discount = expenses[:, 2] * 0.90
print("Shopping expenses after 10 percent discount:", discount)


#---------------------------Level 5: Statistics------------------------------------

#Find maximum expense.
print("Maximum of Expenses : ",np.max(expenses));


#Find minimum expense.
print("Minimum of Expenses : ",np.min(expenses));


#Find median expense.
print("Median of Expenses : ",np.median(expenses));


#Find standard deviation of expenses.
print("Standard Deviation of Expenses : ",np.std(expenses));


#Find variance of expenses.
print("Variance of Expenses : ",np.var(expenses))

#Calculate percentage contribution of each category to total expenses.
total_expense_category=expenses.sum(axis=0)
result=np.sum(expenses)
percentage=(total_expense_category/result)*100
print("Percentage contribution of each category to total expenses : ",percentage)

