import gradebook


sammy = gradebook.Instructor("Sammy", "Buttface", "34",  gradebook.Alive_status.alive)
banlor = gradebook.Instructor('Banlor', 'Supersmurf', "004", gradebook.Alive_status.alive)
ileen = gradebook.Student('Ileen', 'Kilmonger', '76', gradebook.Alive_status.alive)
torg = gradebook.ZipCodeStudent("Torg", "Kilsmash", "786", gradebook.Alive_status.deceased)

print (f""" \nSammy id: {sammy.instructor_id}
            Banlor lastname: {banlor.last_name}
            Torg's Birday: {torg.dob}
       """)
class_room = gradebook.Classroom()

class_room.add_instructor(sammy)
class_room.add_student(ileen)
class_room.add_student(torg)

class_room.print_instructors()
class_room.print_students()

# test_class.print_students()
# test_class.print_instructors()
# #
# #
# test_class.remove_instructor(jim)
# test_class.remove_student(isiah)
# test_class.print_instructor()
# test_class.print_students()