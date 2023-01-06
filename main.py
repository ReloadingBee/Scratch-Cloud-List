import scratchattach as scratch3
import time

#####################################
# FILL IN YOUR INFO
username = 'MyUsername'
password = '123456'
projectID = '783692943'
#####################################


# log in to your Scratch account
session = scratch3.login(username, password)
conn = session.connect_cloud(projectID)

# setup your variables
LIST = []
conn.set_var("REMOVE", 0)
conn.set_var("ADD", 0)
conn.set_var("Refresh", 0)
conn.set_var("Cloud", 0)
conn.set_var("Repeat", 0)
conn.set_var("PlsRefresh", 0)

while True:
    def refresh():  # forces a refresh for all people
        conn.set_var("Refresh", 1)
        repeat = len(LIST)
        conn.set_var("Repeat", repeat)
        for i in LIST:
            conn.set_var("Cloud", i)
            repeat -= 1
            conn.set_var("Repeat", repeat)
            conn.set_var("Cloud", 0)
        time.sleep(1)
        conn.set_var("Refresh", 0)
        conn.set_var("Repeat", 0)
        conn.set_var("Cloud", 0)
        conn.set_var("PlsRefresh", 0)


    def update():  # updates cloud
        if scratch3.get_var(projectID, "ADD") != "0":  # adds an item to a list
            global LIST
            LIST.append(int(scratch3.get_var(projectID, "ADD")))
            conn.set_var("ADD", 0)
            refresh()
        elif scratch3.get_var(projectID, "REMOVE") != "0":  # removes an item from a list
            LIST.pop(int(scratch3.get_var(projectID, "REMOVE")) - 2)
            conn.set_var("REMOVE", "0")
            refresh()
        elif scratch3.get_var(projectID, "PlsRefresh") == "1":  # refreshes the cloud list
            refresh()


    update()
