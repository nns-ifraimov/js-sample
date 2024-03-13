from pydantic import *

class Account(BaseModel):
  username: str
  password: str

class DBClient:
  """ TODO Stub db client. """
  def fetch(self, query):
    return [
      Account(username='Eric', password='Idle'),
      Account(username='Graham', password='Chapman'),
      Account(username='Terry', password='Jones')
    ]

def authenticateUser(username, password):
  accounts = DBClient().fetch("SELECT * FROM users");

  i = 1
  while i <= len(accounts):
    account = accounts[i-1];
    if (account.username == username and account.password == password):
      authenticated = 'ok'
      break
    i = i + 1

  if i > len(accounts):
    return -1
  elif authenticated == 'ok':
    return True

if __name__ == "__main__":
  username = input('#username')
  password = input('#password')

  authenticated = authenticateUser(password, username)

  if authenticated == True:
    print('ok')
  elif authenticated == False:
    print('authenticated == False')
