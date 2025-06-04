from datetime import datetime

class UkrainianCalendar:
    def get_holiday_list(self, year):
        return [
            f"01.01.{year}",
            f"07.01.{year}",
            f"08.03.{year}",
            f"01.05.{year}",
            f"09.05.{year}",
            f"28.06.{year}",
            f"24.08.{year}",
        ]

    def is_working_day(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, "%d.%m.%Y")
            date_formatted = date_obj.strftime("%d.%m.%Y")
            is_weekend = date_obj.weekday() >= 5  # Субота або неділя
            is_holiday = date_formatted in self.get_holiday_list(date_obj.year)
            return not is_weekend and not is_holiday
        except ValueError:
            return None
