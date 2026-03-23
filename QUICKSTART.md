# Quick Start Guide

## Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: `http://localhost:5000`

---

## Running Playwright Tests

### Install Playwright (first time only)
```bash
pip install playwright pytest
playwright install
```

### Run All Tests
```bash
pytest test_insurance_app.py -v
```

### Run Specific Test
```bash
pytest test_insurance_app.py::TestInsuranceApplication::test_home_page_loads -v
```

### Run with Output
```bash
pytest test_insurance_app.py -v -s
```

---

## Project Structure Overview

```
insuranceapplication/
├── app.py                    # Flask app with all routes
├── requirements.txt          # Python packages
├── README.md                 # Full documentation
├── test_insurance_app.py     # Playwright test suite
├── .gitignore               # Git ignore file
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── index.html          # Home
│   ├── step1.html          # Personal Info
│   ├── step2.html          # Line of Business
│   ├── step3.html          # Coverage Selection
│   ├── step4.html          # Premium Calc
│   ├── step5.html          # Policy Cert
│   └── completion.html     # Completion
├── static/
│   ├── css/
│   │   └── style.css       # All styling
│   └── js/
│       └── form-validation.js  # Client-side logic
└── uploads/                # File uploads (auto-created)
```

---

## Common Tasks

### Change Port
Edit `app.py` last line:
```python
app.run(debug=True, port=5001)  # Use 5001 instead of 5000
```

### Modify Premium Calculations
Edit `app.py` constants:
- `COVERAGE_PREMIUMS` - Coverage prices
- `LINE_OF_BUSINESS_BASE` - Base prices
- `COVERAGE_TYPES` - Multipliers

### Write Your Own Tests
Use the test IDs provided in each form element:
```python
page.fill('[data-testid="full_name_input"]', 'Your Name')
page.select_option('[data-testid="line_of_business_select"]', 'auto')
page.check('[data-testid="coverage_liability_coverage"]')
```

---

## Troubleshooting

**Port 5000 already in use?**
- Change port in `app.py`
- Or: `lsof -i :5000` (macOS/Linux) then `kill -9 <PID>`

**Module not found error?**
- Activate virtual environment: `source venv/bin/activate`
- Install requirements: `pip install -r requirements.txt`

**CSS/JS not loading?**
- Clear browser cache (Ctrl+Shift+Delete or Cmd+Shift+Delete)
- Check static file paths in templates

**Tests failing?**
- Ensure Flask app is running on port 5000
- Check test IDs match the templates
- Review Playwright documentation

---

## Next Steps

1. ✅ Start the Flask app
2. ✅ Navigate through all steps manually
3. ✅ Review the test examples in `test_insurance_app.py`
4. ✅ Run tests with Playwright
5. ✅ Create your own test cases
6. ✅ Practice different Playwright selectors and actions

Happy testing! 🚀
