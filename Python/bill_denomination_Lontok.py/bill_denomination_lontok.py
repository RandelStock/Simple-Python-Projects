amount = eval(input("Enter An Amount : "))

thousand = amount // 1000
thousand1 = amount % 1000

fivehundred = thousand1 // 500
fivehundred1 = thousand1 % 500

twohundred = fivehundred1 // 200
twohundred1 = fivehundred1 % 200

onehundred = twohundred1 // 100
onehundred1 = twohundred1 % 100

fifty = onehundred1 // 50
fifty1 = onehundred1 % 50

twenty = fifty1 // 20 
twenty1 = fifty1 % 20

ten = twenty1 // 10
ten1 = twenty1 % 10

five = ten1 // 5
five1 = ten1 % 5

piso = five1 // 1
piso1 = five1 % 1

print(thousand,"-1000")
print(fivehundred,"-500")
print(twohundred,"-200")
print(onehundred,"-100")
print(fifty,"-50")
print(twenty,"-20")
print(ten,"-10")
print(five,"-5")
print(piso,"-1")