import math
loan_amount = [1250.0, 500.0, 1450.0, 200.0, 700.0, 100.0, 250.0, 225.0, 1200.0, 150.0, 600.0, 300.0, 700.0, 125.0, 650.0, 175.0, 1800.0, 1525.0, 575.0, 700.0, 1450.0, 400.0, 200.0, 1000.0, 350.0]
country_name = ['Azerbaijan', 'El Salvador', 'Bolivia', 'Paraguay', 'El Salvador', 'Philippines', 'Philippines', 'Nicaragua', 'Guatemala', 'Philippines', 'Paraguay', 'Philippines', 'Bolivia', 'Philippines', 'Philippines', 'Madagascar', 'Georgia', 'Uganda', 'Kenya', 'Tajikistan', 'Jordan', 'Kenya', 'Philippines', 'Ecuador', 'Kenya']
time_to_raise = [193075.0, 1157108.0, 1552939.0, 244945.0, 238797.0, 1248909.0, 773599.0, 116181.0, 2288095.0, 51668.0, 26717.0, 48030.0, 1839190.0, 71117.0, 580401.0, 800427.0, 1156218.0, 1166045.0, 2924705.0, 470622.0, 24078.0, 260044.0, 445938.0, 201408.0, 2370450.0]
num_lenders_total = [38, 18, 51, 3, 21, 1, 10, 8, 42, 1, 18, 6, 28, 5, 16, 7, 54, 1, 18, 22, 36, 12, 8, 24, 8]

#  Level 1 Questions
# 1) What is the total amount of money loaned?
# 2) What is the average loan amount?
# 3) What is the largest/smallest loan?
# 4) What country got the largest/smallest loan?
# 5) What is average number of lenders per loan?
# 6) What is total number of loans made to the Philippines?
# 7) For each unique country name, print a line that shows the name of the country and then the number of loans made in that country.

#1
loan_total = 0

for loan in loan_amount:
    loan_total += loan
print('Total amount of money loaned: ' + str(loan_total))

#2
loan_average = loan_total / len(loan_amount)
print('Average loan amount: ' + str(loan_average))

#3
min_loan = min(loan_amount)
max_loan = max(loan_amount)
print('Smallest loan: ' + str(min_loan))
print('Largest loan: ' + str(max_loan))

#4
min_country = country_name[loan_amount.index(min_loan)]
max_country = country_name[loan_amount.index(max_loan)]
print('Country with smallest loan: ' + str(min_country))
print('Country with largest loan: ' + str(max_country))

#5
average_lenders = sum(num_lenders_total) / len(loan_amount)
print('Average number of lenders per loan: ' + str(average_lenders))

#6
philippines_count = country_name.count('Philippines')
print('Total number of loans made to the Philippines: ' + str(philippines_count))

#7
unique_countries = ['Guatemala', 'Paraguay', 'Tajikistan', 'Kenya', 'Azerbaijan', 'El Salvador', 'Bolivia', 'Ecuador', 'Georgia', 'Philippines', 'Uganda', 'Madagascar', 'Nicaragua', 'Jordan']
total_country = 0

for country in range(len(unique_countries)):
    for entry in range(len(country_name)):
        if country_name[entry] == unique_countries[country]:
            total_country += 1
    print(str(unique_countries[country])+ ' ' + str(total_country))
    total_country = 0



#   Level 2 Questions
# 1) What is the average amount of loans made to people in the Philippines?
# 2) In which country was the loan granted that took the longest to fund?
# 3) What is the average amount of time / dollar it takes to fund a loan?
# 4) What is the standard deviation of the money loaned? The Empirical Rule or 68-95-99.7% Rule 
# reminds us that 68% of the population falls within 1 standard deviation. Does this hold for our data?
# 5) Calculate the pearson correlation between the loan_amount and the num_lenders_total.

#1
#The index positions for the Phillipines are [5, 6, 9, 11, 13, 14, 22]
index_philippines = [5, 6, 9, 11, 13, 14, 22]
p_loan_amount = 0
p_num_lenders = 0

for i in index_philippines:
    p_loan_amount += loan_amount[i]
p_average = p_loan_amount / 7   #Data from previous question
print('Average amount of loans made to people in the Philippines: {0:.2f}'.format(p_average))

#2
longest_to_fund = country_name[time_to_raise.index(max(time_to_raise))]
print('Country with the loan that took the longest to raise: ' + str(longest_to_fund))

#3
time_dollar = 0

for i in range(len(loan_amount)):
    time_dollar += time_to_raise[i] / loan_amount[i]
a_mean = time_dollar / len(loan_amount)
print('Arithmetic mean of the time / dollar it takes to fund a loan: {0:.2f}'.format(a_mean))

#4
variance_loan = 0

for value in loan_amount:
    variance_loan += ((value - loan_average) ** 2) / len(loan_amount)
loan_stdev = math.sqrt(variance_loan)
print('Standard deviation of the loan_amount: {0:.2f}'.format(loan_stdev))

#5
num_lenders_average = sum(num_lenders_total) / len(num_lenders_total)
covariance = 0
covariance_nominator = 0

for i in range(len(loan_amount)):
    covariance_nominator += (loan_amount[i] - loan_average) * (num_lenders_total[i] - num_lenders_average)
    covariance = covariance_nominator / len(num_lenders_total)
variance_lenders = 0

for value in num_lenders_total:
    variance_lenders += ((value - num_lenders_average) ** 2) / len(num_lenders_total)
num_lenders_stdev = math.sqrt(variance_lenders)
pearson = covariance / (loan_stdev * num_lenders_stdev)
print('Pearson correlation between the loan_amount and the num_lenders_total: {0:.2f}'.format(pearson))