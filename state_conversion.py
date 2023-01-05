# Adrian Figueredo
# Project 4
# April. 2022
# 1250 1:00pm lab

# State Name and State Abbreviation Conversion Program

# program greeting

print('This program allows the user to lookup a states name')
print('or two letter abbreviation by entering the opposite value')
print()
print('Please type "n" or "a" when prompted')
print('Please type "y or "n" when prompted')
print()

# list of state abbreviations

states_abbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL",
                        "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
                        "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
                        "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
                        "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
                        "VA", "WA", "WV", "WI", "WY"]

# list of state names

state_names=['ALABAMA', 'ALASKA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 
             'CONNECTICUT', 'DELAWARE', 'FLORIDA', 'GEORGIA', 'HAWAII', 'IDAHO',
             'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
             'MAINE', 'MARYLAND', 'MASSACHUSETTS', 'MICHIGAN', 'MINNESOTA',
             'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 'NEVADA', 
             'NEW HAMPSHIRE', 'NEW JERSEY', 'NEW MEXICO', 'NEW YORK',
             'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OKLAHOMA', 'OREGON',
             'PENNSYLVANIA', 'RHODE ISLAND', 'SOUTH CAROLINA', 'SOUTH DAKOTA',
             'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT','VIRGINIA', 'WASHINGTON',
             'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']

# setting choice with value 1

choice = 1

# start loop

while choice == 1:
    
    # user input for conversion
    
    direction = input('Type "n" for state name to abbreviation or type "a" for abbreviation to state name: ')

    direction = direction.lower()
    
    print()
    
    # error check user input
    
    while direction != 'n' and direction != 'a':
        
        print('Invalid input, please enter either an "n" or an "a" to continue')

        print()
        
        direction = input('Please type "n" for state name to abbreviation or type "a" for abbreviation to state name: ')

        direction = direction.lower()

        print()
    
    # if user selection is "n" start conversion
        
    if direction == 'n':
        
        name = input("Please enter state name: ").upper()

        print()

        # error check state input
        
        while name not in state_names:
            
            print("Please enter a correct state name")

            print()
            
            name = input("Please enter state name: ").upper()

            print()
        
        # find index of state names
            
        else:
            
            for i in range(len(state_names)):
                
                if(state_names[i] == name):
                    
                    print('The state abbreviation is', states_abbreviations[i])

                    print()
    
    # if user selection is "a" start conversion
                    
    elif direction == 'a':
        
        name = input("Please enter a state abbreviation: ").upper()

        print()
        
        # validate state abbreviation
        
        while name not in states_abbreviations:
            
            print("Please enter a correct state Abbreviation")

            print()
            
            name = input("Please enter a state Abbreviation: ").upper()

            print()
            
        else:
            
            for i in range(len(states_abbreviations)):
                
                if(states_abbreviations[i] == name):
                    
                    print('The state name is', state_names[i])

                    print()
    
    # user input to end or continue program
                    
    
    end = input('Would you like to continue the program, if yes type "y" or if no input "n": ')

    print()

    end = end.lower()
    
    # check for valid input

    while end != 'y' and end != 'n':
    
        end = input('Error please enter either "n" for no or "y" for yes: ')

        print()
        
        end = end.lower()

    # exit main loop

    if end == 'n':

        choice = False

        print('Have a great day!')


    

    
    
