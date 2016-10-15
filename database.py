import peewee
import skyscanner.py

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
	link = CharField()
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
	locations = find_best_route(locations)

	Trip = TripTable (
		MovieID = MovieID,
		MovieName = MovieName
		)

	prev = home
	for Location in locations:
		temp = LocationTable.get_or_create(LocationTable.name=Location)

		Location_Relation = TripLocationRelation(
			Trip = Trip,
			Location = temp
			)
		prize = skyscanner.get_prize(prev, Location, date)
		link = skyscanner.get_link(prev, Location, date)

		Flight = FlightTable.get_or_create(origin = prev, destination = Location, date = date, link = link, prize = prize)
		Flight_Relation = TripFlightRelation(
			Trip = Trip,
			Flight = Flight
			)
		prev = Location



def find_best_route(locations):
	# populate dict
	distance = {}
	for i in locations:
		distance[i] = {}
		for j in locations:
			if i == j:
				distance[i][j] = 0
			else:
				distance[i][j] = skyscanner.get_prize(i, j)

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



def add_flight():
	pass

if __name__ == '__main__':
	# Connects the Database
	before_request_handler()

	create_tables()
	add_locations("Berlin")
	add_locations("Lissabon")
	add_locations("London")
	add_locations("Paris")
	add_locations("Madrid")
	add_locations("Barcelona")




		