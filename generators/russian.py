class Russian: 
    _words = []
    
    def __init__(self) -> None:
        with open("dictionaries/russian.txt", "r", encoding="utf-8") as f:
            self._words = f.read()