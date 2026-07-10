bill = 1000
people = 4
def split_bill(total, people, tip_rate=0.10):
    total_with_tip = total + (total * tip_rate)
    return total_with_tip / people
share = split_bill(bill, people)
friends = ["Abel", "Sara", "Miki", "John"]
for person in friends:
    print(person, "pays", share, "ETB")