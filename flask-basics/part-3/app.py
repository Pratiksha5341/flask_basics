from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    student_name = "Pratiksha"
    return render_template('index.html', name=student_name)  # Pass variable to template as {{ name }}


@app.route('/profile')
def profile():
    return render_template('profile.html',
        name='Pratiksha',
        age=22,
        course='Web Development',
        is_enrolled=True,
        email='pratiksha@example.com',
        city='Pune'
)

@app.route('/skills')
def skills():
    programming_skills = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']
    return render_template('skills.html', skills=programming_skills)  # Pass list to loop through in template


@app.route('/projects')
def projects():
    project_list = [
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript'},
    ]

    return render_template('projects.html', projects=project_list)


@app.route('/grades')
def grades():
    grades_data = {
        'Mathematics': 'A',
        'Python Programming': 'A+',
        'Web Development': 'A',
        'Data Structures': 'B+',
        'Machine Learning': 'A'
    }

    return render_template('grades.html', grades=grades_data)

if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# JINJA2 SYNTAX QUICK REFERENCE:
# =============================================================================
#
# {{ variable }}          - Output a variable
# {{ variable|upper }}    - Use a filter (uppercase)
# {{ variable|default('N/A') }} - Default value if variable is empty
#
# {% if condition %}      - If statement
#   ...
# {% endif %}
#
# {% for item in list %}  - For loop
#   {{ item }}
# {% endfor %}
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 3.1: Add more data
#   - Add more fields to the profile (email, city, etc.)
#   - Display them in profile.html
#
# Exercise 3.2: Conditional display
#   - In profile.html, show "Enrolled" or "Not Enrolled" based on is_enrolled
#   - Use {% if is_enrolled %} ... {% else %} ... {% endif %}
#
# Exercise 3.3: Create a grades page
#   - Create a new route /grades
#   - Pass a dictionary of subjects and grades
#   - Display them in a table using a for loop
#
# =============================================================================
