"""
READ THIS:
- do not use these headers with out knowing what are you doing, it my cause break your application.
- use these config along your web server secure header config is ok, BUT do not config these headers in two places.
"""
# Content-Security-Policy
## read the documents first https://django-csp.readthedocs.io/en/latest/
## for configing Content-Security-Policy you need to install Django-CSP(pip intsall django-csp) and add this line to your MIDDLEWARE 
MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
]
## this example is configed for recaptcha and google-analytics and bootstarpcdn, you can cofig this for your self
CSP_DEFAULT_SRC = ("'none'",)
CSP_SCRIPT_SRC = ("'self'", 'https://www.google.com/recaptcha/', 'www.google-analytics.com', 'https://www.gstatic.com/recaptcha/')
CSP_INCLUDE_NONCE_IN = ['script-src'] # read the document for nonce hash and template setting
CSP_IMG_SRC = ("'self'", 'data:', 'www.google-analytics.com')
CSP_OBJECT_SRC = ("'self'",)
CSP_MEDIA_SRC = ("'self'",)
CSP_FRAME_SRC = ("'self'", 'https://www.google.com',)
CSP_FONT_SRC = ("'self'", 'data:', 'https://stackpath.bootstrapcdn.com', 'https://fonts.gstatic.com')
CSP_STYLE_SRC = ("'self'", 'https://stackpath.bootstrapcdn.com', "https://www.gstatic.com/")
CSP_FRAME_ANCESTORS = ("'self'",)
CSP_FORM_ACTION = ("'self'",)
CSP_BASE_URI = ("'self'",)

## for report only 
if DEBUG:
   CSP_REPORT_ONLY = True






# change some Djnago defult secure header
## more info : https://docs.djangoproject.com/en/2.1/topics/security/
## for configing other headers (maybe some of these too read Django Doc) using your webserver is better

## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True
## X-Frame-Options
X_FRAME_OPTIONS = 'DENY'
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True
## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'


