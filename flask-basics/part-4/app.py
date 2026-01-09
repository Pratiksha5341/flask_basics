from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# Product database (simulated)
products = {
    1: {'name': 'Wireless Mouse', 'price': 29.99, 'category': 'electronics', 'description': 'Ergonomic wireless mouse with long battery life'},
    2: {'name': 'Python Book', 'price': 39.99, 'category': 'books', 'description': 'Learn Python programming from scratch'},
    3: {'name': 'Coffee Mug', 'price': 12.50, 'category': 'home', 'description': 'Ceramic mug with Python logo'},
    4: {'name': 'Laptop Stand', 'price': 45.00, 'category': 'electronics', 'description': 'Adjustable aluminum laptop stand'},
    5: {'name': 'Desk Lamp', 'price': 34.99, 'category': 'home', 'description': 'LED desk lamp with adjustable brightness'}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)
    return render_template('post.html', post_id=post_id, post=post)

@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/links')
def show_links():
    links = {
        'home': url_for('home'),
        'about': url_for('about'),
        'user_alice': url_for('user_profile', username='Alice'),
        'user_bob': url_for('user_profile', username='Bob'),
        'post_1': url_for('show_post', post_id=1),
        'post_2': url_for('show_post', post_id=2),
        'product_1': url_for('show_product', product_id=1),
        'category_electronics': url_for('category_product', category_name='electronics', product_id=1),
    }
    return render_template('links.html', links=links)

# Exercise 4.1: Product page route
@app.route('/product/<int:product_id>')
def show_product(product_id):
    product = products.get(product_id)
    return render_template('product.html', product_id=product_id, product=product)

# Exercise 4.2: Category and product route
@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):
    product = products.get(product_id)
    if product and product['category'] == category_name:
        return render_template('category_product.html', 
                             category_name=category_name, 
                             product_id=product_id, 
                             product=product)
    else:
        return render_template('category_product.html', 
                             category_name=category_name, 
                             product_id=product_id, 
                             product=None)

# Exercise 4.3: Search route
@app.route('/search/<query>')
def search_results(query):
    results = []
    for pid, product in products.items():
        # Skip coffee-related products
        if 'coffee' in product['name'].lower() or 'coffee' in product['description'].lower():
            continue
            
        if query.lower() in product['name'].lower() or query.lower() in product['description'].lower():
            results.append((pid, product))
    
    return render_template('search.html', query=query, results=results)

# Bonus: Search form handler
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form.get('search_query', '')
        return redirect(url_for('search_results', query=query))
    
    return render_template('search_form.html')

# Route to serve CSS file directly - FIXED FUNCTION NAME
@app.route('/style.css')
def serve_css():  # Changed from 'css' to 'serve_css'
    return app.send_static_file('style.css')

# Route for Products page
@app.route('/products')
def show_products():
    # Filter out coffee products if you want
    filtered_products = {pid: product for pid, product in products.items() if pid != 3}
    return render_template('products.html', products=filtered_products)

# Route for Product Categories page
@app.route('/categories')
def show_categories():
    # Get all unique categories from products (filter out coffee if needed)
    filtered_products = {pid: product for pid, product in products.items() if pid != 3}
    categories = set(product['category'] for product in filtered_products.values())
    return render_template('categories.html', 
                         categories=categories, 
                         products=filtered_products)

# Route for specific category products
@app.route('/category/<category_name>')
def show_category_products(category_name):
    # Get products in this category (excluding coffee if needed)
    filtered_products = {pid: product for pid, product in products.items() if pid != 3}
    category_products = {}
    for pid, product in filtered_products.items():
        if product['category'] == category_name:
            category_products[pid] = product
    return render_template('category_products.html', 
                         category_name=category_name, 
                         products=category_products)

# Debug route to check products data
@app.route('/debug/products')
def debug_products():
    return str(products)

# Debug route to check categories data  
@app.route('/debug/categories')
def debug_categories():
    filtered_products = {pid: product for pid, product in products.items() if pid != 3}
    categories = set(product['category'] for product in filtered_products.values())
    return str(list(categories))

if __name__ == '__main__':
    app.run(debug=True)