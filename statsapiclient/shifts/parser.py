"""Module for parsing TOI HTML reports."""
import re

from bs4 import BeautifulSoup


class ShiftReportParser:
    """Parser class for TOI shift report HTML."""

    def __init__(self, raw_html):
        self.html_soup = BeautifulSoup(raw_html, "html.parser")
        self.player_shifts = {}

        self._current_player_number = 0

    def parse(self):
        """Runs the whole parsing process."""
        raw_toi_data = self.find_target_shift_data()

        return self.parse_shift_data(raw_toi_data)

    def find_target_shift_data(self):
        """Finds contents of main table element.

        Returns:
            list (obj): A list of element objects.
        """
        main_div = self.html_soup.find_all("div", class_="pageBreakAfter")
        main_div_children = main_div[0].children
        main_table = self.remove_new_lines(main_div_children)[0]
        main_table_row = self.remove_new_lines(main_table.contents)[3]
        main_table_cell = self.remove_new_lines(main_table_row)[0]
        target_table = self.remove_new_lines(main_table_cell.contents)[0]
        target_rows = self.remove_new_lines(target_table.contents)

        return target_rows

    def parse_shift_row_data(self, row_data):
        """Parses shift data from each target row.

        Returns:
            list (dict): A list of player shift dicts.
        """
        row_data = [value.contents[0] for value in row_data]

        start_of_shift = row_data[2].split("/")[0].strip()
        end_of_shift = row_data[3].split("/")[0].strip()
        event = row_data[5] if row_data[5] in ("G", "P") else ""

        shift_dict = {
            "shift_number": int(row_data[0]),
            "period": int(row_data[1]),
            "start_of_shift": start_of_shift,
            "end_of_shift": end_of_shift,
            "duration": row_data[4],
            "event": event,
        }

        self.player_shifts[self._current_player_number]["shifts"].append(shift_dict)

    def parse_player_heading(self, header_data):
        """Parses content from player heading.

        Args:
            header_data: A header row with text contents.
        """
        raw_player_name = header_data.contents[0]
        player_name_match = re.search(
            r"(\d{1,2}) ([-'a-zA-Z]+), ([-'a-zA-Z]+)",
            raw_player_name,
        )

        player_number = player_name_match.group(1)
        player_last_name = player_name_match.group(2)
        player_first_name = player_name_match.group(3)

        self.player_shifts[player_number] = {
            "player_name": f"{player_first_name} {player_last_name}",
            "shifts": [],
        }

        self._current_player_number = player_number

    def parse_shift_data(self, raw_toi_data):
        """Parses each row of shift data.

        Args:
            raw_toi_data (list): A list of row objects.

        Returns:
            dict: A dict of player shifts.
        """

        for row in raw_toi_data:
            row_contents = self.remove_new_lines(row.contents)
            row_classes = row.attrs.get("class", ())

            if len(row_contents) == 0:
                print("no contents in row...skipping.")
                continue

            if "evenColor" in row_classes or "oddColor" in row_classes:
                self.parse_shift_row_data(row_contents)

            if "playerHeading" in row_contents[0].attrs.get("class", ()):
                self.parse_player_heading(row_contents[0])

        return self.player_shifts

    @staticmethod
    def remove_new_lines(contents):
        """Removes newline characters from an iterable.

        Returns:
            list (obj): A list of element objects.
        """

        return [item for item in contents if item != "\n"]
