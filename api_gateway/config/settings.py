import os

EMPLOYEE_SERVICE_URL = os.getenv('EMPLOYEE_SERVICE_URL', 'http://employee_service:8000')
PAYROLL_SERVICE_URL = os.getenv('PAYROLL_SERVICE_URL', 'http://payroll_service:8000')
