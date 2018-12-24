#!/usr/bin/python
"""
Pull requests are always welcome :)
"""
import getopt
import requests
import sys
import json
import datetime


def report(url):
    """
    function to generate a report for each url
    :param url:
    :return: report list object
    """
    # simple url validity
    try:
        report = requests.get(url)
    except:
        print("url is wrong or unreachable")
        return False
    if report.status_code != 200:
        print('status_code: ' + report.status_code)
        return False
    # making report list
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
    return output

def main(argv):
    url = ''
    filename = ''
    help_text = "report.py -u <url> -o <Output Filename>\n example: report.py -u https://certfa.com -o certfa "
    try:
        opts, args = getopt.getopt(argv, "hu:o", ["url=", "output"])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt in ("-u", '--url'):
            url = arg
        elif opt in ("-o", '--output'):
            filename = arg

    this_sit_report = report(url)
    """
    #show only 
    info = 'more information about this header https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/'
    for head in this_sit_report:
        print(head + " : " + this_sit_report[head] if this_sit_report[head] is not None else head + " : " + info + head)
    """
    filename = filename + "_" + str(datetime.datetime.now()) + '.json'
    if this_sit_report is not False:
        with open(filename, 'a') as outfile:
            outfile.write('\n{ "' + url + '":\n')
            json.dump(this_sit_report, outfile)
            outfile.write('\n}\n')

        print('Reported: ' + url)
    else:
        print('Fail :' + url)

if __name__ == "__main__":
    print(__doc__)
    main(sys.argv[1:])
