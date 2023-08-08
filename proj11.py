#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:29:57 2022

Main:
    driver of program
    creates a calender object
    prints menu and promtps for input until valid
    prompts user to add, delete, or list events until user wants to quit
    once quit is input, ends program
    
"""
#imports and inits
from p11_calendar import P11_Calendar
from p11_event import P11_Event

CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''

def check_time(time,duration):
    ''' 
    checks if time and duration are valid
    returns false if not valid, true if valid
    '''
    #returns false if duration 0
    if duration == 0:
        return False
    #tries to set start time and end time in minute values
    try:
        start_time = int(time[0:time.index(':')])*60 + int(time[time.index(':')+1:])
        end_time = start_time + duration#adds duration to start time
        if not (6*60<=start_time<end_time<=17*60):#if start time and end time are not between 6am to 5pm
            return False#returns false
    except:
        return False#returns false if error
    return True#if valid returns true
    
def event_prompt():
    ''' prompts for event details
    creates and event from class
    loops until valid event
    returns event if valid
    '''
    valid = True#inits variable to loop
    #prompts for event details
    date_ep = input("Enter a date (mm/dd/yyyy): ")
    time = input("Enter a start time (hh:mm): ")
    duration = int(input("Enter the duration in minutes (int): "))
    cal_type = input("Enter event type ['meeting','event','appointment','other']: ")
    #loops until valid details
    while valid == True:
        event = P11_Event(date_ep,time,duration,cal_type)#creates an event object
        if not (event.get_valid() and check_time(time, duration)):#if not valid event, using functions and methods
            print("Invalid event. Please try again.")#error prompt
            #reprompts for event details
            date_ep = input("Enter a date (mm/dd/yyyy): ")
            time = input("Enter a start time (hh:mm): ")
            duration = int(input("Enter the duration in minutes (int): "))
            cal_type = input("Enter event type ['meeting','event','appointment','other']: ")
        else:
            return event#if not invalid, returns event
                
def main():
    calander = P11_Calendar()#creates calender object from class
    #prints menu and prompts for option
    print(MENU)
    option = input("Select an option: ").lower()
    #loops until user quits
    while option != 'q':
        if option == 'a':#if add
            event = event_prompt()#prompts for event using function
            print("Add Event")#header
            add =calander.add_event(event)#creates add obj and adds event to calender 
            if add == True:
                print("Event successfully added.")#prints if event was added
            elif add == False:
                print("Event was not added.")#prints if event was unable to be added
        elif option =='d':#if delete
            print("Delete Event")#header
            #prompts for date and time
            date_d = input("Enter a date (mm/dd/yyyy): ")
            time = input("Enter a start time (hh:mm): ")
            delete = calander.delete_event(date_d, time)#creates delete obj and deletes event with date and time
            if delete == True:
                print("Event successfully deleted.")#prints if event was deleted
            elif delete == False:
                print("Event was not deleted.")#prints if event was unable to be deleted
        elif option =='l':#if list
            print("List Events")#prints header
            date_l = input("Enter a date (mm/dd/yyyy): ")#prompts for date
            event_list = calander.day_schedule(date_l)#sets event list to events from that date using method
            if event_list == []:#if blank list
                print("No events to list on {}".format(date_l))#error statement
            else:
                for event in event_list:#for each event in list
                    print(str(event))#prints formatted event details
        #prints menu and reprompts for option
        print(MENU)
        option = input("Select an option: ").lower()
    
        
        
#LETS GOOOO LAST PROJECT DONE
#If you're reading this I hope you have a great summer    
    
    
    
if __name__ == '__main__':
     main()