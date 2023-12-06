from msg_pb2 import MessageBytesExtra
from roomdata_pb2 import ChatRoomData

txt = open("roomdata.txt", 'rb')
chatroom = ChatRoomData()
chatroom.ParseFromString(txt.read())
print(chatroom)

msg = open("msg_data.txt", 'rb')
msgbytes = MessageBytesExtra()
msgbytes.ParseFromString(msg.read())
print(msgbytes)
