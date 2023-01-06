# Scratch-Cloud-List
(infinite) Cloud list for scratch.mit.edu


The code would look something like this:

`import scratchattach as scratch3
import time

session = scratch3.login("ReloadingAlt", "123456")
conn = session.connect_cloud("783692943")

LIST = []
conn.set_var("REMOVE", 0)
conn.set_var("ADD", 0)
conn.set_var("Refresh", 0)
conn.set_var("Cloud", 0)
conn.set_var("Repeat", 0)
conn.set_var("PlsRefresh", 0)

while True:
    def refresh():  # forces a refresh for all people
        print("refresh")
        conn.set_var("Refresh", 1)
        repeat = len(LIST)
        conn.set_var("Repeat", repeat)
        for i in LIST:
            conn.set_var("Cloud", i)
            print(i)
            repeat -= 1
            conn.set_var("Repeat", repeat)
            conn.set_var("Cloud", 0)
        time.sleep(1)
        conn.set_var("Refresh", 0)
        conn.set_var("Repeat", 0)
        conn.set_var("Cloud", 0)
        conn.set_var("PlsRefresh", 0)
        print(LIST)

    def update():  # updates cloud
        print("checking")
        if scratch3.get_var("783692943", "ADD") != "0":  # adds an item to a list
            print("add")
            global LIST
            LIST.append(int(scratch3.get_var("783692943", "ADD")))
            print(LIST)
            conn.set_var("ADD", 0)
            refresh()
        elif scratch3.get_var("783692943", "REMOVE") != "0":  # removes an item from a list
            print("remove")
            LIST.pop(int(scratch3.get_var("783692943", "REMOVE")) - 2)
            print(LIST)
            conn.set_var("REMOVE", "0")
            refresh()
        elif scratch3.get_var("783692943", "PlsRefresh") == "1":  # refreshes the cloud list
            refresh()
        else:
            print("nothing")

    update()`
