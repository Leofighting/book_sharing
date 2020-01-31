from app.view_modle.book import BookViewModel


class TradInfo:
    """交易信息"""
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__parse(goods)

    def __parse(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    @staticmethod
    def __map_to_trade(single):
        if single.create_datetime:
            time = single.create_datetime.strftime("%Y-%m-%d")
        else:
            time = "未知"
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id,
        )


class MyTrade:
    """我的交易信息"""
    def __init__(self, trades_of_mine, trades_count_list):
        self.trades = []
        self._trades_of_mine = trades_of_mine
        self._trades_count_list = trades_count_list

        self.trades = self.__parse()

    def __parse(self):
        temp_trades = []
        for trade in self._trades_of_mine:
            my_trade = self.__matching(trade)
            temp_trades.append(my_trade)
        return temp_trades

    def __matching(self, trade):
        count = 0

        for trade_count in self._trades_count_list:
            if trade.isbn == trade_count["isbn"]:
                count = trade_count["count"]

        r = {
            "trades_count": count,
            "book": BookViewModel(trade.book),
            "id": trade.id
        }
        return r
