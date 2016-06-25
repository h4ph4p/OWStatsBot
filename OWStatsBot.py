import praw
import datetime
import traceback
import json
from collections import OrderedDict
from time import sleep
from userinfo import reddit, settings

SLEEP_TIME   = 30
DATA_SOURCE  = settings['json_source']
TABLE_HEADER = 'Attribute|Value\n-|-\n'

# Authenticate to Reddit using OAuth
r = praw.Reddit(user_agent=reddit['user_agent'])
r.set_oauth_app_info(client_id=reddit['client_id'],
                    client_secret=reddit['client_secret'],
                    redirect_uri=reddit['redirect_uri'])
r.refresh_access_information(reddit['refresh_token'])


def main():
    print(reddit['user_agent'])
    print(datetime.datetime.now())

    running = True
    while running:
        try:
            mentions = r.get_mentions()
            mentions = list(mentions)

            # Check for new mentions
            for comment in mentions:
                if not comment.new:
                    continue

                # Extract hero and ability arguments
                hero = get_args(comment.body)[0]
                ability = get_args(comment.body)[1]
                # Parse the json file and print data in Reddit table format
                if hero and ability:
                    text = ''
                    data = parse_json(hero, ability)
                    for k, v in data.iteritems():
                        text += (k + '|' + v + '\n')

                    reply_to_user(comment, text)

            sleep(SLEEP_TIME)
        except KeyboardInterrupt:
            running = False
        except Exception as e:
            now = datetime.datetime.now()
            print now.strftime("%d-%m-%Y %H:%M")
            print traceback.format_exc()
            print 'ERROR:', e
            print 'Bot is snoozing for 30seconds\n'
            sleep(SLEEP_TIME)
            continue


# Parse a comment, searching for valid usage parameters
def get_args(comment):
    txt = comment.lower().split('\n\n')
    args = ''
    for line in txt:
        if line.startswith('/u/owstatsbot'):
            args = line.split()
    args = args[1:]
    return args


# Parse the json file, return the requested data in order
def parse_json(hero, ability):
    with open(DATA_SOURCE) as data_file:
        data = json.load(data_file, object_pairs_hook=OrderedDict)
    info = data.get(hero).get(ability)
    return info


# Adds the Reddit table header and a signature at the end of the reply
def add_header_signature(text):
    signature = '\n[How to use /u/OWStatsBot](https://github.com/h4ppily/OWStatsBot#usage) | ' \
            '[GitHub](https://github.com/h4ppily/OWStatsBot) | ' \
            '[Twitter](https://twitter.com/h4ppilyxyz)\n\n'
    signature += 'If you have any suggestions please PM me.'
    return TABLE_HEADER + text + signature


# Replies to the requested comment and marks it as read.
def reply_to_user(comment, reply):
    now = datetime.datetime.now()
    print now.strftime("%d-%m-%Y %H:%M")
    print "Replied to %s\'s request." % comment.author.name
    comment.reply(add_header_signature(reply))
    comment.mark_as_read()


if __name__ == "__main__":
    main()
