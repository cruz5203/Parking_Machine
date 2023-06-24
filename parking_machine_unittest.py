from tkinter import Tk
import tkinter.messagebox as mbox
import unittest
import unittest.mock
from parking_machine import Parking_Machine


class TestMyApp(unittest.TestCase):
    def test_sreach_lecen_plate_btn_click(self):  # 測試輸入車牌後是否查詢的到
        root = Tk()
        app = Parking_Machine(root)
        app.Input_licen_plate("123")
        app.licen_plate_entry.insert(0, "123")
        app.sreach_lecen_plate_btn.invoke()
        self.assertEqual(app.licen_plate, "123")
        root.destroy()

    def test_input_money_error(self):  # 測試非法的貨幣面值是否會跳出警告視窗
        with unittest.mock.patch("tkinter.messagebox.showwarning") as mock_showwarning:
            root = Tk()
            app = Parking_Machine(root)
            app.Input_Money(-1)
            mock_showwarning.assert_called_once_with("警告", "非法貨幣")
            root.destroy()

    def test_input_money(self):  # 測試正確的面值輸入及加總
        root = Tk()
        app = Parking_Machine(root)
        app.Input_Money(1)
        app.Input_Money(5)
        app.Input_Money(10)
        app.Input_Money(50)
        app.Input_Money(100)
        app.Input_Money(200)
        app.Input_Money(500)
        app.Input_Money(1000)
        app.Input_Money(2000)
        self.assertEqual(app.input_money_entry.get(), "3866")
        root.destroy

    def test_input_licen_plate_error_1(self):  # 測試重複輸入車牌是否會跳出警告視窗
        with unittest.mock.patch("tkinter.messagebox.showwarning") as mock_showwarning:
            root = Tk()
            app = Parking_Machine(root)
            app.Input_licen_plate("123")
            app.Input_licen_plate("123")
            mock_showwarning.assert_called_once_with("警告", "車牌已存在\n請在確認車牌")
            root.destroy()

    def test_input_licen_plate_error_2(self):  # 測試不輸入值是否會跳出警告視窗
        with unittest.mock.patch("tkinter.messagebox.showwarning") as mock_showwarning:
            root = Tk()
            app = Parking_Machine(root)
            app.Input_licen_plate("")
            mock_showwarning.assert_called_once_with("警告", "請輸入車牌")
            root.destroy()

    def test_input_licen_plate(self):  # 測試輸入車牌後是否加入字典
        root = Tk()
        app = Parking_Machine(root)
        app.Input_licen_plate("123")
        self.assertIn("123", app.licen_plate_infos)
        root.destroy()

    def test_cancel_button_click(self):  # 測試點擊取消付款後畫面是否重置
        root = Tk()
        app = Parking_Machine(root)
        app.Input_licen_plate("123")
        app.licen_plate_entry.insert(0, "123")
        app.cancel_pay_money_button.invoke()
        self.assertEqual(app.input_money_entry.get(), "0")
        root.destroy()

    def test_all_1(self):  # 整合測試成功付款
        with unittest.mock.patch("tkinter.messagebox.showinfo") as mock_showinfo:
            root = Tk()
            app = Parking_Machine(root)
            app.Input_licen_plate("123")
            app.licen_plate_entry.insert(0, "123")
            app.sreach_lecen_plate_btn.invoke()
            app.Input_Money(2000)
            app.confirm_pay_money_button.invoke()
            mock_showinfo.assert_called_once_with("付款成功", unittest.mock.ANY)

    def test_all_2(self):  # 整合測試付款失敗
        with unittest.mock.patch("tkinter.messagebox.showwarning") as mock_showwarning:
            root = Tk()
            app = Parking_Machine(root)
            app.Input_licen_plate("123")
            app.licen_plate_entry.insert(0, "123")
            app.sreach_lecen_plate_btn.invoke()
            app.Input_Money(100)
            app.confirm_pay_money_button.invoke()
            mock_showwarning.assert_called_once_with("付款失敗", "投入金額不足")


if __name__ == "__main__":
    unittest.main()
