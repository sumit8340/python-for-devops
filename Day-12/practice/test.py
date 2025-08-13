# task
# update server
#1-- Read the file
#2-- variable list
#3-- write mode
#4-- updating max connections

def update_server_config(file_path, key, value):
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)
update_server_config("server.conf", "PORT", "8080")                    


