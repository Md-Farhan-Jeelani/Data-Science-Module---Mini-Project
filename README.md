# Data-Science-Module---Mini-Project
You are a Controller of Examination (COE) in an Examination body which regularly organises an online examination. As a part of your reasonability you need to generate various reports from the database. Your task is to automate the entire process using pandas. Details of database are as follows:

Application_ID : ID of applicant
D_O_B : Date of Birth 
Sex : Gender of Candidate
H_Qual : Highest qualification of the candidate 
TH_CENT_CH : First choice of examination city
SEC_TH_CEN : Second Choice of Examination City 
CATEGORY : Category of student 
Rollno : Roll Number of the candidate (To be filled by CEO) 
cent_allot : Examination centre district (To be filled by CEO) 
cent_add : Examination Centre Address (To be filled by CEO)
examDate : Examination Date (To be filled by CEO)
batch : Allotted batch on examination Date (To be filled by CEO)
rep_time : Reporting time for examination (To be filled by CEO) 

# Stage One: Finalization of Candidate Count

1. Calculate Candidate count in each district based on the first choice of examination city. 

2. Assume that as per policy district having more than 25 students should have examination centre. District in which students are less than 25, adjust those students to other districts based on their second choices and find the final candidate count of each district. 

3. Find out the number of General, SC, ST &amp; OBC candidates and visualize the distribution using a suitable plot identifying ratio of women candidates in each of these categories.

# Stage Two: Preparation of Database 

In each examination centre, exam is to be organised in two shifts batch I &amp; batch II(reporting time 9:00 AM &amp; 2 PM). Exam can be conducted any number of days in a city during December 1-30, 2020 depending upon the number of candidate in a city. Note in each city only one examination centre is possible and in one shift maximum 20 students can appear.

4. Based on the information mentioned above complete the examination database by allocating: 
# Rollno:
Roll number of the candidate will start from NL2000001 onwards(eg: NL2000001,NL2000002,NL2000003……) 
# cent_allot :
allocate centre by putting examination city code o cent_add: put NIELIT &lt;District Name> as center address in each location (for eg if district name is ADI then centre add is NIELIT ADI) 
# examDate:
Allocate any exam date between December 1,2020 to December 30, 2020 keeping minimum no of examination days and not violating any conditions mentioned above 
# batch:
allocate batch I or II ensuring all the conditions mentioned above 
# rep_time:
for batch I reporting time is 9 AM and for batch II reporting time is 2 PM.
