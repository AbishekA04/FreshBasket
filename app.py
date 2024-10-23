

app = Flask(__name__)

# Route for Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Route for Shop Page
@app.route('/shop')
def shop():
    return render_template('shop.html')

# Route for Cart Page
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Route for Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for Register Page
@app.route('/register')
def register():
    return render_template('register.html')

# Route for Admin Dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Route for User Dashboard
@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

# Route for Items Page (shows detailed view of an item)
@app.route('/item/<int:item_id>')
def item(item_id):
    # In a real application, you'd fetch item details from a database
    # For simplicity, we're using a dictionary to represent item details
    items = {
        1: {'name': 'Fresh Apples', 'price': '$2.50 / kg', 'description': 'Crisp and sweet apples perfect for snacking or baking.'},
        2: {'name': 'Organic Bananas', 'price': '$1.20 / kg', 'description': 'Delicious, naturally ripened bananas, full of flavor and nutrients.'}
    }
    
    item_details = items.get(item_id, None)
    if item_details:
        return render_template('items.html', item=item_details)
    else:
        return "Item not found", 404

if __name__ == "__main__":
    app.run(debug=True)
