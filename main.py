from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crm.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    accounts = conn.execute('SELECT * FROM accounts').fetchall()
    conn.close()
    return render_template('index.html', accounts=accounts)

if __name__ == '__main__':
    # ensure Flask listens on all interfaces
    app.run(host='0.0.0.0', port=3000, debug=True)

