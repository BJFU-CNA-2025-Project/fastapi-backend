from services.classes.post import post
from services.classes.activity import activity
from services.classes.topic import topic
from services.classes.users import user

# 将字典转为post对象
def row_to_post(row) -> post:
    return post(
        user_id=row['user_id'],
        post_time=row['post_time'],
        title=row['title'],
        content=row['content'],
        activity=[],
        topics=[],
        like_count=row['like_count'],
        star_count=row['star_count']
    )


# 将字典转为activity对象
def row_to_activity(row) -> activity:
    return activity(
        title=row['title'],
        data=row['date'],
        location=row['location'],
        calorie=row['calorie'],
        duration=row['duration'],
        weather=row['weather'],
        start_place=row['start_place'],
        end_place=row['end_place'],
        time=row['time'],
        difficulty=row['difficulty'],
        type=row['type'],
        image=row['image'],
        star_count = row['star_count']
    )


def row_to_topic(row) -> topic:
    return topic(
        title=row['title'],
        description=row['description'],
        color=row['color'],
        icon=row['icon'],
        image=row['image']
    )

# 行转对象方法
def row_to_user(row: dict) -> user:
    return user(
        name=row['name'],
        avatar=row['avatar'],
        level=row['level'],
        points=row['points'],
        days=row['days'],
        phone_number=row['phone_number'],
        register_time=row['register_time'],
        account=row['account'],
        password=row['password'],
        open_id=row['open_id'],
        union_id=row['union_id']
    )