import psycopg2

# Initialize connection as None
connection = None

def postgre_connect(host='localhost', database='master', user='postgres', password='123456'):
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

def execute_query(query, params=None):
    global connection

    try:
        with connection.cursor() as cursor:
            '''
            # Add LIMIT clause for SELECT queries if a limit is specified
            if limit is not None and query.strip().upper().startswith('SELECT'):
                query += f' LIMIT {limit}'
            '''
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # Fetch and return the results for SELECT queries
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                return result

    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Error executing query: {error}')

def create_table():
    create_master_table_query = """
    CREATE TABLE IF NOT EXISTS master_table (
        query TEXT,
        url TEXT,
        result TEXT,
        CONSTRAINT unique_url_constraint_master UNIQUE (url)
        );
    """
    create_analytics_table_query = """
    CREATE TABLE IF NOT EXISTS analytic_table (
        url TEXT,
        email TEXT,
        username TEXT,
        links TEXT,
        CONSTRAINT unique_url_constraint_analytic UNIQUE (url)
        );
    """
    create_web_archive_table="""
    CREATE TABLE IF NOT EXISTS web_archive(
        
    )
    """
    execute_query(create_master_table_query)
    print('Table master created successfully.')
    execute_query(create_analytics_table_query)
    print('Table  analytical created successfully.')


def list_all_tables(database='master'):
    list_tables_query = f"""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    AND table_catalog = '{database}'
    ORDER BY table_name;
    """
    result = execute_query(list_tables_query)

    if result:
        print(f'Tables in the {database} database:')
        for table in result:
            print(table[0])
    else:
        print(f'No tables found in the {database} database.')

def drop_table(table_name):
    drop_query = f'DROP TABLE IF EXISTS {table_name}'
    execute_query(drop_query)

def postgre_close_connection():
    global connection

    try:
        if connection is not None and connection.closed == 0:
            connection.close()
            print('Database connection closed.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(f'Error closing connection: {error}')

# # Example use
#postgre_connect()
#drop_table("master_table")
#drop_table("analytic_table")
#create_table()
# list_all_tables()
# # Close the connection when done
#execute_query("ALTER TABLE master_table ADD COLUMN id SERIAL PRIMARY KEY;")
#execute_query("ALTER TABLE master_table DROP COLUMN id ")
#postgre_close_connection()
