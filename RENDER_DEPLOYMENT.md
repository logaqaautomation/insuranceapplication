# Deploying to Render

Complete step-by-step guide to deploy the Insurance Practice Application to Render.

## Prerequisites

1. **GitHub Account** - Required to connect your repository
2. **Render Account** - Free at https://render.com
3. **Git installed** - For version control
4. **Application code** - All files committed to GitHub

## Step 1: Prepare Your Repository

### 1.1 Initialize Git (if not already done)
```bash
cd /path/to/insuranceapplication
git init
git add .
git commit -m "Initial commit: Insurance Practice Application"
```

### 1.2 Create `.gitignore` (Already done ✓)
The `.gitignore` file prevents uploading unnecessary files.

### 1.3 Verify Required Files
Ensure these files exist:
- ✓ `Procfile` - Defines how to run the app
- ✓ `runtime.txt` - Specifies Python version
- ✓ `requirements.txt` - Python dependencies
- ✓ `.gitignore` - Ignores unnecessary files
- ✓ `app.py` - Main Flask application
- ✓ `templates/` - HTML templates
- ✓ `static/` - CSS and JS files

## Step 2: Push to GitHub

### 2.1 Create GitHub Repository
1. Go to https://github.com/new
2. Create new repository (e.g., `insurance-practice-app`)
3. **Do NOT** initialize with README/gitignore

### 2.2 Push Code to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/insurance-practice-app.git
git branch -M main
git push -u origin main
```

Note: Replace `YOUR_USERNAME` with your actual GitHub username.

## Step 3: Deploy on Render

### 3.1 Connect GitHub to Render
1. Go to https://render.com and sign up (free tier available)
2. Click **Dashboards** → **New +** → **Web Service**
3. Click **Connect repository**
4. Authorize GitHub access
5. Select your repository

### 3.2 Configure Deployment Settings

In the Render dashboard, configure:

| Setting | Value |
|---------|-------|
| **Name** | `insurance-practice-app` (or your choice) |
| **Environment** | Python 3 |
| **Region** | Select closest to you |
| **Branch** | main |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | Free |

### 3.3 Advanced Settings (Optional)
- **Auto-Deploy** → Enable to auto-deploy on git push
- **Environment Variables** → None needed for this app

### 3.4 Create Web Service
Click **Create Web Service** and wait for deployment (~2 minutes).

## Step 4: Access Your Application

Once deployed, Render will provide a URL like:
```
https://insurance-practice-app-xxxxx.onrender.com
```

### Login Credentials
- **Username:** `loga-automation`
- **Password:** `test1234`

## Step 5: Test the Application

1. Open the URL in browser
2. You should see the login page
3. Login with the provided credentials
4. Test the full workflow (all 5 steps)
5. Verify all features work correctly

## Troubleshooting

### Issue: "Application failed to start"
**Solution:**
- Check logs in Render dashboard
- Verify all required files exist
- Ensure Python 3.11 compatibility

### Issue: "502 Bad Gateway"
**Solution:**
- Application may still be loading (takes 1-2 minutes)
- Check if uploads folder is causing issues
- Verify `Procfile` has correct format

### Issue: "404 - Page Not Found"
**Solution:**
- Clear browser cache
- Verify URL is correct
- Check that all routes are accessible

### Issue: "Static files not loading (CSS/JS)"
**Solution:**
1. Ensure `static/` directory structure is correct
2. Verify paths in templates use `url_for()`
3. Render automatically serves static files from `static/` folder

## Important Notes

### Port Configuration
- ✓ App automatically uses PORT environment variable
- ✓ Works on both local (5001) and Render (auto-assigned)
- ✓ Do NOT hardcode port 5000 (conflicts with Render)

### Session Management
- Flask session data is stored in memory
- Redeploying clears all sessions
- Users will need to login again

### File Uploads
- Uploaded files are stored in `uploads/` folder
- Files persist as long as dyno is running
- **WARNING**: Files are deleted when dyno restarts/redeploys
- For persistent storage, use Render Disk or external storage

### Database Alternative
For persistent data:
1. Consider adding a database (PostgreSQL on Render)
2. Replace file uploads with database storage
3. Store premium calculations in DB instead of session

## Continuous Deployment

### Auto-Deploy on GitHub Push
1. In Render dashboard → [Your Service] → **Settings**
2. Under "Deploy hooks", enable auto-deploy
3. Any push to `main` branch triggers deployment

### Manual Redeployment
1. Render Dashboard → [Your Service]
2. Click **Manual Deployment** → **Redeploy**

## Monitoring & Logs

### View Application Logs
1. Render Dashboard → [Your Service] → **Logs**
2. See real-time application output
3. Check for errors and debug information

### Monitoring
- **Render Dashboard** shows:
  - CPU usage
  - Memory usage
  - Request logs
  - Error tracking

## Scaling & Performance

### Current Free Tier
- Suitable for demo/testing
- Auto-suspends after 15 minutes of inactivity
- Limited resources but adequate for this app

### Upgrade to Paid (if needed)
- Gets dedicated instance
- No auto-suspension
- Faster performance
- Professional SLA

## Security Considerations

### Current Setup
- ✓ Login authentication implemented
- ✓ Flask session-based security
- ⚠ Password stored in code (okay for demo)

### Production Recommendations
1. Use environment variables for credentials
2. Add SSL/TLS (Render provides free)
3. Implement rate limiting
4. Add CSRF protection
5. Use secure session cookies

## Environment Variables (Optional)

To add environment variables in Render:
1. Dashboard → [Your Service] → **Environment**
2. Add key-value pairs

Example:
```
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

Update `app.py` to use:
```python
app.secret_key = os.environ.get('SECRET_KEY', 'default-key')
```

## Deployment Checklist

- [ ] All files committed to Git
- [ ] GitHub repository created
- [ ] Render account created
- [ ] GitHub connected to Render
- [ ] Web Service created
- [ ] Deployment successful (no red errors)
- [ ] Application loads at provided URL
- [ ] Login works with correct credentials
- [ ] All 5 steps complete successfully
- [ ] File upload works
- [ ] Logout works
- [ ] URL is accessible from internet

## Support Resources

- **Render Docs**: https://render.com/docs
- **Flask Docs**: https://flask.palletsprojects.com/
- **Gunicorn Docs**: https://gunicorn.org/

## Summary

Your Insurance Practice Application is now live on the internet and accessible from anywhere! 🎉

**Your Public URL:**
```
https://insurance-practice-app-xxxxx.onrender.com
```

You can now use this URL for:
- Live testing
- Sharing with team members
- Playwright automation testing from anywhere
- Portfolio/demo purposes
