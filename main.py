from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = '<mysql ???>'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '<???>'
app.config['MYSQL_DB'] = 'DB'

mysql = MySQL(app)


@app.route('/users', methods=['GET'])
def get_items():
   cur = mysql.connection.cursor()
   cur.execute("SELECT * FROM <???>")
   rv = cur.fetchall()
   payload = []
   content = {}
   for result in rv:
      content = {'id': result[0], 'username': result[1], 'password': result[2]}
      payload.append(content)
      content = {}
   return jsonify(payload) 

if __name__ == '__main__':
    app.run()
