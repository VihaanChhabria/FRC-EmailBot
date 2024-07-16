import csv

import utils.EmailGeneration as EmailGeneration
import utils.EmailSend as EmailSend

INPUT_COMPANIES_DIR = "companyData/inputCompanies.csv"
DO_NOT_EMAIL_LIST_DIR = "companyData/doNotEmailList.txt"

inputCompanies = list(csv.reader(open(INPUT_COMPANIES_DIR, encoding='utf-8-sig')))

doNotEmailList = []
for email in list(open(DO_NOT_EMAIL_LIST_DIR)):
    doNotEmailList.append(email.strip("\n"))

for companyData in inputCompanies[1:]:
    if not (companyData[0] in doNotEmailList):
        print(companyData)

        message = EmailGeneration.generateEmail(companyData[0])
        print(message+"\n\n\n\n\n")
        #EmailSend.sendEmail(message, companyData[1])