import json
import pyfiglet
student ={
    'name': 'Alex',
    'full name': 'Alex Casperantos',
    'age': 32,
    'Born Date': '12:03:1990',
    'languages': ['python', 'javascript', 'go']
}

try:
    with open('my_json.json', 'w') as conv_file:
        conv_file.write(json.dumps(student, indent=4))
except Exception:
    print(f'Problem with {Exception}')
else:
    ascii_banner = pyfiglet.figlet_format('Successfully')
    print(ascii_banner)
