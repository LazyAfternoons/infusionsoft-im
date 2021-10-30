# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from infusionsoft.infusionsoft import Infusionsoft


def test():
    infusionsoft = Infusionsoft('xQVp45csXdgxvDYaEZNNNqonC4Kx8FOg', 'UUxUkviH6uIxpebf')
    if infusionsoft.is_token_serialized():
        print("Serialized token found")
        token = infusionsoft.deserialize_token()
        infusionsoft.set_token(token)
        print(token.access_token)
        if token.is_expired():
            print("Refreshing Token")
            infusionsoft.refresh_token()
    elif len(sys.argv) == 4:
        print("Creating a new token")
        access_token = sys.argv[1]
        refresh_token = sys.argv[2]
        end_of_life = sys.argv[3]
        token = infusionsoft.get_new_token(access_token, refresh_token, end_of_life)
        infusionsoft.set_token(token)
    else:
        print("No serialized token found or input parameters provided")
        sys.exit()

    infusionsoft.set_debug(True)
    params = {
        "email_addresses": [
            {
                "email": "test@test.it",
                "field": "EMAIL1"
            }
        ],
          "given_name": "string",
          "job_title": "string",
          "lead_source_id": 0,
          "middle_name": "string",
          "opt_in_reason": "string"
        }
    #print(infusionsoft.contact().create_contact(params))
    #print(infusionsoft.email().list_emails())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
