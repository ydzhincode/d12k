В этом домашнем задании создан механизм логирования в приложении на Django.

Настройки логирования выполняют следующее:

В консоль выводятся все сообщения уровня DEBUG и выше, включающие время, уровень сообщения, сообщения.
Для сообщений WARNING и выше дополнительно выводится путь к источнику события (используется аргумент pathname в форматировании).
А для сообщений ERROR и CRITICAL еще выводится стэк ошибки (аргумент exc_info). Сюда попадают все сообщения с основного логгера django.

В файл general.log выводятся сообщения уровня INFO и выше только с указанием времени, уровня логирования, модуля, в котором возникло сообщение (аргумент module) и само сообщение.
Сюда также попадают сообщения с регистратора django

В файл errors.log выводятся сообщения только уровня ERROR и CRITICAL.
В сообщении указывается время, уровень логирования, само сообщение, путь к источнику сообщения и стэк ошибки.
В этот файл попадают сообщения только из логгеров django.request, django.server, django.template, django.db_backends.

В файл security.log попадают только сообщения, связанные с безопасностью, а значит только из логгера django.security.
Формат вывода предполагает время, уровень логирования, модуль и сообщение.
На почту отправляются сообщения уровней ERROR и выше из django.request и django.server, по формату как в errors.log, но без стэка ошибок.

Более того, при помощи фильтров указано, что в консоль сообщения отправляются только при DEBUG = True, а на почту и в файл general.log только при DEBUG = False.

Кроме этого, в файле custom_log_filters.py определены собственные фильтры, которые применены к обработчикам для исключения дублирования записей.
