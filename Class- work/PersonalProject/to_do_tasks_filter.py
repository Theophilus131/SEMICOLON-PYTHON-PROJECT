
tasks = ["buy milk", "finish homework","call mom","milk the cow"]
user_input = input("Enter a word: ")
for task in tasks:
    if user_input in task:
        print(task)

