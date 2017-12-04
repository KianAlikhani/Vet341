import sqlite3

conn = sqlite3.connect('test.db')

c = conn.cursor()

c.execute('''CREATE TABLE Owners(
  o_id real primary key, o_name text, o_address text, phone_number real)
''')

c.execute('''CREATE TABLE Animals
( a_id real primary key, o_id real, a_name text, type text, breed text, foreign key(o_id) references Owners(o_id))
''')

c.execute('''CREATE TABLE Employees
( e_id real primary key, e_name text, e_type text)
''')

c.execute('''CREATE TABLE Procedures
( p_id real primary key, p_name text)
''')

c.execute('''CREATE TABLE Offices
( office_id real primary key, address text, manager_name text)
''')

c.execute('''CREATE TABLE Payments
( r_id real primary key, o_id real, status text, amount real, method text, date real, foreign key(o_id) references Owners(o_id))
''')

c.execute('''CREATE TABLE Appointments
( a_id real not null, e_id real not null, date real not null, time real not null, p_id real, office_id real,
  primary key(a_id, e_id, date, time),
  foreign key(a_id) references Animals(a_id), foreign key (e_id) references Employees(e_id), 
  foreign key(p_id) references Procedures(p_id), foreign key(office_id) references Offices(office_id))
''')

conn.commit()

conn.close()