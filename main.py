import module_tools

module_tools.say_hello()
likes_count = 0


def add_like():
    global likes_count
    likes_count += 1

# Repository
#   -   main.py
#   -   module_tools.py
#
#
#
#
#   створити репозиторій
#          BRANCH NAME
# git init -b main
#
#   додати файли до репозиторію
#      <filename or directory name>
# git add .
#
#   створити комміт
# git commit -m "message"
#
#   видалити файли з репозиторію (з відстеження)
# git rm --cached
#
