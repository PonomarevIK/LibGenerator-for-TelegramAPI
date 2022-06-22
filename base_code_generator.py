import re
API_URL = "https://api.telegram.org/bot{token}/{method}"

class BaseObject:
    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters


class BaseMethod(BaseObject):
    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.return_type = self.get_return_type()

    def get_return_type(self) -> str:
        """Finds what type of object a method returns based on its description (not 100 % reliable but works for now).
        The way it works is it finds a sentence with word 'return' in it. Then finds and returns the first
        capitalized word from that sentence, because type names are capitalized in the docs"""
        return_type = "Null"
        capitalized_word = re.compile(r"(?!Array)\b([A-Z]\w*)\b")  # finds any capitalized word except for "Array"

        for sentence in self.description.split("."):
            if "error" in sentence.lower():
                continue
            if "return" in sentence.lower():
                if match := capitalized_word.search(sentence.lstrip(), 1):  # skip the first letter, its always capital
                    return_type = match.group()
                    if "array" in sentence.lower():
                        return_type = f"[{return_type.removesuffix('s')}]"
        return return_type
