/**
 * Form Validation and Interaction Scripts
 */

document.addEventListener('DOMContentLoaded', function () {
    initializeFormValidation();
    attachEventListeners();
});

/**
 * Initialize form validation
 */
function initializeFormValidation() {
    const forms = document.querySelectorAll('form[id^="step"]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function (e) {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
    });
}

/**
 * Validate form based on its ID
 */
function validateForm(form) {
    const formId = form.getAttribute('id');
    let isValid = true;

    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(el => {
        el.textContent = '';
    });

    if (formId === 'step1-form') {
        isValid = validateStep1();
    } else if (formId === 'step2-form') {
        isValid = validateStep2();
    } else if (formId === 'step3-form') {
        isValid = validateStep3();
    }

    return isValid;
}

/**
 * Validate Step 1 - Personal Information
 */
function validateStep1() {
    let isValid = true;

    // Validate Full Name
    const fullName = document.getElementById('full_name');
    if (!fullName.value.trim()) {
        document.getElementById('full_name_error').textContent = 'Full name is required';
        fullName.style.borderColor = '#e74c3c';
        isValid = false;
    } else if (fullName.value.trim().length < 3) {
        document.getElementById('full_name_error').textContent = 'Full name must be at least 3 characters';
        fullName.style.borderColor = '#e74c3c';
        isValid = false;
    } else {
        fullName.style.borderColor = '';
    }

    // Validate Age
    const age = document.getElementById('age');
    if (!age.value) {
        document.getElementById('age_error').textContent = 'Age is required';
        age.style.borderColor = '#e74c3c';
        isValid = false;
    } else if (age.value < 18 || age.value > 99) {
        document.getElementById('age_error').textContent = 'Age must be between 18 and 99';
        age.style.borderColor = '#e74c3c';
        isValid = false;
    } else {
        age.style.borderColor = '';
    }

    // Validate Address
    const address = document.getElementById('address');
    if (!address.value.trim()) {
        document.getElementById('address_error').textContent = 'Address is required';
        address.style.borderColor = '#e74c3c';
        isValid = false;
    } else if (address.value.trim().length < 5) {
        document.getElementById('address_error').textContent = 'Address must be at least 5 characters';
        address.style.borderColor = '#e74c3c';
        isValid = false;
    } else {
        address.style.borderColor = '';
    }

    return isValid;
}

/**
 * Validate Step 2 - Line of Business
 */
function validateStep2() {
    let isValid = true;

    // Validate Line of Business
    const lob = document.getElementById('line_of_business');
    if (!lob.value) {
        document.getElementById('lob_error').textContent = 'Please select a line of business';
        lob.style.borderColor = '#e74c3c';
        isValid = false;
    } else {
        lob.style.borderColor = '';
    }

    // Validate Coverage Type
    const coverageType = document.querySelector('input[name="coverage_type"]:checked');
    if (!coverageType) {
        document.getElementById('coverage_error').textContent = 'Please select a coverage type';
        isValid = false;
    }

    return isValid;
}

/**
 * Validate Step 3 - Coverage Selection
 */
function validateStep3() {
    // Step 3 doesn't have required validations, but we can add optional warnings
    const coverageCheckboxes = document.querySelectorAll('input[name^="Liability"], input[name^="Collision"], input[name^="Comprehensive"], input[name^="Medical"], input[name^="Uninsured"]');
    
    const isAnyChecked = Array.from(coverageCheckboxes).some(cb => cb.checked);
    
    if (!isAnyChecked) {
        console.warn('No coverages selected - this is allowed but unusual');
    }

    return true;
}

/**
 * Attach event listeners for real-time validation
 */
