# 说明

使用项目[WeChatMsg](https://github.com/LC044/WeChatMsg)时，发现没有办法获取群昵称和人员信息

- 聊天数据均放在MSG.db文件、在MSG表中存储。其中字段BytesExtra存储的是pb序列化后的数据。里面有发送人的微信id
- 联系人信息、群聊信息在MicroMsg.db文件。

> Contact表：联系人
>
> ContactHeadImgUrl： 联系人头像信息
>
> ChatRoom: 群聊信息. 其中RoomData字段放置的pb数据是群成员的微信id和群昵称。
>
> ChatRoomInfo: 群聊详情

这个库主要要来去解析这两个pb序列化后的字段

## 解析

```shell
protoc --decode_raw < msg_data.txt
```

## 根据解析结果，设置.proto文件

```shell
1 {
  1: 16
  2: 0
}
3 {
  1: 1
  2: "wxid_4b1t09d63spw22"
}
3 {
  1: 7
  2: "<msgsource>\n\t<alnode>\n\t\t<fr>2</fr>\n\t</alnode>\n\t<sec_msg_node>\n\t\t<uuid>c6680ab2c57499a1a22e44a7eada76e8_</uuid>\n\t</sec_msg_node>\n\t<silence>1</silence>\n\t<membercount>198</membercount>\n\t<signature>v1_Gj7hfmi5</signature>\n\t<tmp_node>\n\t\t<publisher-id></publisher-id>\n\t</tmp_node>\n</msgsource>\n"
}
3 {
  1: 2
  2: "c13acbc95512d1a59bb686d684fd64d8"
}
3 {
  1: 4
  2: "yiluoAK_47\\FileStorage\\Cache\\2023-08\\2286b5852db82f6cbd9c2084ccd52358"
}
```

## 生成python文件

```shell
protoc --python_out=. msg.proto
```