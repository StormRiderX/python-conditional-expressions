age = 23

if age >= 18 :
    print("Eligible")
else :
    print("not eligible")



if age >= 18 :
    message = "Eligible"
else :
    message = "Not Eligible"

print (message)

## hvordan forkortes ovenstående

message = ("Eligible") if age >= 18 else ("not eligible")
print(message)