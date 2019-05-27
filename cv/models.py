from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL

class Resume(models.Model):
    name = models.CharField('姓名', max_length=50)
    position = models.CharField('职位', max_length=50)
    profile = models.TextField('基本信息',default="")
    contact = models.TextField('联系方式',default="")
    # skill = models.TextField('技能')
    stack = models.TextField('技术栈',default="")
    education = models.TextField('教育信息',default="")
    work = models.TextField('工作经历',default="")
    project = models.TextField('个人项目',default="")
    trophy = models.TextField('奖项与证书',default="")
    aboutme = models.TextField('自我评价',default="")
    created = models.DateTimeField('创建时间', auto_now_add=True)
    user = models.ForeignKey(User, related_name='user',on_delete=models.CASCADE)


    def __str__(self):
        return '{}-{}'.format(self.name,self.position)

    class Meta:
        verbose_name='简历信息'
        verbose_name_plural = verbose_name