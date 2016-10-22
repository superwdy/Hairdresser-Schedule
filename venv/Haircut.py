# Use datetime library to compare time and realize summation operation for time.
from datetime import datetime as dt
from datetime import timedelta as delta


# Define one base class: Service.
class Service(object):
        def __init__(self, service, time, id):
            self.service = service
            self.time = time
            self.id = id
            info = []
            info.append(self.service)
            info.append(self.time)
            info.append(self.id)
            appointments.append(info)

# Define two subclasses: Haircut and Shampoo_Haircut.
class Haircut(Service):
    # The init function accepts an additional parameter which is named "id" to distinguish different appointments.
    def __init__(self, service, time, id):
        # Invoke the class constructor function in the parent class "Service()"
        super(Haircut, self).__init__(service, time, id)
        # time + 30min = end
        end = dt.strptime(time, "%H:%M") + delta(minutes=30)
        end = end.strftime("%H:%M")
        availability[time] = end


class Shampoo_Haircut(Service):
    # The init function accepts an additional parameter which is named "id" to distinguish different appointments.
    def __init__(self, service, time, id):
        # Invoke the class constructor function in the parent class "Service()"
        super(Shampoo_Haircut, self).__init__(service, time, id)
        # time + 1hour = end
        end = dt.strptime(time, "%H:%M") + delta(hours=1)
        end = end.strftime("%H:%M")
        availability[time] = end


# Define a list to store the info of appointments and a dictionary to check if a specific time is available.
appointments = []
availability = {}


# Define functions and classes as following:
def List():
    # item is a list that is contained in another list appointment
    print "Service", "Time", "ID"
    for item in appointments:
        print item

# Define a function named requestTime to be invoked once users input a unavailable time.
def requestTime():
    time = raw_input("What time is this appointment?\n(Please input time in the format like 08:10/10:30)")

    # Check if the time if in a correct format. If the format is not correct, invoke the requestTime() function again.
    if len(time) != 5:
        print "The format of time is not correct!\n(The format must be XX:XX!!!)"
        requestTime()

    # Check if the time is available. If the time is not available, invoke the requestTime() function again.
    for key, value in availability.items():
        if key < time < value:
            print "The time is not available!"

            # Invoke itself recursively to request another time if the time input is not available.
            requestTime()

    return time

# Define a function named requestService to be invoked once users input a incorrect service.
def requestService():
    service = raw_input("What services does the customer want?\n(Please say 'Haircut'or'Shampoo&Haircut'!)")
    if service == "Haircut" or service == "haircut":
        service = "Haircut"

        # Request time.
        time = requestTime()

        # If the time is available, record the info of the appointment.
        id = raw_input("What is the service id by which you could distinguish different appointments?")
        newService = Haircut(service, time, id)

    elif service == "Shampoo&Haircut" or service == "shampoo&haircut" or service == "Shampoo" or service == "shampoo":
        service = "Shampoo&Haircut"

        # Request time.
        time = requestTime()

        # If the time is available, record the info of the appointment.
        id = raw_input("What is the service id by which you could distinguish different appointments?")
        newService = Shampoo_Haircut(service, time, id)

    # If customers request a wrong service, print an alert and invoke the requestService() function again.
    else:
        print "Sorry! This service doesn't exist!"

        # Invoke itself recursively to request another service if the service input is incorrect.
        requestService()

    return service




while True:
    # Users are allowed to request actions they want.
    action = raw_input("What would you do?\n(Please say 'List', 'Schedule' or 'Exit'!)")

    # Invoke corresponding functions according user's request.
    if action == "List" or action == "list":
        List()
    elif action == "Exit" or action == "exit":
        print "You exited the program!"
        break
    elif action == "Schedule" or action == "schedule":
        service = requestService()

    # If users request a wrong function, print an alert and go back to the beginning of the whole program.
    else:
        print "Sorry! This function is invalid!"