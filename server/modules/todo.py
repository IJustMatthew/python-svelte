# Dummy database
todos = [
    {
        "id": "1",
        "title": "Todo 1",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus congue consequat. Integer consectetur placerat augue, nec accumsan enim egestas finibus. Nullam ornare orci quis ipsum maximus porta. Suspendisse pellentesque est sed metus molestie, eget sagittis ex consectetur.",
    },
    {
        "id": "2",
        "title": "Todo 2",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus congue consequat. Integer consectetur placerat augue, nec accumsan enim egestas finibus.",
    },
    {
        "id": "3",
        "title": "Todo 3",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas luctus congue consequat. Integer consectetur placerat augue, nec accumsan enim egestas finibus. Nullam ornare orci quis ipsum maximus porta. Suspendisse pellentesque est sed metus molestie, eget sagittis ex consectetur.",
    },
]


def get_todos():
    """Get all todos"""
    global todos
    return todos


def add_todo(data):
    """Add a todo"""
    global todos
    todos.append(data)

    return get_todos()


def delete_todo(id):
    """Delete a todo"""
    global todos
    new_list = list(filter(lambda todo: todo["id"] != id, todos))
    todos = new_list

    return new_list


def update_todo(data):
    """Update a todo"""
    global todos
    print(data)
    for i, todo in enumerate(todos):
        if todo["id"] == data["id"]:
            todos[i] = data

    return todos
