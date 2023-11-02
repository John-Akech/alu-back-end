/bin/python3

import requests
import json

def get_employee_todo_progress():
    """
    Retrieves and exports the TODO list progress of all employees using a REST API.
    Returns:
    - None
        Exports the employee TODO list progress of all employees in JSON format.
    """
    # Sending a GET request to the API endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    
    # Checking if the request was successful
    if response.status_code == 200:
        todos = response.json()
        
        # Creating a dictionary to store the tasks
        tasks = {}
        
        # Adding each task to the dictionary
        for todo in todos:
            employee_id = str(todo['userId'])
            if employee_id not in tasks:
                tasks[employee_id] = []
            
            task = {
                "username": todo['username'],
                "task": todo['title'],
                "completed": todo['completed']
            }
            tasks[employee_id].append(task)
        
        # Exporting the tasks to a JSON file
        filename = "todo_all_employees.json"
        with open(filename, 'w') as file:
            json.dump(tasks, file, indent=4)
        
        print(f"TODO list for all employees has been exported to {filename}.")
    else:
        print("Error: Failed to retrieve TODO list for all employees.")

# Example usage:
get_employee_todo_progress()
