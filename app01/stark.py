from django.shortcuts import HttpResponse,render,redirect
from django.utils.safestring import mark_safe
from django.conf.urls import url
from stark.service import v1
from app01 import models
from django.forms import ModelForm

class UserInfoModelForm(ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        error_messages = {
            'name':{
                'required':'用户名不能为空'
            }
        }

class UserInfoConfig(v1.StarkConfig):

    list_display = ['id','name']

    show_add_btn = True

    model_form_class = UserInfoModelForm

    # def extra_url(self):
    #     url_list = [
    #         url(r'^xxxxx/$', self.func),
    #     ]
    #     return url_list
    #
    # def func(self,request):
    #     return HttpResponse('....')

v1.site.register(models.UserInfo,UserInfoConfig) # UserInfoConfig(UserInfo,)

class RoleConfig(v1.StarkConfig):

    list_display = ['id','name']
v1.site.register(models.Role,RoleConfig) # StarkConfig(Role)



#:完成那个插件后添加一条数据可以完成简单的增删改查功能
class HostModelForm(ModelForm):
    class Meta:
        model = models.Host
        fields = ['id','hostname','ip','port']
        error_messages = {
            'hostname':{
                'required':'主机名不能为空',
            },
            'ip':{
                'required': 'IP不能为空',
                'invalid': 'IP格式错误',
            }

        }

class HostConfig(v1.StarkConfig):
    def ip_port(self,obj=None,is_header=False):
        if is_header:
            return '自定义列'
        return "%s:%s" %(obj.ip,obj.port,)

    list_display = ['id','hostname','ip','port',ip_port]
    # get_list_display

    show_add_btn = True
    # get_show_add_btn

    model_form_class = HostModelForm
    # get_model_form_class


    def extra_url(self):
        urls = [
            url('^report/$',self.report_view)
        ]
        return urls

    def report_view(self,request):
        return HttpResponse('自定义报表')

    def delete_view(self,request,nid,*args,**kwargs):
        if request.method == "GET":
            return render(request,'my_delete.html')
        else:
            self.model_class.objects.filter(pk=nid).delete()
            return redirect(self.get_list_url())


v1.site.register(models.Host,HostConfig)
