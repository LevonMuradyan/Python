#!/usr/bin/env python

'''Declaring Date class'''
class Date:
    '''This class is a prototype of Date class

    Hidden members of Class:

    __day 
    __month 
    __year 
    __month_days

    Methods:
    Constructors:
        void __init__(int,int,int) 
    Setters:
        void set_day(int)
        void set_month(int)
        void set_year(int) 
    Getters:
        int get_day()
        int get_month()
        int get_year()

    
    '''
    
    '''Hidden members of Class'''
    __day = 1
    __month = 1
    __year = 1
    
    '''Count of days for each month '''   
    __month_days = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    
    '''Date parameterized constructor'''
    def __init__(self, day, month, year):
        if day < 1 or month < 1 or year < 1 \
             or type(day) != int or type(month) != int or type(year) != int:
            print "All function parameter(s) must be positive integer(s)"
            exit()
        self.__day = day
        self.__month = month
        self.__year = year
   
    '''Setting day'''
    def set_day(self, day):
        if day < 1 or type(day) != int :
            print "All function parameter(s) must be positive integer(s)"
            exit()
        self.__day = day

    '''Setting month'''
    def set_month(self, month):
        if month < 1 or type(month) != int:
            print "All function parameter(s) must be positive integer(s)"
            exit()
        self.__month = month
    
    '''Setting year'''
    def set_year(self, year):
        if year < 1 or type(year) != int:
            print "All function parameter(s) must be positive integer(s)"
            exit()
        self.__year = year

    
    '''Getting day'''
    def get_day(self):
        return self.__day

    '''Getting month'''
    def get_month(self):
        return self.__month
    
    '''Getting year'''
    def get_year(self):
        return self.__year

    '''Checking if year is leap'''
    def is_leap(self):
        return (((self.__year % 4 == 0) and (self.__year % 100 != 0)) \
            or (self.__year % 400 == 0))

    '''Counting all leap years till current year'''
    def leap_years_count(self): 
      
        years = self.__year  
      
        ''' Check if the current year needs to be considered 
            for the count of leap years or not
        '''  
        if (self.__month <= 2) : 
                years-= 1
          
        ''' An year is a leap year if it is a multiple of 4,  
            multiple of 400 and not a multiple of 100. 
        ''' 
        return int( years / 4 - years / 100 + years / 400 )
    
    ''' This function returns number of days between two   
        given dates
    '''  
    def get_difference(self,date) : 
   
        ''' Count total number of days before first date '''  
  
        ''' initialize count using years and day ''' 
        n1 = self.__year * 365 + self.__day 
  
        '''Add days for months in given date'''  
        for i in range(1, self.__month):
            n1 += self.__month_days[i]  
  
        '''Since every leap year is of 366 days,  
            Add a day for every leap year
        '''  
        n1 += self.leap_years_count()  

        '''Similary, count total number of days before second date '''  
  
        n2 = date.__year * 365 + date.__day  
        for i in range(1, date.__month) : 
            n2 += date.__month_days[i]  
        n2 += date.leap_years_count()  
  
        '''return difference between two counts'''  
        return abs(n2 - n1)

    '''This function add days and returns calculated date'''
    def add_day(self, num):

        if num < 0 or type(num) != int:
            print "All Add function parameter(s) must be positive integer(s) or zero"
            exit()

        '''Calculating days count from 1.1.current_year till 
            current_day.current_month.current_year
        '''
        count = 0
        for i in range(1, self.__month):
            count += self.__month_days[i]
        '''Adding calculated days'''
        num += count + self.__day  

        '''Now let's began from the beginnig of year'''
       
        self.__month = 1
        self.__day = 0
                
        '''Calculating years'''
        while True:

            if self.is_leap():
                if num > 366:
                    num -= 366 
                    self.__year += 1
                else:
                    break

            else:
                if num > 365:
                    num -= 365
                    self.__year += 1
                else:
                    break
            

        '''Calculating months'''
        if num > self.__month_days[self.__month ]:
            while self.__day + num > self.__month_days[self.__month]:
                if self.is_leap():
                    if self.__month == 2:
                        num -= (self.__month_days[self.__month] + 1)
                        self.add_month(1)
                        continue
                
                num -= self.__month_days[self.__month]
                self.add_month(1)
        
        '''Calculating days'''
        self.__day += num 


    '''This function adds count of months to current month'''    
    def add_month(self, num):

        if num < 0 or type(num) != int:
            print "All Add function parameter(s) must be positive integer(s) or zero"
            exit()

        if self.__month + num > 12:
            self.__year += 1
        self.__month = (self.__month + num) % 12
        '''If the rest is 0, means that '''
        if self.__month == 0:
            self.__month = 12
        
            
    '''This function adds count of years to current year'''
    def add_year(self,num):

        if num < 0 or type(num) != int:
            print "All Add function parameter(s) must be positive integer(s) or zero"
            exit()

        self.__year += num



if __name__ == "__main__":

    d1 = Date(1,1,2011)
    d2 = Date(10,11,1594617)

    d3 = Date(1,1,2012)
    d4 = Date(1,1,2013)

    d5 = Date(1,1,2012)
    d6 = Date(31,12,2012)

    diff1 = d2.get_difference(d1)
    diff2 = d3.get_difference(d4)
    diff3 = d5.get_difference(d6)

    print "\nDifference between 1.1.2011 and 10.11.1594617 = ",diff1
    d1.add_day(581687710)
    print "After adding",diff1,"to 1.1.2011 = " + str(d1.get_day()) \
        + "." + str(d1.get_month()) + "." + str(d1.get_year())

    print "\nDifference between 1.1.2012 and 1.1.2013 = ",diff2
    d3.add_day(366)
    print "After adding",diff2,"to 1.1.2012 = " + str(d3.get_day()) \
        + "." + str(d3.get_month()) + "." + str(d3.get_year())

    print "\nDifference between 1.1.2012 and 31.12.2012 = ",diff3
    d5.add_day(365)
    print "After adding",diff3,"to 1.1.2012 = " + str(d5.get_day()) \
        + "." + str(d5.get_month()) + "." + str(d5.get_year())


