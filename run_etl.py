# Main function to run the script
from sql_functions import create_database, create_connection, create_tables, insert_data, query_data, transform_data, load_to_csv

def main():
    create_database()
    connection = create_connection()
    if connection:
        create_tables(connection)
        insert_data(connection)
        data = query_data(connection)
        transformed_data = transform_data(data)
        load_to_csv(transformed_data)
        connection.close()

if __name__ == "__main__":
    main()
