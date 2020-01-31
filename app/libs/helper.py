def is_isbn_or_key(word):
    """判断用户输入的是 关键字 或者 isbn编码"""
    # isbn编码的组成：13个数字 or 10个数字（含有"-"）
    isbn_or_key = "key"
    if len(word) == 13 and word.isdigit():
        isbn_or_key = "isbn"
    short_word = word.replace("-", "")
    if "-" in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = "isbn"

    return isbn_or_key
