import enum

RE_GAME_ID = r"\w+-\w+-\w+-\w+-\w+"


class CommandData(str, enum.Enum):
    START = "start"
    HELP = "help"

    def __str__(self):
        return self.value

    @property
    def description(self):
        match self:
            case self.START:
                return "Запустить бота"
            case self.HELP:
                return "Справка"


class CallbackData(str, enum.Enum):
    EXAMPLE = "example"
    IGNORE = "ignore"
    UNKNOWN = ".*"

    def __str__(self):
        return self.value

    @property
    def regex(self):
        return "^" + self + "$"
