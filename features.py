from urllib.parse import urlparse
import requests
import string
import ipaddress
import tldextract
import whois
import datetime
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs

#Features:

# 1 'having_IP_Address'
# 2 'URL_Length'
# 3 'Shortining_Service'
# 4 'having_At_Symbol'
# 5 'double_slash_redirecting'
# 6 'Prefix_Suffix'
# 7 'having_Sub_Domain'
# 8 'SSLfinal_State'
# 9 'Domain_registeration_length',
# 10 'Favicon'
# 11 'HTTPS_token'
# 12 'Request_URL'
# 13 'URL_of_Anchor',
# 14 'Links_in_tags'
# 15 'SFH'
# 16 'Submitting_to_email'
# 17 'Redirect'
# 18 'on_mouseover'
# 19 'RightClick'
# 20 'Iframe',
# 21 'age_of_domain'
# 22 'DNSRecord'
# 23 'web_traffic'
# 24 'Page_Rank',
# 25 'Statistical_report'

def f1_having_IP_Address(domain):
    #1. checking hex digits
    domainhex = domain
    domainhex = domainhex.replace(".", "")
    domainhex = domainhex.replace("0x", "0")
    count = 0
    for dig in domainhex:
        if dig in string.hexdigits:
            count+=1

    if(count>=len(domainhex)):
        return -1

    #2. checking direct IP address
    try:
        ipaddress.ip_address(domain)
        return -1
    except:
        return 1

def f2_URL_Length(url):
    if len(url)>=54:
        if len(url)>75:
            return -1
        return 0
    return 1

def f3_Shortening_Service(url):
    services = ['bit.ly', 'tinyurl.com', 'goo.gl', 'tr.im', 'is.gd', 'cli.gs', 'yfrog.com', 'migre.me', 'rebrand.ly', 't.co', 'youtu.be', 'ow.ly', 'w.wiki', 'ff.me', 'tiny.cc', 'ur14.eu', 'twurl.nl', 'snipurl.com', 'short.to' ]
    
    ind = url.find("https://")
    newurl = url
    if(ind!=-1):
        newurl = url[(ind+8):]

    index = newurl.find("/")
    if(index==-1):
        return 1
    service = newurl[:index]

    if service in services:
        return -1
    else:
        return 1

def f4_having_At_Symbol(url):
    if "@" in url:
        return -1
    return 1

def f5_double_slash_redirecting(url):
    pos = url.rfind("//")
    if (pos > 5):
        if (pos > 6):
            return -1
        else:
             return 1
    else:
        return 1

def f6_Prefix_Suffix(domain):
    if "-" in domain:
        return -1
    return 1

def f7_having_sub_domain(domain):
    subdom = domain[3: domain.rfind(".")]
    count = 0
    for pt in subdom:
        if pt==".":
            count+=1
    
    if count>1:
        if count>2:
            return -1
        else:
            return 0
    else:
         return 1

def f9_Domain_registration_length(domain):
    try:
        w = whois.whois(domain)
    except Exception:
        return -1
    else:
        whois_info = whois.whois(domain)
        exp_date = whois_info.expiration_date
        try:
            today = datetime.datetime.now()
            length = exp_date[0] - today
            if length>datetime.timedelta(days=365):
                return 1
            else:
                return -1
        except:
            return -1

def f10_Favicon(domain):
    # icon = soup.find_all("link", rel="shortcut icon")
    # href = icon.get('href')
    # dom = urlparse(href).netloc
    # if(dom!="favicon.ico"):
    #     return -1
    # return 1
    href = []
    for icon in soup.find_all("link", rel="shortcut icon"):
        href.append(icon.get('href'))

    for h in href:
        if(href=="favicon.ico"):
            return 1
        else:
            dom = urlparse(h).netloc
            if (dom!=domain and dom!='' and dom!=b''):
                return -1
    return 1



def f11_HTTPS_token(domain):
    if ("https" in domain) or ("http" in domain):
        return -1
    return 1

def checkperc(oth, cnt):
    perc = 0
    if(cnt!=0):
        perc = (oth*100)/cnt
    return perc

def f12_Request_URL(domain):
    percimg = f121_findsrcdomain('img', domain)
    percvid = f121_findsrcdomain('video', domain)
    percdoc = f121_findsrcdomain('', domain)
    percsound = f121_findsrcdomain('embed', domain)

    perc = percimg + percvid + percdoc + percsound

    if perc>=21:
        if perc>=61:
            return -1
        else:
            return 0
    else:
        return 1

def f121_findsrcdomain(tag, domain):

    srcs = []
    invalidhref = 0
    count = 0

    for t in soup.find_all(tag):
        srcs.append(t.get('src'))

    for src in srcs:
        dom = urlparse(src).netloc
        if (dom!=domain and dom!='' and dom!=b''):
            invalidhref+=1 
        count+=1

    perc = checkperc(invalidhref, count)
    return (perc)

