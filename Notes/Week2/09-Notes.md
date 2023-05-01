# Public Key Infrastructure (PKI)

## Name the three main components which make up PKI.
Certificate Authority (CA)
Registration Authority (RA)
Certificate Revocation List (CRL)

## How would you explain, to a non-technical friend, the role PKI plays in protecting traffic between your browser and a web server.
When you connect to a website using a browser, the website sends its digital certificate to your browser. This certificate contains a public key that your browser uses to encrypt any data that is sent to the web serve

## What is the main weakness of the PKI architecture?
If a CA is compromised, either by a hacker or an insider, they can issue fraudulent digital certificates, which can be used to conduct man-in-the-middle attacks. In a man-in-the-middle attack, an attacker intercepts the communication between two parties and can read, modify, or inject new messages.