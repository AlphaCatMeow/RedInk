# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in RedInk, please report it responsibly.

**Do NOT open a public GitHub issue for security vulnerabilities.**

Instead, please email: **histonemax@gmail.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

## Response Timeline

- **Acknowledgment**: Within 48 hours
- **Initial assessment**: Within 1 week
- **Fix release**: As soon as possible, depending on severity

## Scope

The following are in scope:
- Backend API vulnerabilities
- Authentication/authorization issues
- Data exposure risks
- Injection vulnerabilities (SQL, XSS, command injection)
- Docker configuration security issues

The following are out of scope:
- Third-party API key management (user responsibility)
- Denial of service via API rate limiting (handled by upstream providers)

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | Yes       |
| < Latest | No      |

We recommend always using the latest version.
