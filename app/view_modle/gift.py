from app.view_modle.book import BookViewModel


class MyGifts:
    """我的礼物集合"""
    def __init__(self, gifts_of_mine, wish_count_list):
        self.gifts = []
        self.__gifts_of_mine = gifts_of_mine
        self.__wish_count_list = wish_count_list
        self.gifts = self.__parse()

    def __parse(self):
        temp_list = []
        for gift in self.__gifts_of_mine:
            my_gift = self.__matching(gift)
            temp_list.append(my_gift)
        return temp_list

    def __matching(self, gift):
        count = 0
        for wish_count in self.__wish_count_list:
            if gift.isbn == wish_count["isbn"]:
                count = wish_count["count"]

        r = {
            "wishes_count": count,
            "book": BookViewModel(gift.book),
            "id": gift.id
        }

        return r
