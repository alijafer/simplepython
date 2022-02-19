from dataclasses import dataclass
from datetime import datetime
import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
regex1 = '[^<script>]'  
def check(email):   
    return bool(re.search(regex,email))
"""    if(re.search(regex,email)):   
        pass   
    else:   
        print("inv") """
    
def check_body(body):
    return bool(re.search(regex1, body))

@dataclass(frozen=True, order=True)
class Abc:
    id: int
    name: str
    isActive: bool
    createTime: datetime

class Email:
    def send(efrom:str, to:str, body:str):
        if check(efrom) is True:
            if check(to) == True:
                if check_body(body) == True:

                    return print("done")
                else:
                    print("body uncorrect")
            else:
                return print("to not riht")
        else:
            return print("from not riht")
def main():
    """ abc = Abc(1, "ali", True, datetime.now())
    abc1 = Abc(2, "ali", True, datetime.now())
    print(abc)
    print()
    print(hash(abc.name))
    print(abc==abc1) """
    Email.send(efrom="ali@ali.com", to="ali@a.sa", body="dfrdfg")
if __name__ == "__main__":
    main()