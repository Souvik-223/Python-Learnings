#Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 
sub1= int(input("Enter the marks of 1st subject: "))
sub2= int(input("Enter the marks of 2nd subject: "))
sub3= int(input("Enter the marks of 3rd subject: "))
if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail")
elif((sub1+sub2+sub3)/3 <40):
    print("You are fail because of the total percentage being less than 40%")
else:
    print("You passed")