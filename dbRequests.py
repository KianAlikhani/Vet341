import sqlite3

DB_NAME = 'test.db'


def getAppointmentHistory(animal_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("select * from Appointments as a where a.a_id=?", (animal_id,))
    ret = c.fetchall()

    conn.close()
    return ret


def getPaymentRecords(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("select * from Payments as p where p.o_id=?", (user_id,))
    ret = c.fetchall()

    conn.close()
    return ret


def getPetAppointments(animal_id, date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("select * from Appointments as a where a.a_id=? and a.date > ?", (animal_id, date))
    ret = c.fetchall()

    conn.close()
    return ret



