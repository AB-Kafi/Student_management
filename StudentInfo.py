import json as js
from os import path


def takecourse():
    Course_List = []
    n = int(input("Enter Number of Courses:"))
    while n != 0:
        Course_name = input("Enter Course Name:")
        Course_Code = input("Enter Course Code:")
        Course_Section = input("Enter Course_Section:")
        Course_List.append({Course_name: Course_Code,'Course_section':Course_Section})
        n -= 1
    return Course_List


def takeinfo():
    name = input("Enter name: ")
    id = input("Enter id: ")
    section = input("Enter section: ")
    course = takecourse()
    status = input("Enter status: ")
    return name, id, section, course, status


def todict(args):
    (name, id, section, course, status) = args

    info_dict = {"name": name,
                 "id": id,
                 "section": section,
                 "course": course,
                 "status": status
                 }
    return info_dict


def createfile():
    if not path.isfile('studentinfo.txt'):
        with open('studentinfo.txt', 'w+') as outfile:
            info_dict = {'student': []}
            js.dump(info_dict, outfile, indent=4)


def savetojson(args):
    info_dict = {'student': [args]}
    with open('studentinfo.txt', 'w+') as outfile:
        js.dump(info_dict, outfile, indent=4)


def fromjson():
    with open('studentinfo.txt') as outfile:
        jsobect = js.load(outfile)
    return jsobect


def dumpjsonobject(object):
    with open('studentinfo.txt', 'w+') as outfile:
        js.dump(object, outfile, indent=4)


def update():
    object = fromjson()
    x = takeinfo()
    p = todict(x)
    object["student"].append(p)
    print("Student Added")

    return object


def updatestatus():
    string = ['pending', 'partially complete', 'complete']
    choice = int(input("Enter 0 for pending 1 for partially complete 2 for complete: "))
    return string[choice]


def search(id):
    object = fromjson()
    flag=False
    index = -1
    for student in object['student']:
        for x, val in student.items():
            if val == id:
                flag=True
                print(student)
                choice = int(input('''\nEnter :
                 0 for update status 
                 1 to delete record
                 2 to Return
                            :'''))
                if choice == 0:
                    student["status"] = updatestatus()
                    dumpjsonobject(object)
                    print("Updated")
                elif choice == 1:
                    print(object)
                    del object['student'][index]
                    dumpjsonobject(object)
                    print("Record Deleted")
                elif choice == 2:
                    return
        index += 1
    if not flag:
        print("Student not found")
    return


def currentstatus():
    object = fromjson()
    studentnumber = 0
    status = "status"
    pending = 0
    complete = 0
    partiallycomplete = 0
    notfound = 0
    if len(object["student"]) != 0:
        for student in object["student"]:
            studentnumber += 1
            for key, val in student.items():
                if key == status:
                    if val == 'pending':
                        pending += 1
                    elif val == 'complete':
                        complete += 1
                    elif val == 'partially complete':
                        partiallycomplete += 1
                    else:
                        notfound += 1
    print(f'''Current Status:
             Total Student : {studentnumber}

             Registration:
                 Complete: {complete}
                 Partially Complete: {partiallycomplete} 
                 Pending :{pending}
                 Not Found:{notfound}
    ''')


def program():
    choice = 0

    while (choice != 3):

        currentstatus()
        choice = int(input('''        Enter:
                            1 for Data entry
                            2 for search
                            3 for exit
        Your Choice :'''))

        if choice == 1:
            q = update()
            dumpjsonobject(q)
        elif choice == 2:
            id = input("Enter ID for search:")
            search(id)


createfile()
program()
