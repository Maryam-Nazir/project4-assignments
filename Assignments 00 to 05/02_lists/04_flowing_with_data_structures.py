# Add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list.
# Don't return anything and see what happens! 
# Compare this process to the x = change(x) example and note the differences.
def main(my_list,msg):
   for i in range(3):
      my_list.append(msg)
def woman():
   msg = input("Enter a msg")
   myList = []
   print(f"before my list {myList}")
   main(myList,msg)
   print(f"after my list {myList}")
woman()

