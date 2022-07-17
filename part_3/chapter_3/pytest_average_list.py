def average_list(l) :
    if not l : 
        return None;

    return sum(l) / len(l);


def test_average_list() : 
    assert 3.0 == average_list([1,2,3,4,5])