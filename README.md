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
1. Extracts domain based features:<br />
     a. having_IP_Address<br />
     b. Redirect, Prefix_Suffix<br />
     c. having_sub_domain<br />
     d. Domain_registration_length<br />
     e. HTTPS_token<br />
     f. Request_URL<br />
     g. URl_of_Anchor<br />
     h. Links_in_tags<br />
     i. age_of_domain<br />
     j. DNSRecord<br /><br />
2. Extracts url based features:<br />
     a. URL_Length<br />
     b. having_At_Symbol<br />
     c. double_slash_redirecting<br />
     d. web_traffic<br />
     e. Shortening_Service<br /><br />
3. Extracts JS features:  <br />
     a. Submitting_to_email<br />
     b. on_mouseover<br />
     c. RightClick<br />
     d. Iframe<br />
     e. Favicon<br />

## Features to be added:
1. Database to stored searched queries.
2. Removing saved queries after specific time.

## Setup
To run this project, install libraries given above:

```
$ cd WaterPhish/
$ flask run
```
![image](https://user-images.githubusercontent.com/50488701/131995995-4482b5fd-6313-4f1f-bdca-afbd34e0c8bf.png)
![image](https://user-images.githubusercontent.com/50488701/131996049-3a68b4d4-a359-4e6e-8030-cc08f41fe49b.png)


