#For the autograder to pass you will need MAX_LENGTH to be 3.
MAX_LENGTH : int = 3
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)
def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop.")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop.")
    return lst
def main():
    lst =  get_lst()
    shorten(lst)
main()



