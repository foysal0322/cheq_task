# End-to-End Automation Testing with Selenium, Pytest, and Allure Reports
#### This repository contains an end-to-end (E2E) automation project that uses Python, Selenium WebDriver, Pytest, and Allure for generating test reports. The project supports dynamic test execution for labeled test suites such as regression, sanity, and parallel testing. It is designed with modularity in mind to ensure code reusability, and it integrates with external data sources like Excel for data-driven testing.





# Project Overview
The project automates the process of testing a web application available at ***https://suites.uat.cheqplease.com/*** using Selenium WebDriver. It includes steps such as logging in with valid credentials, selecting events and suites, adding items to the cart, making payment with test card details, and verifying test outcomes. 

# Prerequisites
Before setting up and running the tests, ensure the following:
1. Python: Python 3.6 or higher is required.
2. Dependencies: Install the required Python packages using the following command:
>``` pip install -r requirements.txt ```
# Setup Instructions
 **Clone this repository to your local machine:**
> ```git clone https://github.com/foysal0322/cheq_task```
```cd cheq_task```

**Install the necessary dependencies by running:**
>```pip install -r requirements.txt```

Ensure that your ChromeDriver is compatible with the version of Google Chrome installed on your machine.The ==selenium_driver.py== script is set up to use Chrome by default. You can change the browser in the configuration if needed.
# Test Execution
**To run the tests with pytest, execute the following command:**
> ```pytest -m sanity --alluredir=allure-results```

**For parallel test execution, you can use the _pytest-xdist_ plugin. Install it by running:**
>```pip install pytest-xdist```

Then, run tests in parallel using:
> ```pytest -n 4  # Run tests in 4 parallel processes```

Allure Report: To generate an Allure report, ensure you have Allure installed on your machine. 
After running the tests with pytest, generate the Allure report by running:
> ```allure serve allure-results```

# Test Data
The test data is stored in the external Excel file *info.xlsx*. This file contains the dynamic input values required for various test cases.





