import csv
import shutil
from tempfile import NamedTemporaryFile


myfile ='Assessment.csv'
tempFile = NamedTemporaryFile(delete=False)

with open(myfile, 'rb') as csvfile, tempFile:
    fieldnames = ["Are you a Nigerian",
                  "Sex",
                  "Age (in years)",
                  "Occupation",
                  "Marital Status",
                  "Please indicate the highest level of education you have completed",
                  "How long (in years) have you been using social network sites?",
                  "How many social network sites are you a member of?",
                  "How often do you use your social network sites?",
                  "On average, how many hours do you spend online in a typical week?",
                  "Which of the social network sites are you a member of? (Please tick all that apply)",
                  "Which device do you use to access your social network sites? (Please tick all that apply)",
                  "What information do you include on your social network sites? (Please tick all that apply)",
                  "What do you essentially use social network sites for? (Please tick all that apply)",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Malware, e.g. virus]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Malicious apps, e.g., fake antivirus software]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Default privacy setting which are often poor]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Automated crawling and access]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Unauthorized exploitation and commercialization of usersâ€™ information by social network proprietors]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Social engineering: manipulating unsuspecting users on social network to act on otherwise risky behavior]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Phishing: a type of social engineering that involves deceiving users using social network to disclose their sensitive information]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Identity theft: appropriating a legitimate userâ€™s personal information without their knowledge to commit theft or fraud, including creating fake accounts in their name and posting messages under their ID]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Addiction: excessive/loss of control over use, which may lead to loss of interest in other activities]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Spamming: unsolicited messages]",
                  
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Cyberstalking: the repeated use of electronic communications to harass, threaten or frighten someone]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Malicious users with fake accounts]",
                  "Please indicate how much you are aware of each of the following risks posed by social network sites: [Clickjacking: a malicious technique of tricking a social network user into clicking on something different from what the user perceives they are clicking on]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Customization of privacy setting]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [â€˜Unfriendingâ€™ someone]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Avoiding accidental sharing of personal details]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Being acquainted with privacy policy of social network site]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Selective disclosure of information]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Being selective with friend requests]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Turning off geotagging]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Removal of third-party plugins]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Use of strong passwords]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Using different passwords for different social network accounts]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Clicking links with caution]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Installation of anti-virus on device(s) used to access social network sites]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Not tagging or posting your specific location]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Always logging out of your social network]",
                  "Please indicate how much you are familiar with each of the following measures to mitigate risks on social network sites: [Not accepting connections or friendships with unfamiliar people]",
                  ]
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(tempFile, fieldnames=fieldnames)
    for rows in reader:
        rows['Sex'] = ''
        rows['Age (in years)'] = ''
        rows['Occupation'] = ''
        writer.writerow(rows)
    shutil.move(tempFile.name, csvfile)    
        









    
