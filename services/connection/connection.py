from json import JSONDecodeError

import mysql.connector
import json

def get_database_connection():
    try:
        with open('services/connection/DatabaseConfig.json', 'r') as config_file:
            config = json.load(config_file)
    except JSONDecodeError as err:
        print(f"json格式错误！:{err}")
    except IOError as err:
        print(f"文件不存在！:{err}")

    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except mysql.connector.Error as err:
        print(f"数据库连接失败！: {err}")
        return None


def handle_db_error(e: Exception):

    if isinstance(e, mysql.connector.Error):
        err_code = e.errno
        msg = e.msg.split('(')[0].strip()  # 提取基础错误信息

        # 常见错误类型处理
        error_mapping = {
            # 重复键错误
            1062: {'message': '数据已存在', 'code': 'DUPLICATE_ENTRY'},
            # 外键约束失败
            1452: {'message': '关联数据不存在', 'code': 'FOREIGN_KEY_CONSTRAINT'},
            # 必填字段为空
            1364: {'message': '缺少必要字段: ' + msg.split("'")[-2], 'code': 'MISSING_FIELD'},
            # 数据过长
            1406: {'message': '数据长度超过限制', 'code': 'DATA_TOO_LONG'},
            # 无效数据类型
            1366: {'message': '数据类型无效', 'code': 'INVALID_DATA_TYPE'},
            # 表不存在
            1146: {'message': '数据表不存在', 'code': 'TABLE_NOT_FOUND'},
            # 字段不存在
            1054: {'message': '字段不存在', 'code': 'UNKNOWN_COLUMN'},
            # 连接错误
            2002: {'message': '数据库连接失败', 'code': 'CONNECTION_FAILED'},
            # 权限不足
            1045: {'message': '数据库访问被拒绝', 'code': 'ACCESS_DENIED'},
            # 锁等待超时
            1205: {'message': '操作超时，请重试', 'code': 'LOCK_TIMEOUT'},
            # 死锁
            1213: {'message': '系统繁忙，请稍后重试', 'code': 'DEADLOCK'},
            # 事务错误
            1207: {'message': '事务冲突，请重试', 'code': 'TRANSACTION_CONFLICT'}
        }

        # 查找预定义的错误处理
        if err_code in error_mapping:
            return {
                'success': False,
                'message': error_mapping[err_code]['message'],
                'detail': str(e)
            }

        # 处理字段相关错误 (以ER_开头)
        if hasattr(e, 'sqlstate') and e.sqlstate:
            sqlstate = e.sqlstate
            if sqlstate.startswith('ER_'):
                return {
                    'success': False,
                    'message': '数据验证失败',
                    'detail': msg
                }

        # 默认数据库错误处理
        return {
            'success': False,
            'message': '数据库操作失败',
            'detail': str(e)
        }

    # 非数据库错误的处理
    return {
        'success': False,
        'message': '系统内部错误',
        'detail': str(e)
    }