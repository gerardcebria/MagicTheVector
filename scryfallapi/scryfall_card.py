class Card:
    def __init__(self, card_id: str, type_line: str, colors: str, oracle_text: str,
                 set_id: str, card_name: str, image_url: str) -> None:
        self._card_id = card_id
        self._type_line = type_line
        self._colors = colors
        self._oracle_text = oracle_text
        self._set_id = set_id
        self._card_name = card_name
        self._image_url = image_url

    # Getter methods
    def get_card_id(self) -> str:
        return self._card_id

    def get_type_line(self) -> str:
        return self._type_line

    def get_colors(self) -> str:
        return self._colors

    def get_oracle_text(self) -> str:
        return self._oracle_text

    def get_set_id(self) -> str:
        return self._set_id

    def get_card_name(self) -> str:
        return self._card_name

    def get_image_url(self) -> str:
        return self._image_url

    # Setter methods
    def set_card_id(self, card_id: str) -> None:
        self._card_id = card_id

    def set_type_line(self, type_line: str) -> None:
        self._type_line = type_line

    def set_colors(self, colors: str) -> None:
        self._colors = colors

    def set_oracle_text(self, oracle_text: str) -> None:
        self._oracle_text = oracle_text

    def set_set_id(self, set_id: str) -> None:
        self._set_id = set_id

    def set_card_name(self, card_name: str) -> None:
        self._card_name = card_name

    def set_image_url(self, image_url: str) -> None:
        self._image_url = image_url
