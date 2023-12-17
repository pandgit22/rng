import mysql.connector
from subprocess import check_output

# authorize to database.
auth_db = {
    'host': 'localhost',
    'user': 'pauls',
    'password': 'Udens123!',
    'database': 'rng_base',
}

# function to run the constructor and save it to db.
def run_and_save_constr_output(file_name):
    try:
        # run the constr.
        file_path = f'/home/paul/{file_name}'
        output_bytes = check_output(['python3', file_path]) # gives byte string;
        output_str = output_bytes.decode('utf-8').strip() # decodes to regular string.

        # check if the output is a valid int value.
        try:
            random_number = int(output_str)
        except ValueError:
            raise ValueError(f"The output from {file_name} is not a valid integer: {output_str}")

        # connect to db.
        connection = mysql.connector.connect(**auth_db)
        cursor = connection.cursor()

        # save output to db.
        insert_query = "INSERT INTO rngtable (random_number) VALUES (%s)"
        data = (random_number,)
        cursor.execute(insert_query, data)

        # commit changes and close connection.
        connection.commit()
        connection.close()
        # console message to show if something happened.
        print(f"{file_name} Output correctly stored in database.")
    except Exception as e:
        print(f"Error executing {file_name}: {e}")

# checks if script is run as main program.
if __name__ == "__main__":
    run_and_save_constr_output('rng_konstr.py')

