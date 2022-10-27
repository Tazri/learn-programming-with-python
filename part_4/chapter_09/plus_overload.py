class Point : 
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y) + ')'

    def __add__(self,point):
        self.x += point.x;
        self.y += point.y;
        return self;

if __name__ == "__main__":
    point_one = Point(2,4);
    print('point_one :',point_one);
    point_two = Point(1,1);
    print("point_two : ",point_two);

    print("after point_one + point_two : point_one");
    added_point = point_one + point_two;
    print(added_point);