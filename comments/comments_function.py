import os.path

comments = []


def create_file_if_not_exists():
    if not os.path.exists('./comments.db'):
        with open('./comments.db', 'w'):
            pass


def load_comments_from_file():
    global comments

    create_file_if_not_exists()

    with open('./comments.db', 'r') as file:
        for line in file.readlines():
            comments.append(line)


def save_comments_to_file():
    global comments

    with open('./comments.db', 'w') as file:
        for comment in comments:
            file.write(comment + "\n")


def add_comment(text):
    global comments
    comments.append(text)

    if comments:
        print('Old comments:')

    for comment in comments:
        print('\t' + comment)

