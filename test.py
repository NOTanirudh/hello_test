sub1=int(input("enter marks in sub1 : "))
sub2=int(input("enter marks in sub2 : "))
sub3=int(input("enter marks in sub3 : "))
sub4=int(input("enter marks in sub4 : "))
sub5=int(input("enter marks in sub5 : "))
total_marks=sub1+sub2+sub3+sub4+sub5
percentage=(total_marks/500)*100
print(total_marks)
print(percentage)
print('Passing marks required are 40')
if sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40 and sub5>=40:
    print('you passed')
else:
    print('you failed')