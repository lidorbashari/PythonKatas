def generate_boarding_pass(passenger):
    name = passenger['name']
    split_name = name.split()
    first_name = split_name[0]
    last_name = split_name[1]
    flight_number = passenger['flight_number']
    departing = passenger['departing']
    arrival = passenger['arrival']
    boarding_time = passenger['boarding_time'].replace(':','')
    seat = passenger['seat'].upper()
    return f'{flight_number}//{last_name}//{departing}-{arrival}//{boarding_time}//{seat}'
    """
    Generates a boarding pass code for the given passenger.
    """


passenger_info = {
    'name': 'Jane Smith',
    'flight_number': 'CD456',
    'seat': '5b',
    'boarding_time': '15:45',
    'departing': 'LCA',
    'arrival': 'LAX'
}

result = generate_boarding_pass(passenger_info)
print(result)  # Expected output: CD456//Smith//LCA-LAX//1545//5B

"""
To complete this exercise:
--------------------------
Implement the 'generate_boarding_pass' function to create a formatted boarding pass code for a passenger, as follows:

[flight_number]//[last name only]//[departing]-[arrival]//[boarding_time digits only]//[seat upper case]


Exercise Breakdown:
-------------------
The`f` string formatting is used to embed expressions inside string literals, using curly braces `{}`. 
`f` strings are much more readable than using the '+' operator to concat strings: 

name = 'John'
greeting = f"Hello, {name}"

print(greeting) # Output: Hello, John
"""