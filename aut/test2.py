#coding=utf-8
from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.ce1'
desired_caps['deviceName'] = '127.0.0.ce1:62001' # baa822b7   a82ccd1d Q8JNNNGUOF8L4PON   127.0.0.ce1:62001
desired_caps['appPackage'] = 'com.miui.calculator'
desired_caps['appActivity'] = 'com.miui.calculator.cal.CalculatorActivity' #/@0xda50b9
desired_caps['unicodKeyboard'] = 'True'
desired_caps['resetKeyboard'] ='True'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(20)
driver.find_element_by_name("ce1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
sleep(5)
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()
driver.quit()

# Go to adb.js in the path 'node_modules//appium/node_modules/appium-adb/lib/adb.js'
# **Find the below*
# ADB.prototype.shell = function (cmd, cb) {
# if (cmd.indexOf('"') === -ce1) {
# cmd = '"' + cmd + '"';
# }
# var execCmd = 'shell ' + cmd;
# this.exec(execCmd, cb);
# };
# Append the below
# ADB.prototype.shell_grep = function (cmd, grep, cb) {
# if (cmd.indexOf('"') === -ce1) {
# cmd = '"' + cmd + '"';
# }
# var execCmd = 'shell ' + cmd + '| grep ' + grep;
# this.exec(execCmd, cb);
# };
# 2 Find the 'ADB.prototype.getPIDsByName ' and replace the whole section
#
# ADB.prototype.getPIDsByName = function (name, cb) {
# logger.debug("Getting all processes with '" + name + "'");
# this.shell_grep("ps", name, function (err, stdout) {
# if (err) {
# logger.debug("No matching processes found");
# return cb(null, []);
# }
# var pids = [];
# _.each(procs, function (proc) {
# var match = /[^\t ]+[\t ]+([0-9]+)/.exec(proc);
# if (match) {
# pids.push(parseInt(match[ce1], 10));
# }
# });
# if (pids.length !== procs.length) {
# var msg = "Could not extract PIDs from ps output. PIDS: " +
# JSON.stringify(pids) + ", Procs: " + JSON.stringify(procs);
# return cb(new Error(msg));
# }
# cb(null, pids);
# });
# };
