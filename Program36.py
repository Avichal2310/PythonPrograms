"""
WAP to input a date in dd/mm/yyyy format and show in dd-mmm-yyyy.
"""
print("Enter a date in dd/mm/yyyy format : ")
d,m,y=map(int,input().split("/"))
if m==1:
    m="Jan"
elif m==2:
    m="Feb"
elif m==3:
    m="Mar"
elif m==4:
    m="Apr"
elif m==5:
    m="May"
elif m==6:
    m="Jun"
elif m==7:
    m="Jul"
elif m==8:
    m="Aug"
elif m==9:
     m="Sep"
elif m==10:
     m="Oct"
elif m==11:
    m="Nov"
elif m==12:
    m="Dec"

print(f"{d}-{m}-{y}")
