# 📌 File Handling Tasks in Python
# 👶 Beginner Task:
# 📝 Task 1: Write & Read a File
file = "data.txt"
with open(file,"w") as file:
    file.writelines(["Hello This Is One Line\n","Welcome to the python Programming\n","This is Third Line"])
with open("data.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)