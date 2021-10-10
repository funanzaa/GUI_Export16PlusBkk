import psycopg2
from configparser import ConfigParser
import os

class DataBase:
    def __init__(self):
        self.config_object = ConfigParser()
        self.config_object.read(r"config\config.ini")
        self.serverinfo = self.config_object["SERVERCONFIG"]
        self.dbname = self.serverinfo["dbname"]
        self.user = self.serverinfo["user"]
        self.host = self.serverinfo["host"]
        self.port = self.serverinfo["port"]
        self.password = self.serverinfo["passwd"]

    def export(self, file, dateform, dateto):
        print(file)
        print(dateform)
        print(dateto)
        with open(r"sql\{}.sql".format(file), mode="r", encoding="utf8") as f:
            sql = f.read()
        connection = psycopg2.connect(user=self.user, password=self.password, host=self.host, port=self.port,
                                      database=self.dbname)
        cursor = connection.cursor()
        cursor.execute(sql, {'_dateform': dateform, '_dateto': dateto})
        updated_rows = cursor.fetchall()
        # print(len(updated_rows[0]))

        # cursor = connection.cursor()
        # SQL_for_file_output = "COPY ({0}) TO STDOUT WITH DELIMITER '|' CSV".format(sql)
        # t_path_n_file = dir + "/" + file + ".txt"
        # with open(t_path_n_file, 'w') as f_output:
        #     cursor.copy_expert(SQL_for_file_output, f_output)
        # print(sql2)
        # with open("table.text", "w") as file:
        #     cursor.copy_expert(sql2, file)

        for i in range(len(updated_rows)):
            p = len(updated_rows[0])
            # print("first : " + str(p))
            for j in range(len(updated_rows[i])):
                with open(r"file_export\{}.txt".format(file), "a", encoding="utf8") as f:
                    # print("before : " + str(p))
                    p = p - 1
                    if p == 0:
                        # print("p == 0 : " + str(p))
                        if str(updated_rows[i][j]) == 'None':
                            empty = ''
                            f.write("{}".format(empty))
                        else:
                            f.write("{}".format(updated_rows[i][j]))
                    elif p > 0:
                        # print("p > 0 : " + str(p))
                        if str(updated_rows[i][j]) == 'None':
                            empty = ''
                            f.write("{}|".format(empty))
                        else:
                            f.write("{}|".format(updated_rows[i][j]))
            with open(r"file_export\{}.txt".format(file), "a", encoding="utf8") as f:
                f.write("\n")
        print("ok")