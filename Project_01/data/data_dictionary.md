# Data Dictionary

| Entity | Attribute | Data Type | Description |
|---------|----------|--------------|-------------|
| Student | id | int | Unique identifier for the student |
| Student | name | varchar | Name of the student |
| Student | gender | varchar | Gender of the student |
| Student | age | int | Age of the student |
| Student | marital_status | varchar | Marital status of the student |
| Student | educational_level | varchar | Educational level of the student |
| Student | job | varchar | Information about whether the student works or not |
| Student | income | int | Income of the student |
| Student | socioeconomic_stratum | int | Socioeconomic stratum of the student |
| Student | region | varchar | Region of residence of the student |
| Student | institution_type | varchar | Type of institution where the student studies |
| Student | academic_program_id | int | ID of the academic program the student is taking |
| Student | modality | varchar | Modality of study of the student (face-to-face, virtual, etc.) |
| Student | schedule | varchar | Study schedule of the student (day, night, etc.) |
| Student | dropout | boolean | Indicates whether the student dropped out or not |
| Student | academic_performance | float | Academic performance of the student |
| Student | attendance | float | Attendance of the student to classes |
| Student | commitment_level | float | Level of commitment of the student with their studies |
| Student | socioeconomic_factors | varchar | Socioeconomic factors that may affect the student |
| Student | personal_factors | varchar | Personal factors that may affect the student |
| Student | social_interactions | varchar | Information about the social interactions of the student |
| Student | feelings | varchar | Information about the feelings of the student |
| Institution | id | int | Unique identifier for the institution |
| Institution | name | varchar | Name of the institution |
| Institution | type | varchar | Type of institution (public, private, etc.) |
| Institution | region | varchar | Region where the institution is located |
| Academic_Program | id | int | Unique identifier for the academic program |
| Academic_Program | name | varchar | Name of the academic program |
| Academic_Program | level | varchar | Level of the academic program (undergraduate, postgraduate, etc.) |
| Academic_Program | duration | int | Duration of the academic program in semesters |
| Academic_Program | institution_id | int | ID of the institution offering the academic program |
| Social_Interaction | id | int | Unique identifier for the social interaction |
| Social_Interaction | student_id | int | ID of the student participating in the social interaction |
| Social_Interaction | type | varchar | Type of social interaction (online, in person, etc.) |
| Social_Interaction | date | date | Date of the social interaction |
| Social_Interaction | sentiment | varchar | Sentiment expressed in the social interaction |
| Alert | id | int | Unique identifier for the alert |
| Alert | student_id | int | ID of the student the alert refers to |
| Alert | date | date | Date of the alert |
| Alert | risk | varchar | Risk level of the alert (high, medium, low) |
| Alert | probability | float | Probability of the student dropping out of the institution |


