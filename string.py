
def string_comparison(string_1, string_2):
    if  not type(string_1)==str or not type(string_2)==str:
        print (0)
    elif string_1==string_2:
        print (1)
    elif not string_1==string_2 and len(string_1)>len(string_2):
        print (2)
    elif not string_1==string_2 and string_2=="learn":
        print (3)

if __name__ == "__main__":
    string_comparison(2, "да")
    string_comparison("привет", "машина")
    string_comparison("да", "да")
    string_comparison("обед", "learn")
    string_comparison("нет", 7478.9)