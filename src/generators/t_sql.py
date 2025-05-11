from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class TransactSqlGenerator(GeneratorABC):

    @property
    def display_name(self): return "Transact-SQL"

    keyboard_lang = KeyboardLanguage.ENGLISH

    _level_symbols = [
        set('asdfghjkl '),  # level 0
        set('asdfghjkl qwertyuiop'),  # level 1
        set('asdfghjkl qwertyuiop zxcvbnm'),  # level 2
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM .,*'),  # level 3
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 .,*()'),  # level 4
        set('asdfghjkl qwertyuiop zxcvbnm ASDFGHJKL QWERTYUIOP ZXCVBNM 1234567890 `~!@#$%^&*()-=+[]{}\\|;:",<.>/?_' + "'")  # level 5
    ]

    _words = [
        # SQL Keywords
        'select', 'from', 'where', 'insert', 'into', 'values', 'update', 'set', 'delete', 'join', 'merge', 'using'
        'inner join', 'left join', 'right join', 'full join', 'on', 'group by', 'order by', 'having',
        'as', 'distinct', 'limit', 'offset', 'union', 'all', 'exists', 'not exists', 'in', 'not in',
        'null', 'is null', 'is not null', 'between', 'like', 'and', 'or', 'not', 'case', 'when', 'then', 'else', 'end',

        "add", "external", 'proc', "procedure", "all", "fetch", "public", "alter", "file",
        "raiserror", 'error', '@@error', "and", "fillfactor", "read", "any", "for", "readtext",
        "foreign", "reconfigure", "asc", "freetext", "references", "authorization",
        "freetexttable", "replication", "backup", "from", "restore", "begin", "full",
        "restrict", "between", "function", "return", "break", "goto", "revert",
        "browse", "grant", "revoke", "bulk", "group", "right", "by", "having", "rollback",
        "cascade", "holdlock", "@@rowcount", "case", "identity", "rowguidcol", "check",
        "identity_insert", "rule", "checkpoint", "identitycol", "save", "close", "if",
        "schema", "clustered", "in", "securityaudit", "coalesce", "index", "select",
        "collate", "inner", "column", "insert", '@@identity', '@@trancount', 'isnull',
        "commit", "intersect", 'ToString()', 'string_split',
        "compute", "into", "session_user", "constraint", "is", "set", "contains",
        "join", "setuser", "containstable", "key", "shutdown", "continue", "kill",
        "some", "convert", "left", "statistics", "create", "like", "system_user",
        "cross apply", "lineno", "table", "current", "load", "tablesample", "current_date",
        "merge", "textsize", "current_time", "national", "then", "current_timestamp",
        "nocheck", "to", "current_user", "nonclustered", "top", "cursor", "not",
        "tran", "database", "null", "transaction", "dbcc", "nullif", "trigger", "deallocate",
        "of", "truncate", "declare", "off", "try_convert", "default", "offsets", "tsequal",
        "delete", "on", "union", "deny", "open", "unique", "desc", "opendatasource",
        "unpivot", "disk", "openquery", "update", "distinct", "openrowset", "updatetext",
        "distributed", "openxml", "use", "double", "option", "user", "drop", "or",
        "values", "dump", "order", "varying", "else", "outer apply", "view", "over",
        "waitfor", "errlvl", "percent", "when", "escape", "pivot", "where", "except",
        "plan", "while", "exec", "precision", "with", "execute", "primary", "within group",
        "exists", "print", "writetext", 'union all', 'cast', 'try_cast', 'dbo',

        # aliases
        't', 'c', 'target', 'source', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',

        # common sql functions
        'count', 'sum', 'avg', 'min', 'max', 'now', 'getdate', 'datediff', 'dateadd',
        'cast', 'convert', 'length', 'substring', 'upper', 'lower', 'round',

        # data types
        'int', 'integer', 'bigint', 'smallint', 'tinyint', 'decimal', 'numeric', 'float', 'real', 'xml',
        'char', 'varchar', 'text', 'nchar', 'nvarchar', 'ntext', 'date', 'datetime', 'time', 'bit', 'boolean',
        'datetime2',

        # ddl statements
        'create table', 'drop table', 'alter table', 'add column', 'drop column', 'rename column', 'constraint',
        'create index', 'drop index', 'primary key', 'foreign key', 'references', 'unique', 'check', 'default',
        'create user', 'create login', 'external provider',

        # dcl & tcl
        'grant', 'revoke', 'commit', 'rollback', 'savepoint', 'transaction',

        # symbols
        '@', '*', '=', '!=', '<>', '<', '>', '<=', '>=', '+', '-', '/', '%', '(', ')', ',', '.', ';',

        # table hints
        'nolock', 'holdlock', 'updlock', 'xlock', 'tablock', 'tablockx', 'paglock', 'rowlock', 'readcommitted', 'readcommittedlock', 'readpast', 'readuncommitted', 'repeatableread', 'serializable', 'snapshot', 'forcescan', 'forceseek', 'index(...)', 'fastfirstrow', 'keepidentity', 'keepdefaults', 'ignore_constraints', 'ignore_triggers', 'check_constraints', 'optimize for unknown',

        # index options (used with create/alter index ... with (...))
        'pad_index', 'fillfactor', 'ignore_dup_key', 'statistics_norecompute', 'statistics_incremental', 'allow_row_locks', 'allow_page_locks', 'sort_in_tempdb', 'drop_existing', 'online', 'data_compression', 'maxdop', 'resumable', 'wait_at_low_priority', 'optimize_for_sequential_key', 'xml_compression',

        # query options
        'hash join', 'merge join', 'loop join', 'force order', 'robust plan', 'keep plan', 'keepfixed plan', 'expand views', 'fast n', 'maxdop n', 'optimize for (...)', 'optimize for unknown', 'recompile', 'use plan', 'querytraceon n', 'parameterization simple', 'parameterization forced',

        # common table names
        "Users", "Customers", "Clients", "Employees", "Managers", "Admins", "Roles",
        "Permissions", "Groups", "Teams", "Members", "Departments", "Locations", "Branches",
        "Products", "ProductCategories", "Inventory", "Stock", "Suppliers", "Vendors",
        "Purchases", "PurchaseOrders", "Orders", "OrderItems", "Shipments", "Deliveries",
        "Carts", "CartItems", "Wishlists", "Returns", "Refunds", "Invoices", "Payments",
        "Transactions", "Accounts", "BankAccounts", "Billing", "Subscriptions", "Plans",
        "Services", "Features", "Licenses", "Contracts", "Projects", "ProjectTasks",
        "Tasks", "TaskAssignments", "Milestones", "Tickets", "Issues", "Bugs", "Sprints",
        "Meetings", "Events", "Notifications", "Messages", "Chats", "Comments", "Posts",
        "Blogs", "Articles", "Pages", "Files", "Documents", "Media", "Attachments",
        "AuditLogs", "LoginLogs", "ActivityLogs", "Analytics", "Stats", "Reports",
        "Settings", "Configurations", "Preferences", "Themes", "Languages", "Translations",
        "Categories", "Tags", "Labels", "Ratings", "Reviews", "Feedback", "Surveys",
        "Responses", "Forms", "Fields", "Answers", "Questions", "Campaigns", "Ads",
        "Affiliates", "Referrals", "Coupons", "Discounts", "Taxes", "Zones", "Countries",
        "Regions", "States", "Cities", "Addresses", "GeoLocations", "IpAddresses",
        "Devices", "Browsers", "Sessions", "Tokens", "ApiKeys", "Webhooks", "Integrations",
        "Uploads", "Downloads", "Imports", "Exports", "Queues", "Jobs", "Schedules",
        "CronJobs", "Backups", "Restores", "Migrations", "Versions",

        # common column names
        'order_total', 'product_name', 'created_date', 'last_updated', 'is_active', 'customer_address',
        "id", "uuid", "slug", "reference_id", "external_id", "user_id", "customer_id",
        "client_id", "employee_id", "manager_id", "admin_id", "order_id", "product_id",
        "invoice_id", "payment_id", "transaction_id", "project_id", "task_id", "parent_id",
        "category_id", "tag_id", "role_id", "permission_id", "group_id", "team_id",
        "location_id", "address_id", "comment_id", "message_id", "file_id", "page_id",
        "post_id", "media_id", "coupon_id", "discount_id", "plan_id", "subscription_id",
        "question_id", "answer_id", "rating_id", "review_id", "status", "type", "priority",
        "title", "name", "first_name", "last_name", "full_name", "username", "email",
        "phone", "mobile", "dob", "gender", "company", "department", "position", "bio",
        "about", "avatar", "photo", "thumbnail", "url", "website", "domain", "ip_address",
        "device", "browser", "language", "timezone", "country", "state", "region", "city",
        "zipcode", "address", "street", "latitude", "longitude", "amount", "price", "cost",
        "subtotal", "total", "balance", "credit", "debit", "tax", "fee", "rate", "quantity",
        "stock", "availability", "score", "level", "rank", "points", "votes", "likes",
        "dislikes", "comment", "message", "note", "feedback", "summary", "description",
        "content", "details", "tags", "keywords", "meta_title", "meta_description",
        "created_at", "updated_at", "deleted_at", "started_at", "ended_at", "submitted_at",
        "confirmed_at", "cancelled_at", "completed_at", "expires_at", "due_date", "birth_date",
        "password", "password_hash", "reset_token", "confirmation_token", "token",
        "session_id", "api_key", "secret", "key", "enabled", "active", "verified", "approved",
        "archived", "locked", "failed_attempts", "last_login", "login_count", "version",
        "revision", "checksum", "hash", "notes", "options", "settings", "config", 'category',

        # system views
        'sys.tables', 'sys.columns', 'sys.objects', 'sys.schemas', 'sys.types', 'sys.indexes',
        'sys.index_columns', 'sys.foreign_keys', 'sys.foreign_key_columns', 'sys.key_constraints',
        'sys.check_constraints', 'sys.default_constraints', 'sys.computed_columns', 'sys.views',
        'sys.procedures', 'sys.parameters', 'sys.sql_modules', 'sys.triggers', 'sys.identity_columns',
        'sys.all_objects', 'sys.all_columns', 'sys.database_principals', 'sys.server_principals',
        'sys.database_permissions', 'sys.schemas', 'sys.synonyms', 'sys.tablesample_clause',
        'sys.sequences', 'sys.stats', 'sys.stats_columns', 'sys.partition_schemes',
        'sys.partition_functions', 'sys.partitions', 'sys.filegroups', 'sys.database_files',
        'sys.dm_db_index_usage_stats', 'sys.dm_db_partition_stats', 'sys.dm_db_index_physical_stats',
        'sys.dm_exec_requests', 'sys.dm_exec_sessions', 'sys.dm_exec_connections',
        'sys.dm_exec_query_stats', 'sys.dm_exec_sql_text', 'sys.dm_exec_query_plan',

    ]
