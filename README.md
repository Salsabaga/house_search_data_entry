# House Search Data Entry using Selenium Webdriver

Project from 100 Days of Code in which I use the Selenium Webdriver to scrape 25 results based on my queries for 
searching a house. The project uses Zoopla for UK house prices for rent and has default searches put in place such as
its *price per month* and *location*. **This project will only work with the link inside the first .get() method**.

**NOTE**

*As of writing, using a chromedriver with the Selenium webdriver requires the webdriver Service class instance, and
executable path parameter has since been deprecated.*

```python
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

s=Service(r"C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=s)
```

### Using the Data Entry Automation Project

Due to the nature of selenium targeting specific elements based on a webpage's selector, and the [GDPR on
obtaining data via cookies](https://gdpr.eu/cookies/), the project must remove the page's iframe using the click method once the overlay pops
up. However, loading times may cause the automated browser to stop. If this happens, **please click on accept all cookies
button** and program shall resume itself. **An element of the project in which I will fix**

After the webdriver scrapes the details of price, location and link, it will then add all this information into a Google
form sheet provided and can be converted to a spreadsheet for easier readability.

## Questions/Queries

For any other questions or merges please contact me on my email provided in my profile page.

Thank you for reading!!

Danny Baldeon Abril
