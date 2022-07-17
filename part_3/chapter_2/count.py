def demo(n) : 
    n = int(n); # O(1)

    count = 0; # O(1)

    for i in range(n) : # iterate n'th time
        for j in range(n) : # iterate n²'th time
            count += 1; # O(n * n) = O(n²)

    return count; # O(1)

'''
Calculate demo time complexity : 
O(demo(n)) = O(1) + O(1) + O(n²) + O(1)
           = 3*O(1) + O(n²)
           = O(n²)

Calculate demo space complexity : 
O(1) -> for n variable
O(1) -> for count variable
total space complexity : O(1) + O(1) 
                       = O(1)

Time Complexity : O(n²)
Space Complexity : O(1)

'''


if __name__ == "__main__" : 
    print("demo(5) : ",demo(5));
    print("demo(3) : ",demo(3));
    print("demo(6) : ",demo(6));
    print("demo(7) : ",demo(7));
    print("demo(2) : ",demo(2));