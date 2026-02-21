```markdown
# File Integrity Verification – SHA-256

## Objective
Demonstrate integrity validation using cryptographic hashing.

---

## Generate Baseline Hash

```bash
sha256sum confidential_data.txt > hashes.sha256

This generates a unique fingerprint of the file content.

Simulate File Tampering
chmod u+w confidential_data.txt
echo "Unauthorized modification" >> confidential_data.txt
Verify Integrity
sha256sum -c hashes.sha256

Result:

FAILED

Security Impact:

Detects unauthorized changes

Validates file authenticity

Supports forensic verification
