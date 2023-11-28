import pandas as pd

# Load data from CSV files (replace file paths with actual paths)
school_data = pd.read_csv('school_data.csv')
student_data = pd.read_csv('student_data.csv')

# Merge school and student data on school_id
merged_data = pd.merge(student_data, school_data, how='left', on=['school_id', 'school_id'])

# Calculate district summary statistics
total_schools = merged_data['school_name'].nunique()
total_students = merged_data['student_id'].count()
total_budget = school_data['budget'].sum()
average_math_score = merged_data['math_score'].mean()
average_reading_score = merged_data['reading_score'].mean()
passing_math_percentage = (merged_data['math_score'] >= 70).sum() / total_students * 100
passing_reading_percentage = (merged_data['reading_score'] >= 70).sum() / total_students * 100
overall_passing_percentage = (merged_data[(merged_data['math_score'] >= 70) & 
                                           (merged_data['reading_score'] >= 70)]['student_id'].count() / total_students) * 100

# Create a district summary DataFrame
district_summary = pd.DataFrame({
    'Total Schools': [total_schools],
    'Total Students': [total_students],
    'Total Budget': [total_budget],
    'Average Math Score': [average_math_score],
    'Average Reading Score': [average_reading_score],
    '% Passing Math': [passing_math_percentage],
    '% Passing Reading': [passing_reading_percentage],
    '% Overall Passing': [overall_passing_percentage]
})

# Print district summary
print(district_summary)