import pyodbc

con_string = "DRIVER={SQL Server};" \
             "SERVER=SQL-KITOTBB\TICHNUT;" \
             "DATABASE=Sari_Etinger;"


def get_max_command():
    with pyodbc.connect(con_string) as connection:
        cursor = connection.cursor()
        query = "select pok_name,pok_weight from Pokemon where pok_weight=( " \
                "select max(pok_weight) from Pokemon);"
        result = cursor.execute(query)
        data = result.fetchone()
        print(data)


get_max_command()
