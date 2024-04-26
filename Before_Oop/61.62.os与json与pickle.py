import json
import pickle

datas = {
    "student": [

    ],
    "course": [
    ],
}

with open("test.txt", "r+") as f:
    serial_data = f.read()
    cur_datas = json.loads(serial_data)
    cur_datas["student"].append({"id": 101, "name": 'aaa'})
    # print(cur_datas, type(cur_datas))
    cur_datas = json.dumps(cur_datas)
    cur_datas = cur_datas.replace(', "course"', ',\n"course"')
    cur_datas = cur_datas.replace('}, {', '},\n{')
    f.seek(0)
    f.write(cur_datas)
# with open("test.txt", "w") as f:
#     serial_data = json.dumps(datas)
#     f.write(serial_data)
#
# with open("test.txt", "r") as f:
#     serial_data = f.read()
#     datas = json.loads(serial_data)
#     print(datas, type(datas))