def f13_URl_of_Anchor(domain):
    
    href = []
    count = 0
    invalidhref = 0

    for a in soup.find_all('a'):
        href.append(a.get('href'))
    nullweb = ['#', '#content', '#skip', 'JavaScript ::void(0)']

    for h in href:
        if h in nullweb:
            invalidhref+=1
        else:
            dom = urlparse(h).netloc
            if (dom!=domain and dom!='' and dom!=b''):
                invalidhref+=1 
        count+=1

    perc = checkperc(invalidhref, count)

    if perc>=31:
        if perc>67:
            return -1
        else:
            return 0
    return 1

def f14_Links_in_tags(domain):

    othlink, cntlink = f141_find_domain('link', domain)
    othscript, cntscript = f141_find_domain('script', domain)
    othmeta, cntmeta = f141_find_domain('meta', domain)

    perclink = checkperc(othlink, cntlink)
    percscript = checkperc(othscript, cntscript)
    percmeta = checkperc(othmeta, cntmeta)
    
    perc = perclink + percmeta + percscript
    
    if perc>=17:
        if perc>81:
            return -1
        else:
            return 0
    return 1

def f141_find_domain(tag, domain):
    href = []
    link_other_domain = 0
    count = 0

    for t in soup.find_all(tag):
        href.append(t.get('href'))

    for h in href:
        dom = urlparse(h).netloc
        if (dom!=domain and dom!='' and dom!=b''):
            link_other_domain+=1
        count+=1

    return (link_other_domain, count)

def f16_Submitting_to_email():
    form = str(soup.form)
    email = form.find("mail()")
    if email == -1:
        email = form.find("mailto:")
    if email == -1:
        return 1
    return -1

def f18_on_mouseover():
    if str(soup).lower().find('onmouseover="window.status')!=-1:
        return -1
    return 1

def f19_RightClick():
    if str(soup).lower().find("event.button==2")!=-1:
        return -1
    return 1

def f20_Iframe(result):
    if result=="":
        return -1
    if str(soup.iframe).lower().find("frameborder") == -1:
        return 1
    return -1

def f21_age_of_domain(domain):
    try:
        w = whois.whois(domain)
    except Exception:
        return -1
    else:
        try:
            whois_info = whois.whois(domain)
            cre_date = whois_info.creation_date
            exp_date = whois_info.expiration_date
            age = exp_date[0]-cre_date[0]
            if age>=datetime.timedelta(days=180):
                return 1
            else:
                return -1
        except:
            return -1

def f22_DNSRecord():
    extract_res = tldextract.extract(url)
    url_ref = extract_res.domain + "." + extract_res.suffix
    try:
        whois_res = whois.whois(url)
        return 1
    except:
        return -1

def f23_web_traffic(url):
    try:
        extract_res = tldextract.extract(url)
        url_ref = extract_res.domain + "." + extract_res.suffix
        html_content = requests.get("https://www.alexa.com/siteinfo/" + url_ref).text
        soup = bs(html_content, "lxml")
        value = str(soup.find('div', {'class': "rankmini-rank"}))[42:].split("\n")[0].replace(",", "")
    except:
        return -1
        
    if not value.isdigit():
        return -1

    value = int(value)
    if value < 100000:
        return 1
    return 0


#driver function

features = []

for i in range(25):
    features.append('-')

url =  "https://cse.iiitd.ac.in/"

features[2] = f3_Shortening_Service(url)

if(features[2]==-1):
    ind = url.find("https://")       #remove https if present in tinyurl
    if(ind!=-1):
        url = url[(ind+8):]
    url = requests.head("http://"+url).headers['location']

domain = urlparse(url).netloc

try:
    result = requests.get(url)
    src = result.content
    soup = bs(src, 'lxml')
    flag = 0
except:
    print("Website doesn't exist!")
    for i in range(25):
        features[i]=-1
    flag = 1


if flag==0:

    #domain based features
    features[0] = f1_having_IP_Address(domain)
    features[5] = f6_Prefix_Suffix(domain)
    features[6] = f7_having_sub_domain(domain)
    features[8] = f9_Domain_registration_length(domain)
    features[10] = f11_HTTPS_token(domain)
    features[11] = f12_Request_URL(domain)
    features[12] = f13_URl_of_Anchor(domain)
    features[13] = f14_Links_in_tags(domain)
    features[20] = f21_age_of_domain(domain)

    #url based features
    features[1] = f2_URL_Length(url)
    features[3] = f4_having_At_Symbol(url)
    features[4] = f5_double_slash_redirecting(url)
    features[22] = f23_web_traffic(url)

    #other
    features[15] = f16_Submitting_to_email()
    features[17] = f18_on_mouseover()
    features[18] = f19_RightClick()
    features[19] = f20_Iframe(result)
    features[21] = f22_DNSRecord()
    features[7] = 1
    features[9] = f10_Favicon(domain)

count = 0
for i in range(25):
    if features[i]==0 or features[i]==-1 or features[i]==1:
        print("f", i+1, " = ", features[i])
        count+=1

#url list
#tinyurl.com/4jtbxwtr
#https://tinyurl.com/4jtbxwtr
#https://bit.ly/3hArRGi - phish
