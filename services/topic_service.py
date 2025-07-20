from services.classes.row_to_class import row_to_post, row_to_topic, row_to_activity, row_to_user
from services.connection.connection import get_database_connection, handle_db_error
from services.classes.post import post
from services.classes.activity import activity
from services.classes.topic import topic
from services.classes.users import user
from datetime import datetime

class topic_service:
    def __init__(self):
        self.connection = get_database_connection()

    def __del__(self):
        if self.connection:
            self.connection.close()
    # 添加新话题
    # 参数：
    """
    new_topic: Topic对象
    """
    # 返回：
    """
    成功添加话题时：
    {
        'success': True,            
        'message': '话题创建成功',
        'data': {
            'topic_id': topic_id,   # 新创建的话题id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def add_topic(self, new_topic: topic):

        cursor = self.connection.cursor()
        try:
            query = """
            INSERT INTO topic 
            (title, description, color, icon, image)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                new_topic.title,
                new_topic.description,
                new_topic.color,
                new_topic.icon,
                new_topic.image,
            ))
            topic_id = cursor.lastrowid

            self.connection.commit()

            return {
                'success': True,
                'message': '话题创建成功',
                'data': {
                    'topic_id': topic_id,
                }
            }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 删除话题（连带删除关联关系）
    # 参数：
    """
        topic_id: 话题ID
    """
    # 返回：
    """
    成功删除话题时：
    return {
        'success': True,
        'message': "删除成功！",
        'detail': {
            'topic_id': topic_id,   # 话题id
        }
    }
    当失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def remove_topic(self, topic_id: int):

        cursor = self.connection.cursor()
        try:
            # 外键约束会自动删除topic_blog关联记录
            query = "DELETE FROM topic WHERE topic_id = %s"
            cursor.execute(query, (topic_id,))

            self.connection.commit()

            if cursor.rowcount == 0:
                return {
                    'success': False,
                    'message': "删除失败！",
                    'detail': '数据库中不存在该话题的记录'
                }
            else:
                return {
                    'success': True,
                    'message': "删除成功！",
                    'detail': {
                        'topic_id': topic_id,
                    }
                }
        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 获取热门话题（按关联帖子数排序）
    # 参数：
    """
    limit: 返回数量限制
    """
    # 返回值：
    """
    当成功获取时：
    {
        'success': True,
        'message': '获取成功',
        'data': [                   # 话题数组
            {
                'id': int,          # 话题id
                'topic': topic,     # 话题对象
                'post_count': int   # 关联的帖子总数
            },
            ...
        ]
    }
    失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_hot_topics(self, limit: int = 10):

        cursor = self.connection.cursor(dictionary=True)
        try:
            query = """
            SELECT 
                t.*,
                COUNT(tb.blog_id) as post_count
            FROM topic t
            LEFT JOIN topic_blog tb ON t.topic_id = tb.topic_id
            GROUP BY t.topic_id
            ORDER BY post_count DESC 
            LIMIT %s
            """
            cursor.execute(query, (limit,))

            return {
                'success': True,
                'message': '获取成功',
                'data': [{
                    'id': row['topic_id'],
                    'topic': row_to_topic(row),
                    'post_count': row['post_count']
                } for row in cursor]
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()

    # 根据话题获取关联帖子（分页）
    # 参数：
    """
    参数:
        topic_id: 话题ID
        page: 页码
        page_size: 每页数量
    """
    # 返回值：
    """
    当查询成功时：
    {
        'success': True,
        'message': '查询成功',
        ‘data’: {
            'topic_info': {         # 话题信息
                'id': int,          # 话题id
                'title': str,       # 话题标题
                'description': str  # 话题描述
            },
            'posts': [              # 帖子数组
                {
                    'id': int,      # 帖子id
                    'title': str,   # 帖子标题
                    'content': str, # 帖子内容
                    'post_time': datetime,  # 发布时间
                    'author': {     # 作者
                        'id': int,  # 发布者id
                        'name': str # 发布者昵称
                    }
                }，
                。。。
            ],
            'pagination': {         # 页码相关
                'total': int,
                'page': int,
                'page_size': int
            }
        }
    }
    失败时：
    {
        'success': False,
        'message': ?                # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def get_posts_by_topic(
            self,
            topic_id: int,
            page: int = 1,
            page_size: int = 10
    ):

        cursor = self.connection.cursor(dictionary=True)
        try:
            # 获取话题基本信息
            topic_query = """
            SELECT title, description 
            FROM topic 
            WHERE topic_id = %s
            """
            cursor.execute(topic_query, (topic_id,))
            topic_info = cursor.fetchone()

            if not topic_info:
                return None

            # 获取帖子总数
            count_query = """
            SELECT COUNT(*) as total 
            FROM topic_blog 
            WHERE topic_id = %s
            """
            cursor.execute(count_query, (topic_id,))
            total = cursor.fetchone()['total']

            # 获取分页帖子
            offset = (page - 1) * page_size
            posts_query = """
            SELECT 
                b.blog_id, b.title, b.content, b.post_time,
                u.id as user_id, u.name as user_name
            FROM blogs b
            JOIN topic_blog tb ON b.blog_id = tb.blog_id
            JOIN users u ON b.user_id = u.id
            WHERE tb.topic_id = %s
            ORDER BY b.post_time DESC
            LIMIT %s OFFSET %s
            """
            cursor.execute(posts_query, (topic_id, page_size, offset))

            return {
                'success': True,
                'message': '查询成功！',
                'data': {
                    'topic_info': {
                        'id': topic_id,
                        'title': topic_info['title'],
                        'description': topic_info['description']
                    },
                    'posts': [{
                        'id': row['blog_id'],
                        'title': row['title'],
                        'content': row['content'],
                        'post_time': row['post_time'],
                        'author': {
                            'id': row['user_id'],
                            'name': row['user_name']
                        }
                    } for row in cursor],
                    'pagination': {
                        'total': total,
                        'page': page,
                        'page_size': page_size,
                        'total_pages': (total + page_size - 1) // page_size
                    }
                }
            }
        except Exception as e:
            return handle_db_error(e)
        finally:
            cursor.close()