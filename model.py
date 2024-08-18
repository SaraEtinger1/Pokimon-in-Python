import pyodbc

con_string = "DRIVER={SQL Server};" \
             "SERVER=SQL-KITOTBB\TICHNUT;" \
             "DATABASE=Sari_Etinger;"

# def insert_poke(id_, name, type_, height, weight):
#     with pyodbc.connect(con_string) as connection:
#         cursor = connection.cursor()
#         query = "INSERT INTO Pokemon VALUES(?,?,?,?,?)"
#         result = cursor.execute(query, (id_, name, type_, height, weight))
#         print(result.rowcount)

# def is_owner_exist(name_o, town_o):
#     with pyodbc.connect(con_string) as connection:
#         cursor = connection.cursor()
#         query = "select * from ownedby " \
#                 " where  own_name=? and own_type=?"
#         result = cursor.execute(query, (name_o, town_o))
#         data = result.fetchall()
#         if len(data) == 0:
#             return False
#         else:
#             return True


# def insert_ownedby(name_o, town_o):
#     with pyodbc.connect(con_string) as connection:
#         cursor = connection.cursor()
#         query = "INSERT INTO ownedby VALUES(?,?)"
#         if not is_owner_exist(name_o, town_o):
#             result = cursor.execute(query, (name_o, town_o))
#             print(result.rowcount)


# def insert_trainers(id_, name_o, town_o):
#     with pyodbc.connect(con_string) as connection:
#         cursor = connection.cursor()
#         query = "INSERT INTO trainers VALUES(?,?)"
#         id_o = get_id_by_name(name_o, town_o)
#         result = cursor.execute(query, (id_, id_o))


# def get_id_by_name(name_o, town_o):
#     with pyodbc.connect(con_string) as connection:
#         cursor = connection.cursor()
#         query = "select * from ownedby" \
#                 " where  own_name=? and own_type=?"
#         result = cursor.execute(query, (name_o, town_o))
#         data = result.fetchone()
#         return data[0]
