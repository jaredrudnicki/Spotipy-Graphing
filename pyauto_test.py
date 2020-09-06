import pyautogui as pa



pa.PAUSE = 2.5

user_id = pa.prompt(text='enter profile link after user/', title='profile link user', default='soccerboy?si=mofnFRxHRzJ-VjmG8gGZOg')

pa.press('win')
pa.write('spotify')
pa.press('enter')
pa.press('space')



pa.hotkey('win','r')
pa.hotkey('ctrl','a')
pa.press('delete')
pa.write('cmd')
pa.press('enter')

#client_id = pa.prompt(text='enter client_id', title='client_id', default='')
#client_secret = pa.prompt(text='enter client_secret', title='client_secret', default='')
#redirect_uri = pa.prompt(text='enter redirect_uri', title='redirect_uri', default='http://google.com/')
pa.write('cd OneDrive\n')
pa.write('cd Desktop\n')

pa.write('SET client_secret = \'6a112ea19cc04a64b18164c1218198cb\'\n')
pa.write('SET client_id = \'ac16b07b2e97494eab56f93868924969\'\n')
pa.write('SET redirect_uri = \'http://google.com/\'\n')


pa.write('python sp_test.py ' + user_id + '\n')

pa.alert(text='copy and past the url that just opened into the command prompt', title='Instructions', button='ok')




