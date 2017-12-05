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


def getAvailableVets(input_date, input_time):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''select * from Employees as e where not exists
                (select * from Appointments as a where a.date = ? and a.time = ?)''', (input_date, input_time))
    ret = c.fetchall()

    conn.close()
    return ret


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


def getDailyAppointments(employee_id, todays_date):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("select * from Appointments as a where a.e_id=? and a.date =?", (employee_id, todays_date))
    ret = c.fetchall()

    conn.close()
    return ret


def getPreviouslyTreatedAnimals(employee_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("select a.a_id from Appointments as a where a.e_id=?", (employee_id,))
    ret = c.fetchall()

    conn.close()
    return ret


def getPerformedProcedures(employee_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("select a.p_id from Appointments as a where a.e_id=?", (employee_id,))
    ret = c.fetchall()

    conn.close()
    return ret


def getUnpaidBills():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("select * from Payments as p where p.status = 'Unpaid'")
    ret = c.fetchall()

    conn.close()
    return ret


def getCommonProcedures():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''select p.p_name from Procedures as p group by count(
                  select * from Appointments as a where a.p_id = p.p_id)''')
    ret = c.fetchall()

    conn.close()
    return ret


def getAnimalsWithMostAppointments():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''select * from Animals as a group by count(
                  select * from Appointments as ap where a.a_id = ap.a_id)''')
    ret = c.fetchall()

    conn.close()
    return ret


def getOwnersWithMultAnimals():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute('''select * from Owners as o where count(
                      select * from Animals as a where a.o_id = o.o_id) > 1''')
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

