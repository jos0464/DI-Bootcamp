# ------------------------
# Functions Implementation
# ------------------------

# 1. difference
def difference(a, b):
    return a - b

# 2. print_day
def print_day(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 1 <= num <= 7:
        return days[num - 1]
    return None

# 3. last_element
def last_element(lst):
    return lst[-1] if lst else None

# 4. number_compare
def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Numbers are equal"

# 5. single_letter_count
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())

# 6. multiple_letter_count
def multiple_letter_count(word):
    return {char: word.count(char) for char in word}

# 7. list_manipulation
def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)
    elif command == "add":
        if location == "beginning":
            lst.insert(0, value)
        elif location == "end":
            lst.append(value)
        return lst

# 8. is_palindrome
def is_palindrome(s):
    clean_s = ''.join(s.lower().split())
    return clean_s == clean_s[::-1]

# 9. frequency
def frequency(lst, search_term):
    return lst.count(search_term)

# 10. flip_case
def flip_case(s, letter):
    return ''.join(c.swapcase() if c.lower() == letter.lower() else c for c in s)

# 11. multiply_even_numbers
def multiply_even_numbers(lst):
    product = 1
    for n in lst:
        if n % 2 == 0:
            product *= n
    return product

# 12. mode
def mode(lst):
    return max(set(lst), key=lst.count)

# 13. capitalize
def capitalize(s):
    return s.capitalize()

# 14. compact
def compact(lst):
    return [x for x in lst if x]

# 15. partition
def partition(lst, callback):
    true_list = [x for x in lst if callback(x)]
    false_list = [x for x in lst if not callback(x)]
    return [true_list, false_list]

# 16. intersection
def intersection(lst1, lst2):
    return [x for x in lst1 if x in lst2]

# 17. once
def once(func):
    has_run = {"value": False}
    def wrapper(*args, **kwargs):
        if not has_run["value"]:
            has_run["value"] = True
            return func(*args, **kwargs)
        return None
    return wrapper

# Super Bonus: once as decorator
def run_once(func):
    has_run = {"value": False}
    def wrapper(*args, **kwargs):
        if not has_run["value"]:
            has_run["value"] = True
            return func(*args, **kwargs)
        return None
    return wrapper

# ------------------------
# Tests & Examples
# ------------------------

print("difference(2,2) ->", difference(2,2))  # 0
print("difference(0,2) ->", difference(0,2))  # -2

print("print_day(4) ->", print_day(4))  # Wednesday
print("print_day(41) ->", print_day(41))  # None

print("last_element([1,2,3,4]) ->", last_element([1,2,3,4]))  # 4
print("last_element([]) ->", last_element([]))  # None

print("number_compare(1,1) ->", number_compare(1,1))  # Numbers are equal
print("number_compare(1,2) ->", number_compare(1,2))  # Second is greater
print("number_compare(2,1) ->", number_compare(2,1))  # First is greater

print("single_letter_count('amazing','A') ->", single_letter_count('amazing','A'))  # 2
print("multiple_letter_count('hello') ->", multiple_letter_count('hello'))  # {'h':1,'e':1,'l':2,'o':1}
print("multiple_letter_count('person') ->", multiple_letter_count('person'))  # {'p':1,'e':1,'r':1,'s':1,'o':1,'n':1}

print("list_manipulation([1,2,3], 'remove', 'end') ->", list_manipulation([1,2,3], "remove", "end"))  # 3
print("list_manipulation([1,2,3], 'remove', 'beginning') ->", list_manipulation([1,2,3], "remove", "beginning"))  # 1
print("list_manipulation([1,2,3], 'add', 'beginning', 20) ->", list_manipulation([1,2,3], "add", "beginning", 20))  # [20,1,2,3]
print("list_manipulation([1,2,3], 'add', 'end', 30) ->", list_manipulation([1,2,3], "add", "end", 30))  # [1,2,3,30]

print("is_palindrome('testing') ->", is_palindrome('testing'))  # False
print("is_palindrome('tacocat') ->", is_palindrome('tacocat'))  # True
print("is_palindrome('hannah') ->", is_palindrome('hannah'))  # True
print("is_palindrome('a man a plan a canal Panama') ->", is_palindrome('a man a plan a canal Panama'))  # True

print("frequency([1,2,3,4,4,4], 4) ->", frequency([1,2,3,4,4,4], 4))  # 3
print("frequency([True, False, True, True], False) ->", frequency([True, False, True, True], False))  # 1

print("flip_case('Hardy har har', 'h') ->", flip_case("Hardy har har", "h"))  # "hardy Har Har"

print("multiply_even_numbers([2,3,4,5,6]) ->", multiply_even_numbers([2,3,4,5,6]))  # 48

print("mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) ->", mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]))  # 4

print("capitalize('tim') ->", capitalize("tim"))  # "Tim"
print("capitalize('matt') ->", capitalize("matt"))  # "Matt"

print("compact([0,1,2,'',[], False, {}, None, 'All done']) ->", compact([0,1,2,'',[], False, {}, None, 'All done']))  # [1,2,"All done"]

def is_even(num):
    return num % 2 == 0
print("partition([1,2,3,4], is_even) ->", partition([1,2,3,4], is_even))  # [[2,4],[1,3]]

print("intersection([1,2,3], [2,3,4]) ->", intersection([1,2,3], [2,3,4]))  # [2,3]

# once example
def add(a,b):
    return a + b
one_addition = once(add)
print("one_addition(2,2) ->", one_addition(2,2))  # 4
print("one_addition(2,2) ->", one_addition(2,2))  # None
print("one_addition(12,200) ->", one_addition(12,200))  # None

# run_once decorator example
@run_once
def add2(a,b):
    return a + b
print("add2(2,2) ->", add2(2,2))  # 4
print("add2(2,20) ->", add2(2,20))  # None
print("add2(12,20) ->", add2(12,20))  # None
