
from generators.base import BaseGenerator


class PythonGenerator(BaseGenerator):

    _words = [
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
