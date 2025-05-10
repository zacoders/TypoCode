from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class TypeScriptGenerator(GeneratorABC):

    @property
    def display_name(self): return "TypeScript"

    keyboard_lang = KeyboardLanguage.ENGLISH

    _level_symbols = [
        set('asdfghjkl '),  # level 0
        set('asdfghjkl qwertyuiop'),  # level 1
        set('asdfghjkl qwertyuiop zxcvbnm'),  # level 2
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM .,_;:'),  # level 3
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 .,_:{}[]()$|'),  # level 4
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 `~!@#$%^&*()-=+[]{}\\|;:",<.>/?_' + "'")  # level 5
    ]

    _words = [
        # TypeScript Keywords
        'abstract', 'any', 'as', 'asserts', 'async', 'await', 'bigint', 'boolean', 'break',
        'case', 'catch', 'class', 'const', 'constructor', 'continue', 'debugger', 'declare',
        'default', 'delete', 'do', 'else', 'enum', 'export', 'extends', 'false', 'finally',
        'for', 'from', 'function', 'get', 'if', 'implements', 'import', 'in', 'infer',
        'instanceof', 'interface', 'is', 'keyof', 'let', 'module', 'namespace', 'never', 'new',
        'null', 'number', 'object', 'package', 'private', 'protected', 'public', 'readonly',
        'require', 'return', 'set', 'static', 'string', 'super', 'switch', 'symbol', 'this',
        'throw', 'true', 'try', 'type', 'typeof', 'undefined', 'unique', 'unknown', 'var',
        'void', 'while', 'with', 'yield',

        # Common decorators
        '@Injectable', '@Component', '@Input', '@Output', '@NgModule', '@HostListener', '@Directive',

        # Built-in/Global objects
        'Array', 'Boolean', 'console', 'Date', 'Error', 'Function', 'JSON', 'Map', 'Math', 'Number',
        'Object', 'Promise', 'RegExp', 'Set', 'String', 'Symbol', 'WeakMap', 'WeakSet', 'window', 'document',

        # Common methods
        'push', 'pop', 'shift', 'unshift', 'map', 'filter', 'reduce', 'forEach', 'slice', 'splice',
        'includes', 'indexOf', 'find', 'findIndex', 'join', 'split', 'trim', 'toUpperCase', 'toLowerCase',
        'parseInt', 'parseFloat', 'toString', 'charAt', 'charCodeAt',

        # Common operators
        '=', '==', '===', '!=', '!==', '<', '<=', '>', '>=', '+', '-', '*', '/', '%',
        '&&', '||', '!', '??', '?.', '=>', '...', 'as', 'is', 'instanceof', 'typeof', 'in',

        # Brackets and punctuation
        '(', ')', '[', ']', '{', '}', ';', ':', ',', '.', '`', "'", '"',

        # Common variable names
        'i', 'j', 'k', 'x', 'y', 'z', 'key', 'value', 'item', 'data', 'result', 'error',
        'user', 'input', 'output', 'name', 'type', 'id', 'count', 'flag', 'status', 'index',
        'config', 'settings', 'props', 'state', 'message', 'response', 'request', 'url', 'event',

        # Common class names
        'App', 'Service', 'Component', 'Controller', 'Model', 'View', 'Router', 'Handler',
        'Client', 'Server', 'Logger', 'Database', 'Api', 'Manager', 'Config', 'Session',

        # Common constant names
        'DEFAULT_TIMEOUT', 'MAX_RETRIES', 'API_URL', 'STATUS_OK', 'STATUS_ERROR',
        'AUTH_TOKEN', 'USER_ROLE', 'APP_VERSION', 'ENVIRONMENT', 'HTTP_PORT',

        # camelCase method/var names
        'getData', 'setData', 'loadData', 'fetchData', 'handleError', 'onInit',
        'ngOnInit', 'renderView', 'updateState', 'sendRequest', 'parseJson', 'toJson',
        'saveChanges', 'clearCache', 'addItem', 'removeItem', 'getUserInput',
        'resetForm', 'validateForm', 'createUser', 'deleteUser', 'toggleFlag',

        # CLI commands
        'tsc', 'ts-node', 'npm install', 'npm run', 'npm test', 'npx', 'node', 'tslint', 'eslint', 'prettier',

        # A few easy level 0/1 typing words
        'ask', 'lag', 'flag', 'task', 'desk', 'gas', 'sad', 'fast', 'glass', 'data',

        # Common words
        "Add", "AddRange", "Aggregate", "All", "Any", "Append", "AsEnumerable", "AsParallel", "AsQueryable", "Average",
        "BaseClass", "BeginInvoke", "BinarySearch", "Build", "BuildConfiguration", "BuildManager", "BuildResult", "BuildTask", "BuildTarget",
        "Calculate", "Call", "CanExecute", "Cancel", "CancelEventArgs", "Catch", "Change", "ChangeEventArgs", "Check", "CheckedChanged",
        "Class", "Clear", "Clone", "Close", "Code", "CodeAnalysis", "CodeDom", "CodeGenerator", "CodeProvider", "CodeSnippet",
        "Collection", "Combine", "Compare", "CompareTo", "Compile", "Compiler", "Component", "ComponentModel", "Concat", "Configure",
        "Connection", "ConnectionString", "Console", "Contains", "Content", "Context", "Continue", "Convert", "Copy", "Count",
        "Create", "CreateInstance", "CreateObject", "CreateUser", "Current", "CurrentCulture", "CurrentThread", "Custom", "CustomAttribute", "CustomException",
        "Data", "DataAdapter", "DataColumn", "DataContext", "DataGrid", "DataMember", "DataReader", "DataRow", "DataSet", "DataSource",
        "Date", "DateTime", "Day", "Debug", "DebugLog", "Decimal", "Default", "DefaultValue", "Delegate", "Delete",
        "Deserialize", "Design", "Designer", "Dictionary", "Directory", "Dispose", "Display", "DisplayName", "Do", "DoWork",
        "Document", "Double", "Download", "Draw", "DropDown", "Duration", "Dynamic", "Edit", "Editor", "Element",
        "ElementAt", "Email", "Emit", "Enable", "Enabled", "Encode", "Encrypt", "End", "EndInvoke", "Entity",
        "Enum", "Equals", "Error", "Event", "EventArgs", "EventHandler", "Exception", "Execute", "Exists", "Exit",
        "Expand", "Expression", "Extension", "Factory", "Field", "File", "FileInfo", "FileName", "Fill", "Filter",
        "Find", "First", "FirstOrDefault", "Flag", "Float", "Flush", "Folder", "ForEach", "Format", "FormatException",
        "FormClosing", "FormLoad", "Framework", "Function", "GarbageCollector", "Generate", "Generic", "Get", "GetEnumerator", "GetHashCode",
        "GetType", "Global", "GoTo", "Group", "Guid", "Handler", "HashSet", "Header", "Help", "Helper",
        "Hide", "Hierarchy", "HttpClient", "HttpRequest", "HttpResponse", "ID", "Identity", "If", "Image", "Import",
        "In", "Include", "Index", "IndexOf", "Info", "Initialize", "Input", "Insert", "Instance", "Int",
        "Int16", "Int32", "Int64", "Integer", "Interface", "Internal", "Intersect", "Invoke", "IO", "Is",
        "IsNullOrEmpty", "IsNullOrWhiteSpace", "Item", "Join", "Json", "Key", "KeyDown", "KeyPress", "KeyUp", "KeyValuePair",
        "Label", "Lambda", "Language", "Last", "LastIndexOf", "LastOrDefault", "Launch", "Layout", "Length", "Library",
        "License", "Line", "Link", "List", "Load", "Locale", "Lock", "Log", "Logger", "Login",
        "Long", "Loop", "Main", "Manager", "Map", "Match", "Math", "Max", "Member", "Memory",
        "Menu", "Merge", "Message", "Method", "Min", "Model", "Module", "Monitor", "MouseClick", "Move",
        "Multiply", "Name", "Namespace", "Native", "Navigation", "Network", "New", "Next", "Node", "None",
        "Not", "Notification", "Notify", "Null", "Number", "Object", "Observable", "Observer", "OnClick", "OnLoad",
        "Open", "Operation", "Operator", "Option", "OrderBy", "OrderByDescending", "Output", "Override", "Package", "Page",
        "Panel", "Parameter", "Parse", "Partial", "Password", "Path", "Pause", "Perform", "Permission", "Persist",
        "Pipe", "Placeholder", "Platform", "Plugin", "Pointer", "Policy", "Pool", "Port", "Position", "Post",
        "Predicate", "Preferences", "Prepare", "Presentation", "Preserve", "Press", "Preview", "Previous", "Print", "Priority",
        "Private", "Process", "Processor", "Product", "Profile", "Program", "Progress", "Project", "Property", "Protected",
        "Provider", "Proxy", "Public", "Push", "Query", "Queue", "Raise", "Random", "Range", "Read",
        "ReadAll", "ReadLine", "ReadOnly", "ReadText", "Real", "Rebuild", "Receive", "Record", "Recover", "Rectangle",
        "Redirect", "Reference", "Refresh", "Register", "Registry", "Release", "Reload", "Remove", "Render", "Replace",
        "Report", "Request", "Require", "Reset", "Resize", "Resource", "Response", "Restart", "Restore", "Result",
        "Return", "Retry", "Retrieve", "ReturnType", "Reverse", "Review", "Role", "Rollback", "Root", "Rotate",
        "Row", "Run", "Runtime", "Save", "Scale", "Scan", "Schedule", "Schema", "Scope", "Script",
        "Scroll", "Search", "Secure", "Security", "Select", "Selection", "Send", "Serialize", "Server", "Service",
        "Session", "Set", "Settings", "Setup", "Shared", "Shell", "Shift", "Short", "Show", "Shutdown",
        "Signal", "SignIn", "SignOut", "Simple", "Single", "Size", "Skip", "Sleep", "Slice", "Socket",
        "Sort", "Source", "Space", "Span", "Split", "Sql", "Stack", "Start", "Startup", "State",
        "Static", "Status", "Stop", "Storage", "Store", "Stream", "String", "Struct", "Style", "Submit",
        "Subscribe", "Subtract", "Sum", "Summary", "Support", "Suspend", "Switch", "Sync", "System", "Table",
        "Tag", "Task", "Template", "Test", "Text", "Thread", "Throw", "Timeout", "Timer", "Title",
        "ToArray", "ToList", "Token", "Tool", "Top", "Total", "Trace", "Track", "Transaction", "Transform",
        "Translate", "Transmit", "Tree", "Trim", "Try", "Type", "TypeOf", "UI", "Uninstall", "Unit",
        "Unity", "Unload", "Unlock", "Unregister", "Update", "Upload", "Url", "User", "Username", "Util",
        "Utility", "Validate", "Value", "Variable", "Vector", "Version", "View", "Virtual", "Visibility", "Visible",
        "Void", "Wait", "Warning", "Web", "Widget", "Width", "Window", "With", "Worker", "Write",
        "WriteLine", "Xml", "Yield", "Zip",

        # Common variable names
        "userName", "userEmail", "userPassword", "userId", "userProfile",
        "accountNumber", "accountBalance", "accountStatus", "accountType", "accountHolder",
        "customerName", "customerAddress", "customerPhone", "customerEmail", "customerId",
        "orderNumber", "orderDate", "orderTotal", "orderStatus", "orderItems",
        "productName", "productPrice", "productId", "productCategory", "productStock",
        "invoiceNumber", "invoiceDate", "invoiceTotal", "invoiceStatus", "invoiceItems",
        "paymentMethod", "paymentDate", "paymentAmount", "paymentStatus", "paymentId",
        "transactionId", "transactionDate", "transactionAmount", "transactionType", "transactionStatus",
        "employeeName", "employeeId", "employeeEmail", "employeePhone", "employeeDepartment",
        "departmentName", "departmentId", "departmentHead", "departmentLocation", "departmentBudget",
        "projectName", "projectId", "projectStartDate", "projectEndDate", "projectStatus",
        "taskName", "taskId", "taskDescription", "taskStartDate", "taskEndDate",
        "fileName", "filePath", "fileSize", "fileType", "fileExtension",
        "directoryPath", "directoryName", "directorySize", "directoryFiles", "directorySubfolders",
        "configSetting", "configValue", "configKey", "configFile", "configPath",
        "logMessage", "logLevel", "logTimestamp", "logFile", "logEntry",
        "errorMessage", "errorCode", "errorDetails", "errorTimestamp", "errorStackTrace",
        "exceptionMessage", "exceptionType", "exceptionSource", "exceptionStackTrace", "exceptionInnerException",
        "responseStatus", "responseMessage", "responseCode", "responseData", "responseTime",
        "requestUrl", "requestMethod", "requestHeaders", "requestBody", "requestParams",
        "apiEndpoint", "apiKey", "apiSecret", "apiVersion", "apiResponse",
        "databaseName", "databaseUser", "databasePassword", "databaseHost", "databasePort",
        "connectionString", "connectionTimeout", "connectionStatus", "connectionId", "connectionPool",
        "queryString", "queryParameters", "queryResult", "queryExecutionTime", "queryError",
        "sessionId", "sessionUser", "sessionStartTime", "sessionEndTime", "sessionData",
        "tokenValue", "tokenExpiration", "tokenType", "tokenIssuer", "tokenAudience",
        "authUser", "authToken", "authMethod", "authStatus", "authProvider",
        "cacheKey", "cacheValue", "cacheExpiration", "cacheSize", "cacheStatus",
        "threadId", "threadName", "threadStatus", "threadPriority", "threadStartTime",
        "processId", "processName", "processStatus", "processStartTime", "processEndTime",
        "eventName", "eventDate", "eventLocation", "eventDescription", "eventType",
        "notificationMessage", "notificationType", "notificationDate", "notificationStatus", "notificationRecipient",
        "emailSubject", "emailBody", "emailSender", "emailRecipient", "emailTimestamp",
        "smsMessage", "smsSender", "smsRecipient", "smsTimestamp", "smsStatus",
        "phoneNumber", "phoneType", "phoneCarrier", "phoneCountryCode", "phoneExtension",
        "addressLine1", "addressLine2", "addressCity", "addressState", "addressZipCode",
        "locationLatitude", "locationLongitude", "locationName", "locationType", "locationDescription",
        "imageUrl", "imageAltText", "imageWidth", "imageHeight", "imageFormat",
        "videoUrl", "videoTitle", "videoDuration", "videoFormat", "videoResolution",
        "audioUrl", "audioTitle", "audioDuration", "audioFormat", "audioBitrate",
        "documentTitle", "documentContent", "documentAuthor", "documentDate", "documentType",
        "reportTitle", "reportContent", "reportAuthor", "reportDate", "reportStatus",
        "chartType", "chartData", "chartTitle", "chartLabels", "chartColors",
        "graphType", "graphData", "graphTitle", "graphNodes", "graphEdges",
        "mapLocation", "mapCoordinates", "mapZoomLevel", "mapType", "mapMarkers",
        "formName", "formFields", "formData", "formMethod", "formAction",
        "inputValue", "inputType", "inputName", "inputPlaceholder", "inputLabel",
        "buttonText", "buttonType", "buttonAction", "buttonIcon", "buttonStyle",
        "labelText", "labelFor", "labelClass", "labelId", "labelStyle",
        "tableName", "tableColumns", "tableRows", "tableData", "tableHeaders",
        "columnName", "columnType", "columnLength", "columnDefault", "columnNullable",
        "rowId", "rowData", "rowIndex", "rowStatus", "rowTimestamp",
        "cellValue", "cellType", "cellFormat", "cellStyle", "cellAlignment",
        "headerText", "headerLevel", "headerStyle", "headerId", "headerClass",
        "footerText", "footerStyle", "footerId", "footerClass", "footerLinks",
        "navMenu", "navItems", "navLinks", "navStyle", "navPosition",
        "sidebarMenu", "sidebarItems", "sidebarLinks", "sidebarStyle", "sidebarPosition",
        "breadcrumbItems", "breadcrumbLinks", "breadcrumbSeparator", "breadcrumbStyle", "breadcrumbPosition",
        "paginationCurrentPage", "paginationTotalPages", "paginationPageSize", "paginationTotalItems", "paginationLinks",
        "sliderImages", "sliderInterval", "sliderTransition", "sliderControls", "sliderIndicators",
        "carouselItems", "carouselInterval", "carouselTransition", "carouselControls", "carouselIndicators",
        "modalTitle", "modalContent", "modalFooter", "modalSize", "modalBackdrop",
        "tooltipText", "tooltipPosition", "tooltipTrigger", "tooltipDelay", "tooltipStyle",
        "popoverTitle", "popoverContent", "popoverPlacement", "popoverTrigger", "popoverStyle",
        "alertMessage", "alertType", "alertDismissible", "alertDuration", "alertIcon",
        "badgeText", "badgeType", "badgePosition", "badgeStyle", "badgeIcon",
        "progressValue", "progressMax", "progressMin", "progressBarColor", "progressLabel",
        "spinnerType", "spinnerSize", "spinnerColor", "spinnerSpeed", "spinnerStyle",
        "tabName", "tabContent", "tabActive", "tabDisabled", "tabIndex",
        "accordionItems", "accordionActiveItem", "accordionCollapse", "accordionExpand", "accordionStyle",
        "dropdownItems", "dropdownSelectedItem", "dropdownToggle", "dropdownMenu", "dropdownStyle",
        "listItems", "listType", "listStyle", "listClass", "listId",
        "gridColumns", "gridRows", "gridGap", "gridTemplate", "gridArea",
        "flexDirection", "flexWrap", "flexGrow", "flexShrink", "flexBasis",
        "animationName", "animationDuration", "animationTimingFunction", "animationDelay", "animationIterationCount",
        "transitionProperty", "transitionDuration", "transitionTimingFunction", "transitionDelay", "transitionEffect",
        "keyframeName", "keyframeFrom", "keyframeTo", "keyframePercentage", "keyframeStyle",
        "mediaQuery", "mediaType", "mediaCondition", "mediaFeature", "mediaValue",
        "themeName", "themeColor", "themeFont", "themeLayout", "themeStyle",
        "layoutType", "layoutWidth", "layoutHeight", "layoutMargin", "layoutPadding",
        "spacingUnit", "spacingScale", "spacingDirection", "spacingValue", "spacingStyle",
        "colorPrimary", "colorSecondary", "colorAccent", "colorBackground", "colorText",
        "fontFamily", "fontSize", "fontWeight", "fontStyle", "fontLineHeight",
        "borderWidth", "borderStyle", "borderColor", "borderRadius", "borderCollapse",
        "shadowOffsetX", "shadowOffsetY", "shadowBlur", "shadowColor", "shadowInset",
        "zIndex", "opacityLevel", "visibilityState", "displayType", "positionType",
        "topPosition", "rightPosition", "bottomPosition", "leftPosition", "positionOffset",
        "overflowX", "overflowY", "overflowBehavior", "overflowWrap", "overflowClip",
        "cursorType", "cursorStyle", "cursorHover", "cursorActive", "cursorDisabled",
        "pointerEvents", "userSelect", "touchAction", "scrollBehavior", "scrollSnapType",
        "transformScale", "transformRotate", "transformTranslateX", "transformTranslateY", "transformSkew",
        "filterBlur", "filterBrightness", "filterContrast", "filterGrayscale", "filterSepia",
        "backdropFilter", "mixBlendMode", "backgroundBlendMode", "isVisible", "isEnabled",
        "hasError", "isLoading", "isActive", "isSelected", "isFocused",
    ]
