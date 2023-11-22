from django.db import models

#   模型 == 表结构
#   类属性 == 表字段
#   对象 == 表的一行记录



class UserModel(models.Model):
    name = models.CharField(max_length=30,unique=True)#对应SQL语句 name varchar(30)
    age = models.IntegerField(default=18)#对应SQL语句 age int default 18
    sex = models.CharField(max_length=20)#对应SQL语句 sex varchar(20)
    is_deleted = models.BooleanField(default=False)
    objects = models.Manager()


#表字段
#用户名称   name
#用户年龄   age
#用户性别   sex
#是否删除   is_delete



#ps:
#数据迁移:models表结构一旦改变需要重新迁移
#迁移的概念:就是将模型映射到数据库的过程
#生成迁移的文件: python manage.py makemigrations
#执行迁移: python manage.py migrate