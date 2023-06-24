from tkinter import Tk, ttk, Label, Entry, Button, Text, Toplevel
import tkinter.messagebox as mbox
import parking_machine_import


car_infos = {}
money = 0
car_name = None


def error_money():
    mbox.showwarning("警告", "非法貨幣")


def pay_money():
    if car_name == None:
        mbox.showwarning("警告", "請輸入車牌")
    else:
        if car_infos[car_name].seach_car_pay() <= money:
            ctl = Toplevel(window)
            ctl.title("付款成功")
            ctl.geometry("100x170")
            ctl.resizable(False, False)
            car_name_lable = Label(ctl, text=car_name, justify="center")
            car_name_lable.grid(row=0, column=0, padx=5, pady=5)
            car_in = Label(
                ctl,
                text="應付金額:"
                + str(
                    car_infos[car_name].seach_car_pay(),
                ),
                justify="center",
            )
            car_in.grid(row=1, column=0, padx=5, pady=5)
            car_out = Label(ctl, text="實付金額:" + str(money), justify="center")
            car_out.grid(row=2, column=0, padx=5, pady=5)
            car_more = Label(
                ctl,
                text="找零:" + str(money - car_infos[car_name].seach_car_pay()),
                justify="center",
            )

            car_more.grid(row=3, column=0, padx=5, pady=5)

            def yes():
                ctl.destroy()

            btn = Button(ctl, text="確認", width=5, command=yes)
            btn.grid(row=4, column=0, padx=5, pady=5)
            car_infos.pop(car_name)
        else:
            mbox.showerror("付款失敗", "投入金額不足")
        cancel_pay_money()


def cancel_pay_money():
    sreach_answer_text.config("")


def sreach_car_name():
    global car_name
    if car_name_entry.get() in car_infos:
        car_name = car_name_entry.get()
        car_infos[car_name].car_out()
        sreach_answer_text.config(state="normal")
        sreach_answer_text.insert("1.0", "\n")
        sreach_answer_text.insert("2.0", car_name + "\n\n")
        sreach_answer_text.insert(
            "4.0",
            "進場:" + car_infos[car_name].search_car_in() + "\n\n",
        )
        sreach_answer_text.insert(
            "6.0",
            "出場:" + car_infos[car_name].search_car_out() + "\n\n",
        )
        sreach_answer_text.insert(
            "8.0",
            "費用:" + str(car_infos[car_name].seach_car_pay()) + "\n\n",
        )
        sreach_answer_text.tag_configure("center", justify="center")
        sreach_answer_text.tag_add("center", "1.0", "end")
        sreach_answer_text.config(state="disabled")
    elif car_name_entry.get() == "":
        mbox.showwarning("警告", "請輸入車牌")
    else:
        mbox.showwarning("警告", "查無車牌\n請重新確認車牌號碼")
        global money
        money = 0
        car_name_entry.delete(0, "end")
        sreach_answer_text.config(state="normal")
        sreach_answer_text.delete("1.0", "end")
        sreach_answer_text.config(state="disabled")
        new_money()


def convert_to_uppercase():
    input_text = car_name_entry.get()
    uppercase_text = input_text.upper()
    car_name_entry.delete(0, "end")
    car_name_entry.insert(0, uppercase_text)


def new_car_name():
    if in_car_name_entry.get() in car_infos:
        mbox.showwarning("警告", "車牌已存在\n請在確認車牌")
    else:
        car = parking_machine_import.ParkingMachine()
        car.add_car(in_car_name_entry.get())
        car_infos[in_car_name_entry.get()] = car


def cancel_pay_money():
    global need_money
    global car_name
    global money
    global car_in_time
    global car_out_time
    need_money = 0
    car_name = ""
    money = 0
    car_in_time = 0.0
    car_out_time = 0.0
    car_name_entry.delete(0, "end")
    sreach_answer_text.config(state="normal")
    sreach_answer_text.delete("1.0", "end")
    sreach_answer_text.config(state="disabled")
    new_money()


def new_money():
    enter_money_entry.config(state="normal")
    enter_money_entry.delete(0, "end")
    enter_money_entry.insert(0, str(money))
    enter_money_entry.config(state="readonly")


def money_1():
    global money
    money += 1
    new_money()


def money_5():
    global money
    money += 5
    new_money()


