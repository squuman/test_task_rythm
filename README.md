
Для инициализации проекта запустить init.sh (для *unix).

Если у вас windows, то придется делать ручками.

Для запуска тестов: pytest --browser Chrome/Firefox

Поддерживает только браузеры Chrome и Firefox.

Если у вас ошибка запуска Firefox с кодом 127, то требуется, чтобы корень запуска браузера был в /usr/bin, т.к скорее всего он у вас находится в /snap/...