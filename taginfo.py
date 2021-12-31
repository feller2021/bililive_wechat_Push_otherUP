import requests
import json

url = 'https://api.live.bilibili.com/room/v1/Room/get_status_info_by_uids'
header = {'Content-Type': 'application/json'}


def area_v2_name(uid):
    middle = {'uids': [uid]}
    payload = json.dumps(middle)
    r = requests.post(url, data=payload, headers=header)
    dict = r.json()

    area_v2_name = dict["data"][str(uid)]['area_v2_name']
    try:
        area_v2_parent_name = dict["data"][str(uid)]['area_v2_parent_name']
    except:
        area_v2_parent_name=''

    try:
        tag_name=dict["data"][str(uid)]['tag_name']
    except:
        tag_name=''

    try:
        tags=dict["data"][str(uid)]['tags']
    except:
        tags=''



    return area_v2_name,area_v2_parent_name,tag_name,tags


def main(uid):
    uid = uid
    Members = [uid]
    tagss = ""
    for member in Members:
        judge = area_v2_name(member)
        judge=str(judge)
        tagss+=judge

        # print(judge)
    return tagss


# if __name__ == '__main__':
#     fgh=main()
#
#     fgh=fgh.replace("'", "")
#     fgh = fgh.replace("(", "")
#     fgh = fgh.replace(")", "")
#     fgh = fgh.replace(",", " ")
#     fgh = fgh.replace("  ", " ")
#     print(fgh)


def tags(uid):
    fgh = main(uid)

    fgh = fgh.replace("'", "")
    fgh = fgh.replace("(", "")
    fgh = fgh.replace(")", "")
    fgh = fgh.replace(",", " ")
    fgh = fgh.replace("  ", " ")
    return fgh





