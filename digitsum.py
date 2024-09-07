n=int(input("enter a number of six digits: "))
sum=0
sumOeven=0
sumOodd=0
if len(str(n))<7:
    if n>0:
        while n>0:
            dig=n%10
            sum+=dig
            if dig%2==0:
                sumOeven+=dig
            else:
                sumOodd+=dig
            n=n//10
        print(f"sum of digits: {sum}")
        print(f"sum of even digits: {sumOeven}")
        print(f"sum of odd digits: {sumOodd}")
    else:
        num=abs(n)
        while num>0:
            dig=num%10
            sum+=dig
            if dig%2==0:
                sumOeven+=dig
            else:
                sumOodd+=dig
            num=num//10
        print(f"sum of digits are: {-abs(sum)}")
        print(f"sum of even digits: {-abs(sumOeven)}")
        print(f"sum of odd digits: {-abs(sumOodd)}")
else:
    print("number exceed then 6")