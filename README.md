# DouBan
douban by go
# API

## JWT

### `/auth  `  	POST

| 请求参数 | 类型 | 说明   |
| -------- | ---- | ------ |
| Username | 必选 | 登录名 |
| Password | 必选 | 密码   |

| 返回参数 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| status   | 状态码                                                       |
| info     | 返回消息                                                     |
| token    | 用户token (使用时携带在header的Authorization 开头加上Bearer 空格隔开 ) 有效期2小时 |

| status | info                     | 说明                 |
| ------ | ------------------------ | -------------------- |
| `2000` | `"success"`              | 成功                 |
| `2001` | `"无效的参数"`           | 参数无效             |
| `2002` | `"鉴权失败"`             | 失败                 |
| `2003` | `"请求头中auth为空"`     | 请求头中auth为空     |
| `2004` | `"请求头中auth格式有误"` | 请求头中auth格式有误 |
| `2005` | `"无效的Token"`          | token无效或过期      |

## user



### `/login  `  	POST

- `application/x-www-form-urlencoded`
- 密码登录



| 请求参数 | 类型 | 说明   |
| -------- | ---- | ------ |
| username | 必选 | 登录名 |
| password | 必选 | 密码   |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status  | info                 | 说明                            |
| ------- | -------------------- | ------------------------------- |
| `false` | `"用户名不存在"`     | `username` 不存在               |
| `false` | `"密码错误"`         | `username` 与 `password` 不匹配 |
| `true`  | `"username登陆成功"` | `loginName` 与 `password` 匹配  |



### `/newuser  `  	POST

- `application/x-www-form-urlencoded`
- 注册账户

| 请求参数 | 类型 | 说明           |
| -------- | ---- | -------------- |
| username | 必选 | 登录名         |
| password | 必选 | 密码           |
| ques1    | 必选 | 密保问题一     |
| ques2    | 必选 | 密保问题二     |
| ans1     | 必选 | 密保问题一答案 |
| ans2     | 必选 | 密保问题二答案 |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status  | info                   | 说明                         |
| ------- | ---------------------- | ---------------------------- |
| `false` | `"用户名超过长度限制"` | `username` 超过长度限制(>20) |
| `false` | `"密码超过长度限制"`   | `password` 超过长度限制(>20) |
| `false` | `"用户名重复了！"`     | `username`重复               |
| `true`  | `""`                   | 成功注册                     |



### `/getques  ` 	POST

- `application/x-www-form-urlencoded`
- 得到密保问题

| 请求参数 | 类型 | 说明   |
| -------- | ---- | ------ |
| username | 必选 | 登录名 |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回信息 |
| data     | 密保问题 |

| status  | info           | 说明       |
| ------- | -------------- | ---------- |
| `false` | `"用户不存在"` | 用户不存在 |
| `true`  | `""`           | 成功       |

### `/findpassword  `  	POST

- `application/x-www-form-urlencoded`
- 找回密码

| 请求参数 | 类型 | 说明           |
| -------- | ---- | -------------- |
| username | 必选 | 登录名         |
| ans1     | 必选 | 密保问题答案一 |
| ans2     | 必选 | 密保问题答案二 |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 密码     |

| status  | info                   | 说明                       |
| ------- | ---------------------- | -------------------------- |
| `false` | `"密保问题答案错误！"` | 两个密保问题答案有任意错误 |
| `true`  | `"找回密码成功"`       | 召回的密码                 |

### `/user/newpassword` 	PUT

| 请求参数    | 类型 | 说明      |
| ----------- | ---- | --------- |
| username    | 必选 | 登录名    |
| BefPassword | 必选 | 旧密码    |
| NewPassword | 必选 | 新密码    |
| **token**   | 必选 | 用户token |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status  | info                   | 说明                |
| ------- | ---------------------- | ------------------- |
| `false` | `"密码错误"`           | 旧密码错误          |
| `false` | `"修改失败"`           | 服务器错误 修改失败 |
| `false` | `"用户不存在"`         | 用户不存在          |
| `false` | `"新密码超过长度限制"` | 新密码超长(>20)     |
| `true`  | `"修改成功"`           | 修改成功            |



