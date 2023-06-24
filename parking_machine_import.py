import datetime
import math


class ParkingMachine:
    def __init__(self):
        self.license_plate = None
        self.car_in = None
        self.car_outs = None
        self.cost = None

    def add_car(self, license_plate):  # 加入車輛
        car_in = datetime.datetime.now()
        self.car_in = car_in
        self.license_plate = license_plate

    def search_car(self, license_plate):  # 查詢車輛是否存在
        if self.license_plate != None:
            return True
        else:
            return False

    def car_out(self):  # 離場
        parking_time_out = datetime.datetime.now()
        parking_time_out += datetime.timedelta(minutes=1440)
        self.car_outs = parking_time_out

    def time1(self, time):  # 可控離場時間
        car_out = self.car_in
        car_out += datetime.timedelta(minutes=time)
        self.car_outs = car_out

    def search_car_in(self):  # 查詢入場時間
        car_in = self.car_in
        formatted_time = car_in.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time.split(".")[0]  # 移除秒的小數部分

    def search_car_out(self):  # 查詢出場時間
        car_outs = self.car_outs
        formatted_time = car_outs.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time.split(".")[0]  # 移除秒的小數部分

    def seach_car_pay(self):  # 查詢價格
        if self.car_in is None or self.car_outs is None:
            print("車牌", self.license_plate, "的入場或離場時間未完整記錄")
            return 0
        day = self.car_outs.weekday() + 1
        money = self.money(day)  # 傳遞平日參數
        return money

    def money(self, day):
        minutes_parked = self.time()  # 計算停車時間
        minutes_parkeds = 0
        moneys = 0  # 宣告和初始化
        car_date = self.car_outs
        car_in_date = self.car_in.date()
        car_out_date = car_date.date()
        while minutes_parked > 0:
            if self.is_weekend(day):
                rate = 20
                max_charge = 420
            else:
                rate = 15
                max_charge = 300

            if car_in_date == car_out_date:
                minutes_parkeds = minutes_parked
                minutes_parked = 0
                print(minutes_parkeds)
                print(minutes_parked)
            else:
                if car_date.hour != 0 or car_date.minute != 0:
                    minutes_parkeds = car_date.hour * 60 + car_date.minute
                    car_date = car_date.replace(hour=0, minute=0)  # 更新 car_date
                    minutes_parked -= minutes_parkeds
                    car_out_date -= datetime.timedelta(days=1)
                    day -= 1
                    print(minutes_parkeds)
                    print(minutes_parked)
                else:
                    minutes_parkeds = 1440
                    minutes_parked -= 1440
                    car_out_date -= datetime.timedelta(days=1)
                    day -= 1
                    print(minutes_parkeds)
                    print(minutes_parked)
            if day == 0:
                day = 7
            payment = (minutes_parkeds // 30) * rate
            payment = min(payment, max_charge)
            moneys += payment
        return moneys

    def pay_money(self, payment, money):  # 支付判斷
        if money is None:
            print("找不到價格資訊")
            return False
        if payment >= money:
            return True
        else:
            return False

    def give_change(self, payment, money):  # 找零
        if money is None:
            print("找不到價格資訊")
            return None
        givechange = payment - money
        return givechange

    def time(self):  # 分鐘計算
        parking_time = self.car_outs - self.car_in
        minutes_parked = parking_time.total_seconds() // 60
        return minutes_parked

    def is_weekend(self, day):  # 判斷假日
        return day in [6, 7]


if __name__ == "__main__":
    machine = ParkingMachine()

    # 加入車輛
    license_plate = "ABC123"
    machine.add_car(license_plate)

    # 離場
    machine.car_out()

    # 查詢入場時間
    car_in_time = machine.search_car_in()
    print("入場時間:", car_in_time)

    # 查詢出場時間
    car_out_time = machine.search_car_out()
    print("出場時間:", car_out_time)

    # 查詢價格
    price = machine.seach_car_pay()
    print("停車費用:", price)

    # 支付
    payment = 500
    if machine.pay_money(payment, price):
        change = machine.give_change(payment, price)
        print("支付成功，找零:", change)
    else:
        print("支付失敗，金額不足")

    # 可控離場時間
    machine.time1(60)  # 設定離場時間延後60分鐘

    # 再次查詢價格
    price = machine.seach_car_pay()
    print("停車費用:", price)
