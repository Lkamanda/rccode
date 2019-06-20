
def get_android_devices():
    android_devices_list = []
    device_config = []
    b = os.popen('adb devices')
    device_text = b.read()
    # 根据换行符对str进行切片

    # print(type(device_text))
    # print(device_text)
    b.close()
    # print(re.split(r'[\s]\s*', device_text))
    device_list = re.split(r'[\n]\n*', device_text)[1:-1]
    device_count = len(device_list)
    print(device_count)
    for i in device_list:
        print(re.split(r'[\s]\s*', i)[0])
        andoid_devices = re.split(r'[\s]\s*', i)[0]
        android_devices_list.append(andoid_devices)
    print(android_devices_list)
    mobile_config = {
        "UEUNW16C29005125": "8.0.0",
        "a82ccd1d": "8.0.0"
    }
    for i in android_devices_list:
        if i in mobile_config.keys():
            device_config.append((i, mobile_config[i]))
    print(device_config)
    return device_config, device_count


def startServers():
    pass


def desired_caps(z,port, mobile_config):
    # print('进入整个测试类')
    # PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
    # 连接手机app，初始化一些东西
    # mobile_config = [["UEUNW16C29005125", "8.0.0"], ["a82ccd1d", "8.0.0"]]
    #mobile_config, device_count = get_android_devices()
    print(mobile_config)
    desired_caps = {'platformName': 'Android',  # 手机类型
                    'platformVersion': mobile_config[z][1],  # 被测试手机，   baa822b7
                    'deviceName': mobile_config[z][0],  # baa822b7  a82ccd1d Q8JNNNGUOF8L4PON   设备名称， adb devices
                    'appPackage': 'com.erlinyou.worldlist',
                    'appActivity': 'com.erlinyou.map.Erlinyou',
                    'unicodeKeyboard': True,  # appium 传输中使用自己的输入法，可以传输中文
                    'resetKeyboard': True,  # 程序结束时重置原来的输入法
                    'noReset': True,  # 如果app存在则不重新安装
                    # 'autoGrantPermissions': 'True'
                    # 'app': r"C:\Users\zhoujialin\PycharmProjects\aut_LT\LT\apps\boobuz.apk"
                    # desired_caps['autoGrantPermissions'] = 'True'
                    }

    time.sleep(3)

if __name__ == '__main__':
    # global port, z, mobile_config
    threads_server = []     # 定义server 线程池
    threads_run = []        # 定义driver 线程池
    port = 4723             # 初始化端口
    runner = runner()
    mobile_config, devices_count = get_android_devices()

    for z in range(devices_count):
        # 启用多线程
        desired_caps(z=z,port=port,mobile_config=mobile_config)
        threads_server.append(threading.Thread(target=startServers()), args=())
        threads_run.append(threading.Thread(target=runner.main()), args=())

    for i in threads_server:
        i.start()
    for i in threads_run:
        i.start()
