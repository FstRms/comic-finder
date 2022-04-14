"""Module to format data"""


class Formatter:
    """
    Formatter class
    """

    def __init__(self, data):
        self.data = data

    def format_character(self):
        """
        Format data
        """
        output = []
        for obj in self.data:
            mapping = {
                "id": obj["id"],
                "name": obj["name"],
                "image": obj["thumbnail"]["path"],
                "appearances": obj["comics"]["available"],
            }
            output.append(mapping)
        return output

    def format_comic(self):
        """
        Format data
        """
        output = []
        for obj in self.data:
            mapping = {
                "id": obj["id"],
                "title": obj["title"],
                "image": obj["images"][0]["path"],
                "OnsaleDate": self.get_date(obj["dates"]),
            }
            output.append(mapping)
        return output

    @staticmethod
    def get_date(dates):
        """
        Get date
        """
        for date in dates:
            if date["type"] == "onsaleDate":
                return date["date"]
