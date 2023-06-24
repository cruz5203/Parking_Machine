import datetime

parking_data = {}


class Parkingpayment:
    def __init__(self):
        self.funcion_obj = funcion()  # 创建funcion类的实例

    def add_car(self, license_plate):
        parking_time = datetime.datetime.now()
        data = {"parking_time_in": parking_time}
        car_data.record_parking_data(license_plate, data)

    def search_car_in(self, license_plate):
        parking_time = car_data.get_parking_data(license_plate).get("parking_time_in")
        formatted_time = parking_time.strftime("%Y-%m-%d %H:%M:%S")
        print("車牌", license_plate, "的停車時間：", formatted_time)
        return parking_time

    def search_car_out(self, license_plate):
        parking_time_out = datetime.datetime.now()
        parking_time_out += datetime.timedelta(minutes=3000)
        car_data.add_additional_data(
            license_plate, "parking_time_out", parking_time_out
        )
        parking_time = car_data.get_parking_data(license_plate).get("parking_time_out")
        formatted_time = parking_time.strftime("%Y-%m-%d %H:%M:%S")
        print("車牌", license_plate, "的離場時間：", formatted_time)
        return parking_time

    def seach_car_pay(self, license_plate):
        car_in = car_data.get_parking_data(license_plate).get("parking_time_in")
        car_out = car_data.get_parking_data(license_plate).get("parking_time_out")
        minutes_parked = self.funcion_obj.time(car_in, car_out)
        day = car_in.weekday() + 1
        money = self.funcion_obj.money(
            license_plate, minutes_parked, day
        )  # 调用money方法计算价格

        return money

    def pay_money(self, license_plate):
        return 0

    def give_change(self, license_plate):
        return 0

    def delete(self, license_plate):
        return 0


class car_data:
    @staticmethod
    def record_parking_data(license_plate, data):
        if license_plate not in parking_data:
            parking_data[license_plate] = {}
        parking_data[license_plate].update(data)

    @staticmethod
    def get_parking_data(license_plate):
        if license_plate in parking_data:
            return parking_data[license_plate]
        else:
            return None

    @staticmethod
    def add_additional_data(license_plate, key, value):
        if license_plate in parking_data:
            parking_data[license_plate][key] = value


class funcion:
    def time(self, car_in, car_out):
        parking_time = car_out - car_in
        minutes_parked = parking_time.total_seconds() // 60
        return minutes_parked

    def money(self, license_plate, minutes_parked, day):  # 價錢判斷
        moneys = 0
        car_in = car_data.get_parking_data(license_plate).get("parking_time_in")
        car_in_data = car_in.minute
        minutes_parkeds = 0
        while minutes_parked > 0:
            if day > 7:
                day = 1
            if self.is_weekend(day):
                rate = 20
                max_charge = 420
            else:
                rate = 15
                max_charge = 300
            if car_in.hour != 0 or car_in.minute != 0:
                minutes_parkeds = 1440 - car_in_data
                minutes_parked -= minutes_parkeds
                day += 1
            else:
                if minutes_parked < 1440:
                    minutes_parkeds = minutes_parked
                else:
                    minutes_parkeds = 1440
                    minutes_parked -= minutes_parkeds
                    day += 1
            payment = (minutes_parkeds // 30) * rate
            payment = min(payment, max_charge)
            moneys += payment
        return moneys

    def is_weekend(self, day):  # 判斷假日
        return day in [6, 7]

    def make_payment(self, amount):  # 支付系統
        coins = []
        while amount > 0:
            coin = int(input("請投入硬幣（5、10, 50, 100, 500, 1000）: "))
            if coin in [5, 10, 50, 100, 200, 500, 1000, 2000]:
                coins.append(coin)
                amount -= coin
            else:
                print("不支援該硬幣")


payment = Parkingpayment()

# 新增車輛的停車資料
payment.add_car("ABC123")

# 查詢車輛的停車時間
parking_time_ABC123 = payment.search_car_in("ABC123")
parking_time_ABC123 = payment.search_car_out("ABC123")

# 获取停车时间并计算费用
minutes_parked = payment.seach_car_pay("ABC123")
print("金錢", minutes_parked)
