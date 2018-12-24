# Secure-Headers

secure header best practices config for Apache, Nginx, lighttpd 

## why secure header
> I suggest you don't copy past config from this repo, especially if you have a custom web application our example may break your software. read these articles first 
- [OWASP secure header ](https://www.owasp.org/index.php/OWASP_Secure_Headers_Project)
- [Mozilla Web Security guideline](https://infosec.mozilla.org/guidelines/web_security)
- [ALEXA TOP 1 MILLION SECURITY ANALYSIS](https://crawler.ninja/)

## Header scanner
- [Mozilla](https://observatory.mozilla.org/) (online)
- [securityheaders.com](https://securityheaders.com) (online)
- [Mozilla cli](https://github.com/mozilla/observatory-cli) (use mozilla api)

## report script
```bash
report.py -u <url>
```

## best practices
how to add header to [Apache](), [nginx](), [lighttpd]()
- [X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)
    - **apache**  
    > ```Header set X-Frame-Options "DENY"```
    - **nginx**  
    > ```add_header X-Frame-Options "DENY";```
    - **lighttpd** 
    > ```setenv.add-response-header = ("X-Frame-Options" => "DENY",)```

- [X-XSS-Protection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection)
    - **apache** 
    > ```Header set X-XSS-Protection "1; mode=block"```
    - **nginx**  
    > ```add_header X-XSS-Protection "1;mode=block";```
    - **lighttpd**  
    > ```setenv.add-response-header = ("X-XSS-Protection" => "1; mode=block",)```

- [X-Content-Type-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options) 
    - **apache**  
    > ```Header set X-Content-Type-Options "nosniff"```
    - **nginx**  
    > ```add_header X-Content-Type-Options "nosniff";```
    - **lighttpd**  
    > ```setenv.add-response-header = ("X-Content-Type-Options" => "nosniff",)```
    
- [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) 
    - [report-uri (online tool to generate CSP)](https://report-uri.com/)
    - [csp cheat sheet](https://scotthelme.co.uk/csp-cheat-sheet/)
    - **apache** 
    > ```Header set Content-Security-Policy "script-src 'self'; object-src 'self'"```
    - **nginx**
    > ```add_header Content-Security-Policy "script-src 'self'; object-src 'self'";```
    - **lighttpd** 
    > ```setenv.add-response-header = ("Content-Security-Policy" => "script-src 'self'; object-src 'self'",)```

- [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)
    - [hsts cheat sheet](https://scotthelme.co.uk/hsts-cheat-sheet/)
    - **apache** : 15768000 seconds = 6 months
    > ```Header always set Strict-Transport-Security "max-age=15768000; includeSubdomains"```
    - **nginx** : 
    > ```add_header Strict-Transport-Security "max-age=15768000; includeSubdomains";```
    - **lighttpd** : 
    > ```setenv.add-response-header = ("Strict-Transport-Security" => "max-age=15768000; includeSubdomains",)```

- [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy)
    - **apache**  
    > ```Header set Referrer-Policy "no-referrer"```
    - **nginx**  
    > ```add_header Referrer-Policy "no-referrer";```
    - **lighttpd**  
    > ```setenv.add-response-header = ("Referrer-Policy" => "no-referrer",)```

- [Feature-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy)
    - **apache**  
    > ```Header set Feature-Policy "accelerometer 'none'; camera 'none'; geolocation 'none'; gyroscope 'none'; magnetometer 'none'; microphone 'none'; payment 'none'; usb 'none';" ```
    - **nginx**  
    > ```add_header Feature-Policy "accelerometer 'none'; camera 'none'; geolocation 'none'; gyroscope 'none'; magnetometer 'none'; microphone 'none'; payment 'none'; usb 'none';";```
    - **lighttpd**  
    > ```setenv.add-response-header = ("Feature-Policy" => "accelerometer 'none'; camera 'none'; geolocation 'none'; gyroscope 'none'; magnetometer 'none'; microphone 'none'; payment 'none'; usb 'none';",) ```   
## optional
- [Clear-Site-Data](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data)
    - **apache** : Edit your apache configuration file and add the following to your VirtualHost.
    > ```Header set Clear-Site-Data "cache"```
    - **nginx** : Add snippet below into configuration file to send X-Frame-Options header.
    > ```add_header Clear-Site-Data "cache";```
    - **lighttpd** : Add snippet below into configuration file to send X-Frame-Options header.
    > ```setenv.add-response-header = ("Clear-Site-Data" => " cache ",)```

## best practice example config
- [apache](/example/nginx.conf) or  [.htaccess](/example/.htaccess)
- [nigix](/example/)
- [lighttpd](/example/)
- [Cloudflare Workers](/example/)
- [netlify](/example/)

## SSL
- [Mozilla SSL Configuration Generator
 Apache ](https://mozilla.github.io/server-side-tls/ssl-config-generator/)
- Free ssl + secure header
    - [letsencrypt you need to config secure header in your web server](https://letsencrypt.org/)
    - [with worker cloudflare  you can add secure header](https://stackoverflow.com/a/50797627/4859688)
    - [netlify use _headers file](https://www.netlify.com/docs/headers-and-basic-auth/#custom-headers)
## TODO
- add netlify.com secure headers best practice
- add Cloudflare Workers custom headers config 
- add CVS and Json export to report script
- add list input to report script
- add secure header suggestions  