#!/bin/bash
# Render Deployment Pre-flight Checklist

echo "🚀 Insurance Practice Application - Render Deployment Checklist"
echo "================================================================"
echo ""

# Check files
echo "✓ Checking required files..."
FILES=("Procfile" "runtime.txt" "requirements.txt" ".gitignore" "app.py")
for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✓ $file exists"
    else
        echo "  ✗ $file MISSING - Required for deployment"
    fi
done

echo ""
echo "✓ Checking directories..."
DIRS=("templates" "static/css" "static/js")
for dir in "${DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo "  ✓ $dir exists"
    else
        echo "  ✗ $dir MISSING - Required for deployment"
    fi
done

echo ""
echo "✓ Checking critical templates..."
TEMPLATES=("login.html" "base.html" "index.html" "step1.html" "step2.html" "step3.html" "step4.html" "step5.html" "completion.html")
for template in "${TEMPLATES[@]}"; do
    if [ -f "templates/$template" ]; then
        echo "  ✓ templates/$template"
    else
        echo "  ✗ templates/$template MISSING"
    fi
done

echo ""
echo "✓ Checking static files..."
if [ -f "static/css/style.css" ]; then
    echo "  ✓ static/css/style.css"
else
    echo "  ✗ static/css/style.css MISSING"
fi

if [ -f "static/css/login.css" ]; then
    echo "  ✓ static/css/login.css"
else
    echo "  ✗ static/css/login.css MISSING"
fi

if [ -f "static/js/form-validation.js" ]; then
    echo "  ✓ static/js/form-validation.js"
else
    echo "  ✗ static/js/form-validation.js MISSING"
fi

if [ -f "static/js/login.js" ]; then
    echo "  ✓ static/js/login.js"
else
    echo "  ✗ static/js/login.js MISSING"
fi

echo ""
echo "✓ Checking requirements..."
if grep -q "Flask" requirements.txt; then
    echo "  ✓ Flask in requirements.txt"
fi
if grep -q "gunicorn" requirements.txt; then
    echo "  ✓ gunicorn in requirements.txt"
fi
if grep -q "Werkzeug" requirements.txt; then
    echo "  ✓ Werkzeug in requirements.txt"
fi

echo ""
echo "✓ Checking Procfile..."
if grep -q "gunicorn app:app" Procfile; then
    echo "  ✓ Procfile has correct format"
else
    echo "  ✗ Procfile format incorrect"
fi

echo ""
echo "✓ Checking runtime.txt..."
if [ -s runtime.txt ]; then
    echo "  ✓ runtime.txt contains Python version: $(cat runtime.txt)"
else
    echo "  ✗ runtime.txt is empty"
fi

echo ""
echo "📋 Deployment Checklist:"
echo "  ☐ All files checked above are present"
echo "  ☐ Code committed to Git (git add . && git commit -m 'message')"
echo "  ☐ Repository pushed to GitHub (git push -u origin main)"
echo "  ☐ Render account created (https://render.com)"
echo "  ☐ GitHub connected to Render"
echo "  ☐ Web Service created on Render"
echo "  ☐ Build command: pip install -r requirements.txt"
echo "  ☐ Start command: gunicorn app:app"
echo ""
echo "🔐 Default Credentials:"
echo "  Username: loga-automation"
echo "  Password: test1234"
echo ""
echo "📖 For detailed instructions, see RENDER_DEPLOYMENT.md"
echo ""
echo "✅ All checks complete!"
echo ""
