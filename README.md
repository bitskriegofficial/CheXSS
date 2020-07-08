# CheXSS

CheXSS is a Python tool for detecting Cross-Site Scripting (XSS) vulnerabilities in web applications for implementing effective filters.

## How does it work?

CheXSS searches for HTML inputs such as form inputs, and iterates various payloads from a wordlist to understand if the web application would be vulnerable to such an attack.

## Goal for Current Version and Future Plans

The first version of this tool aims to at least identify vulnerabilities in form fields that display on the same page. This is a good starting point and will serve as an effective proof of conecept.

Future plans include, but are not restricted to:

- Identifying stored XSS located on separate pages in the same app
- Identifying XSS through URL parameters
- Identifying execution sinks in JS code for DOM based XSS
- Pinpointing exact security flaw and suggesting effective filter

## Quick Start Resources for Contributors

#### Videos about XSS
- [Cracking Websites with Cross Site Scripting - Computerphile](https://www.youtube.com/watch?v=L5l9lSnNMxg)
- [Cross-Site Scripting (XSS) Explained](https://www.youtube.com/watch?v=EoaDgUgS6QA)

#### Reading Material
- [Portswigger](https://portswigger.net/web-security/cross-site-scripting)
- [Brutelogic](https://brutelogic.com.br/blog/xss101/)
- [OWASP](https://owasp.org/www-community/attacks/xss/)

For more information about the technologies in use, refer to CONTRIBUTING.md

## Disclaimer

> This tool WILL attempt malicious code against a web application, so use it only in situations where you have the appropriate permissions. The author and organization do not bear any responsibility in cases of unauthorized or malicious use.

## Licensing

*To be decided*
