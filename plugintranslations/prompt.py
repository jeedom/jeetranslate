class Prompt():

    def __init__(self, text) -> None:
        self._text: str = text
        self._translations: dict[str, str] = {}

    def get_text(self) -> str:
        return self._text

    def has_translation(self, language: str) -> bool:
        return language in self._translations and self._translations[language] != ''

    def set_translation(self, language: str, translation: str) -> None:
        self._translations[language] = translation

    def get_translation(self, language: str) -> str:
        return self._translations[language] if language in self._translations else ''

    def set_translations(self, translations: dict[str, str]) -> None:
        self._translations = translations

    def get_translations(self) -> dict[str, str]:
        return self._translations
