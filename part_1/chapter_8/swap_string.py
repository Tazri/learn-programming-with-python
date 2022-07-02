text = input("Enter the text : ");
length = len(text) ;
swap_text = '';

if length & 1 : length -= 1;

for i in range(0,length,2) :
    swap_text += text[i+1];
    swap_text += text[i];

print(swap_text);