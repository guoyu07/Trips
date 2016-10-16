import peewee
from peewee import *

import skyscanner

database = SqliteDatabase("database.db")

def before_request_handler():
	database.connect()

def after_request_hander():
	database.close()

class BaseModel(Model):
	class Meta:
		sqlitedb = database

class FlightTable(BaseModel):
	origin = CharField()
	destination = CharField()
	date = CharField()
	price = IntegerField()

class TripTable(BaseModel):
	MovieID = PrimaryKeyField()
	MovieName = CharField()

class TripFlightRelation(BaseModel):
	Flight = ForeignKeyField(FlightTable)
	Trip = ForeignKeyField(TripTable)

class LocationTable(BaseModel):
	name = CharField()

class TripLocationRelation(BaseModel):
	Location = ForeignKeyField(LocationTable)
	Trip = ForeignKeyField(TripTable)

def create_tables():
	tables = [FlightTable, TripTable, TripFlightRelation, LocationTable, TripLocationRelation]
	database.create_tables(tables)


def add_trip(MovieID, locations, MovieName, home, date):
	locations = find_best_route(locations, date)
	#print FlightTable.get_or_create.__doc__

	Trip = TripTable (
		MovieID = MovieID,
		MovieName = MovieName
		).save()

	prev = home
	for location in locations:
		temp = LocationTable.get_or_create(name=location)[0]

		Location_Relation = TripLocationRelation(
			Trip = Trip,
			Location = temp
			).save()
		price = skyscanner.get_price(prev, location, date)

		Flight = FlightTable.get_or_create(origin = prev, destination = location, date = date, price = price)[0]

		Flight_Relation = TripFlightRelation(
			Trip = Trip,
			Flight = Flight
			).save()
		prev = location



def find_best_route(locations, date):
	# populate dict
	distance = {}
	for i in locations:
		distance[i] = {}
		for j in locations:
			if i == j:
				distance[i][j] = 0
			else:
				distance[i][j] = skyscanner.get_price(i, j, date)

	d = lambda a,b:distance[a][b]

	result = [locations[0], locations[1]]

	for l in locations[2:]:
		index = len(result)
		for i in range(0, len(result-1)):
			if d(locations[i], locations[i+1]) + d(locations[i+1], l) > \
				d(locations[i], l) + d(l, locations[i+1]):
				index = i+1
		result.insert(i, l)
	return result


if __name__ == '__main__':
	# Connects the Database
	before_request_handler()

	create_tables()
	add_trip(1, ["Barcelona", "Berlin"], "Lydia", "Berlin", "2017-02-15")

	after_request_hander()	




		