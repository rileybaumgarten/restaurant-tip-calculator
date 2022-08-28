print("Welcome to the tip calculator.\n")
bill = float(input("What was the subtotal bill? \n$"))
tip = int(input("What percentage tip would you like to give? 15%, 18%, or 20%? \n"))
people = int(input("How many people to split the bill? \n"))
tax_dollar_amount = float(input("What was the bill's tax in $?\n"))
tip_percent = tip/100
bill_w_tip = (bill * tip_percent)
total_bill = bill + bill_w_tip
total_bill_tax = total_bill + tax_dollar_amount
bill_per_person =  (total_bill_tax / people)
final_bill_person = "{:.2f}".format(bill_per_person)
tip_for_total = "{:.2f}".format(bill_w_tip)
total_bill = "{:.2f}".format(total_bill_tax)
print(f"\nTotal tip amount of {tip}%: ${tip_for_total}")
print(f"*If splitting* (each person pays): ${final_bill_person}")
print(f"\nTotal bill: ${total_bill}")