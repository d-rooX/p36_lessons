import module_tools
from comments import comments_function
from likes import likes_function

module_tools.say_hello()

comments_function.load_comments_from_file()

while True:
    action = input('Write your action: [add_like, add_comment, quit]: ')
    match action:
        case 'add_like':
            likes_function.add_like()
        case 'add_comment':
            text = input('Write comment text: ')
            comments_function.add_comment(text)
        case 'quit':
            break

comments_function.save_comments_to_file()


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
#   поточний статус
# git status
#
#   історія змін репозиторію
# git log
#
#   різниця між двома коммітами або гілками
# git diff
#
#   створити гілку
# git branch <branch>
#
#   змінити гілку
# git checkout <branch>
