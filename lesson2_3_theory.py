#находим алерт и закрываем его
alert = browser.switch_to.alert
alert.accept()

#получаем текст из алерта
alert = browser.switch_to.alert
alert_text = alert.text

#вид окна, когда можно не согласиться
confirm = browser.switch_to.alert
confirm.accept()
#можно отказаться
confirm.dismiss()

#отправка ответа в промт
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()

#переключение между вкладками
browser.switch_to.window(window_name)

#поиск имени вкладки по номеру
new_window = browser.window_handles[1]
first_window = browser.window_handles[0]