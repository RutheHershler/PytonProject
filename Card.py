import datetime
import logging
logging.basicConfig(filename='card_logging.log', level=logging.INFO)

logger = logging.getLogger("enter_card_logging")

now = datetime.datetime.now()

class card:

    COINS_VALUES={
        "quarters": 0.25,
        "dimes": 0.10,
        "half": 0.5,
        "shekels": 1.0
    }

    def __init__(self):

        """עודף"""
        self.surplus_get = 0
        """כסף שהתקבל"""
        self.money_received = 0
        self.cost=20
        self.date = now.strftime("%Y-%m-%d")
        self.time = now.strftime(" %H:%M:%S")
        logger.info(f"surplus get {self.surplus_get} \n"
                    f", money received {self.money_received} \n"
                    f", cost{self.cost} \n"
                    f"  date{ self.date}\n"
                    f"time { self.time }\n")

    def coins(self):
        """פונקצייה שמחשבת האם התקבל מספיק כסף"""
        self.money_received=self.COINS_VALUES["quarters"]*int(input("enter coins  quarters"))
        self.money_received+=self.COINS_VALUES["dimes"]*int(input("enter coins  dimes"))
        self.money_received+=self.COINS_VALUES["half"]*int(input("enter coins  half"))
        self.money_received+=self.COINS_VALUES["shekels"]*int(input("enter coins  shekels"))
        print(self.money_received)
        print("cost card" ,self.cost)
        self.check(self.money_received)
        logger.info(f"surplus get {self.surplus_get} \n"
                    f", money received {self.money_received} \n"
                    f", cost{self.cost} \n")


    def check(self,price):
        if self.cost==price:
            return self.money_received
        elif self.cost<price:
            self.surplus(price)
        else:
            print("you have less ",self.cost-price)
        logger.info(f"check price "
                    f"date{ self.date}\n"
                    f"time { self.time }\n")

    def surplus(self,price):
        """מחזירה את הסכום לעודף"""
        self.surplus_get=price-self.cost
        print(self.surplus_get)
        # if self.coins()==True and self.money_received>price:
        return self.surplus_get

    def print_card(self,name):
        """פונקציה המדפיסה כרטיס"""

        date = now.strftime("%Y-%m-%d")
        time = now.strftime(" %H:%M:%S")
        newcard=open(f"../cards/cardof{name}.txt" ,"w")
        lesspay=self.cost-self.money_received

        print("====")
        if self.surplus_get==0 and self.money_received<20:
            newcard.write(f"האיחור של: שם{name} שעה:\n {time} תאריך :\n {date}  \n מחיר :{self.cost}\n סכום שהתקבל:{self.money_received}\n חסר:{lesspay} ")
        else :
            newcard.write(f"האיחור של: שם{name} שעה:\n {time} תאריך :\n {date}  \n מחיר :{self.cost}\n סכום שהתקבל:{self.money_received}\n עודף ללקוח:{self.surplus_get} ")
            logger.info(f"האיחור של: שם{name} שעה:\n {time} תאריך :\n {date}  \n מחיר :{self.cost}\n סכום שהתקבל:{self.money_received}\n עודף ללקוח:{self.surplus_get} ")

