# [OWStatsBot](http://reddit.com/u/OWStatsBot)

/u/OWStatsBot will listen for mentions on Reddit and reply to your comment if a valid call is found. It will respond with the data in a key-pair value, formatted using Reddit tables.

Usage
-----
* Simply make a comment in any publically available subreddit with the bots username + hero + abilities default PC keybind (separated by spaces).
* /u/OWStatsBot can be anywhere in your comment, as long as it's on a new line by itself.
* NOTE: You can only call the bot once per comment.

Examples
------------
* /u/OWStatsBot dva shift
* /u/OWStatsBot soldier76 stats
* /u/OWStatsBot torbjorn shift

Calls
------------
You can call one ability on any hero. Below is a list of the possible calls:
* `stats, lmb, rmb, shift, e, q`

Details
------------
/u/OWStatsBot was written to run in Python 2.7 and PRAW 3.5, it has the following dependency:
* PRAW (Reddit Python API)

You can install PRAW using PIP found [here](https://pip.pypa.io/en/stable/installing/).


