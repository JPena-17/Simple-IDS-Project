# Simple Intrusion Detection System (IDS)
# Project: Python Security Automation
# Description:
# This program analyzes security logs and detects
# repeated failed login attempts from IP addresses.

import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path


# Project settings
BASE_DIR = Path(__file__).resolve().parent

LOG_FILE = BASE_DIR / "sample_logs.txt"
ALERT_FILE = BASE_DIR / "alerts.txt"

# Generate an alert after 5 failed login attempts
FAILED_LOGIN_THRESHOLD = 5


# Function to read the security log file
def read_logs():

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            logs = file.readlines()

        print("[INFO] Security log file loaded successfully.")

        return logs

    except FileNotFoundError:

        print("[ERROR] Security log file not found.")

        return None

    except OSError as error:

        print(f"[ERROR] Unable to read log file: {error}")

        return None


# Function to detect suspicious login activity
def detect_intrusions(logs):

    failed_attempts = defaultdict(int)

    # Search for failed login attempts
    for line in logs:

        if "Failed login" in line:

            # Extract the IP address
            ip_match = re.search(
                r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
                line
            )

            if ip_match:

                ip_address = ip_match.group()

                # Count failed login attempts
                failed_attempts[ip_address] += 1

    return failed_attempts


# Function to generate security alerts
def generate_alerts(failed_attempts):

    alerts = []

    for ip_address, count in failed_attempts.items():

        if count >= FAILED_LOGIN_THRESHOLD:

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            alert = (
                f"[ALERT] {timestamp} - "
                f"Suspicious activity detected from "
                f"IP address {ip_address}. "
                f"Failed login attempts: {count}"
            )

            alerts.append(alert)

    return alerts


# Function to save alerts to a file
def save_alerts(alerts):

    try:
        with open(ALERT_FILE, "w", encoding="utf-8") as file:

            for alert in alerts:
                file.write(alert + "\n")

        print("[INFO] Alert results saved to alerts.txt.")

    except OSError as error:

        print(f"[ERROR] Unable to save alerts: {error}")


# Main function
def main():

    print("=" * 50)
    print(" SIMPLE INTRUSION DETECTION SYSTEM ")
    print("=" * 50)

    print("[INFO] Starting security log analysis...")

    logs = read_logs()

    if logs is None:
        return

    failed_attempts = detect_intrusions(logs)

    print("\n[INFO] Failed Login Summary:")

    if not failed_attempts:
        print("No failed login attempts found.")

    for ip_address, count in failed_attempts.items():

        print(f"IP Address: {ip_address} | Attempts: {count}")

    alerts = generate_alerts(failed_attempts)

    print("\n[INFO] Security Alert Results:")

    if alerts:

        for alert in alerts:
            print(alert)

    else:

        print("[INFO] No suspicious activity detected.")

    save_alerts(alerts)

    print("\n[INFO] Security analysis completed.")


# Run the IDS program
if __name__ == "__main__":
    main()