### `/getusername` 	POST

| 请求参数 | 类型 | 说明   |
| -------- | ---- | ------ |
| id       | 必选 | 用户ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 用户名   |

| status | info           | 说明       |
| ------ | -------------- | ---------- |
| `200`  | `"获取成功"`   | 成功       |
| `201`  | `"用户不存在"` | 用户不存在 |



### `/user/getuserinfo` 	GET

| 请求参数  | 类型 | 说明      |
| --------- | ---- | --------- |
| **token** | 必选 | 用户token |

| 返回参数 | 说明                             |
| -------- | -------------------------------- |
| status   | 状态码                           |
| info     | 返回消息                         |
| data     | 一个包含用户名，简介，头像的JSON |



### `/user/getwant` 	GET

| 请求参数  | 类型 | 说明      |
| --------- | ---- | --------- |
| **token** | 必选 | 用户token |

| 返回参数 | 说明       |
| -------- | ---------- |
| status   | 状态码     |
| info     | 返回消息   |
| data     | 一串filmid |



### `/user/getwatched` 	GET

| 请求参数  | 类型 | 说明      |
| --------- | ---- | --------- |
| **token** | 必选 | 用户token |

| 返回参数 | 说明       |
| -------- | ---------- |
| status   | 状态码     |
| info     | 返回消息   |
| data     | 一串filmid |



### `/user/updateportrait` 	PUT

更新用户头像	

