# Insurance Practice Application

A comprehensive Flask-based insurance application designed for practicing **Playwright automation testing**. This application implements a complete multi-step insurance policy creation workflow with various UI elements to test.

## 🎯 Features

### Step-by-Step Workflow
- **Step 1**: Personal Information (TextBox, TextArea, Buttons)
- **Step 2**: Line of Business & Coverage Type (ListBox, Radio Buttons)
- **Step 3**: Coverage Selection & Document Upload (Checkboxes, File Upload, Tables)
- **Step 4**: Premium Calculation (Tables, Dynamic Data)
- **Step 5**: Policy Certificate (Tables, Summary, Links)

### UI Elements for Testing
- ✓ TextBox inputs
- ✓ TextArea
- ✓ Select dropdowns (ListBox)
- ✓ Radio buttons
- ✓ Checkboxes
- ✓ File upload
- ✓ Web tables
- ✓ Buttons & Links
- ✓ Forms with validation
- ✓ Navigation between steps

### Automation-Friendly Features
- All form elements have `data-testid` attributes
- Consistent naming conventions
- Clear error messages
- Real-time form validation
- Session-based data persistence
- Responsive design

### Security & Authentication
- ✓ Login page with credentials validation
- ✓ Session-based authentication on all steps
- ✓ Logout functionality
- ✓ Protected routes (login required)

### Cloud Deployment Ready
- ✓ Production-ready with Gunicorn
- ✓ Deploy to Render, Heroku, or similar in minutes
- ✓ Environment-based configuration
- ✓ Static file serving optimized

## 🌐 Live Demo & Deployment

### Option 1: Run Locally (Development)
```bash
python3 app.py
# Access at http://localhost:5001
```

### Option 2: Deploy to Render (Production)
Deploy for free on Render and access from anywhere on the internet!

