# XSS with w3af, DVWA

## Explain how a cross-site scripting attack works in non-technical terms.
In a cross-site scripting attack, a malicious person sneaks harmful code into a trusted website. When you visit that website, your browser unknowingly runs the code, which can steal your personal information or redirect you to a fake website to collect sensitive data. To stay safe, use secure websites and be cautious when interacting with content from untrusted sources.

## What are the three types of XSS attacks?
- Stored XSS: In this type of attack, the malicious code is permanently stored on a target website. When other users access that particular page or view the infected content, their browsers execute the malicious code, potentially compromising their information or delivering harmful payloads.
- Reflected XSS: In a reflected XSS attack, the malicious code is embedded in a URL or input field of a vulnerable website. When a user clicks on a specially crafted link or submits a form, the website includes the malicious code in the response, which is then executed by the user's browser. This attack is called "reflected" because the injected code is reflected back to the user.
- DOM-based XSS: This type of XSS attack exploits vulnerabilities in the Document Object Model (DOM), which represents the structure of a webpage in a browser. The attack occurs when the website's JavaScript code dynamically modifies the DOM using untrusted data, allowing an attacker to inject malicious code. When the manipulated DOM is processed, the code executes in the user's browser, leading to potential data theft or other malicious actions.

## If an attacker successfully exploits a XSS vulnerability, what malicious actions would they be able to perform?
Stealing sensitive information: The attacker can use XSS to steal sensitive data entered by users on the compromised website. This could include usernames, passwords, credit card information, or personal details.
Session hijacking: By exploiting XSS, an attacker can gain unauthorized access to a user's session. They can take over the user's session and perform actions on their behalf, such as making unauthorized transactions or manipulating their account settings.

## What are some security controls that can be implemented to prevent XSS attacks?
Input validation and sanitization: Implement strict validation and filtering mechanisms to ensure that user input is properly validated and sanitized before it is displayed on web pages. This helps to prevent the execution of malicious scripts.

Output encoding: Apply output encoding to user-generated content to neutralize any potentially malicious code. This ensures that user input is treated as plain text and not executable code.

Content Security Policy (CSP): Implement a Content Security Policy that defines the trusted sources of content, such as scripts, stylesheets, and images. It helps to restrict the execution of untrusted scripts and mitigate the impact of XSS attacks.