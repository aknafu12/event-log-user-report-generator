def get_event_date(event):
    """
    Get the date of the event.
    
    Args:
        event (Event): The event object.
    
    Returns:
        str: The date of the event.
    """
    return event.date
# end def

def current_users(events):
    """
    Retrieve the current users on each machine based on login and logout events.

    Args:
        events (list): List of Event objects.

    Returns:
        dict: A dictionary where keys are machine names and values are sets of current users.
    """
    events.sort(key=get_event_date)
    machines = {}

    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()

        if event.type == 'login':
            machines[event.machine].add(event.user)
        elif event.type == 'logout':
            machines[event.machine].remove(event.user)
    return machines
# end def

def generate_report(machines):
    """
    Generate a report displaying the current users on each machine.

    Args:
        machines (dict): Dictionary containing current users on each machine.
    """
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ', '.join(users)
            print('{}: {}'.format(machine, user_list))
# end def

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        """
        Initialize an Event object.

        Args:
            event_date (str): The date of the event.
            event_type (str): The type of the event ('login' or 'logout').
            machine_name (str): The name of the machine.
            user (str): The username associated with the event.
        """
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user
