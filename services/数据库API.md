# ��ĿĿ¼�ṹ��
```
services/
��
������ classes/
��   ������ __init__.py
��   ������ activity.py
��   ������ post.py
��   ������ row_to_class.py
��   ������ topic.py
��   ������ users.py
��
������ connection/
��   ������ __init__.py
��   ������ connection.py
��   ������ DatabaseConfig.py
��
������ sql/
��   ������ sql.sql
��
������ __init__.py
������ activity_service.py
������ post_service.py
������ tag_service.py
������ topic_service.py
������ user_service.py
```

## ��Ҫģ��˵��

1. **����ģ��(classes/)**
   - ����Ӧ�ú������ݽṹ��Python��
   - ����������ӡ����⡢�û���ģ�Ͷ���
   - `row_to_class.py`�ṩ���ݿ��е�Python�����ת������

2. **���ݿ�����(connection/)**
   - ��װ�������ݿ���������߼�
   - �������ӳع�������ü���

3. **����ģ��**
   - �ṩ����ҵ�����ӿ�
   - ÿ�������Ӧһ������ҵ������
   - ��ѭͳһ��API��ƹ淶

4. **SQL�ű�(sql/)**
   - ���ݿ��ʼ���ű�
   - ��ṹ�ͻ������ݶ���

# Ŀ¼��

