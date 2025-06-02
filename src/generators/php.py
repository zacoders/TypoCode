from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class PhpGenerator(GeneratorABC):

    @property
    def display_name(self): return "PHP"

    keyboard_lang = KeyboardLanguage.ENGLISH

    _level_symbols = [
        set('asdfghjkl '),  # level 0
        set('asdfghjkl qwertyuiop'),  # level 1
        set('asdfghjkl qwertyuiop zxcvbnm'),  # level 2
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM .,;_'),  # level 3
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 .,;_{}[]()'),  # level 4
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 .,;_`~!@#$%^&*()-=+[]{}\\|:"<>/?' + "'")  # level 5
    ]

    _words = [
        # Keywords
        "abstract", "and", "array", "as", "break", "callable", "case", "catch", "class", "clone", "const",
        "continue", "declare", "default", "die", "do", "echo", "else", "elseif", "empty", "enddeclare",
        "endfor", "endforeach", "endif", "endswitch", "endwhile", "eval", "exit", "extends", "final",
        "finally", "for", "foreach", "function", "global", "goto", "if", "implements", "include",
        "include_once", "instanceof", "insteadof", "interface", "isset", "list", "namespace", "new",
        "or", "print", "private", "protected", "public", "require", "require_once", "return", "static",
        "switch", "throw", "trait", "try", "unset", "use", "var", "while", "xor", "yield", "yield from",
        "true", "false", "null", "TRUE", "FALSE", "NULL", "__halt_compiler", "match", "readonly",

        # Special Identifiers
        "$this", "self", "parent", "static", "__CLASS__", "__METHOD__", "__FUNCTION__", "__LINE__",
        "__FILE__", "__DIR__", "__NAMESPACE__", "__TRAIT__", "$_GET", "$_POST", "$_REQUEST", "$_SESSION",
        "$_COOKIE", "$_SERVER", "$_ENV", "$_FILES", "$GLOBALS", "$argc", "$argv",

        # Common Built-in Functions
        "array_merge", "array_push", "array_pop", "array_shift", "array_unshift", "array_slice", "array_splice",
        "array_keys", "array_values", "array_search", "array_key_exists", "array_filter", "array_map",
        "array_reduce", "array_walk", "array_sum", "array_product", "array_unique", "array_reverse",
        "count", "sizeof", "empty", "isset", "unset", "var_dump", "print_r", "var_export", "serialize",
        "unserialize", "json_encode", "json_decode", "strlen", "strpos", "strrpos", "substr", "str_replace",
        "str_ireplace", "strtolower", "strtoupper", "ucfirst", "ucwords", "trim", "ltrim", "rtrim",
        "explode", "implode", "preg_match", "preg_replace", "preg_split", "preg_match_all", "file_get_contents",
        "file_put_contents", "fopen", "fclose", "fread", "fwrite", "fgets", "file", "is_file", "is_dir",
        "file_exists", "mkdir", "rmdir", "unlink", "copy", "rename", "basename", "dirname", "pathinfo",
        "realpath", "scandir", "opendir", "readdir", "closedir", "time", "date", "strtotime", "mktime",
        "microtime", "sleep", "usleep", "rand", "mt_rand", "srand", "mt_srand", "min", "max", "abs",
        "round", "ceil", "floor", "number_format", "is_numeric", "is_int", "is_float", "is_string",
        "is_array", "is_object", "is_null", "is_bool", "gettype", "settype", "intval", "floatval",
        "strval", "boolval", "hash", "md5", "sha1", "base64_encode", "base64_decode", "urlencode",
        "urldecode", "htmlspecialchars", "htmlentities", "strip_tags", "nl2br",

        # Common Dunder (Magic) Methods
        "__construct", "__destruct", "__call", "__callStatic", "__get", "__set", "__isset", "__unset",
        "__sleep", "__wakeup", "__serialize", "__unserialize", "__toString", "__invoke", "__set_state",
        "__clone", "__debugInfo", "__autoload", "__get_state", "__set_state",

        # Common Standard Library Modules
        "PDO", "PDOStatement", "mysqli", "curl", "GuzzleHttp", "DateTime", "DateTimeImmutable", "DateInterval",
        "DatePeriod", "Exception", "ErrorException", "InvalidArgumentException", "RuntimeException",
        "LogicException", "BadMethodCallException", "DomainException", "OutOfBoundsException",
        "OutOfRangeException", "UnexpectedValueException", "ArrayObject", "ArrayIterator", "SplFileInfo",
        "SplFileObject", "DirectoryIterator", "RecursiveDirectoryIterator", "SplAutoloader", "Reflection",
        "ReflectionClass", "ReflectionMethod", "ReflectionProperty", "DOMDocument", "SimpleXMLElement",
        "XMLWriter", "XMLReader", "ZipArchive", "SoapClient", "SoapServer",

        # Symbols and Operators
        "+", "-", "*", "/", "%", "**", "++", "--", "==", "===", "!=", "!==", "<", ">", "<=", ">=",
        "<=>", "=", "+=", "-=", "*=", "/=", "%=", "**=", ".=", "&&", "||", "!", "and", "or", "xor",
        "&", "|", "^", "~", "<<", ">>", "?:", "??", "??=", "->", "=>", "::", "\\", "@", "$",

        # Delimiters
        "(", ")", "[", "]", "{", "}", ":", ";", ",", ".", "->", "::", "?", "\"", "'", "`", "<<<",
        "<<<EOD", "<<<'EOD'", "<?php", "<?=", "?>", "/*", "*/", "//", "#", "\n", "\r\n",

        # Other
        "<?php", "<?= echo", "if ($var)", "foreach ($array as $item)", "function name()", "class Name",
        "new Class()", "$var = new", "try { } catch", "public function", "private $property",

        # Common variable names
        "$name", "$age", "$count", "$result", "$data", "$item",
        "$value", "$index", "$temp", "$exception", "$args", "$input", "$output", "$filename",
        "$path", "$url", "$response", "$status", "$message", "$error", "$config", "$settings", "$file",
        "$records", "$timestamp", "$startTime", "$endTime", "$isValid", "$buffer", "$size", "$key",
        "$obj", "$model", "$query", "$connection", "$log", "$env", "$local", "$localhost", "$text",
        "$content", "$line", "$lines", "$word", "$words", "$char", "$num", "$number", "$total",
        "$sum", "$avg", "$maxVal", "$minVal", "$arr", "$list", "$row", "$rows", "$col", "$cols",

        # Common class names
        "App", "Base", "Config", "Controller", "Database", "Data", "Entity", "Error", "Exception", "Factory",
        "Handler", "Helper", "Job", "Logger", "Manager", "Mapper", "Model", "Node", "Parser", "Processor",
        "Queue", "Reader", "Registry", "Request", "Response", "Router", "Scheduler", "Serializer", "Service",
        "Session", "Settings", "Singleton", "State", "Strategy", "Task", "Thread", "Tracker", "Transformer",
        "Unit", "User", "Validator", "View", "Worker", "Writer", "Adapter", "Builder", "Command", "Component",
        "Observer", "Client", "Server", "Connection", "Interface", "Abstract", "Concrete", "Mixin", "Trait",

        # Common constant names
        "PI", "MAX_INT", "MIN_INT", "NULL", "TRUE", "FALSE", "DEFAULT", "SUCCESS", "FAILURE", "ERROR",
        "TIMEOUT", "CACHE_TIMEOUT", "BUFFER_SIZE", "MAX_LENGTH", "MIN_LENGTH", "MAX_SIZE", "MIN_SIZE", "API_KEY",
        "AUTH_TOKEN", "DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD", "LOG_LEVEL", "LOG_FILE",
        "CACHE_LIMIT", "SESSION_TIMEOUT", "MAX_CONNECTIONS", "RETRY_INTERVAL", "PAGE_SIZE", "TIME_FORMAT",
        "DATE_FORMAT", "DEBUG", "VERBOSE", "PRODUCTION", "DEVELOPMENT", "TEST", "STAGING", "APP_ENV",
        "APP_DEBUG", "APP_KEY", "APP_URL", "MAIL_HOST", "MAIL_PORT", "MAIL_USERNAME", "MAIL_PASSWORD",

        # Command line
        "php", "php -v", "php -m", "php -i", "composer", "composer install", "composer update", "composer require",
        "composer remove", "composer dump-autoload", "composer create-project", "artisan", "php artisan",
        "symfony", "doctrine", "phpunit", "php-cs-fixer", "phpstan", "psalm", "phing", "phar",
        "pecl", "phpize", "php-config", "xdebug", "opcache",

        # A few words for the first typing level.
        "as", "all", "ask", "lad", "jag", "lag", "sag", "fad", "gag", "hag", "dll", "hall", "fall", "gall", "flag", "slag", "glad", "add", "had", "has", "sad", "gal", "ash", "hash", "dash", "gals", "lags", "jags", "sags", "fads", "gags", "hags", "flash", "slash", "glass", "shall",

        # Common words
        "Add", "AddRange", "Aggregate", "All", "Any", "Append", "Apply", "Args", "Array", "Ascii", "Assert",
        "Assign", "Async", "Attr", "Auth", "Auto", "Await", "Base64", "Batch", "Begin", "Binary", "Bind",
        "Bool", "Break", "Build", "Byte", "Cache", "Call", "Cancel", "Case", "Cast", "Catch", "Chain",
        "Char", "Check", "Choice", "Class", "Clean", "Clear", "Click", "Clone", "Close", "Code", "Column",
        "Combine", "Command", "Compare", "Compile", "Complete", "Config", "Connect", "Console", "Const", "Content",
        "Context", "Continue", "Convert", "Copy", "Count", "Create", "Csv", "Current", "Custom", "Data",
        "Database", "Date", "Day", "Debug", "Decode", "Default", "Define", "Delete", "Depth", "Deserialize",
        "Detail", "Dict", "Diff", "Directory", "Disable", "Display", "Div", "Do", "Doc", "Document",
        "Domain", "Download", "Drop", "Dump", "Duration", "Each", "Edit", "Element", "Else", "Email",
        "Empty", "Enable", "Encode", "End", "Engine", "Enter", "Entity", "Enum", "Equal", "Error",
        "Event", "Every", "Example", "Excel", "Except", "Execute", "Exist", "Exit", "Export", "Expression",
        "Extension", "Extract", "Factory", "Fail", "False", "Feature", "Field", "File", "Fill", "Filter",
        "Find", "First", "Fix", "Flag", "Float", "Folder", "For", "Format", "Form", "Frame", "From",
        "Full", "Function", "Generate", "Get", "Given", "Global", "Go", "Group", "Handle", "Hash",
        "Has", "Head", "Header", "Height", "Help", "Here", "Hide", "High", "Home", "Host",
        "Html", "Http", "Icon", "Id", "If", "Image", "Import", "In", "Include", "Index",
        "Info", "Init", "Input", "Insert", "Install", "Instance", "Int", "Interface", "Internal", "Into",
        "Invalid", "Is", "Item", "Iterator", "Job", "Join", "Json", "Jump", "Just", "Keep",
        "Key", "Keyword", "Kind", "Label", "Language", "Large", "Last", "Launch", "Layer", "Layout",
        "Lead", "Learn", "Left", "Length", "Level", "Library", "License", "Life", "Like", "Limit",
        "Line", "Link", "List", "Load", "Local", "Location", "Lock", "Log", "Login", "Long",
        "Look", "Loop", "Low", "Machine", "Mail", "Main", "Make", "Manager", "Many", "Map",
        "Mark", "Match", "Math", "Max", "Mean", "Member", "Memory", "Menu", "Message", "Method",
        "Middle", "Min", "Missing", "Mode", "Model", "Module", "Monitor", "Month", "More", "Move",
        "Multi", "Multiple", "Name", "Navigate", "Near", "Need", "Network", "New", "Next", "No",
        "Node", "None", "Normal", "Not", "Note", "Nothing", "Now", "Null", "Number", "Object",
        "Of", "Off", "Ok", "Old", "On", "Once", "Only", "Open", "Operation", "Option",
        "Or", "Order", "Other", "Out", "Output", "Over", "Own", "Package", "Page", "Panel",
        "Parameter", "Parent", "Parse", "Part", "Pass", "Password", "Path", "Pattern", "Pause", "Pay",
        "Perform", "Period", "Permission", "Phone", "Pick", "Picture", "Piece", "Place", "Plan", "Play",
        "Please", "Plugin", "Point", "Policy", "Pool", "Pop", "Port", "Position", "Post", "Power",
        "Pre", "Prepare", "Present", "Press", "Pretty", "Previous", "Price", "Primary", "Print", "Private",
        "Process", "Product", "Program", "Project", "Property", "Protect", "Protocol", "Provide", "Public", "Pull",
        "Push", "Put", "Quality", "Query", "Question", "Queue", "Quick", "Quit", "Quote", "Random",
        "Range", "Rate", "Raw", "Read", "Ready", "Real", "Reason", "Receive", "Record", "Red",
        "Reduce", "Reference", "Refresh", "Register", "Regular", "Related", "Release", "Remove", "Repeat", "Replace",
        "Report", "Request", "Require", "Reset", "Resource", "Response", "Rest", "Result", "Return", "Review",
        "Right", "Role", "Root", "Round", "Route", "Row", "Rule", "Run", "Safe", "Same",
        "Save", "Scale", "Scan", "Schedule", "Schema", "Scope", "Score", "Screen", "Script", "Search",
        "Second", "Section", "Security", "See", "Select", "Send", "Series", "Server", "Service", "Session",
        "Set", "Setting", "Setup", "Share", "Shell", "Short", "Show", "Side", "Sign", "Simple",
        "Single", "Site", "Size", "Skip", "Sleep", "Small", "So", "Social", "Socket", "Some",
        "Sort", "Source", "Space", "Special", "Split", "Sql", "Stack", "Stage", "Standard", "Start",
        "State", "Static", "Status", "Step", "Stop", "Storage", "Store", "String", "Strong", "Structure",
        "Style", "Subject", "Submit", "Success", "Such", "Sum", "Summary", "Super", "Support", "Sure",
        "System", "Table", "Tag", "Take", "Task", "Team", "Template", "Term", "Test", "Text",
        "Than", "That", "The", "Theme", "Then", "There", "Thing", "Think", "This", "Thread",
        "Through", "Time", "Title", "To", "Today", "Together", "Token", "Tool", "Top", "Total",
        "Track", "Transaction", "Transform", "Tree", "True", "Try", "Turn", "Type", "Under", "Union",
        "Unique", "Unit", "Until", "Up", "Update", "Upload", "Upper", "Url", "Use", "User",
        "Using", "Util", "Valid", "Value", "Variable", "Vector", "Version", "Very", "Video", "View",
        "Virtual", "Visit", "Visual", "Wait", "Walk", "Want", "Warning", "Watch", "Way", "We",
        "Web", "Week", "Weight", "Well", "What", "When", "Where", "Which", "While", "White",
        "Who", "Why", "Wide", "Width", "Will", "Window", "With", "Within", "Without", "Word",
        "Work", "World", "Write", "Wrong", "Year", "Yes", "Yet", "You", "Your", "Zero",

        # Common variable names
        "$userName", "$userEmail", "$userPassword", "$userId", "$userProfile", "$userData", "$userInfo",
        "$accountNumber", "$accountBalance", "$accountStatus", "$accountType", "$accountHolder",
        "$customerName", "$customerAddress", "$customerPhone", "$customerEmail", "$customerId",
        "$orderNumber", "$orderDate", "$orderTotal", "$orderStatus", "$orderItems", "$orderData",
        "$productName", "$productPrice", "$productId", "$productCategory", "$productStock",
        "$invoiceNumber", "$invoiceDate", "$invoiceTotal", "$invoiceStatus", "$invoiceItems",
        "$paymentMethod", "$paymentDate", "$paymentAmount", "$paymentStatus", "$paymentId",
        "$transactionId", "$transactionDate", "$transactionAmount", "$transactionType", "$transactionStatus",
        "$employeeName", "$employeeId", "$employeeEmail", "$employeePhone", "$employeeDepartment",
        "$departmentName", "$departmentId", "$departmentHead", "$departmentLocation", "$departmentBudget",
        "$projectName", "$projectId", "$projectStartDate", "$projectEndDate", "$projectStatus",
        "$taskName", "$taskId", "$taskDescription", "$taskStartDate", "$taskEndDate", "$taskStatus",
        "$fileName", "$filePath", "$fileSize", "$fileType", "$fileExtension", "$fileContent",
        "$directoryPath", "$directoryName", "$directorySize", "$directoryFiles", "$directorySubfolders",
        "$configSetting", "$configValue", "$configKey", "$configFile", "$configPath", "$configData",
        "$logMessage", "$logLevel", "$logTimestamp", "$logFile", "$logEntry", "$logData",
        "$errorMessage", "$errorCode", "$errorDetails", "$errorTimestamp", "$errorTrace",
        "$exceptionMessage", "$exceptionCode", "$exceptionFile", "$exceptionLine", "$exceptionTrace",
        "$responseStatus", "$responseMessage", "$responseCode", "$responseData", "$responseTime",
        "$requestUrl", "$requestMethod", "$requestHeaders", "$requestBody", "$requestParams",
        "$apiEndpoint", "$apiKey", "$apiSecret", "$apiVersion", "$apiResponse", "$apiClient",
        "$databaseName", "$databaseUser", "$databasePassword", "$databaseHost", "$databasePort",
        "$connectionString", "$connectionTimeout", "$connectionStatus", "$connectionId", "$pdo",
        "$queryString", "$queryParameters", "$queryResult", "$queryExecutionTime", "$queryError",
        "$sessionId", "$sessionUser", "$sessionStartTime", "$sessionEndTime", "$sessionData",
        "$tokenValue", "$tokenExpiration", "$tokenType", "$tokenIssuer", "$tokenAudience",
        "$authUser", "$authToken", "$authMethod", "$authStatus", "$authProvider", "$authData",
        "$cacheKey", "$cacheValue", "$cacheExpiration", "$cacheSize", "$cacheStatus", "$cacheData",
        "$emailSubject", "$emailBody", "$emailSender", "$emailRecipient", "$emailTimestamp", "$emailAttachments",
        "$jsonData", "$xmlData", "$csvData", "$htmlContent", "$textContent", "$binaryData",
        "$imageUrl", "$imagePath", "$imageWidth", "$imageHeight", "$imageFormat", "$imageSize",
        "$videoUrl", "$videoPath", "$videoDuration", "$videoFormat", "$videoResolution",
        "$audioUrl", "$audioPath", "$audioDuration", "$audioFormat", "$audioBitrate",
        "$documentTitle", "$documentContent", "$documentAuthor", "$documentDate", "$documentType",
        "$reportTitle", "$reportContent", "$reportAuthor", "$reportDate", "$reportStatus",
        "$formData", "$formFields", "$formErrors", "$formIsValid", "$formMethod", "$formAction",
        "$inputValue", "$inputType", "$inputName", "$inputPlaceholder", "$inputLabel",
        "$modelName", "$modelFields", "$modelData", "$modelInstance", "$modelId", "$modelTable",
        "$controllerName", "$controllerAction", "$controllerMethod", "$controllerRequest", "$controllerResponse",
        "$viewName", "$viewData", "$viewTemplate", "$viewPath", "$viewContent", "$viewVars",
        "$routeName", "$routePath", "$routeParams", "$routeController", "$routeAction", "$routeMiddleware",
        "$middlewareName", "$middlewareHandle", "$middlewareRequest", "$middlewareResponse", "$middlewareNext",
        "$serviceProvider", "$serviceContainer", "$serviceName", "$serviceInstance", "$serviceConfig",
        "$repositoryModel", "$repositoryQuery", "$repositoryData", "$repositoryResult", "$repositoryFind",
        "$migrationTable", "$migrationUp", "$migrationDown", "$migrationColumns", "$migrationSchema",
        "$seedData", "$seedTable", "$seedRecords", "$seedFaker", "$seedFactory", "$seedModel",
        "$testCase", "$testMethod", "$testData", "$testResult", "$testAssert", "$testMock",
        "$validationRules", "$validationData", "$validationErrors", "$validationPassed", "$validationFailed",
        "$paginationPage", "$paginationPerPage", "$paginationTotal", "$paginationLinks", "$paginationData",
        "$collectionItems", "$collectionFilter", "$collectionMap", "$collectionReduce", "$collectionSort",
        "$eventName", "$eventData", "$eventListener", "$eventDispatcher", "$eventHandler",
        "$jobName", "$jobData", "$jobQueue", "$jobDelay", "$jobAttempts", "$jobFailed",
        "$mailTo", "$mailFrom", "$mailSubject", "$mailBody", "$mailAttachment", "$mailSend",
        "$notificationUser", "$notificationMessage", "$notificationChannel", "$notificationData", "$notificationSend",
        "$httpClient", "$httpRequest", "$httpResponse", "$httpHeaders", "$httpStatus", "$httpCookies",
        "$curlHandle", "$curlOptions", "$curlResponse", "$curlError", "$curlInfo", "$curlClose",
        "$redisClient", "$redisKey", "$redisValue", "$redisExpire", "$redisPipeline", "$redisConnection",
        "$memcacheClient", "$memcacheKey", "$memcacheValue", "$memcacheExpire", "$memcacheServer",
        "$elasticsearchClient", "$elasticsearchIndex", "$elasticsearchType", "$elasticsearchQuery", "$elasticsearchResult",
        "$mongoClient", "$mongoDatabase", "$mongoCollection", "$mongoDocument", "$mongoQuery", "$mongoCursor",
        "$rabbitConnection", "$rabbitChannel", "$rabbitQueue", "$rabbitMessage", "$rabbitConsumer", "$rabbitPublisher",
    ]
