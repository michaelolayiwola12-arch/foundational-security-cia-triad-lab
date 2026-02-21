```markdown
# Service Availability Monitoring

## Objective
Demonstrate availability monitoring using a local HTTP server and automated Python script.

---

## Start HTTP Service

```bash
python3 -m http.server 8000 &
Validate Service
curl http://localhost:8000/confidential_data.txt
Stop Service (Simulate Failure)
kill <PID>
Monitoring Script

The Python monitoring script performs:

HTTP HEAD request

Timeout control

Status code validation

Timestamp logging

Exit status reporting

This enables automated uptime monitoring.

Security Impact

Validates service availability

Detects service downtime

Supports operational monitoring
