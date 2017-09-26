class ToDo(object):

    def __init__(self):
        self.todo_list = []

    def add_item(self, item, priority):
        """Add to-do item to the list"""
        self.todo_list.append((item.rstrip(), priority))

    def sort_items(self):
        """Sort list of to-do items based on their priority"""
        self.todo_list.sort(key=lambda tup: tup[1])

    def get_multiple_priority_items(self):
        """Return a list of priorities that more than one to-do item associated
        with it"""
        priorities = {}
        for item in self.todo_list:
            if item[1] in priorities.keys():
                priorities[item[1]].append(item)
            else:
                priorities[item[1]] = [item]

        multiple_priorities = []
        for key in priorities:
            if len(priorities[key]) > 1:
                multiple_priorities.append((key, len(priorities[key])))
        return multiple_priorities

    def get_missing_priorities(self):
        priorities = {}
        for item in self.todo_list:
            if item[1] in priorities.keys():
                priorities[item[1]].append(item)
            else:
                priorities[item[1]] = [item]
        missing_priorities = []

        current_priority = 1
        for key in priorities:
            key = int(key)
            if key == current_priority:
                continue
            elif current_priority + 1 != key:
                while key != current_priority:
                    missing_priorities.append(current_priority+1)
                    current_priority = current_priority + 1
        return missing_priorities

    def delete_item(self, position):
        """Remove given to-do item from the list"""
        if not self.todo_list:
            raise Exception('Your to-do list is empty.')
        self.todo_list.pop(position-1)

    def display_list(self):
        """
        Print the current list items.
        TO-DO: return current list to the caller, and the caller will handle
        how it wants to display the list
        """
        if not self.todo_list:
            raise Exception('Your to-do list is empty.')
        else:
            print '----------------'
            print 'Your to-do list:'
            for pos, item in enumerate(self.todo_list):
                print '{}: {}'.format(pos+1, item)
            print '----------------'


def menu_commands():
    """
    Prints out a list of all the commands accepted by the app.
    """
    print 'Please use any of these commands: \
            \nl: list all to-do items \
            \na: add a new to-do item \
            \nd: delete a to-do \
            \nq: quit to-do app \
            \np: return multiple priorities \
            \nhelp: view list of commands \n'


def menu(current_todo):
    """
    Menu loop. Given commands, respond with corresponding action until the
    user quits the app.
    Parameters
    ----------
    current_todo: ToDo
    """
    while True:
        try:
            response = raw_input('Please enter a command: ')
            if response == 'q':
                print 'Goodbye!'
                break
            elif response == 'help':
                menu()
            elif response == 'a':
                add_response = raw_input('What would you like to add to your list? \n')
                priority = raw_input('What priority would you like to give this item?')
                current_todo.add_item(add_response, priority)
                current_todo.sort_items()
                current_todo.display_list()
            elif response == 'l':
                current_todo.display_list()
            elif response == 'd':
                del_response = raw_input('Please enter the position number of the item to delete:')
                current_todo.delete_item(int(del_response))
                current_todo.display_list()
            elif response == 'p':
                p_list = current_todo.get_multiple_priority_items()
                print p_list
            elif response == 'm':
                print current_todo.get_missing_priorities()
            else:
                print 'Undefined command'
        except Exception as ex:
            print ex.message


if __name__ == '__main__':
    print 'Welcome to the world\'s best to-do app!! \n'
    current_todo = ToDo()
    menu_commands()
    menu(current_todo)
