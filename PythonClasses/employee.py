#!/usr/bin/env python

class Employee:
    '''
    Class Employee
        members:
            (int)  salary
            (str)  position
            (str)  name
            (int)  working_days

        Constructors:
            void __init__(str, int, str)
            
        Setters:
            void set_salary(int)
            void set_position(str)
            void set_name(str)
            void set_working_days(int)
        
        Getters:
            int get_salary()
            str get_position()
            str get_name()
            int get_earnings()
    '''
    salary = 0
    position = "Software developer"
    name = "Pogos"

    '''Default working day = 22'''
    working_days = 22                              
    
    '''Constructor'''
    def __init__(self, name, salary, position):
        self.salary = salary
        self.position = position
        self.name = name
    
    '''Setting employee's salary'''
    def set_salary(self, salary):

        if(salary < 0):
            print "Salary must be positive value"
            exit()
        self.salary = salary

    '''Setting employee's position'''
    def set_position(self, position):
        self.position = position

    '''Setting employee's name'''
    def set_name(self, name):
        self.name = name

    '''Setting employee's count of working days'''
    def set_working_days(self, working_days):

        if working_days < 1 or working_days > 31:
            print "Working days must be between 1 and 31"
            exit()
        self.working_days = working_days  


    '''Getting employee's name'''
    def get_name(self):
        return self.name
    
    '''Getting employee's position'''
    def get_position(self):
        return self.position

    '''Getting employee's salary'''
    def get_salary(self):
        return self.salary
    
    '''Getting employee's earnings'''
    def get_earnings(self):
        day_earning = self.salary / 22
        salary = self.working_days * day_earning
        earnings = salary - (salary * 0.5)
        return earnings

    '''Print earnings'''
    def print_earnings(self):
        print self.name, self.position, "Earnings in", self.working_days, "is", self.get_earnings()

class Engineer(Employee):
    '''Class Engineer, child class of Employee'''
    
    
    def __init__(self, name, salary, position):
        '''Call Employee's construtor'''
        Employee.__init__(self, name, salary, position)

    def print_engineer(self):
        '''Prints Engineer members'''
        print "Engineer " + self.name + " in position " + self.position + " earns " + str(self.get_earnings())

class Executive(Employee):
   
    ''' Class Executive, child class of Employee'''

    def __init__(self, name, salary, position):
        '''Call Employee's constructor'''
       
        Employee.__init__(self, name, salary, position)

    '''Prints Exeutive members'''
    def print_executive(self):
        print "Executive employee " + self.name + " in position " + self.position + " for this month earnings is " + str(self.get_earnings())

class Contractor(Employee):
    
    '''Class Contractor, child class of Employee'''
    def __init__(self, name, salary, position):
        '''Call Emplyee's constructor'''
        Employee.__init__(self, name, salary, position)
    
    '''Prints Contractor members'''
    def print_contractor(self):
        
        print "Contractor " + self.name + " in position " \
            + self.position + " for this contract earnings is " + str(self.get_earnings())

    def get_earnings(self):
        """
        getEarnings overridden for contractor
        """
        return (self.salary - (self.salary * 0.2))

    def print_earnings(self):
        """
        printEarnings overridden for contractor
        """
        print self.position, self.name, "Earns", self.get_earnings()

                                                        

if __name__ == "__main__":  
    ep = Employee("Pogos", 150000,  "Software Developer")
    ep.print_earnings()

    en = Engineer("Hovo", 82000, "QA Engineer")
    en.print_engineer()    

    ct = Contractor("Petros", 190000,  "Web Developer")
    ct.print_earnings()      
