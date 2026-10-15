# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
    temp = employee_list['name'] + "_" + employee_list["department"]
    return temp

def to_mod_list(employee_list):
    #nl=list(map(mod, employee_list))
    return list(map(mod, employee_list)) #nl

"""
map(mod, employee_list): The map() function takes two main arguments: a target function (mod) 
and an iterable (employee_list). It applies mod() to every item in employee_list individually 
under the hood—effectively running mod(employee_list[0]), mod(employee_list[1]), and so on.

list(...): map() in Python 3 returns a map object (an iterator) rather than an actual list. 
Wrapping it in list(...) converts that iterator into a standard list of strings that you can 
print, index, or iterate over.
"""

def generate_usernames(mod_list):
    
    return [emp.replace(" ", "_") for emp in mod_list]

"""
for emp in mod_list: This is a standard loop that takes each string from mod_list one by one 
and assigns it to the temporary variable emp.

emp.replace(" ", "_"): For each string stored in emp, .replace(" ", "_") scans the text and 
swaps every space character (" ") with an underscore ("_").

[...]: The surrounding square brackets collect every transformed string into a brand new 
Python list and return it.
"""

def map_id_to_initial(employee_list):
    return {emp["name"][0]: emp["id"] for emp in employee_list}

"""
The general structure of a dictionary comprehension is {key: value for item in iterable}:
for emp in employee_list: Loops through each dictionary (representing an employee) inside the employee_list.

emp["name"][0] (The Key):

emp["name"] gets the employee's name string (e.g., "John").

[0] takes the first character of that string (e.g., 'J').

emp["id"] (The Value): Retrieves the numeric ID associated with that employee (e.g., 12345).

{...}: Wraps the key-value pairs into a new dictionary.
"""


def main():
    mod_emp_list=to_mod_list(employee_list)
    print("Modified employee list: "+str(mod_emp_list)+"\n")
    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    """
    1.
    Python executes the generate_usernames function first, passing in mod_emp_list 
    as its argument.
    Input passed in: ['John_Kitchen', 'Paul_House Floor', ...]
    Function return value: ['John_Kitchen', 'Paul_House_Floor', ...]
    2.
    The f prefix tells Python to evaluate any code placed inside curly braces {} 
    and substitute the returned value into the string as text.
    {generate_usernames(mod_emp_list)} is replaced by the string representation of 
    the returned list.
    3.
    The \n at the end adds a newline character, creating an extra blank line below 
    the output in the console for cleaner formatting.
    """
    print(f"Initials and ids:  {map_id_to_initial(employee_list)}")


if __name__=="__main__":
    main()