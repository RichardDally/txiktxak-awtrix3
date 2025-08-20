from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get("https://app.mecatran.com/utw/ws/gtfsfeed/realtime/txiktxak?apiKey=0f64273f070b7d4621002040646e180d374e5373")
feed.ParseFromString(response.content)

print("-" * 50)
lol = MessageToDict(feed)
for k, v in lol.items():
    print(k)
    print(v)

print("-" * 50)





# print("-" * 50)
# for entity in feed.entity:
#     x = MessageToDict(entity)
#     for k, v in x.items():
#         print(k)
#         print(v)
#         print("-"*50)
#     if entity.HasField('trip_update'):
#         pass
#         # print(entity.trip_update)
