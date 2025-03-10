
from errors import Errors
from generators.base import BaseGenerator
import random


class PythonGenerator(BaseGenerator):

    python_words = [
        # Keywords
        'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
        'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
        'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
        'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield',
        'match', 'case',

        # Special Identifiers
        'self', 'cls', '_', '__', 'self.__', 'self._', '@dataclass', '@classmethod', '@abstractmethod', '@staticmethod',

        # Common Built-in Functions
        'print', "print('...')", 'len', 'range', 'type', 'int', 'str', 'list', 'dict', 'set', 'tuple', 'float', 'bool',
        'open', 'input', 'sum', 'min', 'max', 'sorted', 'abs', 'round', 'enumerate', 'zip',
        'map', 'filter', 'reduce', 'any', 'all', 'isinstance', 'issubclass', 'date',

        # Common Dunder (Magic) Methods
        'def __init__', 'def __init__(self):', 'def __new__', 'def __str__', 'def __repr__', 'def __len__',
        'def __call__', 'def __getitem__', 'def __setitem__', 'def __delitem__',
        'def __iter__', 'def __next__', 'def __enter__', 'def __exit__',

        # Common Standard Library Modules
        'os', 'sys', 'json', 're', 'datetime', 'math', 'random', 'itertools', 'collections',
        'functools', 'logging', 'threading', 'multiprocessing', 'asyncio', 'pathlib', 'enum', "Enum",
        'pytest', 'pygame', 'abc', 'ABC',

        # Symbols and Operators
        '+', '-', '*', '/', '//', '%', '**', '==', '!=', '<', '>', '<=', '>=',
        '=', '+=', '-=', '*=', '/=', '//=', '%=', '**=', 'and', 'or', 'not',
        '&', '|', '^', '~', '<<', '>>', 'in', 'not in', 'is', 'is not',
        '->',

        # Delimiters
        '(', ')', '()', '[', ']', '[]', '{', '}', '{}', ':', ';', ',', '.', '...', '_', '@', "'", '"', "f'...'", 'f"..."',

        # Other
        'while True:', 'number', 'text', 'module', 'attribute', 'library', 'package',

        # Common variable names
        'i', 'j', 'k', 'x', 'y', 'z', 'name', 'age', 'count', 'result',
        'data', 'item', 'value', 'index', 'temp', 'exception', 'ex', 'e'
        'temp_list', 'args', 'kwargs', 'user_input', 'output', 'filename',
        'path', 'url', 'response', 'status', 'message', 'error', 'config',
        'settings', 'file', 'records', 'response_time', 'timestamp', 'start_time',
        'end_time', 'is_valid', 'is_empty', 'buffer', 'length', 'size', 'key',
        'obj', 'obj_list', 'model', 'query', 'connection', 'log', 'undefined',
        'api', 'instance', 'environment', 'env', 'local', 'localhost',

        # Common class names
        "App", "Base", "Config", "Controller", "Database", "Data", "Entity", "Error", "Exception", "Factory",
        "Handler", "Helper", "Job", "Logger", "Manager", "Mapper", "Model", "Node", "Parser", "Processor",
        "Queue", "Reader", "Registry", "Request", "Response", "Router", "Scheduler", "Serializer", "Service",
        "Session", "Settings", "Singleton", "State", "Strategy", "Task", "Thread", "Tracker", "Transformer",
        "Unit", "User", "Validator", "View", "Worker", "Writer", "Adapter", "Builder", "Command", "Component",
        "Controller", "Observer",

        # Common constant names
        'PI', 'E', 'MAX_INT', 'MIN_INT', 'NULL', 'TRUE', 'FALSE', 'DEFAULT',
        'SUCCESS', 'FAILURE', 'ERROR', 'TIMEOUT', 'MAX_RETRIES', 'MIN_RETRIES',
        'CACHE_TIMEOUT', 'BUFFER_SIZE', 'MAX_LENGTH', 'MIN_LENGTH', 'MAX_SIZE',
        'MIN_SIZE', 'MAX_VALUE', 'MIN_VALUE', 'API_KEY', 'AUTH_TOKEN', 'DB_HOST',
        'DB_PORT', 'DB_NAME', 'DB_USER', 'DB_PASSWORD', 'LOG_LEVEL', 'LOG_FILE',
        'CACHE_LIMIT', 'SESSION_TIMEOUT', 'MAX_CONNECTIONS', 'MIN_CONNECTIONS',
        'MAX_THREADS', 'MIN_THREADS', 'MAX_ATTEMPTS', 'RETRY_INTERVAL',
        'PAGE_SIZE', 'PAGE_LIMIT', 'BUFFER_CAPACITY', 'TIME_FORMAT', 'DATE_FORMAT',
        'HTTP_STATUS_OK', 'HTTP_STATUS_NOT_FOUND', 'HTTP_STATUS_ERROR', 'SALT',
        'ENCRYPTION_KEY', 'MAX_NAME_LENGTH', 'MIN_NAME_LENGTH', 'API_URL',


        # Command line
        'python', '--version', '--help', 'venv', 'source bin/activate', 'Scripts\\activate', 'pip install', 'pip install --upgrade', 'pip uninstall', 'pip freeze', 'pip list', 'pip show', 'pip install', 'pip list', 'pip freeze', '-c', 'unittest', 'pydoc', '-i', 'timeit', 'http.server', 'cProfile', 'pdb', 'deactivate', 'pip install --user', 'pip uninstall --yes', 'setup.py install', 'setup.py bdist_wheel', 'ensurepip --upgrade', 'venv --clear', 'pip search', 'tarfile', 'socket', 'smtpd -n -c DebuggingServer', '-m'

    ]

    def get(self, length: int, errors: Errors = Errors()) -> str:
        text = self.__get(length, errors)

        error_words = []
        for error_word, _ in errors.get_error_words():
            error_words.append(error_word)

        error_letters = []
        for error_letter, _ in errors.get_error_letters():
            error_letters.append(error_letter)

        del_words = []
        del_letters = []

        for word in error_words:
            if word in text:
                del_words.append(word)

        for letter in error_letters:
            if letter in del_words:
                del_letters.append(letter)
                print('letter in del_words!!!')

        for word in del_words:
            for letter in del_letters:
                errors.del_error(letter, word)

        if len(text) == length:
            return text
        elif len(text) > length:
            return text[:length]
        return text

    def __get(self, length: int, errors: Errors) -> str:
        total_len = -1
        words = []
        while True:
            if total_len >= length:
                break
            max_word_len = length - total_len - 1
            if max_word_len == 0:
                break

            words_and_weight = {}

            if len(errors.get_error_words()) > 0:
                error_words = []
                for word, _ in errors.get_error_words():
                    error_words.append(word)
                error_word = random.choice(error_words)
                error_weight = 0.5
                words_and_weight[error_word] = error_weight

            elif len(errors.get_error_words()) == 0 and len(errors.get_error_letters()) > 0:
                error_letters = []
                for letter, _ in errors.get_error_letters():
                    error_letters.append(letter)

                letter_word = self._get_random_word_with_letter(
                    max_length=max_word_len, letters=error_letters)
                error_letter_weight = 0.25
                words_and_weight[letter_word] = error_letter_weight

            else:
                usual_word = self._get_random_word(max_length=max_word_len)
                usual_weight = 0.25
                words_and_weight[usual_word] = usual_weight

            all_words = list(words_and_weight.keys())
            weights = list(words_and_weight.values())

            word = random.choices(all_words, weights=weights, k=1)[0]
            words.append(word)
            total_len += len(word) + 1  # + 1 space

        return " ".join(words)

    def _get_random_word(self, min_length: int = 0, max_length: int = 999):
        right_words = filter(lambda w: len(w) >= min_length and len(w) <= max_length, self.python_words)
        return random.choice(list(right_words))

    def _get_random_word_with_letter(self, min_length: int = 0, max_length: int = 999, letters: list[str] | str = ""):
        right_words = filter(
            lambda w: len(w) >= min_length and len(w) <= max_length and any(
                letter in w for letter in letters),
            self.python_words)

        return random.choice(list(right_words))
