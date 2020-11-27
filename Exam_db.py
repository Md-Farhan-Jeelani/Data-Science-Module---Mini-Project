import numpy as np
import pandas as pd
import io
import datetime


df1 = pd.read_csv (r'examdatabase.csv')
print (df1)
# Stage One: Finalization of Candidate Count
# 1. Calculate Candidate count in each district based on the first choice of examination city.
candidate_count = df1.groupby(["TH_CENT_CH"]).size().reset_index(name='Number_of_Candidate')
print(candidate_count)

# 3. Find out the number of General, SC, ST & OBC candidates and visualize the distribution using a suitable plot identifying ratio of women candidates in each of these categories.

Category_count = df1.groupby(["CATEGORY"]).size().reset_index(name='Number_of_Candidate')
print(Category_count)

x = df1.groupby(['CATEGORY','SEX'])['SEX'].count()
y=df1.groupby(['CATEGORY'])['SEX'].count()
r=((x/y)*100).round(2)
print(r)

# Now to plot :

r.plot(kind='bar', stacked=True)


# 2. Assume that as per policy district having more than 25 students should have examination centre. District in which students are less than 25, adjust those students to other districts based on their second choices and find the final candidate count of each district.
df_count = pd.read_csv(io.StringIO("""
Dist    Count
WGL     299
MAHB    289
KUN     249
GUN     198
KARN    196
KRS     171
CTT     169
VIZ     150
PRA     145
NALG    130
MED     128
ADI     123
KPM     119
TRI     107
ANA     107
KHAM    85
NEL     85
VIZI    84
EGOD    84
SOA     84
SIR     80
NIZA    73
PUD     70
KRK     69
WGOD    56
"""), sep=r"\s{2,}", engine="python")

# Stage Two: Preparation of Database
# In each examination centre, exam is to be organised in two shifts batch I & batch II(reporting time 9:00 AM & 2 PM). Exam can be conducted any number of days in a city during December 1-30, 2020 depending upon the number of candidate in a city. Note in each city only one examination centre is possible and in one shift maximum 20 students can appear.
# 4. Based on the information mentioned above complete the examination database by allocating:
# o Rollno: Roll number of the candidate will start from NL2000001 onwards(eg: NL2000001,NL2000002,NL2000003……)
# o cent_allot : allocate centre by putting examination city code
# o cent_add: put NIELIT <District Name> as center address in each location (for eg if district name is ADI then centre add is NIELIT ADI)
# o examDate: Allocate any exam date between December 1,2020 to December 30, 2020 keeping minimum no of examination days and not violating any conditions mentioned above

df = df_count.loc[np.repeat(df_count.index.values, df_count["Count"]), "Dist"]\
    .sample(frac=1)\
    .reset_index(drop=True)\
    .to_frame()\
    .rename(columns={"Dist": "cent_allot"})


df["Rollno"] = df.index.map(lambda s: f"NL2{s+1:06}")
df["cent_add"] = df["cent_allot"].map(lambda s: f"NIELIT {s}")


# Assign the first examDate
first_day = datetime.date(2020, 12, 1)

# running no. grouped by "cent_allot" (i.e. "Dist")
df["gp_no"] = df.groupby("cent_allot").cumcount()

# increase one day for every 40 records
df["examDate"] = df["gp_no"].apply(lambda x: first_day + datetime.timedelta(days=int(x / 40)))

# batch - can be determined by the even-ness of int(no. / 20)
df["batch"] = df["gp_no"].apply(lambda x: 1 + int(x / 20) % 2)

# map batch to time (or "9 AM" / "2 PM" as you'd like)
df["rep_time"] = df["batch"].apply(lambda x: datetime.time(9, 0) if x == 1 else datetime.time(14, 0))

print(df[["Rollno", "cent_allot", "cent_add", "examDate", "batch", "rep_time"]])




