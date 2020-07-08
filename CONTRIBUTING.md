# Introduction

Thank you for considering collaboration with us. We hope to build something valuable with you on board!

Please take a moment to review these guidelines to make the contibution process as smooth and effective as possible. Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

# Ground Rules

## Responsibilites

- Do not add any classes to the codebase. Communicate such concerns beforehand to me
- Stick to the variable names fixed beforehand, and choose relevant variable names if creating new ones
- Stick to the goals of the current version as mentioned in the README. Any major feature additions will be incorporated with newer versions.
- Create issues for any major changes and enhancements that you wish to make. Discuss things transparently and get community feedback.

# Technical Specifications and How to Contribute to them

The script is divided into 2 main parts: crawler.py and intruder.py

### crawler.py

This part parses through the HTML, searching for areas of input to exploit. It makes use of the Python libraries [requests](https://pypi.org/project/requests/) and [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

### intruder.py

This part iterates through a wordlist of XSS attacks from the file attacks.xml and passes it through the inputs. Every XSS payload consists of an alert message that gets validated and patched through a headless browser. It makes use of the Python library [pyppeteer](https://pypi.org/project/pyppeteer/) OR [selenium](https://pypi.org/project/selenium/) for this.

The project also consists of a XML file called attacks.xml that stores the wordlist of potential attacks.

### attacks.xml

*Proper format to be decided*

# Responsible Use

> Do not test the app against web applications where you do not have explicit permissions to do so. The author and organization do not bear any responsibility in cases of unauthorized or malicious use.

# Conclusion

If you follow the above mentioned rules, we should have a great time collaborating together on this awesome project. As this is a learning experience for all of us, feel free to reach out to me if there is anything you think we can do better. Thanks again for considering us on your open source journey.

~ Gaurav (gRevolut1on) and the rest of Team BITSkrieg
