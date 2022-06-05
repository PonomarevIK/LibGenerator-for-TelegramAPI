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
        return_type = "{}"
        for sentence in self.description.split("."):
            if "error" in sentence:
                continue
            if "return" in sentence.lower():
                for word in sentence.split()[1:]:
                    if word.lower() == "array":
                        return_type = "[" + return_type + "]"
                    elif word == "True":
                        return "Boolean"
                    elif word and word[0].isupper():
                        return return_type.format(word.removesuffix("s") if ("[" in return_type) else word)
        return return_type
