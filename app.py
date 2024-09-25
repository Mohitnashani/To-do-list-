
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'username'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'todotask'

tasks = []

@app.route('/')
def index():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    due_date = request.form.get('due_date')
    priority = request.form.get('priority')
    
    if task_name and due_date and priority:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO tasks (task_name, due_date, priority) VALUES (%s, %s, %s)", 
                       (task_name, due_date, priority))
        mysql.connection.commit()
        tasks.append({
            'task_name': task_name,
            'due_date': due_date,
            'priority': priority,
            'done': False  
        })
    
    return redirect('/')

@app.route('/finish/<int:task_id>', methods=['POST'])
def finish_task(task_id):
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE tasks SET done = TRUE WHERE id = %s", (task_id,))
    mysql.connection.commit()
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True  
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    mysql.connection.commit()
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

