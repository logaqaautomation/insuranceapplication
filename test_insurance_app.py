"""
Sample Playwright tests for Insurance Practice Application
Run with: pytest test_insurance_app.py
"""

import pytest
from playwright.sync_api import sync_playwright, expect


class TestInsuranceApplication:
    """Test suite for insurance application workflow"""

    @pytest.fixture
    def browser(self):
        """Setup and teardown browser"""
        with sync_playwright() as p:
            browser = p.chromium.launch()
            yield browser
            browser.close()

    @pytest.fixture
    def page(self, browser):
        """Create a new page for each test"""
        page = browser.new_page()
        page.goto("http://localhost:5000")
        yield page
        page.close()

    def test_home_page_loads(self, page):
        """Test that home page loads successfully"""
        # Verify title and heading
        expect(page.locator('h1')).to_contain_text('Insurance Practice Application')
        
        # Verify start button exists
        start_button = page.locator('a:has-text("Start Application")')
        expect(start_button).to_be_visible()

    def test_step1_personal_information(self, page):
        """Test Step 1 - Personal Information form"""
        # Navigate to step 1
        page.click('a:has-text("Start Application")')
        
        # Verify step 1 page loaded
        expect(page.locator('h2')).to_contain_text('Step 1: Personal Information')
        
        # Fill form
        page.fill('[data-testid="full_name_input"]', 'Jane Smith')
        page.fill('[data-testid="age_input"]', '28')
        page.fill('[data-testid="address_textarea"]', '456 Oak Avenue, Springfield, IL 62701')
        
        # Submit
        page.click('[data-testid="step1_submit_btn"]')
        
        # Verify navigation to step 2
        expect(page.locator('h2')).to_contain_text('Step 2')

    def test_step1_validation_empty_form(self, page):
        """Test Step 1 validation with empty form"""
        # Navigate to step 1
        page.click('a:has-text("Start Application")')
        
        # Try to submit empty form
        page.click('[data-testid="step1_submit_btn"]')
        
        # Verify error messages (form validation should prevent navigation)
        # Note: This depends on client-side validation working
        page_url = page.url
        expect(page).to_have_url('**/step1')

    def test_step1_validation_invalid_age(self, page):
        """Test Step 1 validation with invalid age"""
        page.click('a:has-text("Start Application")')
        
        # Fill form with invalid age
        page.fill('[data-testid="full_name_input"]', 'John Doe')
        page.fill('[data-testid="age_input"]', '15')  # Too young
        page.fill('[data-testid="address_textarea"]', '123 Main St, Test City, TC 12345')
        
        # Try to submit
        page.click('[data-testid="step1_submit_btn"]')
        
        # Verify still on step 1 due to validation
        expect(page).to_have_url('**/step1')

    def test_step2_line_of_business_selection(self, page):
        """Test Step 2 - Line of Business selection"""
        # Complete step 1
        page.click('a:has-text("Start Application")')
        page.fill('[data-testid="full_name_input"]', 'Bob Johnson')
        page.fill('[data-testid="age_input"]', '35')
        page.fill('[data-testid="address_textarea"]', '789 Pine Road, Metropolis, ST 54321')
        page.click('[data-testid="step1_submit_btn"]')
        
        # Test step 2
        expect(page.locator('h2')).to_contain_text('Step 2')
        
        # Select line of business
        page.select_option('[data-testid="line_of_business_select"]', 'home')
        
        # Select coverage type
        page.click('[data-testid="coverage_type_standard"]')
        
        # Submit
        page.click('[data-testid="step2_submit_btn"]')
        
        # Verify navigation to step 3
        expect(page.locator('h2')).to_contain_text('Step 3')

    def test_step3_coverage_selection_and_file_upload(self, page):
        """Test Step 3 - Coverage selection"""
        # Complete steps 1 and 2
        page.click('a:has-text("Start Application")')
        page.fill('[data-testid="full_name_input"]', 'Alice Brown')
        page.fill('[data-testid="age_input"]', '42')
        page.fill('[data-testid="address_textarea"]', '321 Elm Street, Gotham City, GC 99999')
        page.click('[data-testid="step1_submit_btn"]')
        
        page.select_option('[data-testid="line_of_business_select"]', 'auto')
        page.click('[data-testid="coverage_type_premium"]')
        page.click('[data-testid="step2_submit_btn"]')
        
        # Test step 3
        expect(page.locator('h2')).to_contain_text('Step 3')
        
        # Verify information summary table
        expect(page.locator('[data-testid="information_summary_table"]')).to_be_visible()
        expect(page.locator('[data-testid="summary_name"]')).to_contain_text('Alice Brown')
        expect(page.locator('[data-testid="summary_age"]')).to_contain_text('42')
        
        # Select coverages
        page.check('[data-testid="coverage_liability_coverage"]')
        page.check('[data-testid="coverage_collision_coverage"]')
        page.check('[data-testid="coverage_comprehensive_coverage"]')
        
        # Verify checkboxes are checked
        expect(page.locator('[data-testid="coverage_liability_coverage"]')).to_be_checked()
        expect(page.locator('[data-testid="coverage_collision_coverage"]')).to_be_checked()
        
        # Submit
        page.click('[data-testid="step3_submit_btn"]')
        
        # Verify navigation to step 4
        expect(page.locator('h2')).to_contain_text('Step 4')

    def test_step4_premium_display_and_payment_selection(self, page):
        """Test Step 4 - Premium calculation"""
        # Complete steps 1-3
        page.click('a:has-text("Start Application")')
        page.fill('[data-testid="full_name_input"]', 'Charlie Davis')
        page.fill('[data-testid="age_input"]', '50')
        page.fill('[data-testid="address_textarea"]', '555 Maple Drive, Smallville, SV 11111')
        page.click('[data-testid="step1_submit_btn"]')
        
        page.select_option('[data-testid="line_of_business_select"]', 'life')
        page.click('[data-testid="coverage_type_basic"]')
        page.click('[data-testid="step2_submit_btn"]')
        
        page.check('[data-testid="coverage_liability_coverage"]')
        page.check('[data-testid="coverage_medical_payments"]')
        page.click('[data-testid="step3_submit_btn"]')
        
        # Test step 4
        expect(page.locator('h2')).to_contain_text('Step 4')
        
        # Verify premium table exists
        expect(page.locator('[data-testid="premium_details_table"]')).to_be_visible()
        
        # Verify annual premium is displayed
        annual_premium = page.locator('[data-testid="premium_annual"]')
        expect(annual_premium).to_be_visible()
        
        # Verify payment options
        expect(page.locator('[data-testid="payment_monthly"]')).to_be_visible()
        expect(page.locator('[data-testid="payment_quarterly"]')).to_be_visible()
        expect(page.locator('[data-testid="payment_annual"]')).to_be_visible()
        
        # Select payment option
        page.click('[data-testid="payment_quarterly"]')
        expect(page.locator('[data-testid="payment_quarterly"]')).to_be_checked()
        
        # Submit
        page.click('[data-testid="step4_submit_btn"]')
        
        # Verify navigation to step 5
        expect(page.locator('h2')).to_contain_text('Step 5')

    def test_step5_policy_certificate(self, page):
        """Test Step 5 - Policy Certificate"""
        # Complete full workflow
        page.click('a:has-text("Start Application")')
        page.fill('[data-testid="full_name_input"]', 'Diana Prince')
        page.fill('[data-testid="age_input"]', '32')
        page.fill('[data-testid="address_textarea"]', '777 Wonder Woman Lane, Paradise Island, PI 77777')
        page.click('[data-testid="step1_submit_btn"]')
        
        page.select_option('[data-testid="line_of_business_select"]', 'home')
        page.click('[data-testid="coverage_type_standard"]')
        page.click('[data-testid="step2_submit_btn"]')
        
        page.check('[data-testid="coverage_liability_coverage"]')
        page.check('[data-testid="coverage_comprehensive_coverage"]')
        page.check('[data-testid="coverage_uninsured_motorist"]')
        page.click('[data-testid="step3_submit_btn"]')
        
        page.click('[data-testid="payment_annual"]')
        page.click('[data-testid="step4_submit_btn"]')
        
        # Test step 5
        expect(page.locator('[data-testid="policy_success_message"]')).to_be_visible()
        expect(page.locator('h2')).to_contain_text('Policy Successfully Issued')
        
        # Verify policy certificate
        expect(page.locator('[data-testid="policyholder_info_table"]')).to_be_visible()
        expect(page.locator('[data-testid="policy_details_table"]')).to_be_visible()
        
        # Verify policyholder information
        expect(page.locator('[data-testid="cert_name"]')).to_contain_text('Diana Prince')
        expect(page.locator('[data-testid="cert_age"]')).to_contain_text('32')
        expect(page.locator('[data-testid="cert_lob"]')).to_contain_text('Home Insurance')
        
        # Verify policy number exists
        policy_number = page.locator('[data-testid="certificate_policy_number"]')
        expect(policy_number).to_be_visible()
        
        # Complete application
        page.click('[data-testid="step5_complete_btn"]')
        
        # Verify completion page
        expect(page.locator('h2')).to_contain_text('Practice Application Complete')

    def test_navigation_to_previous_step(self, page):
        """Test navigation to previous steps"""
        # Complete step 1 and 2
        page.click('a:has-text("Start Application")')
        page.fill('[data-testid="full_name_input"]', 'Eve Wilson')
        page.fill('[data-testid="age_input"]', '27')
        page.fill('[data-testid="address_textarea"]', '999 Thunder Mountain Road, Asgard, AS 88888')
        page.click('[data-testid="step1_submit_btn"]')
        
        page.select_option('[data-testid="line_of_business_select"]', 'auto')
        page.click('[data-testid="coverage_type_premium"]')
        page.click('[data-testid="step2_submit_btn"]')
        
        # Now on step 3 - go back to step 2
        page.click('a:has-text("← Previous Step")')
        expect(page.locator('h2')).to_contain_text('Step 2')
        
        # Verify previous data is retained
        expect(page.locator('[data-testid="line_of_business_select"]')).to_have_value('auto')
        expect(page.locator('[data-testid="coverage_type_premium"]')).to_be_checked()

    def test_all_coverage_options_available(self, page):
        """Test that all coverage options are available"""
        # Navigate to step 3
        page.click('a:has-text("Start Application")')
        page.fill('[data-testid="full_name_input"]', 'Frank Castle')
        page.fill('[data-testid="age_input"]', '40')
        page.fill('[data-testid="address_textarea"]', '1111 Defense Lane, Metropolis, ST 11111')
        page.click('[data-testid="step1_submit_btn"]')
        
        page.select_option('[data-testid="line_of_business_select"]', 'auto')
        page.click('[data-testid="coverage_type_standard"]')
        page.click('[data-testid="step2_submit_btn"]')
        
        # Verify all coverage checkboxes exist
        coverages = [
            'coverage_liability_coverage',
            'coverage_collision_coverage',
            'coverage_comprehensive_coverage',
            'coverage_medical_payments',
            'coverage_uninsured_motorist'
        ]
        
        for coverage in coverages:
            checkbox = page.locator(f'[data-testid="{coverage}"]')
            expect(checkbox).to_be_visible()
            assert checkbox.input_value() is None or checkbox.input_value() == 'on'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
