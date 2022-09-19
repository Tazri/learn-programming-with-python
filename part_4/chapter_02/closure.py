def addition(n_one):
    def add(n_two):
        return n_one + n_two;

    return add;
    
ten_plus = addition(10); # here ten_plus is closure

print("ten_plus(3) : ",ten_plus(3));
print("addition.__closure__ : ",addition.__closure__)
print("ten_plus.__closure__ : ",ten_plus.__closure__);