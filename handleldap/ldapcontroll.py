import ldap
import ldap.modlist as modlist

class OperateLdap():
    def __init__(self,ldapserver,username,pwd):
        self.succeed=True
        self.ldapserver=ldapserver
        if username=="admin":
            self.username='cn=admin,dc=wm,dc=org'
        else:
            self.username='uid='+username+',ou=people,dc=wm,dc=org'
        self.password=pwd
        try:
            self.conn=ldap.open(self.ldapserver)
            self.conn.simple_bind_s(self.username,self.password)
        except ldap.LDAPError,e:
            self.succeed=False
            print e

    def ModifyPwd(self,user,newpwd):
        dn='uid='+user+',ou=people,dc=wm,dc=org'

        '''the first way to modify pwd'''
       # oldpwd={'userPassword':self.password}
       # newpwd={'userPassword':newpwd}
       # ldif=modlist.modifyModlist(oldpwd,newpwd)
       #conn.modify_s('uid=ouyangshan,ou=people,dc=wm,dc=org',ldif)

        '''the second way to modify pwd'''
        self.conn.passwd_s(dn,None,newpwd)
    def FindUser(self,fuser):
        uid=fuser
        baseDN='ou=people,dc=wm,dc=org'
        searchScope=ldap.SCOPE_SUBTREE
        results=self.conn.search_s(baseDN,searchScope,"(uid=*)")
        for dn,entry in results:
            if uid in entry['uid']:
                return True
            else:
                continue
        return False



if __name__=='__main__':
    o=OperateLdap('server3.wm.org','123456')
