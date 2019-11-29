import re

from rest_framework.views import APIView
from django.core.cache import cache
from django.conf import settings

from libs import tx_sms
from utils.response import APIResponse
from . import models, serializers, throttles


# 多方式登录
class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            return APIResponse(data={
                'username': serializer.user.username,
                'token': serializer.token
            })
        return APIResponse(1, 'failed', data=serializer.errors, http_status=400)


# 发送短信
class SMSAPIView(APIView):
    throttle_classes = [throttles.SMSRateThrottle]
    def post(self, request, *args, **kwargs):
        # 拿到前台手机
        mobile = request.data.get('mobile')
        if not (mobile and re.match(r'^1[3-9][0-9]{9}$', mobile)):
            return APIResponse(2, '手机号格式有误')
        # 获取验证码
        code = tx_sms.get_code()
        # 发送短信
        result = tx_sms.send_sms(mobile, code, settings.SMS_EXP // 60)
        # 服务器缓存验证码
        if not result:
            return APIResponse(1, '发送验证码失败')
        cache.set('sms_%s' % mobile, code, settings.SMS_EXP)
        # 校验发送的验证码与缓存的验证码是否一致
        # print('>>>> %s - %s <<<<' % (code, cache.get('sms_%s' % mobile)))
        return APIResponse(0, '发送验证码成功')


# 手机验证码登录
class LoginMobileAPIView(APIView):
    pass

# 手机验证码注册
class RegisterAPIView(APIView):
    pass


# 手机注册验证
class MobileAPIView(APIView):
    def post(self, request, *args, **kwargs):
        mobile = request.data.get('mobile')

        # 不管前台处不处理格式校验，后台一定需要校验
        if not (mobile and re.match(r'^1[3-9][0-9]{9}$', mobile)):
            return APIResponse(2, '手机号格式有误')

        try:
            # 已经注册了
            models.User.objects.get(mobile=mobile)
            return APIResponse(1, '手机已注册')
        except:
            # 没有注册过
            return APIResponse(0, '手机未注册')


