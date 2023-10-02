import os.path

comments = []

def load_comments_from_file():
    global comments

    if not os.path.exists('./comments.db'):
        # creating file
        with open('./comments.db', 'w'):
            pass

    with open('./comments.db', 'r') as file:
        for line in file.readlines():
            comments.append(line)



def add_comment(text):
    global comments
    comments.append(text)

