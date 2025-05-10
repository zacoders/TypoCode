from generators.generator_abc import GeneratorABC
from generators.keyboard_lang import KeyboardLanguage


class SqlGenerator(GeneratorABC):

    @property
    def display_name(self): return "SQL"

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

        # aliases
        't', 'c', 'target', 'source', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',

        # common sql functions
        'count', 'sum', 'avg', 'min', 'max', 'now', 'getdate', 'datediff', 'dateadd',
        'cast', 'convert', 'length', 'substring', 'upper', 'lower', 'round',

        # data types
        'int', 'integer', 'bigint', 'smallint', 'tinyint', 'decimal', 'numeric', 'float', 'real',
        'char', 'varchar', 'text', 'nchar', 'nvarchar', 'ntext', 'date', 'datetime', 'time', 'bit', 'boolean',

        # ddl statements
        'create table', 'drop table', 'alter table', 'add column', 'drop column', 'rename column', 'constraint'
        'create index', 'drop index', 'primary key', 'foreign key', 'references', 'unique', 'check', 'default',

        # dcl & tcl
        'grant', 'revoke', 'commit', 'rollback', 'savepoint', 'transaction',

        # symbols
        '@', '*', '=', '!=', '<>', '<', '>', '<=', '>=', '+', '-', '/', '%', '(', ')', ',', '.', ';',

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
    ]
