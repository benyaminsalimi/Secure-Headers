# Secure-Headers
secure header best practices config for Apache, Nginx, lighttpd

## why secure header
> I suggest you don't copy past config from this repo, especially if you have a custom web application our example may break your software. read these articles first 

- [OWASP secure header ](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project)
- [Mozilla Web Security guideline](https://infosec.mozilla.org/guidelines/web_security)

## online Header scanner
- [Mozilla tool](https://observatory.mozilla.org/)
- [securityheaders.com](https://securityheaders.com)
- [mozilla cli tool](https://github.com/mozilla/observatory-cli) 

## report script
```bash
report.py -u <url>
```

## secure config
- [apache](/example/) or  [.htaccess](/example/.htaccess)
- [nigix](/example/)
- [lighttpd](/example/)

## TODO
- add netlify.com secure header best practice
- add CVS and Json export to report
- add list input to report script