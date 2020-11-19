import ldap  

conn = ldap.initialize("ldap://corporate.caresoftglobal.com")
conn.set_option(ldap.OPT_REFERRALS, 0)
conn.simple_bind_s('350284', 'Caresoft@1997')
conn.search_st('DC=corporate,DC=caresoftglobal,DC=com', ldap.SCOPE_SUBTREE,"(uid=%(350284)s)")

 
