from todoist_api_python.api import TodoistAPI
from datetime import date


def get_todo_list():

    api = TodoistAPI("f3b6bd8d87c2bc09bc00b50f4fe6ae5f4b478a65")
    task_list = []
    today = date.today()

    try:
        projects = api.get_tasks()
        for line in projects:
            if line.due:
                if line.due.date == str(today):
                    task_list.append(line.content)
    except Exception as error:
        return error

    return task_list
