import mysql.connector

class DB:
    def __init__(self):
        #connect to database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='flights'
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')
        except:
            print('Connection Error!')

    def fetch_city_name(self):
        city = []
        self.mycursor.execute("""
        SELECT DISTINCT(destination) from flights.flightss
        UNION
        SELECT DISTINCT(source) from flights.flightss
        """)

        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flight(self, source, destination):

        self.mycursor.execute("""
        select Airline, Route, Dep_Time, Duration, Price from flights.flightss
        where source = '{}' and destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []

        self.mycursor.execute("""
        select Airline, count(*) from flights.flightss
        group by Airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):

        city = []
        frequency = []

        self.mycursor.execute("""
        select Source, count(*) from (select Source from flights.flightss
                                    union all
                                    select Destination from flights.flightss) t
        group by t.Source
        order by count(*) desc
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):
        date = []
        frequency = []

        self.mycursor.execute("""
                select Date_of_journey, count(*) from flights.flightss
                group by Date_of_journey                           
                
                """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency

