from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class JavaScriptGenerator(GeneratorABC):

    @property
    def display_name(self): return "JavaScript"

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
        "abstract", "arguments", "await", "boolean", "break", "byte", "case", "catch", "char", "class",
        "const", "continue", "debugger", "default", "delete", "do", "double", "else", "enum", "eval",
        "export", "extends", "false", "final", "finally", "float", "for", "function", "goto", "if",
        "implements", "import", "in", "instanceof", "int", "interface", "let", "long", "native", "new",
        "null", "package", "private", "protected", "public", "return", "short", "static", "super", "switch",
        "synchronized", "this", "throw", "throws", "transient", "true", "try", "typeof", "var", "void",
        "volatile", "while", "with", "yield", "async", "from", "of",

        # Special Identifiers
        "this", "super", "arguments", "typeof", "instanceof", "new", "delete", "void", "async", "await",

        # Common Built-in Methods
        "console.log", "console.error", "console.warn", "console.info", "Math.abs", "Math.max", "Math.min", "Math.pow", "Math.sqrt",
        "String.prototype.concat", "String.prototype.slice", "String.prototype.split", "String.prototype.replace", "String.prototype.toUpperCase", "String.prototype.toLowerCase",
        "parseInt", "parseFloat", "Number.parseInt", "Number.parseFloat", "Date.now", "Date.parse", "JSON.stringify", "JSON.parse",
        "Array", "Object", "Map", "Set", "WeakMap", "WeakSet", "Promise", "RegExp",

        # Common Dunder (Magic) Methods
        "toString", "valueOf", "hasOwnProperty", "isPrototypeOf", "propertyIsEnumerable",
        "constructor", "prototype", "__proto__", "call", "apply", "bind",

        # Common Standard Library Modules
        "fs", "path", "http", "https", "url", "querystring", "crypto", "util", "events", "stream",
        "buffer", "os", "process", "child_process", "cluster", "dns", "net", "tls", "readline", "zlib",
        "express", "lodash", "axios", "moment", "jquery", "react", "vue", "angular",

        # Symbols and Operators
        "+", "-", "*", "/", "%", "++", "--", "==", "!=", "<", ">", "<=", ">=",
        "=", "+=", "-=", "*=", "/=", "%=", "&&", "||", "!", "^", "~", "<<", ">>",
        "===", "!==", "??", "?.", "...", "=>", "&", "|",

        # Delimiters
        "(", ")", "[]", "{}", ":", ";", ",", ".", "`", "\"", "'", "${...}",

        # Other
        "function() {}", "const name = ", "let value = ", "if (condition)", "for (let i = 0)", "while (true)", "try { } catch (e)",

        # Common variable names
        "name", "age", "count", "result", "data", "item", "value", "index",
        "temp", "error", "err", "args", "input", "output", "filename", "path", "url", "response", "status",
        "message", "config", "settings", "file", "records", "timestamp", "startTime", "endTime", "isValid",
        "buffer", "size", "key", "obj", "model", "query", "connection", "log", "env", "local", "localhost",

        # Common class names
        "App", "Base", "Config", "Controller", "Database", "Data", "Entity", "Error", "Exception", "Factory",
        "Handler", "Helper", "Job", "Logger", "Manager", "Mapper", "Model", "Node", "Parser", "Processor",
        "Queue", "Reader", "Registry", "Request", "Response", "Router", "Scheduler", "Serializer", "Service",
        "Session", "Settings", "Singleton", "State", "Strategy", "Task", "Thread", "Tracker", "Transformer",
        "Unit", "User", "Validator", "View", "Worker", "Writer", "Adapter", "Builder", "Command", "Component",
        "Observer",

        # Common constant names
        "PI", "MAX_INT", "MIN_INT", "NULL", "TRUE", "FALSE", "DEFAULT", "SUCCESS", "FAILURE", "ERROR", "TIMEOUT",
        "CACHE_TIMEOUT", "BUFFER_SIZE", "MAX_LENGTH", "MIN_LENGTH", "MAX_SIZE", "MIN_SIZE", "API_KEY", "AUTH_TOKEN",
        "DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD", "LOG_LEVEL", "LOG_FILE", "CACHE_LIMIT",
        "SESSION_TIMEOUT", "MAX_CONNECTIONS", "RETRY_INTERVAL", "PAGE_SIZE", "TIME_FORMAT", "DATE_FORMAT",

        # Command line
        "node", "npm", "npm install", "npm run", "npm start", "npm test", "npm build", "npx",
        "yarn", "yarn install", "yarn start", "yarn build", "yarn test", "webpack", "babel", "eslint",

        # A few words for the first typing level.
        "ask", "add", "lag", "sad", "glad", "had", "all", "fall", "hall", "glass", "flag", "flash",
        "dash", "gala", "saga", "alfa", "half", "gas", "has", "ash", "shall", "gag", "jag",
        "flask", "slash", "hash", "lash", "fad", "gals", "jags", "shag", "a", "s", "d", "f", "g", "h", "j", "k", "l",

        # Common words
        "addEventListener", "appendChild", "setAttribute", "getAttribute", "getElementById", "getElementsByClassName", "querySelector", "querySelectorAll",
        "createElement", "createTextNode", "removeChild", "replaceChild", "insertBefore", "cloneNode", "hasChildNodes", "contains",
        "setTimeout", "setInterval", "clearTimeout", "clearInterval", "requestAnimationFrame", "cancelAnimationFrame",
        "fetch", "XMLHttpRequest", "Promise", "async", "await", "then", "catch", "finally", "resolve", "reject",
        "forEach", "map", "filter", "reduce", "find", "findIndex", "some", "every", "includes", "indexOf",
        "push", "pop", "shift", "unshift", "splice", "slice", "concat", "join", "reverse", "sort",
        "length", "split", "replace", "substring", "substr", "charAt", "charCodeAt", "toUpperCase", "toLowerCase",
        "trim", "padStart", "padEnd", "startsWith", "endsWith", "match", "search", "test", "exec",
        "parseInt", "parseFloat", "isNaN", "isFinite", "Number", "String", "Boolean", "Array", "Object",
        "Math", "Date", "RegExp", "JSON", "Error", "TypeError", "ReferenceError", "SyntaxError",
        "undefined", "null", "true", "false", "Infinity", "NaN", "globalThis", "window", "document",
        "console", "localStorage", "sessionStorage", "navigator", "location", "history", "screen",
        "onclick", "onload", "onchange", "onsubmit", "onmouseover", "onmouseout", "onkeydown", "onkeyup",
        "className", "classList", "innerHTML", "innerText", "textContent", "value", "checked", "disabled",
        "style", "display", "visibility", "opacity", "position", "top", "left", "width", "height",
        "margin", "padding", "border", "background", "color", "fontSize", "fontFamily", "fontWeight",
        "flexbox", "grid", "float", "clear", "overflow", "zIndex", "transform", "transition", "animation",
        "addEventListener", "removeEventListener", "preventDefault", "stopPropagation", "target", "currentTarget",
        "event", "type", "bubbles", "cancelable", "defaultPrevented", "eventPhase", "timeStamp",
        "clientX", "clientY", "pageX", "pageY", "screenX", "screenY", "button", "buttons", "which",
        "keyCode", "charCode", "altKey", "ctrlKey", "shiftKey", "metaKey", "key", "code",
        "load", "unload", "resize", "scroll", "focus", "blur", "select", "change", "input", "submit",
        "click", "dblclick", "mousedown", "mouseup", "mousemove", "mouseover", "mouseout", "mouseenter", "mouseleave",
        "keydown", "keyup", "keypress", "touchstart", "touchend", "touchmove", "touchcancel",
        "dragstart", "dragend", "dragover", "dragenter", "dragleave", "drop", "wheel",

        # Common variable names
        "element", "elements", "node", "nodes", "parent", "child", "children", "sibling", "siblings",
        "form", "forms", "input", "inputs", "button", "buttons", "link", "links", "image", "images",
        "table", "tables", "row", "rows", "cell", "cells", "header", "headers", "footer", "footers",
        "nav", "navigation", "menu", "menus", "item", "items", "list", "lists", "container", "containers",
        "wrapper", "wrappers", "content", "contents", "text", "texts", "title", "titles", "label", "labels",
        "field", "fields", "option", "options", "select", "selects", "textarea", "textareas",
        "checkbox", "checkboxes", "radio", "radios", "submit", "submits", "reset", "resets",
        "username", "password", "email", "phone", "address", "city", "state", "zip", "country",
        "firstName", "lastName", "fullName", "displayName", "nickname", "avatar", "profile", "account",
        "userId", "userRole", "userType", "userStatus", "userGroup", "userPermissions", "userSettings",
        "sessionId", "sessionData", "sessionTimeout", "sessionUser", "sessionToken", "sessionExpiry",
        "apiUrl", "apiKey", "apiSecret", "apiToken", "apiVersion", "apiResponse", "apiRequest", "apiData",
        "baseUrl", "endpoint", "endpoints", "route", "routes", "path", "paths", "param", "params",
        "query", "queries", "filter", "filters", "sort", "sorting", "order", "ordering", "limit", "offset",
        "page", "pages", "pageSize", "pageNumber", "totalPages", "totalItems", "currentPage", "nextPage",
        "database", "db", "collection", "collections", "document", "documents", "record", "records",
        "schema", "schemas", "model", "models", "entity", "entities", "relation", "relations",
        "connection", "connections", "transaction", "transactions", "query", "queries", "result", "results",
        "error", "errors", "exception", "exceptions", "warning", "warnings", "info", "debug", "trace",
        "log", "logs", "logger", "loggers", "level", "levels", "message", "messages", "timestamp", "timestamps",
        "config", "configuration", "configurations", "setting", "settings", "option", "options", "preference", "preferences",
        "environment", "env", "development", "production", "staging", "test", "testing", "local", "remote",
        "server", "servers", "client", "clients", "host", "hosts", "port", "ports", "protocol", "protocols",
        "request", "requests", "response", "responses", "header", "headers", "body", "bodies", "payload", "payloads",
        "status", "statusCode", "statusText", "method", "methods", "get", "post", "put", "delete", "patch",
        "cookie", "cookies", "session", "sessions", "cache", "caches", "storage", "storages", "memory", "disk",
        "file", "files", "folder", "folders", "directory", "directories", "path", "paths", "extension", "extensions",
        "upload", "uploads", "download", "downloads", "stream", "streams", "buffer", "buffers", "chunk", "chunks",
        "process", "processes", "thread", "threads", "worker", "workers", "job", "jobs", "task", "tasks",
        "queue", "queues", "stack", "stacks", "heap", "heaps", "memory", "cpu", "performance", "benchmark",
        "timer", "timers", "interval", "intervals", "timeout", "timeouts", "delay", "delays", "schedule", "scheduler",
        "event", "events", "listener", "listeners", "handler", "handlers", "callback", "callbacks", "promise", "promises",
        "observable", "observables", "subject", "subjects", "stream", "streams", "pipe", "pipes", "operator", "operators",
        "component", "components", "module", "modules", "service", "services", "factory", "factories", "provider", "providers",
        "controller", "controllers", "view", "views", "template", "templates", "directive", "directives", "filter", "filters",
        "route", "routes", "router", "routers", "guard", "guards", "interceptor", "interceptors", "middleware", "middlewares",
        "plugin", "plugins", "extension", "extensions", "addon", "addons", "library", "libraries", "framework", "frameworks",
        "package", "packages", "dependency", "dependencies", "version", "versions", "update", "updates", "patch", "patches",
        "build", "builds", "compile", "compilation", "bundle", "bundles", "chunk", "chunks", "asset", "assets",
        "test", "tests", "spec", "specs", "suite", "suites", "case", "cases", "mock", "mocks", "stub", "stubs",
        "debug", "debugging", "breakpoint", "breakpoints", "watch", "watches", "profile", "profiles", "trace", "traces",
        "animation", "animations", "transition", "transitions", "transform", "transforms", "keyframe", "keyframes",
        "media", "responsive", "breakpoint", "mobile", "tablet", "desktop", "screen", "viewport", "resolution",
        "color", "colors", "theme", "themes", "style", "styles", "css", "sass", "scss", "less",
        "font", "fonts", "typography", "text", "size", "weight", "family", "line", "height", "spacing",
        "layout", "grid", "flex", "flexbox", "container", "row", "column", "item", "area", "gap",
        "margin", "padding", "border", "outline", "shadow", "gradient", "background", "image", "position",
        "display", "visibility", "opacity", "overflow", "clip", "mask", "filter", "blend", "mix"
    ]
