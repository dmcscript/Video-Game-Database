# Making game libray storage

import sqlite3 as lite
import sys
def getGames():
	l=[]
	num=int(raw_input("How Many games are you entering? "))
	for i in range(num):
		game= raw_input("%d: Video game Name? " % (i+1))
		system = raw_input("%d: System? " % (i+1))
		t = (game,system)
		l.append(t)
	games = tuple(l)
	return games

# create games tuple list to import into table	
games = getGames()

# ask if the User wants to get a new table
def newTable():
	newtable= raw_input("Do you want a new table (y/n)? ")
	if (newtable == 'y'):
			return True
	else:
			return False
# connect to database
con =lite.connect('game.db')
#start database manipulation
with con:
	cur = con.cursor()
	#asks if the user wants a newtable
	if (newTable()):
		cur.execute("DROP TABLE IF EXISTS Games")
		cur.execute("CREATE TABLE Games(Name TEXT, System TEXT)")
	#insert the games into the tables
	cur.executemany("INSERT INTO Games VALUES(?,?)", games)



			
