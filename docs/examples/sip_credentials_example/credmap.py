from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory

from zang.domain.enums.http_method import HttpMethod
from docs.examples.credentials import sid, authToken

url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
sipDomainsConnector = ConnectorFactory(configuration).sipDomainsConnector

# map credentials list
try:
    credentialsList = sipDomainsConnector.mapCredentialsLists(
        'DomainSid', 'CredentialListSid')
    view = vars(credentialsList)
    print('credentials mapped')
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)
