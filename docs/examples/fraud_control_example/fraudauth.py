from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory


from docs.examples.credentials import sid, authToken
url = 'https://api.zang.io/v2'

configuration = Configuration(sid, authToken, url=url)
fraudControlConnector = ConnectorFactory(configuration).fraudControlConnector

# authorize destination
try:
    rule = fraudControlConnector.authorizeDestination('HR') #Country Code, Enable Mobile, Enable Landline, Enable SMS
    view = vars(rule)
    print('\n')
    for item in view:
        print (item , ' : ' , view[item])
except ZangException as ze:
    print(ze)