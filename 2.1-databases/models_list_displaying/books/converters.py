from datetime import datetime, date

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    date_format = '%Y-%m-%d'


    def to_python(self, value):
        return datetime.strptime(value, self.date_format)

    def to_url(self, value: datetime):
        return value.__str__()