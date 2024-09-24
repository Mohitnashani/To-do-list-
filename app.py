# from flask import Flask, render_template, request, redirect

# app = Flask(__name__)

# # A simple in-memory task list (use a database for real applications)
# tasks = []

# @app.route('/')
# def index():
#         return render_template('index.html', tasks=tasks)


# @app.route('/add', methods=['POST'])
# def add_task():
#     task = request.form.get('task')
#     if task:
#         tasks.append(task)
#         done :false
#     return redirect('/')


# @app.route('/finish', methods=['POST'])
# def finish_tasks():
#     global done
#     done = True  # Set the done flag to True when finishing
#     return redirect('/')


# @app.route('/delete/<int:task_id>')
# def delete_task(task_id):
#     if 0 <= task_id < len(tasks):
#         tasks.pop(task_id)
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    due_date = request.form.get('due_date')
    priority = request.form.get('priority')
    
    if task_name and due_date and priority:
        tasks.append({
            'task_name': task_name,
            'due_date': due_date,
            'priority': priority,
            'done': False  
        })
    
    return redirect('/')

@app.route('/finish/<int:task_id>', methods=['POST'])
def finish_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True  
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
