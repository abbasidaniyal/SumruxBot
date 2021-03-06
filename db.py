
import sqlite3


class DB:
    def __init__(self, dbname="details.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS INFO(city text, pincode integer, req text, standard text, board text, medium text, subjects text, contact integer, email text, details text, confirm text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self, City, Pincode, Req, Standard, Board, Medium, Subjects, Contact, Email, Details, Confirm):
        stmt = "INSERT INTO INFO (city, pincode, req, standard, board, medium, subjects, contact, email, details, confirm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        args = (City, Pincode, Req, Standard, Board, Medium, Subjects, Contact, Email, Details, Confirm)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_item(self, item_text):
        stmt = "DELETE FROM items WHERE description = (?)"
        args = (item_text, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_items(self):
        stmt = "SELECT City, Pincode, Req, Standard, Board, Medium, Subjects, Contact, Email, Details, Confirm FROM INFO"
        return [x[0] for x in self.conn.execute(stmt)]