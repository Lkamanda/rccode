from LT.utils.public_method import *


class Public_element:
    def __init__(self):
        self.PB = Public_method()

    # 首页用户图标 button
    user_avatar = "user_avatar_img"
    # 个人中心 登录/注册 button
    dl = "user_name_tv"
    # 个人中心 微信如口
    wx = "iv_other_login"
    # 微信登录页面 账号名 button
    wx_user = "//*[text='请填写微信号/QQ号/邮箱']"
    # 微信登录页面密码 button
    wx_password = "//android.widget.FrameLayout[@content-desc='当前所在页面,登录微信']/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText"
    # 微信登录页面 登录button
    wx_dl = "com.tencent.mm:id/ch7"

    # //android.widget.FrameLayout[@content-desc="当前所在页面,登录微信"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText
    def get_user_avatar(self):
        print(self.PB.join_together(x=Public_element.user_avatar))
        return print(self.PB.join_together(x=Public_element.user_avatar))


if __name__ == '__main__':
    el = Public_element()
    el.get_user_avatar()
