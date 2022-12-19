<<<<<<< HEAD
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
=======
afe_print_list(my_list=[], x=0):
>>>>>>> 1f4b4c3ca5d8ea8ce31bf594d6aca9c57f71235f
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            pass

    print()
    return (count)
