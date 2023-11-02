#!/usr/bin/python3

import requests
import json

def get_employee_todo_progress(employee_id):
    """
    Retrieves and exports the TODO list progress of a given employee using a REST 
    Parameters:
    - employee_id: int
        The ID of the employee for whom the TODO list progress is to be retrieved.
    Raises:
    - ValueError:
        Raises an error if the employee ID is not a positive integer.
    Returns:
    - None
        Exports the employee TODO list progress in JSON format.
    """
    # Validating the employee ID
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID should be a positive integer.")
    
    # Sending a GET request to the API endpoint
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId=
{employee_id}")
    
    # Checking if the request was successful
    if response.status_code == 200:
        todos = response.json()
        
        # Creating a dictionary to store the tasks
        tasks = {"USER_ID": []}
        
        # Adding each task to the dictionary
        for todo in todos:
            task = {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": todo['username']
            }
            tasks["USER_ID"].append(task)
        
        # Exporting the tasks to a JSON file
        filename = f"{employee_id}.json"
        with open(filename, 'w') as file:
            json.dump(tasks, file, indent=4)
        
        print(f"TODO list for employee ID {employee_id} has been exported to {file
")
    else:
        print(f"Error: Failed to retrieve TODO list for employee ID {employee_id}.

# Example usage:
employee_id = 1
get_employee_todo_progress(employee_id)
