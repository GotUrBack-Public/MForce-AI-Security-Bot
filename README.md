# MForce AI Security Bot

Open-source security automation for GitHub repositories.

## Status

Initial bootstrap. Security scanning and fix-PR automation are being implemented and tested. Installing the GitHub App alone does not start scans.

## Security model

- Review all proposed changes before merging.
- Never commit private keys or access tokens.
- Restrict installations to repositories you intend to scan.
- Do not run untrusted repository code with the GitHub App private key available.

## Configuration

GitHub Actions secret: `MFORCE_APP_PRIVATE_KEY` (private key PEM).

GitHub Actions variable: `MFORCE_APP_ID` (numeric GitHub App ID).

These credentials are not required for the initial static-analysis workflow.
