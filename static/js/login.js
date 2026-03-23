/**
 * Login Form Validation
 */

document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login_form');
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    const loginBtn = document.getElementById('login_submit_btn');

    // Password visibility on focus
    if (passwordInput) {
        passwordInput.addEventListener('focus', function () {
            this.setAttribute('type', 'password');
        });
    }

    // Validate form on submit
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            if (!validateLoginForm()) {
                e.preventDefault();
            }
        });
    }

    // Clear error on input
    if (usernameInput) {
        usernameInput.addEventListener('focus', clearError);
        usernameInput.addEventListener('input', clearError);
    }

    if (passwordInput) {
        passwordInput.addEventListener('focus', clearError);
        passwordInput.addEventListener('input', clearError);
    }
});

/**
 * Validate login form
 */
function validateLoginForm() {
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value;

    if (!username || !password) {
        showError('Please enter both username and password');
        return false;
    }

    if (username.length < 3) {
        showError('Username must be at least 3 characters');
        return false;
    }

    if (password.length < 6) {
        showError('Password must be at least 6 characters');
        return false;
    }

    return true;
}

/**
 * Show error message
 */
function showError(message) {
    const errorDiv = document.getElementById('login_error') || createErrorElement();
    errorDiv.textContent = '✗ ' + message;
    errorDiv.style.display = 'block';
    errorDiv.setAttribute('data-testid', 'login_error');
}

/**
 * Clear error message
 */
function clearError() {
    const errorDiv = document.getElementById('login_error');
    if (errorDiv) {
        errorDiv.remove();
    }
}

/**
 * Create error element if it doesn't exist
 */
function createErrorElement() {
    const errorDiv = document.createElement('div');
    errorDiv.id = 'login_error';
    errorDiv.className = 'error-alert';
    errorDiv.setAttribute('data-testid', 'login_error');
    
    const loginForm = document.querySelector('.login-form');
    loginForm.parentNode.insertBefore(errorDiv, loginForm);
    
    return errorDiv;
}
