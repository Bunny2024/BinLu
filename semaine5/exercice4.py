def student_late(arrivals, name):
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

def student_late(arrivals, name):
    # comment trouver la moitie de ma list
    half = len(arrivals) // 2

    # recherche dans la deuxieme partie de ma liste
    flag = name in arrivals[half:-1]
    return flag

student_attendees = [ 'Adela' , 'Fleda' , 'Owen' , 'May' , 'Mona','Gilbert' , 'Ford']
name = 'Gilbert'
late = student_late(student_attendees ,name)
print(late)