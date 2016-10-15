import peewee

database = SqliteDatabase("database.db")

def before_request_handler():
	database.connect()

def after_request_hander():
	database.close()

class BaseModel(Model):
	class Meta:
		sqlitedb = database

class FlightTable(BaseModel):
	FlightID = PrimaryKryField()
	origin = CharField()
	destination = CharField()
	date = CharField()
	link = CharField()
	price = IntegerField()

class TripTable(BaseModel):
	MovieID = PrimaryKeyField()
	MovieName = CharField()

class TripFlightRelation(BaseModel):
	flight = ForeignKeyField(FlightTable)
	Trip = ForeignKeyField(TripTable)

class LocationTable(BaseModel):
	name = CharField()

class TripLocationRelation(BaseModel):
	LocationTable = ForeignKeyField(LocationTable)
	TripTable = ForeignKeyField(TripTable)

def create_tables():
	tables = [FlightTable, TripTable, TripFlightRelation, LocationTable, TripLocationRelation]
	database.create_tables(tables)



# 
def add_trip(MovieID, locations, MovieName):
	Trip = TripTable (
		MovieID = MovieID
		MovieName = MovieName
		)
	for Location in locations:
		temp = LocationTable.get_or_create(LocationTable.name=Location)

		Relation = TripLocationRelation(
			TripTable = Trip
			LocationTable = temp
			)






def add_flight()

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




		