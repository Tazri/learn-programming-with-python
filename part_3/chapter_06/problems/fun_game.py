'''
problem in details link : 
https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/fun-game-91510e9f/
'''

class Player:
    # constructor 
    def __init__(self,_hand,_n):
        self.hand,self.n = _hand,_n;

        if _hand == 'left':
            self.index = 0;
        else :
            self.index = _n - 1;

    # check player is lose or not
    def is_lose(self) :
        if self.hand == 'left' : # logic to left player lose
            if self.index < self.n :
                return False; # not lose
            else :
                return True;
        else: # logic to right player lose
            if self.index >= 0 :
                return False; # not lose
            else : 
                return True;  

    # remove index 
    def remove(self):
        if self.hand == 'left':
            self.index += 1;
        else:
            self.index -= 1;

def funGame (_arr,_n):
    arr = list(_arr); 
    player_a = Player('left',_n);
    player_b = Player('right',_n);
    output = [];

    # start games 
    while (not player_a.is_lose()) and (not player_b.is_lose()) :
        a = arr[player_a.index];
        b = arr[player_b.index];

        if a > b : 
            output.append(1);
            player_b.remove();
        elif a < b :
            output.append(2);
            player_a.remove();
        else:
            output.append(0);
            player_a.remove();
            player_b.remove();


    return output;

n = int(input())
arr = map(int, input().split())

out_ = funGame(arr,n)
print (' '.join(map(str, out_)))