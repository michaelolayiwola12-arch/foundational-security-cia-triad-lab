# Foundational Security Concepts Lab – CIA Triad

## 📌 Overview

This project demonstrates the practical implementation of the Confidentiality, Integrity, and Availability (CIA) Triad using:

- Kali Linux
- Linux file permission controls
- SHA-256 cryptographic hashing
- Python-based service monitoring

The objective of this lab is to apply foundational security principles in a controlled environment and document their real-world application.

---

# 🔐 1. Confidentiality – File Permission Hardening

Sensitive data was protected using Linux file permission controls.

### Environment Setup

```bash
mkdir -p ~/project && cd ~/project
echo "Top Secret Details" > confidential_data.txt
ls -l

By default, files may allow group/other read access, which violates confidentiality.

Enforcing Confidentiality
chmod 600 confidential_data.txt

Owner: Read & Write

Group: No access

Others: No access

Enforcing Integrity Protection (Read-Only Mode)
chmod 400 confidential_data.txt
echo "Unauthorized change" >> confidential_data.txt

Result:

Permission denied

This prevents unauthorized modifications.

2. Integrity – Hash Verification Using SHA-256

File integrity was validated using cryptographic hashing.

Generate Baseline Hash
sha256sum confidential_data.txt > hashes.sha256
Simulate Tampering
chmod u+w confidential_data.txt
echo "This is an unauthorized modification." >> confidential_data.txt
Verify Integrity
sha256sum -c hashes.sha256

Result:

FAILED

This demonstrates detection of file tampering.

3. Availability – Service Monitoring

A local HTTP service was deployed and monitored.

Start Service
python3 -m http.server 8000 &
Validate Service
curl http://localhost:8000/confidential_data.txt
🐍 Python Monitoring Script

See: availability/monitor.py

This script performs:

HTTP HEAD request

Timeout handling

Status code validation

Timestamp logging

Exit codes for automation

📊 Security Principles Demonstrated
Principle	Method Used	Outcome
Confidentiality	chmod 600 / 400	Restricted access
Integrity	sha256sum verification	Tamper detection
Availability	Python monitoring script	Automated uptime validation
🧠 Skills Demonstrated

Linux file permission management

Access control enforcement

Cryptographic hash validation

Service availability monitoring

Python scripting for automation

Security documentation practices

📄 Documentation

Full lab documentation available in:

docs/Foundational_Security_Concept_Michael_Olayiwola.pdf

🎯 Why This Project Matters

This project demonstrates practical application of foundational security principles that underpin enterprise security controls.

It reflects hands-on security engineering skills rather than theoretical knowledge.