function attachEventListeners() {
    // Real-time validation for text inputs
    const fullName = document.getElementById('full_name');
    if (fullName) {
        fullName.addEventListener('blur', function () {
            if (this.value.trim().length === 0) {
                document.getElementById('full_name_error').textContent = 'Full name is required';
                this.style.borderColor = '#e74c3c';
            } else if (this.value.trim().length < 3) {
                document.getElementById('full_name_error').textContent = 'Full name must be at least 3 characters';
                this.style.borderColor = '#e74c3c';
            } else {
                document.getElementById('full_name_error').textContent = '';
                this.style.borderColor = '';
            }
        });

        fullName.addEventListener('focus', function () {
            document.getElementById('full_name_error').textContent = '';
            this.style.borderColor = '';
        });
    }

    // Real-time validation for age
    const age = document.getElementById('age');
    if (age) {
        age.addEventListener('blur', function () {
            if (!this.value) {
                document.getElementById('age_error').textContent = 'Age is required';
                this.style.borderColor = '#e74c3c';
            } else if (this.value < 18 || this.value > 99) {
                document.getElementById('age_error').textContent = 'Age must be between 18 and 99';
                this.style.borderColor = '#e74c3c';
            } else {
                document.getElementById('age_error').textContent = '';
                this.style.borderColor = '';
            }
        });

        age.addEventListener('focus', function () {
            document.getElementById('age_error').textContent = '';
            this.style.borderColor = '';
        });
    }

    // Real-time validation for address
    const address = document.getElementById('address');
    if (address) {
        address.addEventListener('blur', function () {
            if (this.value.trim().length === 0) {
                document.getElementById('address_error').textContent = 'Address is required';
                this.style.borderColor = '#e74c3c';
            } else if (this.value.trim().length < 5) {
                document.getElementById('address_error').textContent = 'Address must be at least 5 characters';
                this.style.borderColor = '#e74c3c';
            } else {
                document.getElementById('address_error').textContent = '';
                this.style.borderColor = '';
            }
        });

        address.addEventListener('focus', function () {
            document.getElementById('address_error').textContent = '';
            this.style.borderColor = '';
        });
    }

    // Real-time validation for select
    const lob = document.getElementById('line_of_business');
    if (lob) {
        lob.addEventListener('change', function () {
            if (this.value) {
                document.getElementById('lob_error').textContent = '';
                this.style.borderColor = '';
            }
        });
    }

    // Highlight effect for radio buttons
    const radioButtons = document.querySelectorAll('input[type="radio"]');
    radioButtons.forEach(radio => {
        radio.addEventListener('change', function () {
            const parent = this.closest('.radio-item') || this.closest('.payment-item');
            if (parent) {
                // Remove active class from siblings
                const siblings = parent.parentNode.querySelectorAll('.radio-item, .payment-item');
                siblings.forEach(sibling => {
                    sibling.style.borderColor = '';
                    sibling.style.background = '';
                });
                // Add highlight to selected
                parent.style.borderColor = '#3498db';
                parent.style.background = 'rgba(52, 152, 219, 0.05)';
            }
        });
    });

    // Highlight effect for checkboxes
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function () {
            const parent = this.closest('.checkbox-item');
            if (parent) {
                if (this.checked) {
                    parent.style.borderColor = '#3498db';
                    parent.style.background = 'rgba(52, 152, 219, 0.05)';
                } else {
                    parent.style.borderColor = '';
                    parent.style.background = '';
                }
            }
        });
    });
}

/**
 * Format currency values for display
 */
function formatCurrency(value) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2
    }).format(value);
}

/**
 * Update page title with step information
 */
function updatePageTitle(stepNumber, stepName) {
    const titleEl = document.querySelector('h2');
    if (titleEl) {
        titleEl.textContent = `Step ${stepNumber}: ${stepName}`;
    }
}

/**
 * Show/hide sections based on user selection
 */
function toggleSection(selectorToShow, selectorToHide) {
    const showEl = document.querySelector(selectorToShow);
    const hideEl = document.querySelector(selectorToHide);

    if (showEl) showEl.style.display = 'block';
    if (hideEl) hideEl.style.display = 'none';
}

/**
 * Log form submission data (useful for testing)
 */
function logFormData(formId) {
    const form = document.getElementById(formId);
    if (form) {
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        console.log(`Form ${formId} data:`, data);
        return data;
    }
    return null;
}
