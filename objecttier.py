#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through the data tier.
#

import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
    # Constructor
    def __init__(self, lobbyistID, firstName, lastName, phoneNum):
        self._Lobbyist_ID= lobbyistID 
        self._First_Name = firstName 
        self._Last_Name = lastName 
        self._Phone = phoneNum 
   
    # Properties
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone
      

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    # Constructor
    def __init__(self, lobbyistID, salutation, firstName, midInitial, lastName, suffix, add1, add2, city, stateInitial, zipCode, country, email, phoneNum, fax, yearsRegistered, employers, totalComp):
        self._Lobbyist_ID= lobbyistID 
        self._Salutation= salutation 
        self._First_Name = firstName 
        self._Middle_Initial = midInitial 
        self._Last_Name = lastName 
        self._Suffix= suffix 
        self._Address_1= add1 
        self._Address_2 = add2 
        self._City = city 
        self._State_Initial = stateInitial
        self._Zip_Code = zipCode 
        self._Country = country 
        self._Email = email 
        self._Phone = phoneNum 
        self._Fax = fax
        self._Years_Registered = yearsRegistered 
        self._Employers = employers 
        self._Total_Compensation = totalComp 

   
    # Properties
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def Salutation(self):
        return self._Salutation

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Middle_Initial(self):
        return self._Middle_Initial

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Suffix(self):
        return self._Suffix

    @property
    def Address_1(self):
        return self._Address_1

    @property
    def Address_2(self):
        return self._Address_2

    @property
    def City(self):
        return self._City

    @property
    def State_Initial(self):
        return self._State_Initial

    @property
    def Zip_Code(self):
        return self._Zip_Code

    @property
    def Country(self):
        return self._Country

    @property
    def Email(self):
        return self._Email

    @property
    def Phone(self):
        return self._Phone

    @property
    def Fax(self):
        return self._Fax

    @property
    def Years_Registered(self):
        return self._Years_Registered

    @property
    def Employers(self):
        return self._Employers

    @property
    def Total_Compensation(self):
        return self._Total_Compensation


##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
    # Constructor
    def __init__(self, lobbyistID, firstName, lastName, phoneNum, totalComp, clients):
        self._Lobbyist_ID= lobbyistID 
        self._First_Name = firstName 
        self._Last_Name = lastName 
        self._Phone = phoneNum 
        self._Total_Compensation = totalComp 
        self._Clients = clients 
   
    # Properties
    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

    @property
    def Clients(self):
        return self._Clients
   

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
    # query to get number of lobbyists
    sql = """SELECT COUNT(Lobbyist_ID)
                FROM LobbyistInfo;"""
    
    # store data 
    row = datatier.select_one_row(dbConn, sql, parameters = None)

    # query did not retrieve any data or error occurred 
    if (row == ()):
        return -1

    numLobbyists = row[0]

    return numLobbyists # return the number of lobbyists


##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
    # query to get number of employers
    sql = """SELECT COUNT(Employer_ID)
                FROM EmployerInfo;"""
    
    # store data
    row = datatier.select_one_row(dbConn, sql, parameters = None)

    # query did not retrieve any data or error occurred 
    if (row == ()):
        return -1

    numEmployers = row[0]

    return numEmployers # return the number of employers
   

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
    # query to get number of clients
    sql = """SELECT COUNT(Client_ID)
                FROM ClientInfo;"""
    
    # store data 
    row = datatier.select_one_row(dbConn, sql, parameters = None)

    # query did not retrieve any data or error occurred 
    if (row == ()):
        return -1

    numClients = row[0]

    return numClients # return the number of clients


##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
    # query to get info about lobbyists, given a name pattern
    sql = """SELECT Lobbyist_ID, First_Name, Last_Name, Phone
                FROM LobbyistInfo
                WHERE First_Name LIKE ? OR Last_Name LIKE ?
                ORDER BY Lobbyist_ID ASC;"""

    # store data
    rows = datatier.select_n_rows(dbConn, sql, parameters = [pattern, pattern])

    # query did not retrieve any data or error occurred 
    if (rows == None): 
        return []
    
    listOfLobbyists = []

    # store data in a list of Lobbyist Objects
    for r in rows:
        lobbyist = Lobbyist(r[0], r[1], r[2], r[3])
        listOfLobbyists.append(lobbyist)

    return listOfLobbyists


