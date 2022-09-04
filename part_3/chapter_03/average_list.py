def average_list(l) :
    if not l : 
        return None;

    return sum(l) / len(l);


if __name__ == "__main__" : 
    ## Test the average list function
    test_cases = [
        [[45,6,4,3,2,6],11],
        [[3,2],2.5],
        [[3,4],3.5],
        [[2,2,2,2],2],
        [[4,6,8,10],7],
        [[],None],
        [[],3], # wrong result
        # [test_case,expected_result]
    ]

    print(">>>🧪🧪🧪 Test Case Started 🧪🧪🧪<<<\n");

    for case in test_cases :
        result = average_list(case[0]);
        expected_result = case[1];

        if result == expected_result : 
            print(">>> ✅✅✅ Test Pass. Expected Result : ", expected_result," received result : ",result);
        else : 
            print(">>> ❌❌❌ Test Failed. Expected Result : ", expected_result," received result : ",result);
            break;