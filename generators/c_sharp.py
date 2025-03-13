from generators.base import BaseGenerator
from generators.keyboard_lang import KeyboardLanguage


class CSharpGenerator(BaseGenerator):

    keyboard_lang = KeyboardLanguage.ENGLISH

    _words = [
        # Keywords
        "abstract", "as", "base", "bool", "break", "byte", "case", "catch", "char", "checked",
        "class", "const", "continue", "decimal", "default", "delegate", "do", "double", "else", "enum",
        "event", "explicit", "extern", "false", "finally", "fixed", "float", "for", "foreach", "goto",
        "if", "implicit", "in", "int", "interface", "internal", "is", "lock", "long", "namespace",
        "new", "null", "object", "operator", "out", "override", "params", "private", "protected", "public",
        "readonly", "ref", "return", "sbyte", "sealed", "short", "sizeof", "stackalloc", "static", "string",
        "struct", "switch", "this", "throw", "true", "try", "typeof", "uint", "ulong", "unchecked", "unsafe",
        "ushort", "using", "virtual", "void", "volatile", "while", "async", "await", "record", "init",

        # Special Identifiers
        "this", "base", "nameof", "typeof", "default", "var", "dynamic", "async", "await",

        # Common Built-in Methods
        "Console.WriteLine", "Console.ReadLine", "Console.Write", "Math.Abs", "Math.Max", "Math.Min", "Math.Pow", "Math.Sqrt",
        "string.Concat", "string.Join", "string.Format", "string.Split", "string.Replace", "string.ToUpper", "string.ToLower",
        "int.Parse", "double.Parse", "float.Parse", "bool.Parse", "DateTime.Now", "DateTime.Today", "DateTime.UtcNow",
        "List<T>", "Dictionary<T, T>", "HashSet<T>", "Queue<T>", "Stack<T>", "Enumerable.Range", "Enumerable.ToList",

        # Common Dunder (Magic) Methods
        "public override string ToString()", "public override bool Equals(object obj)", "public override int GetHashCode()",
        "public static bool operator ==", "public static bool operator !=", "public static implicit operator",
        "public static explicit operator",

        # Common Standard Library Modules
        "System", "System.IO", "System.Text", "System.Collections.Generic", "System.Linq", "System.Threading", "System.Threading.Tasks",
        "System.Diagnostics", "System.Reflection", "System.Globalization", "System.Net", "System.Net.Http", "System.Xml", "System.Xml.Linq",
        "System.Data", "System.Security.Cryptography", "System.Text.RegularExpressions",

        # Symbols and Operators
        "+", "-", "*", "/", "%", "++", "--", "==", "!=", "<", ">", "<=", ">=",
        "=", "+=", "-=", "*=", "/=", "%=", "&&", "||", "!", "^", "~", "<<", ">>",
        "=>", "??", "??=", "?.", "?.[]", "_",

        # Delimiters
        "(", ")", "[]", "{}", ":", ";", ",", ".", "@", "\"", "'", "$\"...\"",

        # Other
        "while (true)", "int number", "string text", "using System", "namespace Example", "class Program", "static void Main()",

        # Common variable names
        "i", "j", "k", "x", "y", "z", "name", "age", "count", "result", "data", "item", "value", "index",
        "temp", "exception", "ex", "args", "input", "output", "filename", "path", "url", "response", "status",
        "message", "error", "config", "settings", "file", "records", "timestamp", "startTime", "endTime", "isValid",
        "buffer", "size", "key", "obj", "model", "query", "connection", "log", "environment", "local", "localhost",

        # Common class names
        "App", "Base", "Config", "Controller", "Database", "Data", "Entity", "Error", "Exception", "Factory",
        "Handler", "Helper", "Job", "Logger", "Manager", "Mapper", "Model", "Node", "Parser", "Processor",
        "Queue", "Reader", "Registry", "Request", "Response", "Router", "Scheduler", "Serializer", "Service",
        "Session", "Settings", "Singleton", "State", "Strategy", "Task", "Thread", "Tracker", "Transformer",
        "Unit", "User", "Validator", "View", "Worker", "Writer", "Adapter", "Builder", "Command", "Component",
        "Observer",

        # Common constant names
        "PI", "E", "MAX_INT", "MIN_INT", "NULL", "TRUE", "FALSE", "DEFAULT", "SUCCESS", "FAILURE", "ERROR", "TIMEOUT",
        "CACHE_TIMEOUT", "BUFFER_SIZE", "MAX_LENGTH", "MIN_LENGTH", "MAX_SIZE", "MIN_SIZE", "API_KEY", "AUTH_TOKEN",
        "DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD", "LOG_LEVEL", "LOG_FILE", "CACHE_LIMIT",
        "SESSION_TIMEOUT", "MAX_CONNECTIONS", "RETRY_INTERVAL", "PAGE_SIZE", "TIME_FORMAT", "DATE_FORMAT",

        # Command line
        "dotnet", "dotnet build", "dotnet run", "dotnet publish", "dotnet restore", "dotnet new", "dotnet test",
        "csc", "msbuild", "nuget", "dotnet pack", "dotnet add package", "dotnet remove package", "dotnet list package"
    ]
