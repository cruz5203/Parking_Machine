from tkinter import Tk, ttk, Label, Entry, Button, Text, Toplevel
import tkinter.messagebox as mbox
from parking_machine_import import ParkingMachine
import unittest.mock


class Parking_Machine:
    def __init__(self, parking):  # 宣告介面基本元件
        self.parking = parking
        self.licen_plate = None
        self.money = 0
        self.licen_plate_infos = {}
        self.parcking_machine_boundary_frame = ttk.Frame(parking, padding=10)
        self.licen_plate_lable = Label(
            self.parcking_machine_boundary_frame, text="車牌號碼:"
        )
        self.licen_plate_entry = Entry(self.parcking_machine_boundary_frame, width=30)
        self.sreach_lecen_plate_btn = Button(
            self.parcking_machine_boundary_frame,
            text="查詢",
            command=self.Search_Licen_Plate,
        )
        self.sreach_lecen_plate_info = Text(
            self.parcking_machine_boundary_frame, width=45, height=10, state="disabled"
        )
        self.input_money_label = Label(
            self.parcking_machine_boundary_frame, text="投入金額:"
        )
        self.input_money_entry = Entry(
            self.parcking_machine_boundary_frame, width=10, justify="center"
        )
        self.input_money_entry.insert(0, str(self.money))
        self.input_money_entry.config(state="readonly")
        self.pay_money_button_frame = ttk.Frame(self.parcking_machine_boundary_frame)
        self.confirm_pay_money_button = Button(
            self.pay_money_button_frame,
            text="確認付款",
            width=20,
            command=self.Confirm_Pay_Money,
        )
        self.cancel_pay_money_button = Button(
            self.pay_money_button_frame,
            text="取消付款",
            width=20,
            command=self.Cancel_Pay_Money,
        )

    def Search_Licen_Plate(self):  # 查詢車牌按鈕事件
        self.licen_plate = self.licen_plate_entry.get()
        if self.licen_plate in self.licen_plate_infos:
            self.licen_plate_infos[self.licen_plate].car_out()
            self.sreach_lecen_plate_info.config(state="normal")
            self.sreach_lecen_plate_info.insert("1.0", "\n")
            self.sreach_lecen_plate_info.insert("2.0", self.licen_plate + "\n\n")
            self.sreach_lecen_plate_info.insert(
                "4.0",
                "進場:"
                + self.licen_plate_infos[self.licen_plate].search_car_in()
                + "\n\n",
            )
            self.sreach_lecen_plate_info.insert(
                "6.0",
                "出場:"
                + self.licen_plate_infos[self.licen_plate].search_car_out()
                + "\n\n",
            )
            self.sreach_lecen_plate_info.insert(
                "8.0",
                "費用:"
                + str(self.licen_plate_infos[self.licen_plate].seach_car_pay())
                + "\n\n",
            )
            self.sreach_lecen_plate_info.tag_config("center", justify="center")
            self.sreach_lecen_plate_info.tag_add("center", "1.0", "end")
            self.sreach_lecen_plate_info.config(state="disabled")
            self.licen_plate_entry.config(state="readonly")
        elif self.licen_plate == "":
            mbox.showwarning("警告", "請輸入車牌")
            self.licen_plate = None
        else:
            mbox.showwarning("警告", "查無車牌\n請重新確認車牌號碼")
            self.licen_plate = None

    def Confirm_Pay_Money(self):  # 確認付款按鈕事件
        if self.licen_plate == None:
            mbox.showwarning("警告", "請輸入車牌")
        else:
            if self.licen_plate_infos[self.licen_plate].seach_car_pay() <= self.money:
                mbox.showinfo(
                    "付款成功",
                    "找零:"
                    + str(
                        self.money
                        - self.licen_plate_infos[self.licen_plate].seach_car_pay()
                    ),
                )
                self.licen_plate_infos.pop(self.licen_plate)
                self.Reset_Parking_Machine()
            else:
                mbox.showwarning("付款失敗", "投入金額不足")

    def Cancel_Pay_Money(self):  # 取消付款按鈕事件
        self.Reset_Parking_Machine()

    def Input_Money(self, money):  # 投幣事件
        money_value = [1, 5, 10, 50, 100, 200, 500, 1000, 2000]
        if money in money_value:
            self.money += money
            self.Update_Money()
        else:
            mbox.showwarning("警告", "非法貨幣")

    def Input_licen_plate(self, licen_plate):  # 輸入車牌事件
        if licen_plate in self.licen_plate_infos:
            mbox.showwarning("警告", "車牌已存在\n請在確認車牌")
        elif licen_plate == "":
            mbox.showwarning("警告", "請輸入車牌")
        else:
            licen_plate_info = ParkingMachine()
            licen_plate_info.add_car(licen_plate)
            self.licen_plate_infos[licen_plate] = licen_plate_info

    def Update_Money(self):  # 重新整理(付款金額)
        self.input_money_entry.config(state="normal")
        self.input_money_entry.delete(0, "end")
        self.input_money_entry.insert(0, str(self.money))
        self.input_money_entry.config(state="readonly")

    def Reset_Parking_Machine(self):  # 重新整理(視窗)
        self.licen_plate = None
        self.money = 0
        self.licen_plate_entry.config(state="normal")
        self.licen_plate_entry.delete(0, "end")
        self.sreach_lecen_plate_info.config(state="normal")
        self.sreach_lecen_plate_info.delete("1.0", "end")
        self.sreach_lecen_plate_info.config(state="disabled")
        self.Update_Money()

    def Window_Layout(self):  # 視窗版面配置
        self.parking.geometry("370x270")
        self.parking.resizable(False, False)
        self.parking.title("停車繳費系統")
        self.parcking_machine_boundary_frame.pack()
        self.licen_plate_lable.grid(row=0, column=0, padx=5, pady=5)
        self.licen_plate_entry.grid(row=0, column=1, padx=5, pady=5)
        self.sreach_lecen_plate_btn.grid(row=0, column=2, padx=5, pady=5)
        self.sreach_lecen_plate_info.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.input_money_label.grid(row=2, column=0, padx=5, pady=5)
        self.input_money_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.pay_money_button_frame.grid(row=3, column=0, columnspan=3, sticky="nsew")
        self.confirm_pay_money_button.grid(row=0, column=0, padx=10, pady=5)
        self.cancel_pay_money_button.grid(row=0, column=1, padx=10, pady=5)

    def Contrl_Window(self):  # 控制台視窗(模擬後台輸入車牌及投幣)
        ctl_window = Toplevel(self.parking)
        ctl_window.title("控制台")
        ctl_window.geometry("370x130")
        ctl_window.resizable(False, False)
        ctl_frame = ttk.Frame(ctl_window, padding=10)
        ctl_frame.pack()
        in_car_name_lable = Label(ctl_frame, text="車牌號碼:")
        in_car_name_lable.grid(row=0, column=0, padx=5, pady=5)
        in_car_name_entry = Entry(ctl_frame, width=30)
        in_car_name_entry.grid(row=0, column=1, padx=5, pady=5)

        def car_in():
            self.Input_licen_plate(in_car_name_entry.get())

        car_in_btn = Button(
            ctl_frame,
            text="入場",
            command=car_in,
        )
        car_in_btn.grid(row=0, column=2, padx=5, pady=5)
        ctl_frame_money = ttk.Frame(ctl_frame)
        ctl_frame_money.grid(row=1, column=0, columnspan=3)

        def money_1():
            self.Input_Money(1)

        money_btn_1 = Button(ctl_frame_money, text="1", width=7, command=money_1)
        money_btn_1.grid(row=0, column=0, padx=6, pady=5)

        def money_5():
            self.Input_Money(5)

        money_btn_5 = Button(ctl_frame_money, text="5", width=7, command=money_5)
        money_btn_5.grid(row=1, column=0, padx=6, pady=5)

        def money_10():
            self.Input_Money(10)

        money_btn_10 = Button(ctl_frame_money, text="10", width=7, command=money_10)
        money_btn_10.grid(row=0, column=1, padx=6, pady=5)

        def money_50():
            self.Input_Money(50)

        money_btn_50 = Button(ctl_frame_money, text="50", width=7, command=money_50)
        money_btn_50.grid(row=1, column=1, padx=6, pady=5)

        def money_100():
            self.Input_Money(100)

        money_btn_100 = Button(ctl_frame_money, text="100", width=7, command=money_100)
        money_btn_100.grid(row=0, column=2, padx=6, pady=5)

        def money_200():
            self.Input_Money(200)

        money_btn_200 = Button(ctl_frame_money, text="200", width=7, command=money_200)
        money_btn_200.grid(row=1, column=2, padx=6, pady=5)

        def money_500():
            self.Input_Money(500)

        money_btn_500 = Button(ctl_frame_money, text="500", width=7, command=money_500)
        money_btn_500.grid(row=0, column=3, padx=6, pady=5)

        def money_1000():
            self.Input_Money(1000)

        money_btn_1000 = Button(
            ctl_frame_money, text="1000", width=7, command=money_1000
        )
        money_btn_1000.grid(row=1, column=3, padx=6, pady=5)

        def money_2000():
            self.Input_Money(2000)

        money_btn_2000 = Button(
            ctl_frame_money, text="2000", width=7, command=money_2000
        )
        money_btn_2000.grid(row=0, column=4, padx=6, pady=5)

        def error_money():
            self.Input_Money(-1)

        money_btn_error = Button(
            ctl_frame_money, text="-1", width=7, command=error_money
        )
        money_btn_error.grid(row=1, column=4, padx=6, pady=5)


def Start_Window():  # 呼叫視窗
    root = Tk()
    window = Parking_Machine(root)
    window.Window_Layout()
    window.Contrl_Window()
    root.mainloop()


Start_Window()