**See:** [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for step-by-step instructions.

**Quick Deploy:**
1. Push code to GitHub
2. Connect to Render
3. Deploy in 2-3 minutes
4. Share live URL with team

### Login Credentials (All Environments)
| Field | Value |
|-------|-------|
| **Username** | `loga-automation` |
| **Password** | `test1234` |

## 📋 Requirements

- Python 3.8+
- Flask 2.3.2+
- Modern web browser

## 🚀 Installation & Setup

### 1. Clone or Download the Application
```bash
cd /path/to/insuranceapplication
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## 🧪 Playwright Testing Guide

### Sample Test Cases

#### Test 1: Complete the full workflow
```python
from playwright.sync_api import sync_playwright

def test_complete_insurance_workflow():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:5000")
        
        # Step 1: Fill personal information
        page.fill('[data-testid="full_name_input"]', 'John Doe')
        page.fill('[data-testid="age_input"]', '30')
        page.fill('[data-testid="address_textarea"]', '123 Main Street, Anytown, USA')
        page.click('[data-testid="step1_submit_btn"] >> text=Next Step')
        
        # Step 2: Select line of business
        page.select_option('[data-testid="line_of_business_select"]', 'auto')
        page.click('[data-testid="coverage_type_standard"]')
        page.click('[data-testid="step2_submit_btn"] >> text=Next Step')
        
        # Step 3: Select coverages
        page.check('[data-testid="coverage_liability_coverage"]')
        page.check('[data-testid="coverage_collision_coverage"]')
        page.click('[data-testid="step3_submit_btn"] >> text=Next Step')
        
        # Step 4: Select payment option
        page.click('[data-testid="payment_annual"]')
        page.click('[data-testid="step4_submit_btn"] >> text=Issue Policy')
        
        # Step 5: Complete application
        page.click('[data-testid="step5_complete_btn"] >> text=Complete Application')
        
        # Verify success
        assert page.locator('text=Practice Application Complete!').is_visible()
        
        browser.close()
```

#### Test 2: Validate form inputs
```python
def test_form_validation():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:5000/step1")
        
        # Try to submit empty form
        page.click('button:has-text("Next Step")')
        
        # Verify error messages appear
        assert page.locator('text=Full name is required').is_visible()
        assert page.locator('text=Age is required').is_visible()
        
        browser.close()
```

#### Test 3: Test coverage selection
```python
def test_coverage_selection():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:5000")
        
        # Navigate to step 3
        # ... (fill steps 1 & 2)
        
        # Verify all coverage options are available
        coverages = [
            'coverage_liability_coverage',
            'coverage_collision_coverage',
            'coverage_comprehensive_coverage',
            'coverage_medical_payments',
            'coverage_uninsured_motorist'
        ]
        
        for coverage in coverages:
            checkbox = page.locator(f'[data-testid="{coverage}"]')
            assert checkbox.is_visible()
        
        browser.close()
```

## 📁 Project Structure

```
insuranceapplication/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── form-validation.js  # Form validation & interactions
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   ├── step1.html        # Personal Information
│   ├── step2.html        # Line of Business Selection
│   ├── step3.html        # Coverage Selection
│   ├── step4.html        # Premium Calculation
│   ├── step5.html        # Policy Certificate
│   └── completion.html   # Completion page
└── uploads/              # File upload directory (created automatically)
```

## 🔍 Test IDs Reference

All form elements have consistent `data-testid` attributes:

### Step 1 - Personal Information
- `full_name_input` - Full name textbox
- `age_input` - Age input field
- `address_textarea` - Address textarea
- `step1_submit_btn` - Submit button
- `information_summary_table` - Summary table

### Step 2 - Line of Business
- `line_of_business_select` - Line of business dropdown
- `coverage_type_radios` - Radio button group
- `coverage_type_basic` - Basic coverage radio
- `coverage_type_standard` - Standard coverage radio
- `coverage_type_premium` - Premium coverage radio
- `step2_submit_btn` - Submit button

### Step 3 - Coverage Selection
- `coverage_checkboxes` - Checkbox group
- `coverage_liability_coverage` - Liability checkbox
- `coverage_collision_coverage` - Collision checkbox
- `coverage_comprehensive_coverage` - Comprehensive checkbox
- `coverage_medical_payments` - Medical payments checkbox
- `coverage_uninsured_motorist` - Uninsured motorist checkbox
- `document_upload` - File upload input
- `information_summary_table` - Summary table
- `step3_submit_btn` - Submit button

### Step 4 - Premium Calculation
- `premium_details_table` - Premium table
- `premium_lob` - Line of business display
- `premium_age_factor` - Age factor display
- `premium_coverages` - Coverages display
- `premium_annual` - Annual premium display
- `payment_options` - Payment options group
- `payment_monthly` - Monthly payment radio
- `payment_quarterly` - Quarterly payment radio
- `payment_annual` - Annual payment radio
- `monthly_amount` - Monthly amount display
- `quarterly_amount` - Quarterly amount display
- `annual_amount` - Annual amount display
- `step4_submit_btn` - Submit button

### Step 5 - Policy Certificate
- `policy_success_message` - Success message
- `certificate_policy_number` - Policy number
- `certificate_issue_date` - Issue date
- `policyholder_info_table` - Policyholder table
- `policy_details_table` - Policy details table
- `cert_name` - Policyholder name
- `cert_age` - Policyholder age
- `cert_address` - Policyholder address
- `cert_lob` - Line of business
- `cert_coverage_type` - Coverage type
- `cert_coverages` - Selected coverages
- `cert_premium` - Premium amount
- `policy_terms` - Terms list
- `next_steps` - Next steps list
- `step5_complete_btn` - Complete button

## 💡 Testing Tips

1. **Use data-testid attributes**: All form elements have `data-testid` for reliable selector identification
2. **Test IDs are lowercase with underscores**: Easy to remember and type
3. **Form validation**: The app validates inputs before submission
4. **Session persistence**: Data persists across steps using Flask sessions
5. **File uploads**: Test file upload with various formats (PDF, DOC, TXT, JPG, PNG)
6. **Navigation**: Test both "Next" and "Previous" buttons to verify navigation
7. **Error handling**: Test invalid inputs to see error messages

## 🔧 Configuration

### Premium Calculation
Edit `app.py` to modify premium calculations:
- `COVERAGE_PREMIUMS` - Coverage option prices
- `LINE_OF_BUSINESS_BASE` - Base premiums by line
- `COVERAGE_TYPES` - Multipliers for coverage types

### File Upload Settings
- Max file size: 16MB
- Allowed formats: PDF, DOC, DOCX, TXT, JPG, PNG
- Upload directory: `uploads/`

## 📝 Notes

- The application uses Flask sessions, so clearing browser cookies will reset progress
- File uploads are stored in the `uploads/` directory
- All data is in-memory (no database) - restarting the app clears all data
- Perfect for automation testing practice - no need to deal with complex backend logic

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in app.py
app.run(debug=True, port=5001)  # Use different port
```

### Module Not Found
```bash
# Make sure you're in the virtual environment
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### CSS/JS Not Loading
- Clear browser cache
- Make sure static files are in the correct directory structure
- Check browser console for 404 errors

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Playwright Documentation](https://playwright.dev/)
- [HTML Forms](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)

## 📄 License

This application is created for educational and testing purposes.

---

Happy testing! 🚀
