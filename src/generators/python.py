
from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class PythonGenerator(GeneratorABC):

    @property
    def display_name(self): return "Python"

    keyboard_lang = KeyboardLanguage.ENGLISH

    _level_symbols = [
        set('asdfghjkl '),  # level 0
        set('asdfghjkl qwertyuiop'),  # level 1
        set('asdfghjkl qwertyuiop zxcvbnm'),  # level 2
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM .,_'),  # level 3
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 .,_'),  # level 4
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 `~!@#$%^&*()-=+[]{}\\|;:",<.>/?_' + "'")  # level 5
    ]

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
        'python', '--version', '--help', 'venv', 'source bin/activate', 'Scripts\\activate', 'pip install', 'pip install --upgrade', 'pip uninstall', 'pip freeze', 'pip list', 'pip show', 'pip install', 'pip list', 'pip freeze', '-c', 'unittest', 'pydoc', '-i', 'timeit', 'http.server', 'cProfile', 'pdb', 'deactivate', 'pip install --user', 'pip uninstall --yes', 'setup.py install', 'setup.py bdist_wheel', 'ensurepip --upgrade', 'venv --clear', 'pip search', 'tarfile', 'socket', 'smtpd -n -c DebuggingServer', '-m',

        # A few words for the first typing level.
        "dsl", "ask", "gl", "ddl", "gh", "sdk", "lag", "asg", "dfg", "hjd", "ksl", "glk",
        'add', 'flag', 'glass', 'dash', 'fall', 'lad', 'slag',
        'flash', 'flask', 'half', 'gag', 'hall', 'jag',
        'gall', 'has', 'gala', 'afk', 'shad', 'gas',

        # Snake case words
        "add_connection", "add_data", "add_hash", "add_init", "add_item", "add_key", "add_loop", "add_path", "add_safe",
        "add_split", "append_child", "append_data", "apply_filter", "array_index", "assign_value", "async_request",
        "await_response", "base_class", "binary_data", "bind_socket", "build_config", "build_index", "buffer_size",
        "cache_data", "cache_result", "call_function", "cancel_event", "change_status", "check_access", "check_condition",
        "check_exists", "check_flag", "check_input", "check_output", "check_status", "clean_cache", "clean_data",
        "clear_buffer", "clear_cache", "clear_input", "clone_object", "close_connection", "close_file", "commit_changes",
        "compare_data", "compile_code", "compress_data", "compute_hash", "config_file", "config_path", "connect_db",
        "connect_socket", "connection_pool", "constructor_args", "consume_event", "context_manager", "convert_data",
        "copy_file", "copy_list", "count_items", "create_backup", "create_class", "create_file", "create_index",
        "create_instance", "create_object", "create_session", "create_table", "current_index", "current_user",
        "data_buffer", "data_class", "data_field", "data_loader", "data_model", "data_parser", "data_queue", "data_reader",
        "data_source", "data_writer", "debug_log", "debug_mode", "decode_data", "default_args", "default_config",
        "default_dict", "default_value", "defer_task", "delete_data", "delete_file", "deserialize_data", "destroy_instance",
        "dict_keys", "dict_values", "directory_path", "disable_feature", "dispatch_event", "display_data", "display_error",
        "divide_values", "download_file", "dump_data", "duplicate_key", "dynamic_class", "encode_data", "encrypt_data",
        "end_point", "ensure_exists", "env_config", "error_code", "error_handler", "escape_chars", "eval_expression",
        "event_handler", "event_loop", "exclude_list", "execute_command", "execute_query", "exit_code", "export_data",
        "extend_class", "extract_data", "factory_method", "fail_safe", "fallback_value", "fetch_data", "fetch_items",
        "fetch_url", "field_name", "file_buffer", "file_name", "file_path", "file_reader", "file_stream", "file_writer",
        "filter_data", "filter_list", "final_value", "find_index", "find_value", "flush_buffer", "format_date",
        "format_string", "forward_request", "free_space", "from_dict", "function_args", "function_call", "function_name",
        "future_result", "generate_id", "generate_token", "get_class", "get_config", "get_connection", "get_context",
        "get_count", "get_data", "get_error", "get_event", "get_file", "get_id", "get_index", "get_input", "get_instance",
        "get_item", "get_key", "get_list", "get_name", "get_object", "get_output", "get_path", "get_property", "get_result",
        "get_state", "get_status", "get_token", "get_type", "get_user", "global_config", "global_index", "handle_error",
        "handle_event", "handle_input", "handle_output", "handle_request", "handle_response", "handle_signal", "hash_key",
        "header_data", "header_name", "hidden_value", "host_name", "http_client", "http_response", "id_generator",
        "ignore_case", "import_data", "import_file", "import_module", "increment_counter", "index_list",
        "init_class", "init_config", "init_file", "init_object", "init_state", "input_data", "insert_item",
        "install_package", "int_parser", "interface_name", "internal_cache", "invalid_input", "io_stream",
        "is_active", "is_authenticated", "is_empty", "is_enabled", "is_error", "is_none", "is_ready",
        "is_running", "is_valid", "iterate_list", "join_path", "json_data", "json_decoder", "json_encoder", "json_parser", "keep_alive", "key_value", "kill_process", "lambda_func", "last_index", "lazy_loader",
        "length_check", "line_buffer", "list_items", "list_parser", "load_config", "load_data", "load_default",
        "load_file", "load_module", "load_object", "load_session", "local_cache", "local_path", "lock_file", "log_debug",
        "log_error", "log_event", "log_file", "log_info", "log_level", "log_message", "log_output", "log_warning", "main_loop",
        "make_request", "map_values", "match_case", "match_pattern", "max_buffer", "max_count", "max_value", "memory_limit",
        "merge_dicts", "message_body", "method_args", "middleware_stack", "min_buffer", "min_value", "missing_key",
        "module_name", "monitor_task", "move_file", "multi_thread", "mutable_list", "name_error", "name_parser",
        "namespace_map", "network_call", "next_index", "next_token", "node_type", "null_value", "num_retries", "object_ref",
        "object_type", "offset_value", "open_connection", "open_file", "operation_name", "options_list", "output_buffer",
        "output_data", "override_method", "package_name", "packet_size", "page_number", "param_dict", "parse_args",
        "parse_config", "parse_data", "parse_error", "parse_json", "parse_line", "parse_xml", "partial_result",
        "password_hash", "path_exists", "path_name", "path_utils", "payload_data", "perform_check", "ping_host", "pipe_stream",
        "pool_manager", "pop_item", "post_data", "post_request", "prepare_args", "prepare_data", "previous_value",
        "primary_key", "print_error", "print_output", "process_data", "process_id", "process_pool", "progress_bar",
        "project_root", "property_name", "protocol_name", "proxy_config", "push_data", "put_item", "queue_item",
        "query_builder", "query_result", "raise_error", "read_config", "read_data", "read_file", "read_input", "read_line",
        "read_output", "receive_data", "receive_message", "reconnect_socket", "recursive_call", "reduce_data", "refresh_token",
        "register_event", "register_user", "release_lock", "reload_config", "remove_cache", "remove_data", "remove_item",
        "remove_key", "rename_file", "replace_item", "request_data", "request_id", "request_type", "reset_counter",
        "reset_flag", "resize_image", "resolve_path", "response_code", "response_data", "restart_service", "restore_backup",
        "retry_count", "return_code", "return_value", "retry_operation", "reverse_list", "rollback_changes", "root_dir",
        "route_handler", "run_async", "run_job", "run_loop", "run_task", "sanitize_input", "save_changes", "save_config",
        "save_file", "save_json", "schema_name", "search_filter", "secure_connection", "seed_value", "select_fields",
        "self_reference", "send_data", "send_email", "send_message", "send_request", "serialize_data", "server_port",
        "session_data", "session_id", "set_class", "set_config", "set_data", "set_default", "set_event", "set_flag",
        "set_input", "set_output", "set_status", "set_token", "setup_logger", "shared_cache", "shutdown_event",
        "signal_handler", "singleton_class", "skip_step", "sleep_time", "slice_data", "socket_client", "socket_server",
        "sort_items", "sort_list", "source_file", "split_line", "split_string", "sql_query", "start_loop", "start_process",
        "start_service", "start_thread", "state_machine", "static_data", "status_code", "step_count", "stop_event",
        "stop_thread", "stream_data", "string_buffer", "string_utils", "submit_form", "subscribe_event", "subprocess_call",
        "success_flag", "switch_case", "sync_data", "system_path", "table_data", "tag_parser", "task_manager", "temp_buffer",
        "temp_file", "template_engine", "test_case", "test_data", "text_input", "thread_pool", "thread_safe", "time_delay",
        "timeout_error", "timestamp_value", "to_dict", "to_list", "token_expiry", "transform_data", "translation_map",
        "trigger_event", "trim_string", "try_block", "tuple_data", "type_check", "type_error", "type_hint", "unbind_socket",
        "uninstall_package", "unit_test", "unknown_value", "unlock_file", "unpack_data", "update_cache", "update_config",
        "update_data", "update_field", "update_file", "upload_data", "upload_file", "upper_case", "url_parser", "use_cache",
        "user_agent", "user_data", "user_id", "username_field", "uuid_value", "validate_config", "validate_data",
        "validate_input", "validate_output", "value_error", "var_name", "version_check", "wait_event", "warning_message",
        "web_request", "while_loop", "write_buffer", "write_data", "write_file", "write_output", "xml_parser", "zip_file",
        "zip_path", "zip_utils", "zone_info"
    ]
