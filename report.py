#!/usr/bin/python
import getopt
import requests
import sys

def main(argv):
    url = ''
    try:
        opts, args = getopt.getopt(argv, "hu:", ["url="])
    except getopt.GetoptError:
        print('report.py -u <url>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('report.py -u <url>')
            sys.exit()
        elif opt in ("-u", '--url'):
            url = arg

    # simple url validity
    try:
        report = requests.get(url)
    except:
        print("url is wrong or unreachable")
        sys.exit()
    if report.status_code != 200:
        print('status_code: ' + report.status_code)
        sys.exit()

    output = {}

    try:
        output['X-Xss-Protection'] = report.headers['X-Xss-Protection']
    except:
        output['X-Xss-Protection'] = None

    try:
        output['X-Content-Type-Options'] = report.headers['X-Content-Type-Options']
    except:
        output['X-Content-Type-Options'] = None

    try:
        output['Content-Security-Policy'] = report.headers['Content-Security-Policy']
    except:
        output['Content-Security-Policy'] = None

    try:
        output['Set-Cookie'] = report.headers['Set-Cookie']
    except:
        output['Set-Cookie'] = None

    try:
        output['Strict-Transport-Security'] = report.headers['Strict-Transport-Security']
    except:
        output['Strict-Transport-Security'] = None

    try:
        output['Feature-Policy'] = report.headers['Feature-Policy']
    except:
        output['Feature-Policy'] = None

    try:
        output['X-Frame-Options'] = report.headers['X-Frame-Options']
    except:
        output['X-Frame-Options'] = None

    try:
        output['Referrer-Policy'] = report.headers['Referrer-Policy']
    except:
        output['Referrer-Policy'] = None

    try:
        output['Clear-Site-Data'] = report.headers['Clear-Site-Data']
    except:
        output['Clear-Site-Data'] = None

    info = 'set this header https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/'
    for head in output:
        print(head + " : " + output[head] if output[head] is not None else head + " : " + info + head)

if __name__ == "__main__":
    main(sys.argv[1:])