* [1. ����ֵ��ʽ�淶](#1����ֵ��ʽ�淶)
* [2. ����ģ�Ͷ���](#2����ģ�Ͷ���)
    * [2.1 �ģ��](#21-�ģ��)
    * [2.2 �û�ģ��](#22-�û�ģ��)
    * [2.3 ����ģ��](#23-����ģ��)
    * [2.4 ����ģ��](#24-����ģ��)
* [3. ���ݿ�ģ��](#3���ݿ�ģ��)
    * [3.1 �������ݱ�](#31-�������ݱ�)
        * [3.1.1 �û���](#311-�û���)
        * [3.1.2 ���](#312-���)
        * [3.1.3 ���ӱ�](#313-���ӱ�)
        * [3.1.4 �����](#314-�����)
        * [3.1.5 ��ǩ��](#315-��ǩ��)
    * [3.2 ������ϵ��](#32-������ϵ��)
        * [3.2.1 �û����](#321-�û����)
        * [3.2.2 �ղع�ϵ��](#322-�ղع�ϵ��)
        * [3.2.3 ���ݹ�����](#323-���ݹ�����)
        * [3.2.4 ��ǩ������](#324-��ǩ������)
        * [3.2.5 ���޹�����](#325-���޹�����)
    * [3.3 �������ݱ�](#33-�������ݱ�)
        * [3.3.1 ���۱�](#331-���۱�)
        * [3.3.2 �˶����ݱ�](#332-�˶����ݱ�)
* [4. ���ݿ�API�ӿ�](#4���ݿ�api�ӿ�)
    * [4.1 �����](#41-�����)
        * [4.1.1 ����»](#411-����»)
        * [4.1.2 ɾ���](#412-ɾ���)
        * [4.1.3 ��ȡ��ҳ�����](#413-��ȡ��ҳ�����)
        * [4.1.4 ��ȡ�����](#414-��ȡ�����)
        * [4.1.5 �޸Ļ��Ϣ](#415-�޸Ļ��Ϣ)
    * [4.2 ���ӷ���](#42-���ӷ���)
        * [4.2.1 ���������](#421-���������)
        * [4.2.2 ɾ������](#422-ɾ������)
        * [4.2.3 ��ȡ��������](#423-��ȡ��������)
        * [4.2.4 ��ȡ��������](#424-��ȡ��������)
        * [4.2.5 ��ȡ��������](#425-��ȡ��������)
        * [4.2.6 ��������](#426-��������)
        * [4.2.7 ɾ������](#427-ɾ������)
        * [4.2.8 ��������](#428-��������)
        * [4.2.9 ȡ������](#429-ȡ������)
        * [4.2.10 �ղ�����](#4210-�ղ�����)
        * [4.2.11 ȡ���ղ�](#4211-ȡ���ղ�)
    * [4.3 ��ǩ����](#43-��ǩ����)
        * [4.3.1 �����±�ǩ](#431-�����±�ǩ)
        * [4.3.2 Ϊ���ӹ�����ǩ](#432-Ϊ���ӹ�����ǩ)
        * [4.3.3 Ϊ�������ǩ](#433-Ϊ�������ǩ)
    * [4.4 �������](#44-�������)
        * [4.4.1 ����»���](#441-����»���)
        * [4.4.2 ɾ������](#442-ɾ������)
        * [4.4.3 ��ȡ���Ż���](#443-��ȡ���Ż���)
        * [4.4.4 ��ȡ�����������](#444-��ȡ�����������)
    * [4.5 �û�����](#45-�û�����)
        * [4.5.1 ������û�](#451-������û�)
        * [4.5.2 ɾ���û�](#452-ɾ���û�)
        * [4.5.3 ��ȡ�û���Ϣ](#453-��ȡ�û���Ϣ)
        * [4.5.4 �����û���Ϣ](#454-�����û���Ϣ)
        * [4.5.5 �����](#455-�����)
        * [4.5.6 ȡ������](#456-ȡ������)
        * [4.5.7 �ղػ](#457-�ղػ)
        * [4.5.8 ��ȡ�û�����](#458-��ȡ�û�����)
        * [4.5.9 ��ȡ�û��ղ�����](#459-��ȡ�û��ղ�����)
        * [4.5.10 ��ȡ�û��ղػ](#4510-��ȡ�û��ղػ)
        * [4.5.11 ȡ���ղػ](#4511-ȡ���ղػ)
        * [4.5.12 ��ȡ�û���������](#4512-��ȡ�û���������)
        * [4.5.13 ��ȡ�û������](#4513-��ȡ�û������)
        * [4.5.14 ��¼�˶�����](#4514-��¼�˶�����)
        * [4.5.15 ��ȡ�˶�����](#4515-��ȡ�˶�����)

# 1.����ֵ��ʽ�淶

**����ѯ�ɹ�ʱ��**
```json
{
    "success": true,
    "message": "��ѯ�ɹ���",
    "data": "������������"
}
```
**����ѯʧ��ʱ��**
```json
{
    "success": false,
    "message": "��ѯʧ�ܣ�",
    "detail": "����������Ϣ"
}
```

**�ֶ�˵��**
* ```success```: ����ֵ����ʶ�����Ƿ�ɹ�
* ```message```: ���������״̬��Ϣ
* ```data```: �����ɹ�ʱ���ص�ҵ������
* ```detail```: ����ʧ��ʱ����ϸ����˵��

**������˵��**
��```detail```�ֶΰ������¹ؼ���ʱ����������ϵͳ������⣬�뼰ʱ������
* ȱ�ٱ�Ҫ�ֶ�
* ���ݱ�����
* �ֶβ�����
* SQL������

����ֵ������Ӣ�ģ���˵����ʱ�������������ݿ��ڲ���������**AI**ѯ��������ݡ�


# 2.����ģ�Ͷ���
## 2.1 �ģ��
```python
class activity:
    def __init__(self, title : str, data : str, location : str, calorie : int, duration : int, weather : int, start_place : str,
                 end_place : str, time : str, difficulty : str, type : str, image : str, star_count : int):
        self.title = title                  # ����
        self.data = data                    # �����
        self.location = location            # ��ص�
        self.calorie = calorie              # ���Ŀ�·��
        self.duration = duration            # ʱ�������ӣ�
        self.weather = weather              # ����
        self.start_place = start_place      # ���
        self.end_place = end_place          # �յ�
        self.time = time                    # �ʱ��
        self.difficulty = difficulty        # �Ѷ�
        self.type = type                    # �����
        self.image = image                  # ͼ��λ��
        self.star_count = star_count        # �ղ�����
```
## 2.2 �û�ģ��
```python
class user:
    def __init__(self, name : str, avatar : str, level : int, points : int, days : int, phone_number : str,
                 register_time : str, account : str, password : str, open_id : str, union_id : str):
        self.name = name                    # �ǳ�
        self.avatar = avatar                # ͷ��URL
        self.level = level                  # �ȼ�
        self.points = points                # ��������
        self.days = days                    # ����
        self.phone_number = phone_number    # �ֻ���
        self.register_time = register_time  # ע��ʱ��
        self.account = account              # �˺�
        self.password = password            # ����
        self.open_id = open_id              # ΢��open_id
        self.union_id = union_id            # ΢��union_id
```
## 2.3 ����ģ��
```python
class post:
    def __init__(self,user_id : int, post_time : str, title : str, content : str, activity : list, topics : list,
                 like_count : int, star_count : int):
        self.user_id = user_id              # ������
        self.post_time = post_time          # ����ʱ��
        self.title = title                  # ����
        self.content = content              # ����
        self.activity = activity            # �����������
        self.topics = topics                # �������������
        self.like_count = like_count        # ������
        self.star_count = star_count        # �ղ���
```
## 2.4 ����ģ��
```python
class topic:
    def __init__(self, title : str, description : str, color : str, icon : str, image : str):
        self.title = title                  # ����
        self.description = description      # ����
        self.color = color                  # ��ɫ
        self.icon = icon                    # ͼ��
        self.image = image                  # ͼ���ַ
```
��������ݽṹδ������ģ��

# 3.���ݿ�ģ��

## 3.1 �������ݱ�

### 3.1.1 �û���

```sql
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '�û�ID(PK)',
  `name` varchar(20) DEFAULT NULL COMMENT '�û��ǳ�',
  `avatar` varchar(100) DEFAULT NULL COMMENT 'ͷ��URL',
  `level` int DEFAULT NULL COMMENT '�û��ȼ�',
  `points` int DEFAULT NULL COMMENT '��������',
  `days` int DEFAULT NULL COMMENT '��������',
  `phone_number` varchar(20) DEFAULT NULL COMMENT '�ֻ���',
  `register_time` datetime DEFAULT NULL COMMENT 'ע��ʱ��',
  `account` varchar(20) DEFAULT NULL COMMENT '�˺�',
  `password` varchar(20) DEFAULT NULL COMMENT '����',
  `open_id` varchar(30) DEFAULT NULL COMMENT '΢��openId',
  `union_id` varchar(30) DEFAULT NULL COMMENT '΢��unionId',
  PRIMARY KEY (`id`)
) COMMENT='�û���';
```

### 3.1.2 ���
```sql
CREATE TABLE `activities` (
  `activity_id` int NOT NULL AUTO_INCREMENT COMMENT '�ID(PK)',
  `title` varchar(30) DEFAULT NULL COMMENT '����',
  `date` date DEFAULT NULL COMMENT '�����',
  `location` varchar(60) DEFAULT NULL COMMENT '��ص�',
  `calorie` int DEFAULT NULL COMMENT '���Ŀ�·��',
  `duration` int DEFAULT NULL COMMENT 'ʱ��(����)',
  `weather` int DEFAULT NULL COMMENT '����',
  `start_place` varchar(60) DEFAULT NULL COMMENT '���',
  `end_place` varchar(60) DEFAULT NULL COMMENT '�յ�',
  `time` time DEFAULT NULL COMMENT '�ʱ��',
  `difficulty` varchar(10) DEFAULT NULL COMMENT '�Ѷ�',
  `type` varchar(15) DEFAULT NULL COMMENT '�����',
  `image` varchar(150) DEFAULT NULL COMMENT '�ͼƬURL',
  `star_count` int DEFAULT NULL COMMENT '�ղ���',
  PRIMARY KEY (`activity_id`)
) COMMENT='���';
```

### 3.1.3 ���ӱ�
```sql
CREATE TABLE `blogs` (
  `blog_id` int NOT NULL AUTO_INCREMENT COMMENT '����ID(PK)',
  `user_id` int DEFAULT NULL COMMENT '�û�ID(FK)',
  `activity_id` int DEFAULT NULL COMMENT '�ID(FK)',
  `post_time` datetime DEFAULT NULL COMMENT '����ʱ��',
  `title` varchar(50) DEFAULT NULL COMMENT '����',
  `content` varchar(1024) DEFAULT NULL COMMENT '����',
  `like_count` int DEFAULT NULL COMMENT '������',
  `star_count` int DEFAULT NULL COMMENT '�ղ�����',
  PRIMARY KEY (`blog_id`),
  KEY `activity_id` (`activity_id`),
  KEY `blogs_ibfk_1` (`user_id`),
  CONSTRAINT `blogs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `blogs_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='���ӱ�';
```

### 3.1.4 �����
```sql
CREATE TABLE `topic` (
  `topic_id` int NOT NULL AUTO_INCREMENT COMMENT '����ID(PK)',
  `title` varchar(50) DEFAULT NULL COMMENT '����',
  `description` varchar(255) DEFAULT NULL COMMENT '��������',
  `color` varchar(20) DEFAULT NULL COMMENT '����ɫ',
  `icon` varchar(150) DEFAULT NULL COMMENT 'ͼ��',
  `image` varchar(150) DEFAULT NULL COMMENT '����ͼƬ',
  PRIMARY KEY (`topic_id`)
) COMMENT='�����';
```
### 3.1.5 ��ǩ��
```sql
CREATE TABLE `labels` (
  `label_id` int NOT NULL AUTO_INCREMENT COMMENT '��ǩID(PK)',
  `content` varchar(30) DEFAULT NULL COMMENT '����',
  PRIMARY KEY (`label_id`)
) COMMENT='��ǩ��';
```
## 3.2 ������ϵ��
### 3.2.1 �û����
```sql
CREATE TABLE `enroll` (
  `user_id` int NOT NULL COMMENT '�û�ID(FK)',
  `activity_id` int NOT NULL COMMENT '�ID(FK)',
  `enroll_time` datetime DEFAULT NULL COMMENT '����ʱ��',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='�û��������';

CREATE TABLE `user_activity` (
  `user_id` int NOT NULL COMMENT '�û�ID(FK)',
  `activity_id` int NOT NULL COMMENT '�ID(FK)',
  `status` varchar(20) DEFAULT NULL COMMENT '�״̬',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='�û��������';
```
### 3.2.2 �ղع�ϵ��
```sql
CREATE TABLE `star_activities` (
  `user_id` int NOT NULL COMMENT '�û�ID(FK)',
  `activity_id` int NOT NULL COMMENT '�ID(FK)',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='�û��ղػ��';

CREATE TABLE `user_star_blogs` (
  `user_id` int NOT NULL COMMENT '�û�ID(FK)',
  `blog_id` int NOT NULL COMMENT '����ID(FK)',
  PRIMARY KEY (`user_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='�û��ղ����ӱ�';
```
### 3.2.3 ���ݹ�����
```sql
CREATE TABLE `blog_activity` (
  `blog_id` int NOT NULL COMMENT '����ID(FK)',
  `activity_id` int NOT NULL COMMENT '�ID(FK)',
  PRIMARY KEY (`blog_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='���ӹ������';

CREATE TABLE `topic_blog` (
  `topic_id` int NOT NULL COMMENT '����ID(FK)',
  `blog_id` int NOT NULL COMMENT '����ID(FK)',
  PRIMARY KEY (`topic_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`topic_id`) REFERENCES `topic` (`topic_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='����������ӱ�';
```

### 3.2.4 ��ǩ������
```sql
CREATE TABLE `activity_label` (
  `label_id` int NOT NULL COMMENT '��ǩID(FK)',
  `activity_id` int NOT NULL COMMENT '�ID(FK)',
  PRIMARY KEY (`label_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT FOREIGN KEY (`label_id`) REFERENCES `labels` (`label_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) COMMENT='�ӵ�б�ǩ��';

CREATE TABLE `blog_label` (
  `label_id` int NOT NULL COMMENT '��ǩID(FK)',
  `blog_id` int NOT NULL COMMENT '����ID(FK)',
  PRIMARY KEY (`label_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`label_id`) REFERENCES `labels` (`label_id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='����ӵ�б�ǩ��';
```

### 3.2.5 ���޹�����
```sql
CREATE TABLE `user_like_blog` (
  `like_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL COMMENT '�û�ID(FK)',
  `blog_id` int DEFAULT NULL COMMENT '����ID(FK)',
  `content` varchar(255) DEFAULT NULL COMMENT '��������',
  PRIMARY KEY (`like_id`),
  KEY `user_id` (`user_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='�û��������ӱ�';
```

## 3.3 �������ݱ�

### 3.3.1 ���۱�
```sql
CREATE TABLE `comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL COMMENT '�û�ID(FK)',
  `blog_id` int DEFAULT NULL COMMENT '����ID(FK)',
  `content` varchar(255) DEFAULT NULL COMMENT '��������',
  `commentTime` datetime DEFAULT NULL COMMENT '����ʱ��',
  PRIMARY KEY (`comment_id`),
  KEY `user_id` (`user_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) COMMENT='���۱�';
```

### 3.3.2 �˶����ݱ�
```sql
CREATE TABLE `exercise_data` (
  `exercise_id` int NOT NULL AUTO_INCREMENT COMMENT '�˶�����ID(PK)',
  `user_id` int DEFAULT NULL COMMENT '�û�ID(FK)',
  `time` datetime DEFAULT NULL COMMENT '��¼ʱ��',
  `step` int DEFAULT NULL COMMENT '�˶�����',
  PRIMARY KEY (`exercise_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) COMMENT='�˶����ݱ�';
```

˵����

* �û�ϵͳ
�û���(users)�洢�û�������Ϣ�������ǳơ�ͷ�񡢵ȼ������֡�����������ϵ��ʽ�ȡ�ÿ���û���ΨһID��Ϊ������֧��΢�ŵ�¼(open_id/union_id)���˺������¼���ַ�ʽ��

* �����
���(activities)��¼���໧����Ϣ���������⡢ʱ��ص㡢�˶�ָ��(��·�ʱ��)��·����Ϣ(���յ�)���Ѷȵȼ��ȡ��û���ͨ��������(enroll)�����������ղػ(star_activities)���״̬ͨ���û����ϵ��(user_activity)���١�

* ��������
�û��������ӱ�(blogs)�������ݣ����ӿɹ����(blog_activity)�ͻ���(topic_blog)������֧�ֵ���(user_like_blog)���ղ�(user_star_blogs)���ܡ�����ϵͳ(comment)�����û����������ۻ��¼����ʱ������ݡ�

* ��ǩϵͳ
��ǩ��(labels)�ṩ���ı�ǩ����ͨ�����ǩ(activity_label)�����ӱ�ǩ(blog_label)ʵ�ֶ�Զ������֧�ְ���ǩ����������ݡ�

* ���⹦��
�����(topic)����������⡢��������ʽ����(��ɫ/ͼ��)��ͨ���������ӹ�ϵ��(topic_blog)����������ݣ��γɻ���ۺ�ҳ��

* ��������
�˶����ݱ�(exercise_data)��¼�û�ÿ�ղ����Ƚ���ָ�꣬��ʱ������������˶����Ʒ�����

���й���������ü���ɾ����ƣ�ȷ�����������ԡ����磬��ɾ��ĳ������ʱ���������е�����Ҳ���Զ���ɾ����

# 4.���ݿ�API�ӿ�

## 4.1 �����
`activity_service.py` �ṩ���ص���ɾ�Ĳ鹦�ܣ������������ɾ������ѯ���޸ĵȲ�����

### 4.1.1 ����»
* �����壺
```python
def add_activity(self, new_activity: activity):
```
* ������
```
new_activity : �����
```
* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "������ɹ���",
        "activity_id": "int"            // �id
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",               // ���ֿ��ܵĴ�����Ϣ
        "detail" : "str"                // ��ϸ���
    }
    ```

### 4.1.1 ����»
* �����壺
```python
def add_activity(self, new_activity: activity):
```
* ������
```
new_activity : �����
```
* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "������ɹ���",
        "activity_id": "int"            // �id
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",               // ���ֿ��ܵĴ�����Ϣ
        "detail" : "str"                // ��ϸ���
    }
    ```

### 4.1.2 ɾ���
* �����壺
```python
def remove_activity(self, activity_id: int):
```
* ������
```
activity_id : ��ʾ��ɾ���Ļid
```
* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "ɾ���ɹ�",
        "data": {
            "activity_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",               // ���ֿ��ܵĴ�����Ϣ
        "detail" : "str"                // ��ϸ���
    }
    ```

### 4.1.3 ��ȡ��ҳ�Ļ����
* �����壺
```python
def get_all_activities(self, page: int = 1, size: int = 10):
```
* ������
```
page : �ڼ�ҳ
size : ��ȡ�ĸ���
```
* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ȡ�ɹ�",
        "data": {
            "activities": [
                {
                    "id": "int",              // �id
                    "activity": "activity",   // �����
                    "enroll_count": "int"     // ��������  
                }
            ],
            "pagination": {
                "total": "int",             // ����
                "page": "int",               // ��һҳ
                "size": "int",               // �ж���
                "pages": "int" 
            }
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",               // ���ֿ��ܵĴ�����Ϣ
        "detail" : "str"                // ��ϸ���
    }
    ```

### 4.1.4 ��ȡ���ϸ��Ϣ
* �����壺
```python
def get_detail_activity(self, activity_id: int):
```
* ������
```
activity_id : ͨ���id��ȡ��ϸ��Ϣ
```
* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ѯ�ɹ���",
        "data": {
            "id": "int",                      // �id
            "activity": "activity",           // �����
            "enroll_count": "int",            // ��������
            "labels": [                     
                {
                    "id": "int",              // ��ǩid
                    "name": "str"             // ��ǩ����
                }
            ], 
            "related_posts": [              
                {
                    "id": "int",              // ����id
                    "title": "str",           // ���ӱ���
                    "time": "str",            // ����ʱ��
                    "author": "str",          // ������
                    "author_id": "int"        // ������id
                }
            ]
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",               // ���ֿ��ܵĴ�����Ϣ
        "detail" : "str"                // ��ϸ���
    }
    ```
### 4.1.5 �޸Ļ��Ϣ
* �����壺
```python
def modify_activity(self, activity_id: int, **kwargs):
```
* ������
```
activity_id : ��ʾ���޸ĵĻid
kwargs : ��Ҫ�޸ĵ��ֶμ�ֵ��
```
* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�޸ĳɹ�!",
        "data": {
            "activity_id": "int"      // ���ػid
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",               // ���ֿ��ܵĴ�����Ϣ
        "detail" : "str"                // ��ϸ���
    }
    ```

## 4.2 ���ӷ���
`post_service.py` �ṩ������ص���ɾ�Ĳ鹦�ܣ��������Ӵ�����ɾ������ѯ�ͻ����Ȳ�����

### 4.2.1 ���������

* �����壺

```python
def add_post(self, new_post: post):
```

* ������
```
new_post : ���Ӷ���
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ӳɹ�",
        "data": {
            "post_id": "int"        // ����id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",           // ������Ϣ
        "detail": "str"            // ��ϸ���
    }
    ```

### 4.2.2 ɾ������

* �����壺

```python
def remove_post(self, post_id: int):
```

* ������
```
post_id : ��ɾ��������id
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "ɾ���ɹ�",
        "data": {
            "post_id": "int"       // ��ɾ��������id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```

### 4.2.3 ��ȡ��������

* �����壺

```python
def get_all_posts(self):
```

* ������
```
new_post : ���Ӷ���
```

* ����ֵ��
    * ����ѯ�ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ѯ�ɹ���",
        "data": [
            {
                "id": "int",       // ����id
                "user_id": "int",  // ������id
                "post": "post"     // ���Ӷ���
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```

### 4.2.4 ��ȡ��������

* �����壺

```python
def get_post(self, post_id: int):
```

* ������
```
post_id : ����id
```

* ����ֵ��
    * ����ѯ�ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ѯ�ɹ�",
        "data": {
            "id": "int",           // ����id
            "post": "post",        // ���Ӷ���
            "user_info": {         // �û���Ϣ
                "id": "int",       // �û�id
                "name": "str",     // �û���
                "avatar": "str"    // �û�ͷ��
            },
            "activities": "list",  // �����
            "topics": "list"       // ��������
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",           // ������Ϣ
        "detail": "str"            // ��ϸ���
    }
    ```

### 4.2.5 ��ȡ��������

* �����壺

```python
def get_all_comments(self, post_id: int):
```

* ������
```
post_id : ����id
```

* ����ֵ��
    * ����ѯ�ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ѯ�ɹ�",
        "data": [
            {
                "comment_id": "int",       // ����id
                "user_id": "int",         // �û�id
                "blog_id": "int",         // ����id
                "content": "str",         // ��������
                "comment_time": "str",    // ����ʱ��
                "user_info": {            // �û���Ϣ
                    "name": "str",        // �û���
                    "avatar": "str"      // �û�ͷ��
                }
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",           // ������Ϣ
        "detail": "str"            // ��ϸ���
    }
    ```

### 4.2.6 ��������

* �����壺

```python
def leave_comment(self, user_id: int, post_id: int, content: str):
```

* ������
```
user_id : �û�id
post_id : ����id
content : ��������
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ѯ�ɹ�",
        "data": {
            "id": "int",           // ����id
            "user_id": "int",      // �û�id
            "blog_id": "int",      // ����id
            "content": "str",      // ��������
            "comment_time": "str", // ����ʱ��
            "user_info": {         // �û���Ϣ
                "id": "int",       // �û�id
                "name": "str",     // �û���
                "avatar": "str"    // �û�ͷ��
            }
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",           // ������Ϣ
        "detail": "str"            // ��ϸ���
    }
    ```

### 4.2.7 ɾ������

* �����壺

```python
def delete_comment(self, comment_id: int):
```

* ������
```
comment_id : ����id
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "ɾ���ɹ�!",
        "data": {
            "comment_id": "int"    // ��ɾ��������id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",           // ������Ϣ
        "detail": "str"            // ��ϸ���
    }
    ```

### 4.2.8 ��������

* �����壺

```python
def like(self, user_id: int, post_id: int):
```

* ������
```
new_post : ���Ӷ���
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "���޳ɹ�!",
        "data": {
            "user_id": "int",      // �û�id
            "post_id": "int"       // ����id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```

### 4.2.9 ȡ������

* �����壺

```python
def dislike(self, user_id: int, post_id: int):
```

* ������
```
user_id : �û�id
post_id : ����id
```

* ����ֵ��
    * ���ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "ȡ�����޳ɹ�!",
        "data": {
            "user_id": "int",      // �û�id
            "post_id": "int"       // ����id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",           // ������Ϣ
        "detail": "str"            // ��ϸ���
    }
    ```

### 4.2.10 �ղ�����

* �����壺

```python
def bookmark(self, user_id: int, post_id: int):
```

* ������
```
user_id : �û�id
post_id : ����id
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�ղسɹ�!",
        "data": {
            "user_id": "int",      // �û�id
            "post_id": "int"       // ����id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```

### 4.2.11 ȡ���ղ�

* �����壺

```python
def unbookmark(self, user_id: int, post_id: int):
```

* ������
```
user_id : �û�id
post_id : ����id
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "ȡ���ղسɹ�!",
        "data": {
            "user_id": "int",      // �û�id
            "post_id": "int"       // ����id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```

## 4.3 ��ǩ����
`tag_service.py` �ṩ��ǩ��صĴ����͹������ܣ�������ǩ��������ǩ������/��Ĺ����Ȳ�����

### 4.3.1 �����±�ǩ

* �����壺

```python
def add_tag(self, tag_content: str):
```

* ������
```
tag_content : ��ǩ���ݣ���Ψһ��
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�����ɹ�",
        "data": {
            "tag_id": "int"       // ������ǩ��id
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.3.2 Ϊ���ӹ�����ǩ

* �����壺

```python
def add_tag_to_post(self, post_id: int, tag_id: int):
```

* ������
```
post_id : ����ID
tag_id : ��ǩID
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ӳɹ�",
        "data": {
            "tag_id": "int",      // ��ǩID
            "post_id": "int"      // ����ID
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.3.3 Ϊ�������ǩ

* �����壺

```python
def add_tag_to_activity(self, activity_id: int, tag_id: int):
```

* ������
```
activity_id : �ID
tag_id : ��ǩID
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ӳɹ�",
        "data": {
            "tag_id": "int",      // ��ǩID
            "activity_id": "int"  // �ID
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
## 4.4 �������
`topic_service.py` �ṩ������ص���ɾ�Ĳ鹦�ܣ��������ⴴ����ɾ������ѯ�͹������ӵȲ�����
### 4.4.1 ����»���

* �����壺

```python
def add_topic(self, new_topic: topic):
```

* ������
```
activity_id : �ID
tag_id : ��ǩID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "���ⴴ���ɹ�",
        "data": {
            "topic_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.4.3 Ϊ�������ǩ

* �����壺

```python
def remove_topic(self, topic_id: int):
```

* ������
```
topic_id : ����ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "ɾ���ɹ���",
        "detail": {
            "topic_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.4.3 ��ȡ���Ż���

* �����壺

```python
def get_hot_topics(self, limit: int = 10):
```

* ������
```
limit : �����������ƣ�Ĭ��10��
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ȡ�ɹ�",
        "data": [
            {
                "id": "int",
                "topic": "�������",
                "post_count": "int"
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "������Ϣ",
        "detail": "��ϸ���"
    }
    ```
### 4.4.4 ��ȡ�����������

* �����壺

```python
def get_posts_by_topic(self, topic_id: int, page: int = 1, page_size: int = 10):
```

* ������
```
topic_id : ����ID
page : ҳ�루Ĭ��1��
page_size : ÿҳ������Ĭ��10��
```

* ����ֵ��
    * �������ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ѯ�ɹ���",
        "data": {
            "topic_info": {
                "id": "int",
                "title": "str",
                "description": "str"
            },
            "posts": [
                {
                    "id": "int",
                    "title": "str",
                    "content": "str",
                    "post_time": "datetime",
                    "author": {
                        "id": "int",
                        "name": "str"
                    }
                }
            ],
            "pagination": {
                "total": "int",
                "page": "int",
                "page_size": "int",
                "total_pages": "int"
            }
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```

## 4.5 �û�����
`user_service.py` �ṩ�û���ص���ɾ�Ĳ鹦�ܣ������û�������������ղع���Ȳ�����
### 4.5.1 ������û�

* �����壺

```python
def add_user(self, new_user: user):
```

* ������
```
new_user : �û�����
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�û������ɹ�",
        "data": {
            "user_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.2 ɾ���û�

* �����壺

```python
def remove_user(self, user_id: int):
```

* ������
```
user_id : �û�ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�û�ɾ���ɹ���",
        "data": {
            "user_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.3 ��ȡ�û���Ϣ

* �����壺

```python
def get_message(self, user_id: int):
```

* ������
```
user_id : �û�ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�û���Ϣ��ѯ�ɹ�",
        "data": {
            "id": "int",
            "user": "�û�����",
            "stats": {
                "post_count": "int",
                "activity_count": "int",
                "bookmark_count": "int"
            }
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.4 �����û���Ϣ

* �����壺

```python
def update_user(self, user_id: int, name: str, avatar: str):
```

* ������
```
user_id : �û�ID
name : �û���
avatar : ͷ��URL
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�û���Ϣ���³ɹ��ɹ���",
        "data": {
            "user_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.5 �����

* �����壺

```python
def register_activity(self, user_id: int, activity_id: int):
```

* ������
```
user_id : �û�ID
activity_id : �ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�û������ɹ���",
        "data": {
            "user_id": "int",
            "activity_id": "int",
            "enroll_time": "str"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.6 ȡ������

* �����壺

```python
def cancel_registration(self, user_id: int, activity_id: int):
```

* ������
```
user_id : �û�ID
activity_id : �ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "ȡ�������ɹ�",
        "data": {
            "user_id": "int",
            "activity_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.7 �ղػ

* �����壺

```python
def bookmark_activity(self, user_id: int, activity_id: int):
```

* ������
```
user_id : �û�ID
activity_id : �ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ղسɹ�",
        "data": {
            "user_id": "int",
            "activity_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.8 ��ȡ�û�����Ļ

* �����壺

```python
def get_activities(self, user_id: int):
```

* ������
```
user_id : �û�ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�ɹ���ȡ�!",
        "data": [
            {
                "id": "int",
                "activity": "�����",
                "status": "str"
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.9 ��ȡ�û��ղص�����

* �����壺

```python
def get_bookmark_posts(self, user_id: int):
```

* ������
```
topic_id : ����ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "",
        "data": [
            {
                "id": "int",
                "post": "���Ӷ���"
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.10 ��ȡ�û��ղصĻ

* �����壺

```python
def get_bookmark_activities(self, user_id: int):
```

* ������
```
user_id : �û�ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "���ѯ�ɹ�",
        "data": [
            {
                "id": "int",
                "activity": "�����"
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.11 ȡ���ղػ

* �����壺

```python
def unbookmark_activity(self, user_id: int, activity_id: int):
```

* ������
```
user_id : �û�ID
activity_id : �ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ȡ���ղػ",
        "data": {
            "user_id": "int",
            "activity_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.12 ��ȡ�û�����������

* �����壺

```python
def get_publish_posts(self, user_id: int):
```

* ������
```
user_id : �û�ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ȡ���ӳɹ���",
        "data": [
            {
                "id": "int",
                "post": "���Ӷ���",
                "author_info": {
                    "id": "int",
                    "name": "str"
                }
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.13 ��ȡ�û������Ļ

* �����壺

```python
def get_register_activity(self, user_id: int):
```

* ������
```
user_id : �û�ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "��ѯ��ɹ�",
        "data": [
            {
                "id": "int",
                "activity": "�����",
                "time": "str"
            }
        ]
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.14 ��¼�˶�����

* �����壺

```python
def add_exercise_data(self, user_id: int, steps: int, time: str = datetime.now()):
```

* ������
```
user_id : �û�ID
steps : ����
time : ʱ��(��ѡ)
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�˶����ݼ�¼�ɹ�",
        "data": {
            "exercise_id": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```
### 4.5.15 ��ȡ�˶�����

* �����壺

```python
def get_exercise_data(self, user_id: int, limit: int = 30):
```

* ������
```
topic_id : ����ID
```

* ����ֵ��
    * �ɹ�ʱ��
    ```json
    {
        "success": true,
        "message": "�˶����ݲ�ѯ�ɹ���",
        "data": {
            "user_id": "int",
            "recent_data": [
                {
                    "id": "int",
                    "date": "str",
                    "steps": "int"
                }
            ],
            "total_steps": "int",
            "avg_daily_steps": "int"
        }
    }
    ```
    * ��ʧ��ʱ��
    ```json
    {
        "success": false,
        "message": "str",          // ������Ϣ
        "detail": "str"           // ��ϸ���
    }
    ```