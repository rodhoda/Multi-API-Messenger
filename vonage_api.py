import vonage
import todoist_api as todo

client = vonage.Client(key="3fe2d7b4", secret="V7Ahln20Fy7yh8iT")

todo_list = todo.get_todo_list()


def textualize_list(task_list):
    list_string = "Here is your daily list of tasks todo: \n"

    for index, task in enumerate(task_list):
        task = f"\n{index + 1} - {task}\n"
        list_string = list_string + task

    return list_string



responseData = client.sms.send_message(
    {
        "from": "+13524510157",
        "to": "+15103598629",
        "text": textualize_list(todo_list),
    }
)
if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
