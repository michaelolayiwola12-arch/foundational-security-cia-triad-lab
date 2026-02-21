```markdown
# File Permission Hardening – Confidentiality

## Objective
Demonstrate how Linux file permissions enforce confidentiality and integrity.

## Step 1 – Create Sensitive File

```bash
echo "Top Secret Details" > confidential_data.txt
ls -l

Default permissions may allow group/other read access.

Step 2 – Restrict Access
chmod 600 confidential_data.txt

This ensures:

Only the file owner can read/write

No group or other access

Step 3 – Enforce Read-Only Mode
chmod 400 confidential_data.txt

Attempted modification:

echo "Unauthorized modification" >> confidential_data.txt

Result:

Permission denied

Security Impact:

Prevents unauthorized disclosure

Protects data from accidental changes

Enforces principle of least privilege
