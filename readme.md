# webdriver detector
This project is a simple JavaScript script that detects whether a website is being accessed via a web driver for automated web scraping. The script checks for the existence of the <b>navigator.webdriver</b> property, which is set to <b>true</b> when a browser automation tool such as Selenium is being used to access the website.

If the script detects the presence of a web driver, it outputs a message on the web page indicating that the website is not accessible via automated scraping.

# Usage
To use the script, simply include it in the HTML file of the web page that you want to protect from automated scraping.

The script can be added to the HTML file using a script tag, as shown below:

```html
<script src="https://github.com/liad07/selnuimdetector/raw/main/detect-web-driver.js"></script>
```
When a web driver is detected, the script will output the "no scrape for u" message on the web page, making it clear to the user that the website is not accessible via automated scraping.

It's important to note that this script is not foolproof and can be circumvented by more advanced scraping techniques. However, it can still be effective in deterring casual or automated scraping attempts.

# Contributions
Contributions to this project are welcome! If you find a bug or have an idea for an improvement, please feel free to submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for more information.