from applications.models import User, Role, Power
import datetime
now_time = datetime.datetime.now()

roledata = [
    Role(
        id=1,
        code='admin',
        name='校级领导层',
        enable=1,
        details='最高管理员，管理系统和数据',
        sort=1,
        create_time=now_time,
    ),
    Role(
        id=2,
        code='dean',
        name='教学管理部门',
        enable=1,
        details='管理部分系统和数据',
        sort=2,
        create_time=now_time,
    ),
    Role(
        id=3,
        code='input',
        name='负责成绩录入的教师',
        enable=1,
        details='只可以录入成绩，不可修改成绩',
        sort=3,
        create_time=now_time,
    ),
    Role(
        id=4,
        code='show',
        name='大屏展示',
        enable=1,
        details='查看大屏展示',
        sort=4,
        create_time=now_time,
    )
]