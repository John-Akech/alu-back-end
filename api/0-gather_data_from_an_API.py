#!/usr/bin/python3

import requests
 
def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the TODO list progress of a given employee using a REST API.
 
    Parameters:
    - employee_id: int
        The ID of the employee for whom the TODO list progress is to be retrieved.
 
    Raises:
    - ValueError:
        Raises an error if the employee ID is not a positive integer.
 
    Returns:
    - None
        Displays the employee TODO list progress on the standard output.
    """
 
    # Validating the employee ID
    if not isinstance(employee_id, int) or employee_id <= 0:
        raise ValueError("Employee ID should be a positive integer.")
 
    # Sending a GET request to the API endpoint
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee
 
    # Checking if the request was successful
    if response.status_code == 200:
        todos = response.json()
 
        # Counting the number of completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
 
        # Counting the total number of tasks
        total_tasks = len(todos)
 
        # Getting the employee name
        employee_name = todos[0]['username']
 
        # Displaying the employee TODO list progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total
 
        # Displaying the titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Error: Failed to retrieve TODO list for employee ID {employee_id}.")
 
# Example usage:
employee_id = 1
get_employee_todo_progress(employee_id)
