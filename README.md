# Simple Intrusion Detection System (IDS) Using Python

## Project Overview

This project is a Simple Intrusion Detection System (IDS) developed using Python. The purpose of the project is to monitor security log files, identify suspicious login activity, and automatically generate security alerts.

The IDS focuses on detecting repeated failed login attempts from the same IP address. Multiple failed login attempts may indicate an unauthorized user attempting to access a system.

This project was developed individually as part of a cybersecurity and Python security automation course.

## Project Objectives

The main objectives of this project are:

1. Develop a basic Intrusion Detection System using Python.
2. Read and analyze security log files.
3. Identify repeated failed login attempts.
4. Track suspicious activity using IP addresses.
5. Automatically generate security alerts.
6. Save alerts for future review.
7. Demonstrate basic cybersecurity automation techniques.

## Project Features

**Log File Analysis:** Reads a security log file containing login activity.

**Failed Login Detection:** Identifies unsuccessful login attempts.

**IP Address Tracking:** Counts failed login attempts associated with individual IP addresses.

**Suspicious Activity Alerts:** Generates an alert when an IP address has five or more failed login attempts.

**Alert Logging:** Saves detected suspicious activity to a separate file.

**Error Handling:** Displays an error message if the security log file cannot be accessed.

## Technologies Used

* Python 3
* Visual Studio Code
* Git
* GitHub

## Python Libraries

The project uses the following built-in Python libraries:

* `re` — Identifies IP address patterns.
* `collections` — Counts failed login attempts.
* `datetime` — Adds timestamps to security alerts.
* `pathlib` — Manages file locations.

## Project Files

* `ids.py` — Main Intrusion Detection System program.
* `sample_logs.txt` — Sample security log data.
* `alerts.txt` — Automatically generated security alerts.
* `requirements.txt` — Dependency information.
* `.gitignore` — Files excluded from Git tracking.
* `screenshots/` — Screenshots demonstrating program functionality.

## Installation Instructions

For Mac or Linux:

`python3 ids.py`

## How the Program Works

The program reads the `sample_logs.txt` file and searches for failed login attempts.

Each failed login attempt is associated with an IP address.

The program counts the number of failed login attempts for each IP address.

If an IP address has five or more failed attempts, the program generates a security alert.

The alert is displayed in the terminal and saved to `alerts.txt`.

## Testing

The IDS was designed to support the following test scenarios:

1. Detecting repeated failed login attempts.
2. Generating alerts when the threshold is reached.
3. Saving alerts to a text file.
4. Recognizing normal activity without generating alerts.
5. Handling a missing security log file.

Screenshots of completed tests are stored in the `screenshots` folder.

## Project Limitations

This IDS is a beginner-level educational project.

It analyzes saved log files rather than monitoring live network traffic.

It uses a simplified log format and basic IP address pattern matching.

The program counts failed login attempts across the entire file instead of using a time-based detection window.

It does not automatically block suspicious IP addresses or determine whether an actual intrusion occurred.

## Future Improvements

Future improvements could include:

* Real-time log monitoring.
* Network traffic analysis.
* Email security notifications.
* A graphical dashboard.
* Detection of additional suspicious activities.
* More advanced log analysis.
* Time-based failed login detection.

## Project Development

This project was completed individually.

AI assistance was used to support project structure, documentation, and understanding Python security automation concepts.

## Conclusion

This project demonstrates how Python can be used to automate basic cybersecurity monitoring tasks.

By analyzing security logs and generating alerts, the IDS provides a simple example of how security professionals can identify potentially suspicious login activity.

The project also provides an opportunity to practice Python programming, error handling, file management, and security automation.
