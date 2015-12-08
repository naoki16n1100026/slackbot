# -*- coding: utf-8 -*-
import sys
from private import TOKEN
from slacker import Slacker

class Slack(object):

    __slacker = None

    def __init__(self, token):
        self.__slacker = Slacker(token)
        
    def get_channnel_list(self):
        """
        Slackチーム内のチャンネルID、チャンネル名一覧を取得する。
        """
        # bodyで取得することで、[{チャンネル1},{チャンネル2},...,]の形式で取得できる。
        raw_data = self.__slacker.channels.list().body

        channnels = []
        for data in raw_data["channels"]:
            channnels.append(dict(channel_id=data["id"], channel_name=data["name"]))
        return channnels

    def post_to_file(self, file_path, channel):
        result = self.__slacker.files.upload(file_path, channels=[channel])
        self.__slacker.pins.add(channel=channel, file_=result.body['file']['id'])

if __name__ == "__main__":

    param = sys.argv
    file_path = param[1]

    slack = Slack(TOKEN)
    channnels = slack.get_channnel_list()
    slack.post_to_file(file_path, channnels[0]["channel_id"])
    


