from faker import Faker
import pandas as pd
import random

# Instantiate a Faker object
fake = Faker()

# Define the number of records
num_records = 1000

# Create empty lists for each attribute
student_id = []
student_name = []
academic_performance = []
attendance = []
engagement_level = []
socioeconomic_status = []
personal_factors = []
dropout = []

# Generate synthetic data
for _ in range(num_records):
    student_id.append(fake.unique.random_number(digits=5))
    student_name.append(fake.name())
    academic_performance.append(random.uniform(0, 100))
    attendance.append(random.uniform(0, 100))
    engagement_level.append(random.choice(['Low', 'Medium', 'High']))
    socioeconomic_status.append(random.choice(['Low', 'Medium', 'High']))
    personal_factors.append(fake.text())
    dropout.append(random.choice([0, 1]))

# Create a DataFrame
data = pd.DataFrame({
    'student_id': student_id,
    'student_name': student_name,
    'academic_performance': academic_performance,
    'attendance': attendance,
    'engagement_level': engagement_level,
    'socioeconomic_status': socioeconomic_status,
    'personal_factors': personal_factors,
    'dropout': dropout
})

# Save the DataFrame to a CSV file
data.to_csv('datos_desercion.csv', index=False)
