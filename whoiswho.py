import td
import json
import sys

if not td.authorize():
    sys.exit('Not authorized')

contacts = {user['id']: user['last_name'] + ' ' + user['first_name'] for user in td.get_users(td.get_contacts())}

with open('names.txt', mode = 'wb') as out:
    out.write(json.dumps(contacts, ensure_ascii=False, indent='\t').encode())
