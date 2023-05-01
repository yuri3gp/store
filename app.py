from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT,
                    address TEXT
                    );""")
    conn.commit()
    cursor.execute('SELECT * FROM customers')
    data = cursor.fetchall()
    conn.close()
    return render_template('index.html', data=data)


@app.route('/enviar', methods=['POST'])
def enviar():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    dados = request.form
    sql = '''INSERT INTO customers (first_name, last_name, email, phone, address)
            VALUES (?, ?, ?, ?, ?)'''
    cursor.execute(sql, (dados['first_name'], dados['last_name'], dados['email'], dados['phone'], dados['address']))
    conn.commit()
    conn.close()
    return dados


if __name__ == '__main__':
    app.run(debug=True)
