from services.classes.row_to_class import row_to_post, row_to_topic, row_to_activity, row_to_user
from services.connection.connection import get_database_connection, handle_db_error
from services.classes.post import post
from services.classes.activity import activity
from services.classes.topic import topic
from services.classes.users import user
from datetime import datetime

# 帖子服务器对象，提供对帖子相关的增删查改
class post_service:
    # 初始化时获取数据库连接
    def __init__(self):
        self.connection = get_database_connection()

    # 对象被回收时断开数据库连接
    def __del__(self):
        self.connection.close()

    # 添加一个新的帖子到数据库中
    # 参数列表：
    """
    new_post : 一个帖子对象
    """
    # 返回：
    """
    成功添加时：
    {
        'success': True,
        'message': '添加成功',
        'data': {
            'post_id' : int         # 帖子id
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def add_post(self, new_post : post):
        cursor = self.connection.cursor()
        try:
            # 构造插入语句
            query = """
            INSERT INTO blogs 
            (user_id, post_time, title, content, like_count, star_count)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            # 执行事务
            cursor.execute(query, (
                new_post.user_id,
                new_post.post_time,
                new_post.title,
                new_post.content,
                new_post.like_count,
                new_post.star_count
            ))
            # 获取对应的主键
            post_id = cursor.lastrowid
            # 新增帖子关联的活动
            for activity_id in new_post.activity:
                self.__link_post_to_activity(post_id, activity_id)
            # 新增帖子关联的话题
            for topic_id in new_post.topics:
                self.__link_post_to_topic(post_id, topic_id)

            self.connection.commit()  # 执行事务

            return {
                'success': True,
                'message': '添加成功',
                'data': {
                    'post_id' : post_id         # 帖子id
                }
            }

        except Exception as e:
            # 发生异常，事务回滚
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            # 无论如何，都要关闭数据库连接
            cursor.close()

    # 辅助函数，用于添加帖子关联的活动
    def __link_post_to_activity(self, post_id: int, activity_id: int):
        cursor = self.connection.cursor()
        try:
            # 向帖子-活动关联表中添加内容，代表帖子与这个活动相关联
            query = "INSERT INTO blog_activity (blog_id, activity_id) VALUES (%s, %s)"
            cursor.execute(query, (post_id, activity_id))
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 辅助函数，用于添加帖子相关的话题
    def __link_post_to_topic(self, post_id: int, topic_id: int):
        cursor = self.connection.cursor()
        try:
            # 向话题-帖子关联表中添加内容，代表话题与帖子相关联
            query = "INSERT INTO topic_blog (topic_id, blog_id) VALUES (%s, %s)"
            cursor.execute(query, (topic_id, post_id))
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 删除帖子，数据库中与帖子相关的关联表中会自动删除相关内容
    # 参数列表：
    """
    post_id : 被删除的帖子的id
    """
    # 返回值：
    """
    成功删除时：
    {
        'success': True,
        'message': '删除成功',
        'data': {
            'post_id' : int         # 帖子id
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def remove_post(self, post_id: int):
        cursor = self.connection.cursor()
        try:
            # 执行删除
            query = "DELETE FROM blogs WHERE blog_id = %s"
            cursor.execute(query, (post_id,))
            self.connection.commit()    # 执行事物
            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': '帖子不存在',
                    'detail': '数据库中不存在被删除帖子的记录'
                }
            else:
                return {
                    'success': True,
                    'message': '删除成功',
                    'data': {
                        'post_id' : post_id
                    }
                }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取所有的帖子
    # 返回值
    """
    成功时：
    {
        'success': True,
        'message': '查询成功！',
        'data': [
            {
                'id': int,          # 帖子id
                'user_id': int,     # 发布者id
                'post': post        # 帖子对象
            },
            ...
        ]
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_all_posts(self):
        # 以字典的形式返回
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT b.*, u.name as user_name, u.avatar as user_avatar
                FROM blogs b
                JOIN users u ON b.user_id = u.id
                ORDER BY b.post_time DESC
                """
            cursor.execute(query)
            posts = []
            for row in cursor:
                posts.append({
                    'id': row['blog_id'],  # 帖子ID
                    'user_id': row['user_id'],  # 用户ID
                    'post': row_to_post(row),
                })
            return {
                'success': True,
                'message': '查询成功！',
                'data': posts
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 根据帖子获取其相关活动
    # 参数列表：
    """
    post_id : 需要获取关联活动的帖子id 
    """
    # 返回值：list类型
    """
    查询成功时：
    {
        'success': True,
        ‘message’: '查询成功',
        'data': [
            {
                'id' : int,         # 活动id
                'activity' : int,   # 活动对象
            },
            ...
        ]
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_post_activities(self, post_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT a.*
                FROM activities a
                JOIN blog_activity ba ON a.activity_id = ba.activity_id
                WHERE ba.blog_id = %s
                """
            cursor.execute(query, (post_id,))
            return {
                'success': True,
                'message': "查询成功！",
                'data': [{
                    'id': row['activity_id'],  # 活动ID
                    'activity': row_to_activity(row),
                } for row in cursor]
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 根据帖子获取相关的话题
    # 参数列表：
    """
    post_id : 需要获取关联话题的帖子id 
    """
    # 返回值：list类型
    """
    成功时：
    {
        'success': True,
        'message': '查询成功！',
        'data': [                   # 话题数组
            {
                'id': int,          # 话题id
                'topic': topic,     # 话题对象
            },
            ...
        ]
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_post_topics(self, post_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT t.*
                FROM topic t
                JOIN topic_blog tb ON t.topic_id = tb.topic_id
                WHERE tb.blog_id = %s
                """
            cursor.execute(query, (post_id,))
            return {
                'success': True,
                'message': '查询成功！',
                'data': [{
                    'id': row['topic_id'],  # 话题ID
                    'topic': row_to_topic(row),
                } for row in cursor]
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 根据帖子id返回单个帖子
    # 参数
    """
    post_id : 需要获取的帖子id
    """
    # 返回值
    """
    {
        'success': True,
        'message': '查询成功',
        'data': {
            'id' : int,             # 帖子id
            'post' : post,          # 帖子对象
            'user_info': {          # 用户信息
                'id': int,          # 发布者id
                'name': str,        # 发布者昵称
                'avatar': str       # 发布者头像url
            },
            'activities': activity, # 关联的活动
            'topics': topics        # 关联的话题
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_post(self, post_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
                SELECT b.*, u.id as user_id, u.name as user_name, u.avatar as user_avatar
                FROM blogs b
                JOIN users u ON b.user_id = u.id
                WHERE b.blog_id = %s
                """
            cursor.execute(query, (post_id,))
            row = cursor.fetchone()

            if not row:
                return None

            activities = self.get_post_activities(post_id)
            topics = self.get_post_topics(post_id)

            return {
                'success': True,
                'message': '查询成功',
                'data': {
                    'id': post_id,  # 明确返回帖子ID
                    'post': row_to_post(row),
                    'user_info': {
                        'id': row['user_id'],  # 用户ID
                        'name': row['user_name'],
                        'avatar': row['user_avatar']
                    },
                    'activities': activities,
                    'topics': topics
                }
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 根据帖子id获取其下方所有的评论
    # 参数列表：
    """
    post_id : 需要获取的帖子id
    """
    # 返回值：list类型
    """
    {
        'success': True,
        'message': '查询成功'
        'data': [
            {
                'comment_id': row['comment_id'],        # 评论id
                'user_id': row['user_id'],              # 用户id
                'blog_id': row['blog_id'],              # 帖子id
                'content': row['content'],              # 评论内容
                'comment_time': row['commentTime'],     # 评论时间
                'user_info': {                          # 用户信息
                    'name': row['user_name'],           # 发布者姓名
                    'avatar': row['user_avatar']        # 发布者头像url
                }
            },
            ...
        ]
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_all_comments(self, post_id: int):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            SELECT c.*, u.name as user_name, u.avatar as user_avatar
            FROM comment c
            JOIN users u ON c.user_id = u.id
            WHERE c.blog_id = %s
            ORDER BY c.commentTime DESC
            """
            cursor.execute(query, (post_id,))
            return {
                'success': True,
                'message': '查询成功',
                'data': [{
                    'comment_id': row['comment_id'],
                    'user_id': row['user_id'],
                    'blog_id': row['blog_id'],
                    'content': row['content'],
                    'comment_time': row['commentTime'],
                    'user_info': {
                        'name': row['user_name'],
                        'avatar': row['user_avatar']
                    }
                } for row in cursor]
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 对某个帖子下留下新的评论
    # 参数
    """
    user_id : 用户id
    post_id : 帖子id
    content : 评论内容
    """
    # 返回值
    """
    成功时：
    {
        'success': True,
        'message': '查询成功',
        ‘data’: {
            'id': int,              # 评论id
            'user_id': int,         # 用户id
            'blog_id': int,         # 帖子id
            'content': str,         # 评论内容
            'comment_time': str,    # 评论时间
            'user_info': {          # 用户信息
                'id': int,          # 发布者id
                'name': str,        # 发布者姓名
                'avatar': str       # 发布者头像地址
            }
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def leave_comment(self, user_id: int, post_id: int, content: str):
        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            INSERT INTO comment 
            (user_id, blog_id, content, commentTime)
            VALUES (%s, %s, %s, %s)
            """
            current_time = datetime.now()
            cursor.execute(query, (user_id, post_id, content, current_time))
            comment_id = cursor.lastrowid

            # 获取完整的评论信息
            query = """
            SELECT c.*, u.name as user_name, u.avatar as user_avatar
            FROM comment c
            JOIN users u ON c.user_id = u.id
            WHERE c.comment_id = %s
            """
            cursor.execute(query, (comment_id,))
            row = cursor.fetchone()

            self.connection.commit()

            return {
                'success': True,
                'message': '查询成功',
                'data': {
                    'id': comment_id,  # 评论ID
                    'user_id': user_id,
                    'blog_id': post_id,
                    'content': content,
                    'comment_time': current_time,
                    'user_info': {
                        'id': user_id,
                        'name': row['user_name'],
                        'avatar': row['user_avatar']
                    }
                }
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 删除某条评论
    # 参数
    """
    comment_id : 评论id
    """
    # 返回值
    """
    成功时：
    {
        'success': True,
        'message': '删除成功!',
        'data' : {
            'comment_id': comment_id
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def delete_comment(self, comment_id: int):
        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM comment WHERE comment_id = %s"
            cursor.execute(query, (comment_id,))
            self.connection.commit()
            if self.connection.rowcount == 0:
                return {
                    'success': False,
                    'message': '删除失败!',
                    'detail': '数据库中不存在该评论的记录'
                }
            else:
                return {
                    'success': False,
                    'message': '删除失败!',
                    'data' : {
                        'comment_id': comment_id
                    }
                }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 对某个帖子点赞，返回值表示是否被点赞
    # 参数
    """
    user_id : 用户id
    post_id : 帖子id
    """
    # 返回值
    """
    成功时：
    {
        'success': True,
        'message': '删除失败!',
        'data' : {
            'user_id': int,
            'post_id': int
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def like(self, user_id: int, post_id: int):
        cursor = self.connection.cursor()
        try:
            # 检查是否被点赞，如果已经被点赞则直接返回
            check_query = "SELECT * FROM user_like_blog WHERE user_id = %s AND blog_id = %s"
            cursor.execute(check_query, (user_id, post_id))
            if cursor.fetchone():
                return     {
                    'success': False,
                    'message': '点赞失败',
                    'detail' : '数据库中已有点赞记录'
                }

            # 没有被点赞，则加入点赞记录，更新用户-帖子点赞表
            insert_query = "INSERT INTO user_like_blog (user_id, blog_id) VALUES (%s, %s)"
            cursor.execute(insert_query, (user_id, post_id))

            # 更新帖子的点赞数
            update_query = "UPDATE blogs SET like_count = like_count + 1 WHERE blog_id = %s"
            cursor.execute(update_query, (post_id,))

            self.connection.commit()
            return {
                'success': True,
                'message': '点赞成功!',
                'data' : {
                    'user_id': int,
                    'post_id': int
                }
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 对某个帖子取消点赞
    # 参数
    """
    user_id : 用户id
    post_id : 帖子id
    """
    # 返回值
    """
    成功时：
    {
        'success': True,
        'message': '取消点赞成功!',
        'data' : {
            'user_id': int,
            'post_id': int
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def dislike(self, user_id: int, post_id: int):
        cursor = self.connection.cursor()
        try:
            # 检查用户是否没有点赞，如果没有点赞返回false代表操作未成功
            check_query = "SELECT * FROM user_like_blog WHERE user_id = %s AND blog_id = %s"
            cursor.execute(check_query, (user_id, post_id))
            if not cursor.fetchone():
                return {
                    'success': False,
                    'message': '取消点赞失败！',
                    'detail' : '数据库中不存在点赞记录'
                }

            # 从表中删除记录
            delete_query = "DELETE FROM user_like_blog WHERE user_id = %s AND blog_id = %s"
            cursor.execute(delete_query, (user_id, post_id))

            # 减少点赞数
            update_query = "UPDATE blogs SET like_count = GREATEST(0, like_count - 1) WHERE blog_id = %s"
            cursor.execute(update_query, (post_id,))

            self.connection.commit()
            return     {
                'success': True,
                'message': '取消点赞成功!',
                'data' : {
                    'user_id': int,
                    'post_id': int
                }
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 用户收藏某个帖子
    # 参数
    """
    user_id : 用户id
    post_id : 帖子id
    """
    # 返回值
    """
    成功时：
    {
        'success': True,
        'message': '收藏成功!',
        'data' : {
            'user_id': int,
            'post_id': int
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def bookmark(self, user_id: int, post_id: int):
        cursor = self.connection.cursor()
        try:
            # 检查是由已经收藏，如果是，则返回false代表操作失败
            check_query = "SELECT * FROM user_star_blogs WHERE user_id = %s AND blog_id = %s"
            cursor.execute(check_query, (user_id, post_id))
            if cursor.fetchone():
                return {
                    'success': False,
                    'message': '收藏失败！',
                    'detail' : '数据库中已经存在收藏记录'
                }

            # 新增用户收藏记录
            insert_query = "INSERT INTO user_star_blogs (user_id, blog_id) VALUES (%s, %s)"
            cursor.execute(insert_query, (user_id, post_id))

            # 更新帖子的收藏数
            update_query = "UPDATE blogs SET star_count = star_count + 1 WHERE blog_id = %s"
            cursor.execute(update_query, (post_id,))

            self.connection.commit()
            return     {
                'success': True,
                'message': '收藏成功!',
                'data' : {
                    'user_id': int,
                    'post_id': int
                }
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 用户取消收藏某个帖子
    # 参数
    """
    user_id : 用户id
    post_id : 帖子id
    """
    # 返回值
    """
    成功时：
    {
        'success': True,
        'message': '取消收藏成功!',
        'data' : {
            'user_id': int,
            'post_id': int
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def unbookmark(self, user_id: int, post_id: int):
        cursor = self.connection.cursor()
        try:
            # 检查用户是否没有收藏某个帖子，如果是，返回false表示操作失败
            check_query = "SELECT * FROM user_star_blogs WHERE user_id = %s AND blog_id = %s"
            cursor.execute(check_query, (user_id, post_id))
            if not cursor.fetchone():
                return {
                    'success': False,
                    'message': '取消收藏失败！',
                    'detail' : '数据库中不存在收藏记录'
                }

            # 移除收藏记录
            delete_query = "DELETE FROM user_star_blogs WHERE user_id = %s AND blog_id = %s"
            cursor.execute(delete_query, (user_id, post_id))

            # 更新收藏数
            update_query = "UPDATE blogs SET star_count = GREATEST(0, star_count - 1) WHERE blog_id = %s"
            cursor.execute(update_query, (post_id,))

            self.connection.commit()
            return {
                'success': True,
                'message': '取消收藏成功!',
                'data' : {
                    'user_id': int,
                    'post_id': int
                }
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

