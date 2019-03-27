from person_file import Person
# this (Student) file should be saved in the same directy as the person_file.py file
class Student(Person):
    def __init__(self, name, gender, dob, idnumber):
        Person.__init__(self, name, gender, dob) # calls parent's constructor 
        self._idnumber = idnumber  # add specialization
        self.list_of_courses = []
        #gender attribute is not needed, but it's here to shows you canNOT
        #  inadvertantly overwrite _Person__gender attribute, try it
        self.__gender = "x"
        # Create a list for each student to hold courses in

    def __str__(self):
        if self._is_public:
            # return self.__getInfo() will return an error, try it
            return Person.__str__(self) + " Student ID #: " + str(self._idnumber)
        else:
            return self.getName()

    # Add a method here that allows students to add course to their list of
    # courses. A student should only be able to add courses if they don't
    # overlap with their existing courses. 

# add a Course class here (DO THIS FIRST)
''' Courses should be intialized with (at least) a short name (e.g., CS126),
    a number of credits, a start time, and an end time. Include a method that
    will return True if two course times overlap, and False if they do not. '''

def main():
    jane = Student("Jane", "female", "03-06-1999",1671)
    print(jane)
    # create students and courses and add courses to each student's list of courses

if __name__=="__main__":
    main()
