import env_cmd


read_environ = env_cmd.read_environ(
    'APPCONFIG',
    '/etc/polls/web.conf',
    {'DJANGO_SETTINGS_MODULE': 'mysite.settings'},
)
main = env_cmd.main(read_environ)
