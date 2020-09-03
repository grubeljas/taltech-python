# This program counts minimum amount of coins for sum
summ = int(input("Enter a sum: "))
fifty = int(summ // 50)
summ = summ % 50
twenty = int(summ // 20)
summ = summ % 20
ten = int(summ // 10)
summ = summ % 10
five = int(summ // 5)
summ = summ % 5
ones = int(summ // 1)
amount_coins = str(fifty + twenty + ten + five + ones)
print("Amount of coins needed: " + amount_coins)