| 请求参数  | 类型 | 说明      |
| --------- | ---- | --------- |
| **token** | 必选 | 用户token |
| portrait  | 必选 | 头像URL   |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/user/updateintroduction` 	PUT

更新个人简介

| 请求参数     | 类型 | 说明      |
| ------------ | ---- | --------- |
| **token**    | 必选 | 用户token |
| introduction | 必选 | 个人简介  |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



## film

### `/film/getilm  `  	POST

| 请求参数 | 类型 | 说明 |
| -------- | ---- | ---- |
| film_id  | 必选 | id   |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 电影详情 |

| status | info             | 说明     |
| ------ | ---------------- | -------- |
| `true` | `"获取电影成功"` | 获取成功 |



### `/film/addilm  `  	PUT

| 请求参数     | 类型(N/UN) | 说明     |
| ------------ | ---------- | -------- |
| name         | N          | 电影名   |
| directer     | N          | 导演     |
| screenwriter | N          | 编剧     |
| type         | N          | 类型     |
| location     | N          | 地区     |
| language     | N          | 语言     |
| introduction | UN         | 介绍     |
| release_time | N          | 上映时间 |
| length       | N          | 长度     |
| othername    | N          | 别名     |
| IMDb         | N          | IMDb     |
| score        | N          | 评分     |
| post_num     | N          | 评分人数 |
| poster_url   | UN         | 海报图   |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status | info             | 说明     |
| ------ | ---------------- | -------- |
| `true` | `"添加电影成功"` | 获取成功 |



### `/film/deleteilm  `  	DELETE

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| film_id  | N          | 电影id |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status | info         | 说明     |
| ------ | ------------ | -------- |
| `true` | `"删除成功"` | 删除成功 |



### `/film/searchfilm  `  	POST

| 请求参数 | 类型(N/UN) | 说明                          |
| -------- | ---------- | ----------------------------- |
| name     | N          | 搜索的电影名                  |
| aim      | N          | 搜索的对象(name,directer....) |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 搜索结果 |

| status | info         | 说明     |
| ------ | ------------ | -------- |
| `true` | `"搜索成功"` | 搜索成功 |



### `/film/superserch  `  	POST

| 请求参数     | 类型(N/UN) | 说明     |
| ------------ | ---------- | -------- |
| type         | N          | 电影类型 |
| location     | N          | 地区     |
| release_time | N          | 上映时间 |
| tag          | N          | 标签     |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 搜索结果 |

| status | info | 说明 |
| ------ | ---- | ---- |
| `true` | 成功 | 成功 |



### `/filmlist` 	GET

获取排行榜

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 嵌套JSON |



## shortpost

### `/shortpost/addshortpost` 	PUT

| 请求参数 | 类型(N/UN) | 说明      |
| -------- | ---------- | --------- |
| token | N          | token    |
| film_id  | N          | 电影ID    |
| txt      | N          | 内容      |
| score    | N          | 分数      |
| want     | N          | 想看(0/1) |
| watched  | N          | 看过(0/1) |
| likes    | N          | 点赞数    |
| tags     | N          | 标签      |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status | info         | 说明 |
| ------ | ------------ | ---- |
| `true` | 添加短评成功 | 成功 |



### `/shortpost/getshortpostbyfilmid`   	POST

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| film_id  | N          | 电影ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 数据     |

| status | info     | 说明 |
| ------ | -------- | ---- |
| `true` | 搜索成功 | 成功 |

### `/shortpost/getshortpostsofuser`  	GET

| 请求参数 | 类型(N/UN) | 说明  |
| -------- | ---------- | ----- |
| token    | N          | token |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 数据     |



### `/shortpost/deleteshortpost` 	DELETE

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| post_id  | N          | PostID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status | info     | 说明 |
| ------ | -------- | ---- |
| `true` | 删除成功 | 成功 |



### `/shortpost/updateshortpost` 	PUT

| 请求参数 | 类型(N/UN) | 说明      |
| -------- | ---------- | --------- |
| username | N          | 电影类型  |
| film_id  | N          | 电影ID    |
| txt      | N          | 内容      |
| score    | N          | 分数      |
| want     | N          | 想看(0/1) |
| watched  | N          | 看过(0/1) |
| likes    | N          | 点赞数    |
| tags     | N          | 标签      |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status | info     | 说明 |
| ------ | -------- | ---- |
| `true` | 更新成功 | 成功 |



## longpost

### `/longpost/getlongpostbyfilmid` 	POST

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| film_id  | N          | 电影ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| num      | 影评个数 |
| data     | 嵌套JSON |



### `/longpost/addlongpost` 	PUT

| 请求参数    | 类型(N/UN) | 说明   |
| ----------- | ---------- | ------ |
| film_id     | N          | 电影ID |
| txt         | N          | 内容   |
| score       | N          | 分数   |
| likes       | N          | 赞     |
| dislikes    | N          | 踩     |
| title       | N          | 标题   |
| comment_num | N          | 标签   |
| token       | N          | token  |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/longpost/deletelongpost` 	DELETE

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| post_id  | N          | 影评ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/longpost/likelongpost` 	PUT

点赞影评

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| post_id  | N          | 影评ID |
| token    | N          | token  |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/longpost/dislikelongpost` 	PUT

踩影评

| 请求参数  | 类型(N/UN) | 说明   |
| --------- | ---------- | ------ |
| post_id   | N          | 影评ID |
| **token** | N          | token  |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/longpost/updatelongpost	`PUT

| 请求参数  | 类型(N/UN) | 说明   |
| --------- | ---------- | ------ |
| post_id   | N          | 影评ID |
| title     | N          | 标题   |
| score     | N          | 评分   |
| txt       | N          | 正文   |
| **token** | N          | token  |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



## lpcomment

影评回复



### `/lpcomment/addlpcomment` 	PUT

发表影评回复

| 请求参数  | 类型(N/UN) | 说明   |
| --------- | ---------- | ------ |
| post_id   | N          | 影评ID |
| txt       | N          | 正文   |
| **token** | N          | token  |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/lpcomment/getlpcomment` 	post

获取影评回复

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| post_id  | N          | 影评ID |

| 返回参数 | 说明               |
| -------- | ------------------ |
| status   | 状态码             |
| info     | 返回消息           |
| data     | 嵌套JSON，包含数据 |

 

