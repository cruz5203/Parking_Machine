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
        parking_time_out += datetime.timedelta(minutes=3000)
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
        minutes_parked = self.time()
        day = self.car_in.weekday() + 1
        money = self.money(minutes_parked, day)
        return money

    def money(self, minutes_parked, day):
        car_date = self.car_outs - self.car_in
        car_in_data = self.car_in.minute
        minutes_parkeds = 0
        moneys = 0  # 宣告和初始化
        while minutes_parked > 0:
            if day > 7:
                day = 1
            if self.is_weekend(day):
                rate = 20
                max_charge = 420
            else:
                rate = 15
                max_charge = 300
            if car_date.days != 0 and self.car_in.hour != 0 and self.car_in.minute != 0:
                minutes_parkeds = 1440 - car_in_data
                minutes_parked -= minutes_parkeds
                day += 1
            else:
                if minutes_parked < 1440:
                    minutes_parkeds = minutes_parked
                    minutes_parked -= minutes_parkeds
                else:
                    minutes_parkeds = 1440
                    minutes_parked -= minutes_parkeds
                    day += 1
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


# 主程式測試功能
if __name__ == "__main__":
    # 創建一個停車場物件
    parking_machine = ParkingMachine()

    while True:
        print("請選擇操作：")
        print("1. 加入車輛")
        print("2. 查詢車輛是否存在")
        print("3. 車輛離場")
        print("4. 查詢車輛入場時間")
        print("5. 查詢車輛離場時間")
        print("6. 查詢車輛應支付金額")
        print("7. 進行支付")
        print("8. 離開系統")

        choice = input("請輸入選項：")

        if choice == "1":
            license_plate = input("請輸入車牌號碼：")
            parking_machine.add_car(license_plate)
            print("車輛已加入")

        elif choice == "2":
            license_plate = input("請輸入車牌號碼：")
            car_exists = parking_machine.search_car(license_plate)
            if car_exists:
                print("車輛存在")
            else:
                print("車輛不存在")

        elif choice == "3":
            license_plate = input("請輸入車牌號碼：")
            parking_machine.car_out(license_plate)
            print("車輛已離場")

        elif choice == "4":
            license_plate = input("請輸入車牌號碼：")
            car_in_time = parking_machine.search_car_in(license_plate)
            print("車輛入場時間：", car_in_time)

        elif choice == "5":
            license_plate = input("請輸入車牌號碼：")
            car_out_time = parking_machine.search_car_out(license_plate)
            print("車輛離場時間：", car_out_time)

        elif choice == "6":
            license_plate = input("請輸入車牌號碼：")
            money = parking_machine.seach_car_pay(license_plate)
            print("需要支付的金額：", money)

        elif choice == "7":
            payment = float(input("請輸入支付金額："))
            money = parking_machine.seach_car_pay(license_plate)
            if parking_machine.pay_money(payment, money):
                change = parking_machine.give_change(payment, money)
                print("支付成功，找零：", change)
            else:
                print("支付金額不足")

        elif choice == "8":
            print("感謝使用，再見！")
            break

        else:
            print("請輸入有效的選項")
