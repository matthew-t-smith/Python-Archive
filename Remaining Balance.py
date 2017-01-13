balance = float(input("What is the outstanding balance on your card: $"))
annual_rate = input("What is the annual interest rate: ")
if "%" in annual_rate:
    annual_rate = float(annual_rate.strip("%")) / 100
elif ("per" or "perc" or "percent" or "pct") in annual_rate:
    annual_rate = float(annual_rate.strip("per" or "perc" or "percent" or "pct") / 100)
annual_rate = float(annual_rate)
min_monthly = input("What is the minimum monthly payment rate: ")
if "%" in min_monthly:
    min_monthly = float(min_monthly.strip("%")) / 100
elif ("per" or "perc" or "percent" or "pct") in min_monthly:
    min_monthly = float(min_monthly.strip("per" or "perc" or "percent" or "pct") / 100)
min_monthly = float(min_monthly)
paid = []
for m in range(12):
    MMP = min_monthly*balance
    IP = annual_rate/12*balance
    PP = MMP - IP
    balance = balance - PP
    paid.append(MMP)
    print("Month %s" % (m+1))
    print("Minimum monthly payment: $%s" % (round(MMP, 2)))
    print("Principle paid: $%s" % (round(PP, 2)))
    print("Remaining balance is $%s" % (round(balance, 2)))
    print()
total_paid = sum(paid)
print("RESULT")
print("Total amount paid: $%s" % (round(total_paid, 2)))
print("Remaining balance: $%s" % (round(balance, 2)))
    
