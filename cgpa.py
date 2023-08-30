#Enter Number of subjects
Number_of_subjects=int(input("Enter the number of subjects:"))
credits_hours=0
weighted_points=0
for i in range(1,Number_of_subjects+1):
    grade_obtain=input(f"Enter your grade obtain of {i} subject: ")
    credit_hours=int (input("Enter credit hours:"))
    if grade_obtain=='A+':
        g_point=10
    elif grade_obtain=='A':
        g_point=9
    elif grade_obtain=='B':
        g_point=8
    elif grade_obtain=='C':
        g_point=7
    elif grade_obtain=='D':
        g_point=6
    elif grade_obtain=='E':
        g_point=5
    else:
        g_point=0

#calculate Weighted points
weighted_points=credit_hours*g_point
#calculate credits hours
credits_hours+=credit_hours
#calculate cgpa
CGPA=weighted_points/credit_hours
print(f"Your CGPA is {CGPA}")
