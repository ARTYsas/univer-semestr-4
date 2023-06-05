import psycopg2

# Connection to PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="Telephone conversations",
    user="postgres",
    password="postgres"
)
cursor = conn.cursor()

def execute_query(query, params=None):
    cursor.execute(query, params)
    rows = cursor.fetchall()
    return rows

def print_results(rows):
    if len(rows) == 0:
        print("No results found.")
    else:
        for row in rows:
            print(row)

def query_cities_by_tariff(tariff_limit):
    query = "SELECT * FROM Cities WHERE tariff <= %s"
    rows = execute_query(query, (tariff_limit,))
    print_results(rows)

def query_subscribers():
    query = "SELECT last_name, first_name, patronymic, phone_number FROM Subscribers ORDER BY last_name"
    rows = execute_query(query)
    print_results(rows)

def query_subscribers_in_city(city):
    query = """
        SELECT s.last_name, s.first_name, s.patronymic, s.phone_number, c.tariff
        FROM Subscribers s, Cities c
        WHERE c.city_name = %s AND s.subscriber_id = c.city_id
        ORDER BY s.last_name
    """
    rows = execute_query(query, (city,))
    print_results(rows)

def query_total_duration_payment():
    query = """
        SELECT s.subscriber_id, s.last_name, s.first_name, s.patronymic,
               SUM(c.duration_minutes) AS total_duration,
               SUM(c.duration_minutes * ci.tariff) AS total_payment
        FROM Subscribers s
        JOIN Conversations c ON s.subscriber_id = c.subscriber_id
        JOIN Cities ci ON ci.city_id = c.city_id
        GROUP BY s.subscriber_id, s.last_name, s.first_name, s.patronymic
        ORDER BY s.subscriber_id
    """
    rows = execute_query(query)
    print_results(rows)

def query_total_payment_sessions():
    query = """
        SELECT COUNT(*) AS total_sessions, SUM(c.duration_minutes) AS total_duration,
               SUM(c.duration_minutes * ci.tariff) AS total_payment
        FROM Conversations c
        JOIN Cities ci ON ci.city_id = c.city_id
    """
    rows = execute_query(query)
    print_results(rows)

def query_subscribers_new():
    query = "SELECT last_name, first_name, patronymic, phone_number FROM Subscribers ORDER BY last_name"
    rows = execute_query(query)
    print("List of subscribers:")
    if len(rows) == 0:
        print("No subscribers found.")
    else:
        for i, row in enumerate(rows, 1):
            full_name = f"{row[0]} {row[1][0]}.{row[2]}"
            print(f"{i}. {full_name}: {row[3]}")

# Usage
print('Task 1')
tariff_limit = float(input("Enter the maximum tariff per minute: "))
query_cities_by_tariff(tariff_limit)

print("")

print('Task 2')
query_subscribers()

print("")

print('Task 3')
city = input("Enter the city name: ")
query_subscribers_in_city(city)

print("")

print('Task 4.1')
print("Payment for each abonent")
query_total_duration_payment()

print("")

print('Task 4.2')
print("overall total payment amount and the number of conversation sessions")
query_total_payment_sessions()

print("")

print('Task 5')
query_subscribers_new()

# Close the connection
cursor.close()
conn.close()
