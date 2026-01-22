#
# main.py
#
# Presentation tier: Implements 5 commands for the Chicago Lobbyist Database Application
#
# Original author: Tala Shraim
#
# Attribution
# Starter code and database schema were provided as part of a university coursework framework.  
# All application logic, SQL queries, object modeling, and feature implementations were completed independently.
#

import sqlite3
import objecttier

# print general statistics of database
def print_stats(dbConn):
    print("\nGeneral Statistics:")

    # get number of lobbyists
    print("  Number of Lobbyists:", f"{objecttier.num_lobbyists(dbConn):,}")

    # get number of employers
    print("  Number of Employers:", f"{objecttier.num_employers(dbConn):,}")

    # get number of clients
    print("  Number of Clients:", f"{objecttier.num_clients(dbConn):,}")


# command 1: Look up lobbyists by their first or last name,
def command1(dbConn):
    # prompt user for lobbyist name
    name = input("\nEnter lobbyist name (first or last, wildcards _ and % supported): ")

    # retrieve the lobbyists with matching name
    listOfLobbyists = objecttier.get_lobbyists(dbConn, name)

    if listOfLobbyists is None:
        listOfLobbyists = []

    print()
    # get and display number of lobbyists found
    numLobbyists = len(listOfLobbyists)
    print("Number of lobbyists found:", numLobbyists)
    
    # if more than 100 lobbyists found, then print error message
    if numLobbyists > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...")
        return
    elif numLobbyists > 0:
        print()
        # print information about the lobbyists found
        for lobbyist in listOfLobbyists:
            print(lobbyist.Lobbyist_ID, ":", 
                lobbyist.First_Name,
                lobbyist.Last_Name, "Phone:",
                lobbyist.Phone)



# command 2: Look up details on a particular lobbyist by searching their ID,
def command2(dbConn):
    # prompt user for lobbyist id
    lobbyist_id = input("\nEnter Lobbyist ID: ")

    # retrieve the lobbyist with matching id
    lobbyist = objecttier.get_lobbyist_details(dbConn, lobbyist_id)

    print()
    # if no lobbyist found, print error message
    if lobbyist is None:
        print("No lobbyist with that ID was found.")
        return

    # print info about the lobbyist found
    print(lobbyist_id, ":\n",
    "Full Name:", lobbyist.Salutation, lobbyist.First_Name, lobbyist.Middle_Initial, lobbyist.Last_Name, lobbyist.Suffix, "\n",
    "Address:", lobbyist.Address_1, lobbyist.Address_2, ",", lobbyist.City, ",", lobbyist.State_Initial, lobbyist.Zip_Code, lobbyist.Country, "\n",
    "Email:", lobbyist.Email, "\n",
    "Phone:", lobbyist.Phone, "\n",
    "Fax:", lobbyist.Fax, "\n", 
    "Years Registered:", end = " ")

    for year in lobbyist.Years_Registered:
        print(f"{year},", end = " ")
    
    print("\n Employers:", end = " ")

    for employer in lobbyist.Employers:
        print(f"{employer},", end = " ")

    print("\n Total Compensation:", f"${lobbyist.Total_Compensation:,.2f}")
    


# command 3: Find the top N lobbyists by total compensation in a given year,
def command3(dbConn):
    # prompt user for value of N
    N = input("\nEnter the value of N: ")

    newN = int(N)

    # check a positive non-zero value was inputted
    if newN < 1:
        print("Please enter a positive value for N...")
        return
    
    # prompt user for year
    year = input("Enter the year: ")

    # retrieve the top N lobbyist in given year
    clientsObjectsList = objecttier.get_top_N_lobbyists(dbConn, newN, year)
    
    if clientsObjectsList is None:
        return
    elif len(clientsObjectsList) == 0:
        return

    num = 1 
    print()
    # print info about the top N lobbyists
    for lobbyist in clientsObjectsList:
        print(num, ".", lobbyist.First_Name, lobbyist.Last_Name, "\n"
        " Phone:", lobbyist.Phone)

        print(" Total Compensation:", f"${lobbyist.Total_Compensation:,.2f}")
        
        print(" Clients: ", end = "")
    
        for client in lobbyist.Clients:
            print(f"{client},", end = " ")
        
        num = num + 1
        print()
    

# command 4: Insert a new registration year for a lobbyist,
def command4(dbConn):
    # prompt sure for year and lobbyist id that they want to add year to 
    year = input("\nEnter year: ")
    lobbyist_id = input("Enter the lobbyist ID: ")

    # insert the year into the database
    added = objecttier.add_lobbyist_year(dbConn, lobbyist_id, year)

    print()

    # print message stating wether lobbyist was found and year added
    if added < 1:
        print("No lobbyist with that ID was found.")
    else:
        print("Lobbyist successfully registered.")


# command 5: Set the salutation of a lobbyist.
def command5(dbConn):
    # prompt user for lobbyist id and salutation
    lobbyist_id = input("\nEnter the lobbyist ID: ")
    salutation = input("Enter the salutation: ")

    # insert or modify salutation to salutation given
    set = objecttier.set_salutation(dbConn, lobbyist_id, salutation)

    print()

    # print message stating wether lobbyist was found and salutation set
    if set < 1:
        print("No lobbyist with that ID was found.")
    else:
        print("Salutation successfully set.")



# start the menu and complete command given by user
def startMenu(dbConn):
    while True:
        # prompt user for command
        userInput = input("\nPlease enter a command (1-5, x to exit): ") 
        if userInput == "x":
            exit() # exit program if user enters x

        # call appropriate function to compute output based on command given
        elif userInput == "1":
            command1(dbConn)
        elif userInput == "2":
            command2(dbConn)
        elif userInput == "3":
            command3(dbConn)
        elif userInput == "4":
            command4(dbConn)
        elif userInput == "5":
            command5(dbConn)
        # prompt user to enter command again if command unknown
        else:
            print("**Error, unknown command, try again...")
            


##################################################################  
#
# main
#
print('** Welcome to the Chicago Lobbyist Database Application **')

dbConn = sqlite3.connect('Chicago_Lobbyists.db')

# print general Statistics of CTA2 database
print_stats(dbConn)

# start menu to process command given
startMenu(dbConn)

#
# done
#
