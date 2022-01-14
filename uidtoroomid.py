
import requests
import json


def get_livestatus(uid):
    url = 'https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids'
    header = {'Content-Type': 'application/json'}
    middle = {'uids': [uid]}
    payload = json.dumps(middle)
    r = requests.post(url, data=payload, headers=header)
    dict = r.json()
    statusvalue = dict["data"][str(uid)]['room_id']
    return statusvalue




def main():
    Members = ['489412051','388657573','672328094','2832224','27363163']
    room=[]
    for member in Members:

        judge = get_livestatus(member)
        room.append(judge)

        # print(judge)
    return room



if __name__ == '__main__':
    print(main())
