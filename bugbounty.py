from bs4 import BeautifulSoup as sp
import requests
url = "https://www.vulnerability-lab.com/list-of-bug-bounty-programs.php"
webpage = requests.get(url=url)
soup = sp(webpage.content,'html.parser')
tables = soup.find_all('table')
a_tags = tables[4].find_all('a')
sites_list = open("bug-bounty-sites.txt","w")
for a in a_tags:
    sites_list.write(a.get('href')+'\n')

site_list = open("bug-bounty-sites.txt",'r')
sites = site_list.readlines()
domains_list = open("bug-bounty-domains.txt","w")
for site in sites:
    if not 'mailto' in site:
        split_site = site.split('/')
        if len(split_site)>1:
            domains_list.write(split_site[2]+'\n')

domains_list = open("bug-bounty-domains.txt","r")
word_list = open("bug-bounty-wordlist.txt","w")
for domain in domains_list.readlines():
    split_domain = domain.split(".")
    if len(split_domain)>1:
        if len(split_domain[-2])>2:
            word_list.write(split_domain[-2]+"\n")
import tldextract
domains_list = open("bug-bounty-domains.txt","r")
word_list = open("bug-bounty-wordlist.txt","w")
for domain in domains_list.readlines():
    tld = tldextract.extract(domain)
    word_list.write(tld.domain+"\n")

# starting shodan django automation