### `lpcomment/deletelpcomment`	DELETE

| 请求参数     | 类型(N/UN) | 说明       |
| ------------ | ---------- | ---------- |
| lpcomment_id | N          | 影评回复ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



## actor

演员

### `/actor/addactor`	PUT

| 请求参数     | 类型(N/UN) | 说明     |
| ------------ | ---------- | -------- |
| name         | N          | 姓名     |
| mainrole     | N          | 主要职能 |
| sex          | N          | 性别     |
| introduction | N          | 个人简介 |
| picture_yrl  | N          | 头像     |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/actor/getactordetail`	POST

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| actor_id | N          | 演员ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |

| status | info           | 说明       |
| ------ | -------------- | ---------- |
| 200    | `"搜索成功"`   | 获取成功   |
| 201    | `"未找到演员"` | 演员ID有误 |



### `/actor/deleteactor`	DELETE

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| actor_id | N          | 演员ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/actor/getactorbyfilmid`	POST

获取电影参演演员

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| film_id  | N          | 电影ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 嵌套JSON |



### `/actor/getfilmids`

获取演员参演电影

| 请求参数 | 类型(N/UN) | 说明    |
| -------- | ---------- | ------- |
| actor_id | N          | actorID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| num      | 数目     |
| data     | 嵌套JSON |



## act

参演表

### `/act/addact`	PUT

| 请求参数 | 类型(N/UN) | 说明     |
| -------- | ---------- | -------- |
| actor_id | N          | actorId  |
| film_id  | N          | filmId   |
| role     | N          | 参演角色 |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



## POST

讨论区帖子

### `/post/addpost`

| 请求参数  | 类型(N/UN) | 说明  |
| --------- | ---------- | ----- |
| txt       | N          | 正文  |
| title     | N          | 标题  |
| **token** | N          | token |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/post/modifypost`	POST

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| txt      | N          | 正文   |
| title    | N          | 标题   |
| post_id  | N          | 帖子ID |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/post/lookpost`	GET

获取所有帖子

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 数据     |



### `/post/postdetail` GET

查看一条帖子详细信息和其下属评论

| 请求参数 | 类型(N/UN) | 说明   |
| -------- | ---------- | ------ |
| post_id  | N          | 帖子ID |

| status     | 状态码   |
| ---------- | -------- |
| 返回参数   | 说明     |
| info       | 返回消息 |
| commentnum | 回复人数 |
| comments   | 回复     |
| post       | 帖子     |



## comment



### `/comment/addcomment` POST

| 请求参数   | 类型(N/UN) | 说明           |
| ---------- | ---------- | -------------- |
| comment_id | N          | ID             |
| txt        | N          | txt            |
| iscomcom   | N    (0/1) | 是否是评论套娃 |
| **token**  | N          | token          |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/comment/modifycomment` POST

| 请求参数   | 类型(N/UN) | 说明  |
| ---------- | ---------- | ----- |
| comment_id | N          | ID    |
| txt        | N          | txt   |
| title      | N          | title |
| **token**  | N          | token |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/comment/dropcomment`	DELETE

| 请求参数   | 类型(N/UN) | 说明 |
| ---------- | ---------- | ---- |
| comment_id | N          | ID   |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/comment/commentdetail`	POST

| 请求参数   | 类型(N/UN) | 说明 |
| ---------- | ---------- | ---- |
| comment_id | N          | ID   |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 数据     |



## filmpicture

剧照

### `/filmpicture/addfilmpicture`PUT

| 请求参数 | 类型(N/UN) | 说明 |
| -------- | ---------- | ---- |
| film_id  | N          | ID   |
| url      | N          | url  |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |



### `/filmpicture/getfilmpictures` post

| 请求参数 | 类型(N/UN) | 说明 |
| -------- | ---------- | ---- |
| film_id  | N          | ID   |

| 返回参数 | 说明     |
| -------- | -------- |
| status   | 状态码   |
| info     | 返回消息 |
| data     | 数据     |
