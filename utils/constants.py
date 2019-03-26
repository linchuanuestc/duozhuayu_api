#general errno
ERR_SUC     = 0
ERR_UNKNOWN = 1001

#user errno
ERR_NO_USER = 2001

#book errno
ERR_NO_BOOK = 3001

#db error
ERR_DB      = 4001

#errmsg
ERR_DESC = {
        ERR_SUC:     "",
        ERR_UNKNOWN: "unkown errors", 
        ERR_NO_USER: "not found the user", 
        ERR_NO_BOOK: "not found the books", 
        ERR_DB:      "Db Error", 
        }
