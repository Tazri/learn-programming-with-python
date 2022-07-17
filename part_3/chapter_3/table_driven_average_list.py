def average_list(l) :
    if not l : 
        return None;

    return sum(l) / len(l);


def test_average_list() :
    test_cases = [
        {
            "name" : "simple case 1",
            "input" : [45,6,4,3,2,6],
            "expected" : 11
        },
        {
            "name" : "simple case 2",
            "input" : [3,2],
            "expected" : 2.5
        },
        {
            "name" : "simple case 3",
            "input" : [3,4],
            "expected" : 3.5
        },
        {
            "name" : "simple case 4",
            "input" : [2,2,2,2],
            "expected" : 2
        },
        {
            "name" : "simple case 5",
            "input" : [4,6,8,10],
            "expected" : 7
        },
        {
            "name" : "simple case 6",
            "input" : [],
            "expected" : None
        }
    ]

    for case in test_cases :
        assert case['expected'] == average_list(case['input']), case['name']