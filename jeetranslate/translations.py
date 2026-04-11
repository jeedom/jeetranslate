from .prompt import Prompt


class Translations():

    def __init__(self) -> None:
        self._translation: dict[str, Prompt] = {}

    def add_translation(self, language: str, text: str, new_translation: str) -> None:
        if text not in self._translation:
            # new text, save it with current translation
            new_prompt = Prompt(text)
            new_prompt.set_translation(language, new_translation)
            self._translation[text] = new_prompt
        elif not self._translation[text].has_translation(language):
            # not yet translated, save this one
            self._translation[text].set_translation(language, new_translation)
        elif self._translation[text].get_translation(language) != new_translation:
            pass  # we already have a translation for this text and language, but it's different from the new one, we keep the first one and ignore the new one
        else:
            pass  # all fine, we found twice the same text and same translation

    def __contains__(self, text: str) -> bool:
        return text in self._translation

    def get_translations(self, text: str) -> dict[str, str]:
        return self._translation[text].get_translations() if text in self._translation else {}
