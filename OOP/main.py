class Person:
    def __init__(self, name, age, job_position):
        self.name = name
        self.age = age
        self.job_position = job_position
        
    def print_person_data(self):
        print('Name : %s' % self.name)
        print('Age : %d' % self.age)
        print('Job Position : %s' % self.job_position)
    
fadhil = Person('Fadhil', 22, 'Programmer')
fadhil.print_person_data()