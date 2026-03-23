from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import os
from werkzeug.utils import secure_filename
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-for-insurance-app'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create uploads folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Login credentials
VALID_CREDENTIALS = {
    'loga-automation': 'test1234'
}

# Login required decorator
def login_required(f):
    """Decorator to require login for routes"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Premium calculation configuration
COVERAGE_PREMIUMS = {
    'Liability Coverage': 150,
    'Collision Coverage': 200,
    'Comprehensive Coverage': 180,
    'Medical Payments': 100,
    'Uninsured Motorist': 120
}

LINE_OF_BUSINESS_BASE = {
    'auto': 600,
    'home': 800,
    'health': 500,
    'life': 400
}

COVERAGE_TYPES = {
    'Basic Coverage': 0.8,
    'Standard Coverage': 1.0,
    'Premium Coverage': 1.3
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validate credentials
        if username in VALID_CREDENTIALS and VALID_CREDENTIALS[username] == password:
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password')
    
    # If already logged in, redirect to home
    if 'user' in session:
        return redirect(url_for('index'))
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Logout and clear session"""
    session.clear()
    return redirect(url_for('login'))


@app.route('/')
@login_required
def index():
    """Home page"""
    return render_template('index.html')


@app.route('/step1', methods=['GET', 'POST'])
@login_required
def step1():
    """Step 1: Personal Information"""
    if request.method == 'POST':
        session['full_name'] = request.form.get('full_name')
        session['address'] = request.form.get('address')
        session['age'] = request.form.get('age')
        return redirect(url_for('step2'))
    
    return render_template('step1.html')


@app.route('/step2', methods=['GET', 'POST'])
@login_required
def step2():
    """Step 2: Line of Business and Coverage Type Selection"""
    if request.method == 'POST':
        session['line_of_business'] = request.form.get('line_of_business')
        session['coverage_type'] = request.form.get('coverage_type')
        return redirect(url_for('step3'))
    
    if 'full_name' not in session:
        return redirect(url_for('step1'))
    
    return render_template('step2.html')


@app.route('/step3', methods=['GET', 'POST'])
@login_required
def step3():
    """Step 3: Coverage Selection and Document Upload"""
    if request.method == 'POST':
        # Get selected coverages
        coverages = []
        for coverage in COVERAGE_PREMIUMS.keys():
            if request.form.get(coverage):
                coverages.append(coverage)
        session['coverages'] = coverages
        
        # Handle file upload
        if 'document' in request.files:
            file = request.files['document']
            if file and file.filename != '':
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                session['document'] = filename
        
        return redirect(url_for('step4'))
    
    if 'line_of_business' not in session:
        return redirect(url_for('step2'))
    
    user_data = {
        'full_name': session.get('full_name'),
        'age': session.get('age'),
        'address': session.get('address'),
        'line_of_business': session.get('line_of_business')
    }
    
    return render_template('step3.html', coverages=COVERAGE_PREMIUMS.keys(), user_data=user_data)


@app.route('/step4', methods=['GET', 'POST'])
@login_required
def step4():
    """Step 4: Premium Calculation"""
    if request.method == 'POST':
        selected_payment = request.form.get('payment_option')
        session['payment_option'] = selected_payment
        return redirect(url_for('step5'))
    
    if 'coverages' not in session:
        return redirect(url_for('step3'))
    
    # Calculate premium
    base_premium = LINE_OF_BUSINESS_BASE.get(session.get('line_of_business', 'auto'), 600)
    coverage_multiplier = COVERAGE_TYPES.get(session.get('coverage_type', 'Standard Coverage'), 1.0)
    
    # Age discount/surcharge
    age = int(session.get('age', 30))
    if age < 25:
        age_factor = 1.15  # 15% increase for young drivers/buyers
    elif age > 65:
        age_factor = 1.10  # 10% increase for seniors
    else:
        age_factor = 1.0
    
    # Calculate selected coverage premiums
    selected_coverages = session.get('coverages', [])
    coverage_premium = sum([COVERAGE_PREMIUMS.get(cov, 0) for cov in selected_coverages])
    
    # Total calculation
    base_with_type = base_premium * coverage_multiplier
    total_premium = (base_with_type + coverage_premium) * age_factor
    
    premium_data = {
        'base_premium': round(base_premium, 2),
        'coverage_multiplier': coverage_multiplier,
        'age_factor': age_factor,
        'coverage_premium': round(coverage_premium, 2),
        'annual_premium': round(total_premium, 2),
        'monthly_payment': round(total_premium / 12, 2),
        'quarterly_payment': round(total_premium / 4, 2),
        'selected_coverages': selected_coverages
    }
    
    session['premium_data'] = premium_data
    
    return render_template('step4.html', premium_data=premium_data, user_data={
        'age': session.get('age'),
        'line_of_business': session.get('line_of_business'),
        'coverage_type': session.get('coverage_type')
    })


@app.route('/step5', methods=['GET', 'POST'])
@login_required
def step5():
    """Step 5: Policy Issuance"""
    if request.method == 'POST':
        return redirect(url_for('completion'))
    
    if 'premium_data' not in session:
        return redirect(url_for('step4'))
    
    # Generate policy number
    policy_number = f"POL{datetime.now().strftime('%Y%m%d%H%M%S')}"
    session['policy_number'] = policy_number
    
    policy_data = {
        'policy_number': policy_number,
        'issue_date': datetime.now().strftime('%B %d, %Y'),
        'full_name': session.get('full_name'),
        'age': session.get('age'),
        'address': session.get('address'),
        'line_of_business': session.get('line_of_business'),
        'coverage_type': session.get('coverage_type'),
        'coverages': session.get('coverages', []),
        'annual_premium': session.get('premium_data', {}).get('annual_premium', 0),
        'payment_option': session.get('payment_option', 'Annual Payment')
    }
    
    return render_template('step5.html', policy_data=policy_data)


@app.route('/completion')
@login_required
def completion():
    """Completion page"""
    return render_template('completion.html')


@app.route('/get-premium-breakdown')
def get_premium_breakdown():
    """API endpoint for premium breakdown"""
    if 'premium_data' in session:
        return jsonify(session['premium_data'])
    return jsonify({})


if __name__ == '__main__':
    # For local development: use port 5001
    # For production (Render): uses PORT environment variable via gunicorn
    import os
    port = int(os.environ.get('PORT', 5001))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
