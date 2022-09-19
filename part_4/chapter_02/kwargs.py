def take_dict(**kwargs):
    print(kwargs);
    
take_dict(a=3,b=6,c=4);

def show_marks(n,**marks):
    print("\nExam Name is : ",n);
    for name in marks : 
        print(name,":",marks[name]);
        
show_marks("ssc",anonymous=99,sirius=0,kripton=33)

# below code work finly
show_marks(n="hsc",anonymous=9,sirius=1,kripton=33)

# below code work fine as well
show_marks(anonymous=99,sirius=0,kripton=33,n="PSC")