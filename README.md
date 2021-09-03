# WaterPhish
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Features to be added](#features-to-be-added)
* [Setup](#setup)


## General info
This website is a uses machine learning to tell if website is phishing or not.

## Technologies:
1. Python             3.9.6
2. beautifulsoup4     4.9.3
3. Flask              1.1.2
4. ipaddress          1.0.23
5. urllib3            1.25.10
6. tldextract         3.1.2
7. whois              0.9.13
8. scikit_learn       0.24.2
9. numpy              1.21.2
10. pandas             1.3.2

## Features:
1. Extracts domain based features:
     a. having_IP_Address
     b. Redirect, Prefix_Suffix
     c. having_sub_domain
     d. Domain_registration_length
     e. HTTPS_token
     f. Request_URL
     g. URl_of_Anchor
     h. Links_in_tags
     i. age_of_domain
     j. DNSRecord
2. Extracts url based features:
     a. URL_Length
     b. having_At_Symbol
     c. double_slash_redirecting
     d. web_traffic
     e. Shortening_Service
3. Extracts JS features:  
     a. Submitting_to_email
     b. on_mouseover
     c. RightClick
     d. Iframe
     e. Favicon

## Features to be added:
1. Database to stored searched queries.
2. Removing saved queries after specific time.

## Setup
To run this project, install libraries given above:

```
$ cd WaterPhish/
$ flask run
```


