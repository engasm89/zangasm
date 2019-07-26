from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from docs.examples.credentials import sid, authToken

url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
sipDomainsConnector = ConnectorFactory(configuration).sipDomainsConnector

# list domains
try:
    domains = sipDomainsConnector.listDomains()
    view = vars(domains)
    for item in view:
        print (item , ' : ' , view[item])
    for listdomain in domains.elements:
        domain = sipDomainsConnector.viewDomain(listdomain.sid)
        view = vars(domain)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)