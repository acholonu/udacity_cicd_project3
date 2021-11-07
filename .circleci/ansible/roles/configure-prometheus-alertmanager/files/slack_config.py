"""Dynamically configuring alertmanager for security purposes.

    Probably could use a feature store instead of environment variable
    in CircleCI.

"""
import os
from yaml import load, dump, FullLoader

def configure_settings():
    with open('alertmanager_template.yml') as file:
        config_content = load(file, Loader=FullLoader)

    # configure slack
    # WEBHOOK = os.getenv['SLACK_WEBHOOK'] # returns None if key doesn't exist
    slack_content = config_content['global']
    slack_content['slack_api_url']=os.environ['slack_api_url'] #this will error out if key doesn't exist

    # configure email
    email_content = config_content['receivers'][0]['email_configs']
    email_settings = email_content[0]
    email_settings['to']=os.environ['MONITOR_EMAIL']
    email_settings['from']=os.environ['MONITOR_EMAIL']
    email_settings['auth_username']=os.environ['MONITOR_EMAIL']
    email_settings['auth_identity']=os.environ['MONITOR_EMAIL']
    email_settings['auth_password']=os.environ['APP_PASSWORD']
    
    with open('alertmanager.yml','w') as f:
        # by default, dump sorts the key by alphabetical order.  I 
        # turned that off.
        config_file=dump(config_content,f,default_flow_style=False, sort_keys=False)


def main():
    configure_settings()

if __name__ == '__main__':
    main()
