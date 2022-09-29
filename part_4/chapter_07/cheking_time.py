import time
from bisect import bisect

# create decorator for calculating funciton run time
def deco(func):
    def wrapper(num:int):
        start = time.time();
        result = func(num);
        end = time.time();
        need_time = end-start;
        return [result,need_time];

    return wrapper;

def calculate_grade(marks:int)->str:
    if marks >= 80 : return "A+";
    elif marks >= 70 :return "A";
    elif marks >= 60 : return "A-";
    elif marks >= 50 : return "B";
    elif marks >= 40 : return "C";
    else : return "F";


def calculate_grade_bisect(marks:int)->str:
    grades = ['F','C','B','A-','A','A+'];
    grade_list = [40,50,60,70,80];
    i = bisect(grade_list,marks);
    return grades[i];

if __name__ == '__main__':
    grade_times = [];
    bisect_times = [];
    grade_func = deco(calculate_grade);
    bisect_func = deco(calculate_grade_bisect);

    for i in range(101):
        gresult = grade_func(i);
        bresult = bisect_func(i);

        assert gresult[0] == bresult[0], "Test Input : "+i;
        grade_times.append(gresult[1]);
        bisect_times.append(bresult[1]); 

    
    average_time_for_grade = sum(grade_times)/len(grade_times);
    average_time_for_bisect = sum(bisect_times)/len(bisect_times);

    print(">>> calulate_grade time <<<");
    print("> average : ",average_time_for_grade);
    print("> minimum : ",min(grade_times));
    print("> maximum : ",max(grade_times));

    print("\n>>> calculate_grade_bisect time <<<");
    print("> average : ",average_time_for_bisect);
    print("> minimum : ",min(bisect_times));
    print("> maximum : ",max(bisect_times));