def money_10():
    global money
    money += 10
    new_money()


def money_50():
    global money
    money += 50
    new_money()


def money_100():
    global money
    money += 100
    new_money()


def money_200():
    global money
    money += 200
    new_money()


def money_500():
    global money
    money += 500
    new_money()


def money_1000():
    global money
    money += 1000
    new_money()


def money_2000():
    global money
    money += 2000
    new_money()


window = Tk()
window.geometry("370x270")
window.resizable(False, False)
window.title("停車繳費系統")

frame = ttk.Frame(window, padding=10)
frame.pack()

car_name_lable = Label(frame, text="車牌號碼:")
car_name_lable.grid(row=0, column=0, padx=5, pady=5)

car_name_entry = Entry(frame, width=30)
car_name_entry.grid(row=0, column=1, padx=5, pady=5)
# car_name_entry.config(validate="key", validatecommand=convert_to_uppercase)

sreach_btn = Button(frame, text="查詢", command=sreach_car_name)
sreach_btn.grid(row=0, column=2, padx=5, pady=5)

sreach_answer_text = Text(frame, width=45, height=10, state="disabled")
sreach_answer_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

enter_money_lable = Label(frame, text="投入金額:")
enter_money_lable.grid(row=2, column=0, padx=5, pady=5)

enter_money_entry = Entry(frame, width=10, justify="center")
enter_money_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
enter_money_entry.insert(0, str(money))
enter_money_entry.config(state="readonly")

frame_1 = ttk.Frame(frame)
frame_1.grid(row=3, column=0, columnspan=3, sticky="nsew")

yes_btn = Button(frame_1, text="確認付款", width=20, command=pay_money)
yes_btn.grid(row=0, column=0, padx=10, pady=5)

no_btn = Button(frame_1, text="取消付款", width=20, command=cancel_pay_money)
no_btn.grid(row=0, column=1, padx=10, pady=5)

ctl = Toplevel(window)
ctl.title("控制台")
ctl.geometry("370x130")
ctl.resizable(False, False)

ctl_frame = ttk.Frame(ctl, padding=10)
ctl_frame.pack()

in_car_name_lable = Label(ctl_frame, text="車牌號碼:")
in_car_name_lable.grid(row=0, column=0, padx=5, pady=5)

in_car_name_entry = Entry(ctl_frame, width=30)
in_car_name_entry.grid(row=0, column=1, padx=5, pady=5)

car_in_btn = Button(ctl_frame, text="入場", command=new_car_name)
car_in_btn.grid(row=0, column=2, padx=5, pady=5)

ctl_frame_money = ttk.Frame(ctl_frame)
ctl_frame_money.grid(row=1, column=0, columnspan=3)

money_btn_1 = Button(ctl_frame_money, text="1", width=7, command=money_1)
money_btn_1.grid(row=0, column=0, padx=6, pady=5)

money_btn_5 = Button(ctl_frame_money, text="5", width=7, command=money_5)
money_btn_5.grid(row=1, column=0, padx=6, pady=5)

money_btn_10 = Button(ctl_frame_money, text="10", width=7, command=money_10)
money_btn_10.grid(row=0, column=1, padx=6, pady=5)

money_btn_50 = Button(ctl_frame_money, text="50", width=7, command=money_50)
money_btn_50.grid(row=1, column=1, padx=6, pady=5)

money_btn_100 = Button(ctl_frame_money, text="100", width=7, command=money_100)
money_btn_100.grid(row=0, column=2, padx=6, pady=5)

money_btn_200 = Button(ctl_frame_money, text="200", width=7, command=money_200)
money_btn_200.grid(row=1, column=2, padx=6, pady=5)

money_btn_500 = Button(ctl_frame_money, text="500", width=7, command=money_500)
money_btn_500.grid(row=0, column=3, padx=6, pady=5)

money_btn_1000 = Button(ctl_frame_money, text="1000", width=7, command=money_1000)
money_btn_1000.grid(row=1, column=3, padx=6, pady=5)

money_btn_2000 = Button(ctl_frame_money, text="2000", width=7, command=money_2000)
money_btn_2000.grid(row=0, column=4, padx=6, pady=5)

money_btn_error = Button(ctl_frame_money, text="-1", width=7, command=error_money)
money_btn_error.grid(row=1, column=4, padx=6, pady=5)

window.mainloop()
