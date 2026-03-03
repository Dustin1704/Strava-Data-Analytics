import psycopg2 as p2

# Connection Details for Database
conn_host = "192.168.1.100"
conn_port = 5432
conn_user = "postgres"
conn_pass = "6oFPYPIR$Fjn8688@a279F72Ms2EUZnB"
conn_db = "Strava_raw"
connection = p2.connect(host = conn_host, port = conn_port, user = conn_user, password = conn_pass, database = conn_db)

#
current = connection.cursor()
current.execute("""CREATE TABLE test(
                id SERIAL PRIMARY KEY,
                name VARCHAR (20) UNIQUE NOT NULL);
                """)
connection.commit()

current.close()
connection.close()