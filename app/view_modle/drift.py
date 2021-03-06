from app.libs.enums import PendingStatus


class DriftCollection:
    """鱼漂集合"""
    def __init__(self, drifts, current_user_id):
        self.data = []
        self.data = self.__parse(drifts, current_user_id)

    @staticmethod
    def __parse(drifts, current_user_id):
        return [DriftViewModel(drift, current_user_id).data for drift in drifts]


class DriftViewModel:
    """鱼漂"""
    def __init__(self, drift, current_user_id):
        self.data = {}
        self.data = self.__parse(drift, current_user_id)

    @staticmethod
    def requester_or_gifter(drift, current_user_id):
        """判断是需求者还是赠送者"""
        return "requester" if drift.requester_id == current_user_id else "gifter"

    def __parse(self, drift, current_user_id):
        you_are = self.requester_or_gifter(drift, current_user_id)
        pending_status = PendingStatus.pending_str(drift.pending, you_are)
        r = {
            "drift_id": drift.id,
            "book_title": drift.book_title,
            "book_author": drift.book_author,
            "book_img": drift.book_img,
            "date": drift.create_datetime.strftime("%Y-%m-%d"),
            "message": drift.message,
            "address": drift.address,
            "recipient_name": drift.recipient_name,
            "mobile": drift.mobile,
            "status": drift.pending,
            "you_are": you_are,
            "operator": drift.requester_nickname if you_are != "requester" else drift.gifter_nickname,
            "status_str": pending_status,
        }

        return r
