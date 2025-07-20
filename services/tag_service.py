from services.classes.row_to_class import row_to_post, row_to_topic, row_to_activity, row_to_user
from services.connection.connection import get_database_connection, handle_db_error
from services.classes.post import post
from services.classes.activity import activity
from services.classes.topic import topic
from services.classes.users import user
from datetime import datetime

class tag_service:
    def __init__(self):
        self.connection = get_database_connection()

    def __del__(self):
        self.connection.close()

    # 创建新标签
    # 参数
    """
    tag_content: 标签内容（需唯一）
    """
    # 返回值
    """
    当成功时：
    {
        'success': bool,
        'message': '新增标签成功！'
        'data': {
            'tag_id': int       # 返回新增标签的id
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def add_tag(self, tag_content: str):
        cursor = self.connection.cursor()
        try:
            # 简单验证
            if not tag_content or len(tag_content) > 30:
                return {
                    'success': False,
                    'message': '创建标签失败',
                    'detail': '标签长度超过30！'
                }

            # 检查唯一性并插入
            query = """
            INSERT INTO labels (content)
            SELECT %s FROM DUAL
            WHERE NOT EXISTS (
                SELECT 1 FROM labels WHERE content = %s
            )
            """
            cursor.execute(query, (tag_content, tag_content))

            if cursor.rowcount == 0:
                return {'success': False,
                        'message': '标签已存在',
                        'detail': '数据库中已存在该标签'
                    }

            tag_id = cursor.lastrowid
            self.connection.commit()
            return {
                'success': True,
                'message': '创建成功',
                'data' : {'tag_id': tag_id}
            }

        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 为帖子关联标签
    # 参数：
    """
    post_id: 帖子ID
    tag_id: 标签ID
    """
    # 返回值：
    """
    当成功时：
    {
        'success': True, 
        'message': '添加成功',
        'data' : {
            'tag_id': int,
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
    def add_tag_to_post(self, post_id: int, tag_id: int):
        cursor = self.connection.cursor()
        try:
            # 直接尝试插入，依赖唯一约束防止重复
            query = "INSERT INTO blog_label (blog_id, label_id) VALUES (%s, %s)"
            cursor.execute(query, (post_id, tag_id))
            self.connection.commit()
            return {
                'success': True,
                'message': '添加成功',
                'data' : {
                    'tag_id': tag_id,
                    'post_id': post_id
                }
            }

        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()

    # 为活动关联标签
    # 参数
    """
    activity_id: 活动ID
    tag_id: 标签ID
    """
    # 返回值
    """
    当成功时：
    {
        'success': True, 
        'message': '添加成功',
        'data' : {
            'tag_id': int,
            'activity_id': int
        }
    }
    失败时：
    {
        'success': False,
        'message': ?,               # 各种可能的错误信息
        'detail' : ?                # 详细情况
    }
    """
    def add_tag_to_activity(self, activity_id: int, tag_id: int):
        cursor = self.connection.cursor()
        try:
            # 直接尝试插入，依赖唯一约束防止重复
            query = "INSERT INTO activity_label (activity_id, label_id) VALUES (%s, %s)"
            cursor.execute(query, (activity_id, tag_id))
            self.connection.commit()
            return {
                'success': True,
                'message': '添加成功',
                'data' : {
                    'tag_id': int,
                    'activity_id': int
                }
            }

        except Exception as e:
            self.connection.rollback()
            return handle_db_error(e)
        finally:
            cursor.close()