import sqlite3 as lite
import pandas as pd
import pandas.io.sql as psql

cities = (('Las Vegas', 'NV'),
          ('Atlanta', 'GA'),
          ('Orlando', 'FL'),
          ('Chicago', 'IL'),
          ('New York', 'NY'))

weather = (('Las Vegas', 2013, 'July', 'December'),
           ('Atlanta', 2013, 'July', 'January'),
           ('Orlando', 2013, 'July', 'December'),
           ('New York', 2013, 'August', 'November'),
           ('Chicago', 2013, 'July', 'January'))


con = lite.connect('getting_started.db')


# Select all rows and print the result set one row at a time
with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cities")
    cur.execute("DROP TABLE IF EXISTS weather")
    cur.execute("CREATE TABLE cities(Name TEXT, State TEXT)")
    cur.execute("CREATE TABLE weather(City TEXT, Year Int, Warm_Month Text, Cold_Month Text)")
    cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
    cur.executemany("INSERT INTO weather VALUES(?,?,?,?)", weather)

    cur.execute("SELECT Name, State FROM cities inner join weather on name = city where Warm_Month = 'July'")

    rows = cur.fetchall()

    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns=cols)

    StringLoad = "The cities that are warmest in July are: "

    CityState = []

    for row in df.iterrows():
        index, data = row
        CityState.append(data.tolist())


    print(StringLoad, ', '.join(str(p) for p in CityState))