# filter month / day / year
def format_date(date):
    return date.strftime('%m/%d/%y')

from datetime import datetime

# test format_date
# print(format_date(datetime.now()))

# remote extroneous info from URL string, leaving just domain name
def format_url(url):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# test format_url
# print(format_url('http://google.com/test/'))
# print(format_url('https://www.google.com?q=test'))


# correct pluralizing words
def format_plural(amount, word):
    if amount != 1:
        return word + 's'
    
    return word
    
# test format_plural
# print(format_plural(2, 'cat'))
# print(format_plural(1, 'dog'))