##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    # query to get first 15 parameters need to create a LobbyistDetails object
    sql = """SELECT Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City, State_Initial, ZipCode, Country, Email, Phone, Fax
                FROM LobbyistInfo
                WHERE Lobbyist_ID = ?;"""

    # store data
    row = datatier.select_one_row(dbConn, sql, parameters = [lobbyist_id])

    # query did not retrieve any data or error occurred 
    if (row == ()):
        return None


    # query to get 16th parameter: a list of years registered
    sql = """SELECT Year
                FROM LobbyistYears
                WHERE Lobbyist_ID = ?;"""

    # store data    
    years = datatier.select_n_rows(dbConn, sql, parameters = [lobbyist_id])

    yearList = []

    # insert years into a list
    for y in years:
        yearList.append(y[0])


    # query to get 17th parameter: a list of employer names
    sql = """SELECT Employer_Name
                FROM EmployerInfo
                JOIN LobbyistAndEmployer ON LobbyistAndEmployer.Employer_ID = EmployerInfo.Employer_ID
                WHERE Lobbyist_ID = ?
                GROUP BY Employer_Name;"""
    
    # store data    
    employers = datatier.select_n_rows(dbConn, sql, parameters = [lobbyist_id])

    employerList = []

    # insert employers into a list
    for e in employers:
        employerList.append(e[0])


    # query to get 18th parameter: Total_Compensation
    sql = """SELECT SUM(Compensation_Amount)
                FROM Compensation
                WHERE Lobbyist_ID = ?;"""

    # store data
    comp = datatier.select_one_row(dbConn, sql, parameters = [lobbyist_id])

    if (comp[0] is None):
            compensation = 0.0
    else:
            compensation = comp[0]

    # create Lobbyist Details object with retrieved data
    lobbyistDetailsObject = LobbyistDetails(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], yearList, employerList, compensation)
 
    return lobbyistDetailsObject


##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    # query to get info about a lobbyists with top N total compensation, given a year
    sql = """SELECT LobbyistInfo.Lobbyist_ID, First_Name, Last_Name, Phone, SUM(Compensation_Amount) AS total
                FROM LobbyistInfo
                JOIN Compensation ON Compensation.Lobbyist_ID = LobbyistInfo.Lobbyist_ID
                WHERE strftime('%Y', Compensation.Period_End) = ?
                GROUP BY LobbyistInfo.Lobbyist_ID
                ORDER BY total DESC
                LIMIT ?;"""

    # store data
    rows = datatier.select_n_rows(dbConn, sql, parameters = [year, N])

    # query did not retrieve any data or error occurred 
    if (rows == None):
        return []

    # query to get clients
    sql = """SELECT Client_Name
                FROM ClientInfo
                JOIN Compensation ON Compensation.Client_ID = ClientInfo.Client_ID
                WHERE Lobbyist_ID = ? AND strftime('%Y', Period_Start) = ?
                GROUP BY ClientInfo.Client_ID
                ORDER BY Client_Name;"""

    clientList = []
    lobbyistClientsList = []

    # go through the data and insert a LobbyistClients object into the list
    for row in rows:
        # store the clients for each lobbyist
        clients = datatier.select_n_rows(dbConn, sql, parameters = [row[0], year])
        
        # query did not retrieve any data or error occurred 
        if (clients == None): 
            return []
        
        # store the client names into a list
        for c in clients:
            clientList.append(c[0])
        
        # store each lobbyist with info about them in a list
        lobbyistClientsObject = LobbyistClients(row[0], row[1], row[2], row[3], row[4], clientList)
        lobbyistClientsList.append(lobbyistClientsObject)

        clientList = [] # clear the clientList, to store clients for next lobbyist
        
    return lobbyistClientsList


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    # query to check if lobbyist exists
    sql = """SELECT Lobbyist_ID 
                FROM LobbyistInfo 
                WHERE Lobbyist_ID = ?;"""
        
    # store data
    row = datatier.select_one_row(dbConn, sql, parameters = [lobbyist_id])

    # return 0 if lobbyist doesn't exist or error occurred
    if (row == ()):
        return 0

    # query to insert the year for a given lobbyist
    sql = """INSERT INTO LobbyistYears (Lobbyist_ID, Year)
                VALUES (?, ?);"""

    # commit the changes to the database, and get number of rows changed
    rowcount = datatier.perform_action(dbConn, sql, parameters = [lobbyist_id, year])

    return rowcount # return number of rows changed
  

##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    # query to check if lobbyist exists
    sql = """SELECT Lobbyist_ID 
                FROM LobbyistInfo 
                WHERE Lobbyist_ID = ?;"""
        
    # store data
    row = datatier.select_one_row(dbConn, sql, parameters = [lobbyist_id])

    # return 0 if lobbyist doesn't exist or error occurred
    if (row == ()):
        return 0

    # query to update salutation for a given lobbyist
    sql = """UPDATE LobbyistInfo
                SET Salutation = ?
                WHERE Lobbyist_ID = ?;"""

    # commit the changes to the database, and get number of rows changed
    rowcount = datatier.perform_action(dbConn, sql, parameters = [salutation, lobbyist_id])

    return rowcount # return number of rows changed
