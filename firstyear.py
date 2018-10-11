<< << << < HEAD
import numpy as np
import pandas as pd

pd.set_option('display.max_colwidth', -1)
pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=np.nan)


def first(batch):
    index_col_2_yr = "B.TECH. Ist Yr TIMETABLE ODD SEMESTER 2018, JIIT-128(Effective from 12/09/2018)"

    timetable = pd.read_excel("timetable1.xlsx", index_col=index_col_2_yr)

    timetable.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    timetable.columns.name = " "

    # separating days

    mon = timetable.loc["MON":"TUES"].iloc[:-1]
    tue = timetable.loc["TUES":"WED"].iloc[:-1]
    wed = timetable.loc["WED":"THUR"].iloc[:-1]
    thu = timetable.loc["THUR":"FRI"].iloc[:-1]
    fri = timetable.loc["FRI":"SAT"].iloc[:-1]
    sat = timetable.loc["SAT":].iloc[:-1]

    days = [mon, tue, wed, thu, fri, sat]

    classdict = {'P': 'Practical', 'L': 'Lecture', 'T': 'Tutorial'}

    lecturerDict = {'AB': 'Anshu Banwari', 'NC': 'Nilu Chaudhary', 'EKTA': 'Ekta Srivastava', 'DV': 'Deepak Verma',
                    'RG': 'Ruchi Gautam', 'DCB': 'DINESH BISHT', 'SHARIQ': 'SHARIQ MURTAZA',
                    'SUK': 'SUDHANSHU KULSHRESTHA',
                    'VARSHA': 'VARSHA GARG', 'AVP': 'AVINASH CHANDRA PANDEY', 'BDJ': 'BANSIDHAR JOSHI', 'CG': 'CHARU',
                    'DVP': 'DEVPRIYA SONI', 'GN': 'GAURAV KUMAR NIGAM', 'GS': 'GAURAV SAXENA', 'HB': 'HIMANI BANSAL',
                    'HA': 'HIMANSHU AGRAWAL', 'HM': 'HIMANSHU MITTAL', 'KA': 'KRISHNA ASAWA', 'KM': 'KRITIKA RANI',
                    'MS': 'MUKESH SARASWAT', 'PM': 'PULKIT MEHNDIRATTA', 'RP': 'RAJU PAL', 'RA': 'RAVINDER AHUJA',
                    'SP': 'SANJEEV', 'AV': 'Dr. Amit Verma', 'ADV': 'Dr. Anshu D Varshney',
                    'PC': 'Dr. Prashant Chauhan',
                    'SD': 'Dr. Sandeep Chooker', 'SCK': 'Prof. S C Katyal', 'SKA': 'Dr. S K Awasthi',
                    'VM': 'Dr. Vikas Malik',
                    'SKV': 'SANTOSH KUMAR VERMA', 'AKB': 'AKANKSHA BHARDWAJ', 'AM': 'AMBALIKA SARKAR',
                    'AKH': 'ANKUR KULHARI',
                    'AR': 'ANUBHUTI RODA MOHINDRA', 'ARG': 'ANURADHA GUPTA', 'AVP': 'AVINASH CHANDRA PANDEY',
                    'ARTI': 'ARTI JAIN', 'ASH': 'ASHISH TRIPATHI'}

    subjectdict = {'GE111': 'Engineering Drawing & Design', 'MA111': 'Mathematics-1', 'PH111': 'Physics-I',
                   'GE112': 'Workshop', 'CI111': 'Software Development Fundamentals-I', 'PH171': 'Physics lab-I',
                   'HS112': 'English', 'CI171': 'Software development lab-I'}

    rows = []

    for i in range(len(days)):  # Number of days
        newlist = []
        for j in range(1, 10):  # Number of classes per day
            classes_in_slot = list(days[i][j].dropna())
            haveClasses = [i for i in range(len(classes_in_slot)) if
                           batch in classes_in_slot[i] or 'ALL' in classes_in_slot[i]]
            toShow = ''
            for hc in haveClasses:
                temp = classes_in_slot[hc].replace("\n", "")
                for cls in temp.split(', '):
                    typeofclass = cls[0]
                    roomNum = cls[cls.index('-') + 1:cls.index('/')] if (('-') in cls and ('/') in cls) else ""
                    subject = cls[cls.index('(') + 1:cls.index(')')] if ('(' in cls and (')') in cls) else ""
                    lecturer = cls[cls.index('/') + 1:] if (('-') in cls and ('/') in cls) else ""

                    typeofclass = classdict[cls[0]] if typeofclass in classdict else typeofclass
                    subject = subjectdict[subject] if subject in subjectdict else subject
                    lecturer = lecturerDict[lecturer] if lecturer in lecturerDict else lecturer

                    clsDetails = '[' + typeofclass + '][' + subject + '][' + roomNum + '][' + lecturer + ']'
                    toShow += clsDetails + '~'

                # print('toShow is ', toShow)
            newlist.append(toShow[:-1])
            # print('newlist is \n', newlist,'\n')
        rows.append(newlist)

    final = pd.DataFrame(rows, index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], columns=timetable.iloc[0])
    final.columns.name = "Days/Time"

    return final.transpose().to_dict('list')

# e7 = first("F5")

# for k in e7.keys():
#     print(k, '->\n', e7[k])
== == == =
import pandas as pd


def first(batch):
    index_col_2_yr = "B.TECH. Ist Yr TIMETABLE ODD SEMESTER 2018, JIIT-128(Effective from 12/09/2018)"

    data = pd.read_excel("timetable1.xlsx", index_col=index_col_2_yr)
    # sperating cols

    data.columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    data.columns.name = " "

    # seprating days

    mon = data.loc["MON":"TUES"].iloc[:-1]
    tue = data.loc["TUES":"WED"].iloc[:-1]
    wed = data.loc["WED":"THUR"].iloc[:-1]
    thu = data.loc["THUR":"FRI"].iloc[:-1]
    fri = data.loc["FRI":"SAT"].iloc[:-1]
    sat = data.loc["SAT":].iloc[:-1]

    # list of df
    data2 = [mon, tue, wed, thu, fri, sat]

    final = data.dropna()
    # data2
    # final=data.dropna()
    # final
    # edit data frame here . make first row the column labels

    rows = []

    # realgame
    # move all to class and fns

    for i in range(0, 6):
        newlist = []
        for j in range(1, 10):
            new = data2[i][j].dropna()
            new2 = new.str.contains(batch)
            new3 = new.str.contains('ALL')
            new2 = new2 | new3
            if not ((new[new2]).empty):
                temp = new[new2].tolist()[0].replace("\n", "")

                # comment to show subject code
                # temp1=temp.find('(')
                # temp2=temp.find(')')
                # temp=temp[:temp1]+temp[temp2+1:]
                # comment to show subject code

                temp3 = temp.find('/')
                temp = temp[:temp3]
                newlist.append(temp)
                # method 2
                # newlist.append(new[new2].tolist().replace('\n',''))
            else:
                newlist.append(" ")
        rows.append(newlist)

    # final.append(new[new2])
    # final

    final = pd.DataFrame(rows, index=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], columns=data.iloc[0])
    final.columns.name = "Days/Time"

    return (final.transpose().to_dict('list'))

>> >> >> > b7c89282744b1e0e9ef97f6d3f38ecee0b045b32
