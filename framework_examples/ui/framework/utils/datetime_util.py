# coding=utf-8
from datetime import datetime, timezone


class DatetimeUtil(object):
    @staticmethod
    def get_str_datetime(exp_format):
        return datetime.now().strftime(exp_format)

    @staticmethod
    def get_current_time(offset_from_utc=0, date_time_format="%H:%M"):
        utc_dt = datetime.now(timezone.utc)
        dt = utc_dt.replace(hour=utc_dt.time().hour + offset_from_utc)
        return dt.strftime(date_time_format)

    @staticmethod
    def find_min_time(starts: list[datetime], ends: list[datetime]):
        min_time = ends[0] - starts[0]
        min_start = starts[0]
        min_end = ends[0]
        for i in range(1, len(starts)):
            if (ends[i] - starts[i]) < min_time:
                min_time = ends[i] - starts[i]
                min_start = starts[i]
                min_end = ends[i]
        return min_start, min_end

    @staticmethod
    def find_max_time(starts: list[datetime], ends: list[datetime]):
        max_time = ends[0] - starts[0]
        max_start = starts[0]
        max_end = ends[0]
        for i in range(1, len(starts)):
            if (ends[i] - starts[i]) > max_time:
                max_time = ends[i] - starts[i]
                max_start = starts[i]
                max_end = ends[i]
        return max_start, max_end
