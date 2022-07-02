year = input("Enter the year : ");
year = int(year);

if year % 100 and not year % 4 :
    print("Yes");
elif not year % 100 and not year % 400 :
    print("Yes");
else : 
    print("No");