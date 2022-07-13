from abc import ABC
from enum import Enum


class Store:
    __ID:int = 0
    __single: 'Store'
    __store_lst: list['Equip']
    __logs: list['Log']

    def __new__(cls):

        if not cls.__single:
            cls.__single = super(Store, cls).__new__(cls)

        return cls.__single

    @classmethod
    def add_equip(cls, user: 'StoreUser', *equips: 'Equip') -> list['Log']:


        if not user.is_login():
            raise StoreUserError("user not login in store")

        logs_out = []
        for equip in equips:
            cls.__store_lst.append(equip)

            log = Log()
            log.oper_type = StorePriv.ADD
            log.equip_id = equip.equip_id
            logs_out.append(log)
            cls.__logs.append(log)


        return logs_out[:]

    @classmethod
    def del_equip(cls, user: 'StoreUser', *equips: 'Equip') -> list['Log']:
        return []

    @classmethod
    def req_to(cls, user: 'StoreUser', equip_filter: list['EquipFilter']) -> 'StoreReq':
        return StoreReq()

    @classmethod
    def applue_req(cls, req: 'StoreReq') -> list['Log']:
        return []

    @classmethod
    def get_logs(cls, frm=None, to=None) -> list['Log']:
        return []


class EquipFilter:
    equip_type = None
    flt_find: list

    def __init__(self, equip_type, *filts) -> None:
        self.equip_type = equip_type
        self.flt_find = list(filts)


class StorePriv(Enum):
    ADD = 0
    DEL = 1
    REQ = 2
    APP_REQ = 3
    BACK = 4
    ALL_LOG = 5
    USER_LOG = 6

    @staticmethod
    def grop(group_name: str) -> set['StorePriv']:
        if group_name == "admin":
            return set([
                StorePriv.ADD, StorePriv.DEL, StorePriv.REQ,
                StorePriv.APP_REQ, StorePriv.BACK, StorePriv.ALL_LOG])
        elif group_name == "woker":
            return set([
                StorePriv.ADD, StorePriv.DEL,
                StorePriv.APP_REQ, StorePriv.BACK, StorePriv.ALL_LOG])
        elif group_name == "company":
            return set([
                StorePriv.ADD, StorePriv.DEL,
                StorePriv.BACK, StorePriv.ALL_LOG])
        else:
            return set()


class StoreReq:
    ok: dict
    fail: dict


class StoreUser(object):
    __login_name: str
    __priv: set['StorePriv'] = set()

    __passwd: str
    __contr_protect = object()

    @classmethod
    def login(cls, login_: str = "anymous", passwd: str = ""):
        return StoreUser(cls.__contr_protect, login_, passwd)

    def login_name(self):
        return self.login_name()

    def is_login(self) -> bool:
        return self.__login_name != "" and self.__passwd != ""

    def can_do(self, priv: 'StorePriv') ->  bool:
        return priv in self.__priv

    def __init__(self, prt, login_, passwd) -> None:

        assert(prt == StoreUser.__contr_protect), "Please login user by StoreUser.login"



        image = {

            "admin": {"psw": "nimda", "grop": "admin"},
            "store_worker": {"psw": "w0R3R", "grop": "worker"},
            "company": {"psw": "coolCompany123", "grop": "company"},

        }

        if image.get(login_):
            if image[login_]["psw"] == passwd:
                self.__login_name = login_

                self.__passwd = passwd

                
                self.__priv = StorePriv.grop(image[login_]["grop"])

            else:
                raise StoreUserError("login or error incorrect")
        else:
            raise StoreUserError("login or error incorrect")


class StoreExcept(Exception):
    pass


class StoreUserError(StoreExcept):
    pass


class Log:
    equip_id: int
    oper_type: 'StorePriv'
    date_time: None
    correct: bool


class Equip(ABC):
    equip_id: int


class OfficeEquip(Equip):
    pass