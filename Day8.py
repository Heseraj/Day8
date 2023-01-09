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
