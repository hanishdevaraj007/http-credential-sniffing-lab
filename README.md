# HTTP Credential Sniffing Lab (Python + Scapy)

This project demonstrates how credentials transmitted over **unencrypted HTTP traffic** can be intercepted on a network.

The lab simulates a public WiFi login portal and captures the credentials using packet sniffing.

## Technologies Used

- Python
- Flask
- Scapy

## Project Components

### 1. Flask Web Portal
A simple login page simulating a public WiFi captive portal.

File:
```
app.py
```

### 2. Packet Sniffer
Captures HTTP traffic on port 80 and extracts credentials from POST requests.

File:
```
sniffer.py
```

Captured credentials are saved to:

```
captured_credentials.txt
```

## Experiment Setup

1. Start the Flask server
2. Start the packet sniffer
3. Connect another device to the same network
4. Access the login page
5. Submit credentials

The sniffer intercepts the HTTP POST request and extracts the credentials.

## Example Output

```
[+] HTTP POST Request Captured
[+] Username : hanish
[+] Password : test123
Credentials saved to captured_credentials.txt
```

## Lab Demonstration

![Lab Demo](screenshots/lab-demo.jpg)

## Key Learning

This experiment demonstrates why transmitting sensitive data over **HTTP is insecure** and highlights the importance of **HTTPS encryption**.

## Disclaimer

This project was conducted in a **controlled lab environment using my own devices for educational purposes only**.