# This is the start of day 8

def greeting():
    print("Hello", input("please print your name: "))
    print("Tomorrow, will be your first day")
    print("stay positive")


greeting()

#%%
def greet_w_name(name):
    print(f"Hello, {name}")
    print(f"How was your day {name}?")
    
    
greet_w_name("Mosa Rahimi")

#%%
def greet_with(name, location):
    print(f"how are you {name}?")
    print(f"how was traffic in {location}?")

greet_with("Mosa Rahimi", "Philadelphia")
greet_with(location="Philadelphia", name="Mosa Rahimi")

4
#%% It is ok. Don't be tempted. Even if is repetition several times.

def print_calc(width, height, cover):
    area = width * height
    cans = area // cover
    rem_can = area % cover
    if rem_can > cover/2:
        cans +=1
    else:
        cans = cans
    print(f"you need to {cans}  cans for this {area}")

test_h = int(input("what is the hieght of the wall? \n"))
test_w = int(input("what is the width of the wall? \n"))

coverage = 10
print_calc(width=test_w, height=test_h, cover=coverage)

#%%
#%% It is ok. Don't be tempted. Even if is repetition several times.

def print_calc_1(width, height, cover):
    area = width * height
    cans = area // cover
    # rem_can = area % cover
    if cans % cover != 0:
        cans +=1
    else:
        cans = cans
    print(f"you need to {cans}  cans for this {area}")

test_h = int(input("what is the hieght of the wall? \n"))
test_w = int(input("what is the width of the wall? \n"))

coverage = int(input("how many square meters a can can paint? \n "))
print_calc_1(width=test_w, height=test_h, cover=coverage)

#%% Prime number
# took me a long time to figure it but I did figure it.
def prime_number(your_number):
    if your_number //2 == 1:
        print("your number is prime")
    elif your_number % 2 == 0 and your_number > 2:
        print("your number is not prime")
    elif your_number % 3 == 0 and your_number % 2 != 0:
        print("your number is not prime")
    else:
        print("your number is prime")
    
    

prime_number(7919)

#%%
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"the number {number} is a prime number")
    else:
        print(f"your number {number} is NOT a Prime number")
        
        
prime_checker(17)

#%%

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text = "Hello"
shift = 0
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(plain_text, shift_amuont):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    for i in text:
        cipher_text = ""
        # print(alphabet.index(i))
        position = alphabet.index(i)
        # print(type(position))
        new_position = position + 5
        new_letter= alphabet[new_position]
        cipher_text += new_letter
        print(cipher_text)
        
        
def decrypt(ciphertext, shift_amount):
    plain_text = ""
    for letter in ciphertext:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet.index(new_position)
        
        
if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decrypt":
    decrypt(ciphertext=text, shift_amount=shift)

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.

encrypt(text = "hello", shift=0)


#%%
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# text = "helloMosa".lower()
#
# for i in text:
#     # print(alphabet.index(i))
#     position = alphabet.index(i)
#     # print(type(position))
#     new_position = position + 5
#     new_text = alphabet[new_position]
#     print(new_text)


#%% I will repeat cesar cipher

