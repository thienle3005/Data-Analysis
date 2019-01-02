import MySQLdb
import  time

def record_data(people_id, total_people_in, time_people_in, total_people_out, time_people_out):
    connection = MySQLdb.connect (host = "20.203.153.47",
                                  user = "root",
                                  passwd = "",
                                  db = "counting_people")

    cursor = connection.cursor()
    # insert data local
    # sql = "INSERT INTO report (ID, PeopleId, TotalPeopleIn, TimePeopleIn, TotalPeopleOut,TimePeopleOut) VALUES(null, " + str(people_id) + "," + str(total_people_in) + ",'" + str(time_people_in) + "'," + str(total_people_out) + ",'" + str(time_people_out) + "')"
    # insert data server
    sql = "INSERT INTO report (id, PeopleID, NumberPeopleIn, DateTimeIn, NumberPeopleOut,DateTimeOut) VALUES(null, " + str(people_id) + "," + str(total_people_in) + ",'" + str(time_people_in) + "'," + str(total_people_out) + ",'" + str(time_people_out) + "')"

    cursor.execute (sql)
    connection.commit()
    cursor.close()
    connection.close()
