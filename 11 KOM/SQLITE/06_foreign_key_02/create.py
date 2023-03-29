import sqlite3

conn = sqlite3.connect("2602.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE customers(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        street TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL,
        credit_limit REAL NOT NULL)
    """)

cur.execute("""
    INSERT INTO customers(name, street, city, state, credit_limit) 
    VALUES 
    ("Pedro Augusto de Rocha", "Rua Pedro Carlos Hoffman", "Porto Alegre", "RS", 700.00),
    ("Antonio Carlos Mamel", "Av. Pinheiros", "Belo Horizonte", "MG", 3500.50),
    ("Luiza Augusta Mhor", "Rua Salto Grande", "Niteroi", "RJ", 4000.00),
    ("Jane Ester", "Av 7 de setembro", "Erechim", "RS", 800.00),
    ("Marcos Antônio dos Santos", "Av Farrapos", "Porto Alegre", "RS", 4250.25)
    """)
    
cur.execute("""
    SELECT name FROM customers WHERE state = "RS";
    """)

conn.commit()
conn.close()