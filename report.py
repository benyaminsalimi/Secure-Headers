#!/usr/bin/python
"""
GitHub repo : https://github.com/benyaminsalimi/secure-headers
"""
import getopt
import requests
import sys
import json
import datetime
import os


def report(url):
    """
    function to generate a report for each url
    :param url:
    :return: report list object
    """
    # TODO: add simple url validity
    try:
        report = requests.get(url)
    except:
        print("url is wrong or unreachable")
        return False

    if report.status_code != 200:
        print('status_code: ', report.status_code)
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

    site = {}
    site[url] = output
    return site

def json_report(url, filename):
    """
    function to write a url report to filename.json file
    :param url:
    :param filename:
    :return:
    """
    this_sit_report = report(url)
    if this_sit_report is not False:
        with open(filename, 'a') as outfile:
            json.dump(this_sit_report, outfile)
            outfile.write(',')

        print('Success: ' + url)
    else:
        print('Fail:    ' + url)

def main(argv):
    url = ''
    filename = ''
    url_list = ''
    help_text = "python report.py -u <url> -o <Output Filename> -l <Target List Filename> \n\n    example:\n" \
                "   python report.py -u https://facebook.com -o FBreport \n   python report.py -l input.text -o report"
    try:
        opts, args = getopt.getopt(argv, "hu:o:l:", ["url=", "output=", "list="])
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
        elif opt in ("-l", '--list'):
            url_list = arg

    # TODO: add CVS export
    filename = filename + "_" + str(datetime.datetime.now().date()) + '.json'

    if url_list != '':
        with open(filename, 'a') as outfile:
            outfile.write('[')
            outfile.close()

        urls = []
        with open(url_list, "r") as url_file:
            urls = url_file.readlines()
            url_file.close()
        urls = map(lambda s: s.strip(), urls)

        for url in urls:
            if url == '':
                continue
            json_report(url, filename)

        with open(filename, 'rb+') as outfile:
            # remove ',' at the end of file
            outfile.seek(-1, os.SEEK_END)
            outfile.truncate()

            outfile.write(']')
            outfile.close()
    else:
        json_report(url, filename)
        with open(filename, 'rb+') as outfile:
            # remove ',' at the end of file
            outfile.seek(-1, os.SEEK_END)
            outfile.truncate()

    print("Reporting is Done \nYour output file : " + filename)
    sys.exit(2)
    """
    #TODO: add report only arg
    info = 'more information about this header https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/'
    for head in this_sit_report:
        print(head + " : " + this_sit_report[head] if this_sit_report[head] is not None else head + " : " + info + head)
    """


if __name__ == "__main__":
    print(__doc__)
    main(sys.argv[1:])
