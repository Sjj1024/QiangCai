import uiautomator2 as u2

# Specify device serial number if multiple devices are connected
d = u2.connect()
print(d.info)

d.xpath('//*[@text="视频"]').click()