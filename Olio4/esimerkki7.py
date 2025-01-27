class Positive(int):
    def __new__(cls, value):
        if 0 <= value:
            return super().__new__(cls, value)
        raise ValueError('Positive supports only positivie integers.')

    def __init__(self, value) -> None:
        self._value = value

    def __add__(self, other):
        result = super().__add__(other)
        return (Positive(result))

    def __repr__(self):
        return f'Tämän olion arvo on {int(self)}'

print(Positive(5))
