import psycopg2

# Initialize connection as None
connection = None

def connect(host='localhost', database='master', user='postgres', password='123456'):
    global connection

    try:
        connection_params = {
            'host': host,
            'database': database,
            'user': user,
            'password': password
        }

        if connection is None or connection.closed != 0:
            print('Connecting to PostgreSQL database...')
            connection = psycopg2.connect(**connection_params)

        # Set connection parameters
        connection.set_session(autocommit=True)

    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Error connecting to database: {error}')

def execute_query(query, limit=None):
    global connection

    try:
        with connection.cursor() as cursor:
            # Add LIMIT clause for SELECT queries if a limit is specified
            if limit is not None and query.strip().upper().startswith('SELECT'):
                query += f' LIMIT {limit}'

            cursor.execute(query)

            # Fetch and return the results for SELECT queries
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                return result

            print('Query executed successfully.')

    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Error executing query: {error}')

# Example usage
connect()
select_query = "SELECT * FROM example_table;"
result = execute_query(select_query, limit=30)
print(result)
