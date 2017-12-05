import sqlite3

DB_NAME = 'test.db'


def addOwner(owner_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("insert into Owners(o_id, o_name, o_address, phone_number) values(?,?,?,?)", owner_data)
    conn.commit()

    conn.close()


def addAnimal(animal_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("insert into Animals(a_id, o_id, a_name, type, breed) values(?,?,?,?,?)", animal_data)
    conn.commit()

    conn.close()


def addEmployee(employee_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("insert into Employees(e_id, e_name, e_type) values(?,?,?)", employee_data)
    conn.commit()

    conn.close()


def addProcedure(procedure_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("insert into Procedures(p_id, p_name) values(?,?)", procedure_data)
    conn.commit()

    conn.close()


def addOffice(office_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("insert into Offices(office_id, address, manager_name) values(?,?,?)", office_data)
    conn.commit()

    conn.close()


def addPayment(payment_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("insert into Payments(r_id, o_id, status, amount, method, date) values(?,?,?,?,?,?)", payment_data)
    conn.commit()

    conn.close()


def addAppointment(appointment_data):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("insert into Appointments(a_id, e_id, date, time, p_id, office_id) values(?,?,?,?,?,?)", appointment_data)
    conn.commit()

    conn.close()


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


def checkLogin(user):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    u = user,
    c.execute("SELECT o_id FROM Owners where o_name=?", u)

    ret = c.fetchone()
    conn.close()
    if ret is None:
        return -1
    return ret[0]

