
# Table Diagram of Models

```ascii
+-----------------+          +----------------+         +-----------------+         +-------------+
|     Follows     |          |     Likes      |         |      User       |         |   Message   |
+-----------------+          +----------------+         +-----------------+         +-------------+
|user_being_followed_id |    |      id        |         |       id        |         |      id     |
|user_following_id      |    |    user_id     |         |     email       |         |     text    |
+-----------------+          |   message_id   |         |    username     |         |  timestamp  |
                             +----------------+         |   image_url     |         |   user_id   |
                                                        | header_image_url|         +-------------+
                                                        |       bio       |
                                                        |    location     |
                                                        |    password     |
                                                        +-----------------+
```
