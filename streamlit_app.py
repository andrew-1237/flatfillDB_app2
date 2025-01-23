import streamlit as st

st.title("🎈 My new app")


class Record:
    def __init__(self,id,forename,surname,AGE,email):
        self.id = id
        self.forename = forename
        self.surname = surname
        self.AGE = AGE
        self.email = email

    def to_csv(self):
        return f"{self.id},{self.forename},{self.surname},{self.AGE},{self.email}"

class FlatFileDB:
    def __init__(self,filename):
        self.filename = filename

    def save_record(self,record):
        with open(self.filename, "a") as file:
            file.write(record.to_csv()+"\n")

    def read_records (self):
        with open(self.filename, "r") as file:
            return [line.strip().split(",") for line in file]

    def delete_record(self,record_id):
            record = self.read_records()
            records = [record for record in record if record[0] != str(record_id)]
            with open(self.filename, "w") as file:
                for record in records:
                    file.write(",".join(record)+"\n")


db = FlatFileDB("database.txt")


record1 = Record(1, "Alice", "Smith", 30, "alice@example.com")
record2 = Record(2, "Bob", "Brown", 25, "bob@example.com")
record3 = Record(3, "dima", "vasalasky", 18, "dima@example.com")
db.save_record(record1)
db.save_record(record2)
db.save_record(record3)

records = db.read_records()
st.write("Records in the database:")
for rec in records:
    st.write(rec)



deleter = st.radio("Please choose Login or New User", [":rainbow[yes]", ":rainbow[no]"])
if deleter == ":rainbow[yes]":
    usersdelat = st.number_input("what user do you want to delete")
    db.delete_record(usersdelat)
    st.write("Updated records:")
    records = db.read_records()
    for rec in records:
    st.write(rec)

