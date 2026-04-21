age = int(input("Enter your age:"))
doc = input("Did you submit your original documnet ? [yes/no]:")

if age>=6 and doc.lower() == 'yes':
    print ('congratulation!, you are admitted in class PP')
else:
    print("Sorry, you are not eligible for admission")
    
