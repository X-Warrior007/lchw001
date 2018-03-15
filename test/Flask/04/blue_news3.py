from delete_author_book2 import api

@api.route('/news')
def news():
    return 'news info'

