"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configure Jinja2 to trim whitespace automatically
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Sample data - your tasks list
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

@app.route('/')
def index():
    """Home page - display all tasks"""
    return render_template('index.html', tasks=TASKS)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    """Page with a form to add new task"""
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        status = request.form.get('status')
        priority = request.form.get('priority')
        
        # Generate new ID
        new_id = max(task['id'] for task in TASKS) + 1 if TASKS else 1
        
        # Create new task
        new_task = {
            'id': new_id,
            'title': title,
            'status': status,
            'priority': priority
        }
        
        # Add to tasks list
        TASKS.append(new_task)
        
        # Redirect to home page
        return redirect(url_for('index'))
    
    return render_template('add.html')

@app.route('/task/<int:id>')
def view_task(id):
    """View single task details"""
    # Find the task with the given id
    task = next((task for task in TASKS if task['id'] == id), None)
    
    if task is None:
        return "Task not found", 404
    
    return render_template('task.html', task=task)

@app.route('/about')
def about():
    """About the app page"""
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)