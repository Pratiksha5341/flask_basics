"""
Part 5: Mini Project - Personal Website with Flask
===================================================
A complete personal website using everything learned in Parts 1-4.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# =============================================================================
# YOUR DATA - Customize this section with your own information!
# =============================================================================

PERSONAL_INFO = {
    'name': 'Pratiksha',
    'title': 'Java Developer',
    'bio': 'A passionate developer learning Flask and web development.',
    'email': 'yamagrnikarpratiksha0504@gmail.com',
    'github': 'https://github.com/Pratiksha5341',
    'linkedin': 'https://www.linkedin.com/in/pratiksha-yamagrnikar-06849a307/',
}

SKILLS = [
    {'name': 'Python', 'level': 80},
    {'name': 'HTML/CSS', 'level': 85},
    {'name': 'Flask', 'level': 60},
    {'name': 'JavaScript', 'level': 50},
    {'name': 'SQL', 'level': 45},
    {'name': 'Java', 'level': 85},
]

PROJECTS = [
    {'id': 1, 'name': 'PMPML Website', 'description': 'A Flask-powered website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 2, 'name': 'Personal Website', 'description': 'A Flask-powered personal portfolio website.', 'tech': ['Python', 'Flask', 'HTML', 'CSS'], 'status': 'Completed'},
    {'id': 3, 'name': 'Todo App', 'description': 'A simple task management application.', 'tech': ['Python', 'Flask', 'SQLite'], 'status': 'In Progress'},
    {'id': 4, 'name': 'Weather Dashboard', 'description': 'Display weather data from an API.', 'tech': ['Python', 'Flask', 'API'], 'status': 'Planned'},

]

# Add blog posts data
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Getting Started with Flask',
        'content': 'Flask is a lightweight Python web framework that makes it easy to build web applications...',
        'date': '2024-01-15',
        'category': 'Tutorial',
        'author': 'Your Name'
    },
    {
        'id': 2,
        'title': 'Building Dynamic Routes in Flask',
        'content': 'Dynamic routes allow you to create flexible URL patterns that can accept parameters...',
        'date': '2024-01-22',
        'category': 'Web Development',
        'author': 'Your Name'
    },
    {
        'id': 3,
        'title': 'Working with Jinja2 Templates',
        'content': 'Jinja2 is a powerful templating engine for Python that allows you to create dynamic HTML pages...',
        'date': '2024-01-29',
        'category': 'Tutorial',
        'author': 'Your Name'
    }
]
# =============================================================================
# ROUTES
# =============================================================================

@app.route('/')
def home():
    return render_template('index.html', info=PERSONAL_INFO)


@app.route('/about')
def about():
    return render_template('about.html', info=PERSONAL_INFO, skills=SKILLS)


@app.route('/projects')
def projects():
    return render_template('projects.html', info=PERSONAL_INFO, projects=PROJECTS)


@app.route('/project/<int:project_id>')  # Dynamic route for individual project
def project_detail(project_id):
    project = None
    for p in PROJECTS:
        if p['id'] == project_id:
            project = p
            break
    return render_template('project_detail.html', info=PERSONAL_INFO, project=project, project_id=project_id)


@app.route('/contact')
def contact():
    return render_template('contact.html', info=PERSONAL_INFO)

@app.route('/blog')
def blog():
    return render_template('blog.html', 
                         posts=BLOG_POSTS, 
                         info=PERSONAL_INFO)

@app.route('/skill/<skill_name>')
def skill_projects(skill_name):
    # Filter projects that use this skill
    filtered_projects = []
    for project in PROJECTS:
        if skill_name.lower() in [tech.lower() for tech in project['tech']]:
            filtered_projects.append(project)
    
    return render_template('skill_projects.html',
                         skill_name=skill_name,
                         projects=filtered_projects,
                         info=PERSONAL_INFO)

@app.route('/skills')
def skills():
    # Get all unique skills from projects
    all_skills = []
    for project in PROJECTS:
        all_skills.extend(project['tech'])
    
    unique_skills = sorted(set(all_skills))
    
    return render_template('skills.html',
                         skills=unique_skills,
                         projects=PROJECTS,  # Make sure this is included!
                         info=PERSONAL_INFO)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    # Find the blog post by ID
    post = None
    for p in BLOG_POSTS:
        if p['id'] == post_id:
            post = p
            break
    
    return render_template('blog_post.html', 
                         post=post, 
                         post_id=post_id,
                         info=PERSONAL_INFO)

@app.route('/author/<author_name>')
def author_posts(author_name):
    # Filter posts by this author
    author_posts_list = []
    for post in BLOG_POSTS:
        if post['author'].lower() == author_name.lower():
            author_posts_list.append(post)
    
    return render_template('author_posts.html',
                         author_name=author_name,
                         posts=author_posts_list,
                         info=PERSONAL_INFO)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# PROJECT STRUCTURE:
# =============================================================================
#
# part-5/
# ├── app.py              <- You are here
# ├── static/
# │   └── style.css       <- CSS styles
# └── templates/
#     ├── base.html       <- Base template (inherited by all pages)
#     ├── index.html      <- Home page
#     ├── about.html      <- About page
#     ├── projects.html   <- Projects list
#     ├── project_detail.html <- Single project view
#     └── contact.html    <- Contact page
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 5.1: Personalize your website
#   - Update PERSONAL_INFO with your real information
#   - Add your actual skills and projects
#
# Exercise 5.2: Add a new page
#   - Create a /blog route
#   - Add blog posts data structure
#   - Create blog.html template
#
# Exercise 5.3: Enhance the styling
#   - Modify static/style.css
#   - Add your own color scheme
#   - Make it responsive for mobile
#
# Exercise 5.4: Add more dynamic features
#   - Create a /skill/<skill_name> route
#   - Show projects that use that skill
#
# =============================================================================
