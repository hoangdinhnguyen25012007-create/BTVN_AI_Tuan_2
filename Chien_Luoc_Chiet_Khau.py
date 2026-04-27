import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from tkinter import *
from tkinter.ttk import Combobox

xep_hang = ctrl.Antecedent(np.arange(1, 5.5, 0.5), 'xep_hang')
khoi_luong_ban = ctrl.Antecedent(np.arange(0, 101, 1), 'khoi_luong_ban')
bien_loi_nhuan = ctrl.Antecedent(np.arange(0, 41, 1), 'bien_loi_nhuan')
su_kien = ctrl.Antecedent(np.arange(0, 101, 1), 'su_kien')
giam_gia_dt = ctrl.Antecedent(np.arange(0, 51, 1), 'giam_gia_dt')


chiet_khau=ctrl.Consequent(np.arange(0, 51, 1), 'chiet_khau', defuzzify_method='mom')


xep_hang['thap'] = fuzz.trimf(xep_hang.universe, [0, 0, 4])
xep_hang['tb'] = fuzz.trimf(xep_hang.universe, [4, 4.25, 4.5])
xep_hang['cao'] = fuzz.trimf(xep_hang.universe, [4.5, 4.75, 5])

khoi_luong_ban['thap'] = fuzz.trimf(khoi_luong_ban.universe, [0, 0, 30])
khoi_luong_ban['trung_binh'] = fuzz.trimf(khoi_luong_ban.universe, [30, 50, 70])
khoi_luong_ban['cao'] = fuzz.trimf(khoi_luong_ban.universe, [60, 80, 100])

bien_loi_nhuan['thap'] = fuzz.trimf(bien_loi_nhuan.universe, [0, 0, 15])
bien_loi_nhuan['trung_binh'] = fuzz.trimf(bien_loi_nhuan.universe, [15, 20, 25])
bien_loi_nhuan['cao'] = fuzz.trimf(bien_loi_nhuan.universe, [20, 30, 40])

su_kien['thap'] = fuzz.trimf(su_kien.universe, [0, 0, 10])
su_kien['trung_binh'] = fuzz.trimf(su_kien.universe, [10, 20, 30])
su_kien['cao'] = fuzz.trimf(su_kien.universe, [30, 65, 100])

giam_gia_dt['thap'] = fuzz.trimf(giam_gia_dt.universe, [0, 0, 15])
giam_gia_dt['trung_binh'] = fuzz.trimf(giam_gia_dt.universe, [15, 20, 25])
giam_gia_dt['cao'] = fuzz.trimf(giam_gia_dt.universe, [25, 37.5, 50])

chiet_khau['rat_thap'] = fuzz.trimf(chiet_khau.universe, [0, 0, 5])
chiet_khau['thap'] = fuzz.trimf(chiet_khau.universe, [5, 7.5, 10])
chiet_khau['trung_binh'] = fuzz.trimf(chiet_khau.universe, [10, 15, 20])
chiet_khau['cao'] = fuzz.trimf(chiet_khau.universe, [20, 30, 40])
chiet_khau['rat_cao'] = fuzz.trimf(chiet_khau.universe, [40, 55, 70])

rule1 = ctrl.Rule(xep_hang['cao'] & khoi_luong_ban['cao'] & bien_loi_nhuan['cao'], chiet_khau['rat_thap'])
rule2 = ctrl.Rule(xep_hang['thap'] & khoi_luong_ban['thap'] & bien_loi_nhuan['cao'], chiet_khau['cao'])
rule3 = ctrl.Rule(su_kien['cao'] & giam_gia_dt['cao'], chiet_khau['rat_cao'])
rule4 = ctrl.Rule(xep_hang['tb'] & khoi_luong_ban['trung_binh'] & bien_loi_nhuan['trung_binh'], chiet_khau['trung_binh'])
rule5 = ctrl.Rule(giam_gia_dt['thap'] & bien_loi_nhuan['thap'] & khoi_luong_ban['cao'], chiet_khau['rat_thap'])
rule6 = ctrl.Rule(xep_hang['thap'] & su_kien['thap'], chiet_khau['trung_binh'])
rule7 = ctrl.Rule(khoi_luong_ban['thap'] & bien_loi_nhuan['thap'], chiet_khau['rat_cao'])

rule8  = ctrl.Rule(khoi_luong_ban['cao'], chiet_khau['thap'])
rule9  = ctrl.Rule(khoi_luong_ban['trung_binh'], chiet_khau['trung_binh'])
rule10 = ctrl.Rule(khoi_luong_ban['thap'], chiet_khau['cao'])

rule11 = ctrl.Rule(bien_loi_nhuan['cao'], chiet_khau['thap'])
rule12 = ctrl.Rule(bien_loi_nhuan['trung_binh'], chiet_khau['trung_binh'])
rule13 = ctrl.Rule(bien_loi_nhuan['thap'], chiet_khau['cao'])

rule14 = ctrl.Rule(xep_hang['cao'], chiet_khau['thap'])
rule15 = ctrl.Rule(xep_hang['tb'], chiet_khau['trung_binh'])
rule16 = ctrl.Rule(xep_hang['thap'], chiet_khau['cao'])

rule17 = ctrl.Rule(su_kien['cao'], chiet_khau['cao'])
rule18 = ctrl.Rule(su_kien['trung_binh'], chiet_khau['trung_binh'])
rule19 = ctrl.Rule(su_kien['thap'], chiet_khau['thap'])

rule20 = ctrl.Rule(giam_gia_dt['cao'], chiet_khau['cao'])
rule21 = ctrl.Rule(giam_gia_dt['trung_binh'], chiet_khau['trung_binh'])
rule22 = ctrl.Rule(giam_gia_dt['thap'], chiet_khau['thap'])

rule23 = ctrl.Rule(khoi_luong_ban['cao'] & bien_loi_nhuan['thap'], chiet_khau['cao'])
rule24 = ctrl.Rule(khoi_luong_ban['thap'] & bien_loi_nhuan['cao'], chiet_khau['thap'])

rule25 = ctrl.Rule(su_kien['cao'] & bien_loi_nhuan['thap'], chiet_khau['rat_cao'])
rule26 = ctrl.Rule(su_kien['thap'] & bien_loi_nhuan['cao'], chiet_khau['rat_thap'])

rule27 = ctrl.Rule(giam_gia_dt['cao'] & xep_hang['thap'], chiet_khau['rat_cao'])
rule28 = ctrl.Rule(giam_gia_dt['thap'] & xep_hang['cao'], chiet_khau['rat_thap'])

rule_defaul = ctrl.Rule(xep_hang['thap'] | xep_hang['tb'] | xep_hang['cao'], chiet_khau['trung_binh'])

mo_phong_chiet_khau = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule_defaul])

sim = ctrl.ControlSystemSimulation(mo_phong_chiet_khau)

root = Tk()
root.title("Tính Chiết Khấu")
root.geometry("600x600")

tieude = Label(root, text="Hệ thống tính chiết khấu", font=("Arial", 20))
tieude.pack(pady=20)

xep_hang_label = Label(root, text="Xếp hạng (1-5): ", font=("Times New Roman", 15))
xep_hang_label.place(x=50, y=100)
gt_xep_hang = Scale(root, from_=1, to=5, orient="horizontal", length=250, tickinterval=0.5, resolution=0.5)
gt_xep_hang.place(x=250, y=85)

khoi_luong_ban_label = Label(root, text="Khối lượng bán (0-100): ", font=("Times New Roman", 15))
khoi_luong_ban_label.place(x=50, y=160)
gt_khoi_luong_ban = Scale(root, from_=0, to=100, orient="horizontal", length=250)
gt_khoi_luong_ban.place(x=250, y=145)

bien_loi_nhuan_label = Label(root, text="Biên lợi nhuận (0-40)%: ", font=("Times New Roman", 15))
bien_loi_nhuan_label.place(x=50, y=210)
gt_bien_loi_nhuan = Scale(root, from_=0, to=40, orient="horizontal", length=250)
gt_bien_loi_nhuan.place(x=250, y=195)

su_kien_label = Label(root, text="Mức sự kiện (0-100): ", font=("Times New Roman", 15))
su_kien_label.place(x=50, y=260)
gt_su_kien = Scale(root, from_=0, to=100, orient="horizontal", length=250)
gt_su_kien.place(x=250, y=245)

giam_gia_dt_label = Label(root, text="Giảm giá đối thu (0-50)%: ", font=("Times New Roman", 15))
giam_gia_dt_label.place(x=50, y=310)
gt_giam_gia_dt = Scale(root, from_=0, to=50, orient="horizontal", length=250)
gt_giam_gia_dt.place(x=250, y=295)

def tinh_toan():
    try :
        sim.input['xep_hang'] = gt_xep_hang.get()
        sim.input['khoi_luong_ban'] = gt_khoi_luong_ban.get()
        sim.input['bien_loi_nhuan'] = gt_bien_loi_nhuan.get()
        sim.input['su_kien'] = gt_su_kien.get()
        sim.input['giam_gia_dt'] = gt_giam_gia_dt.get()
        sim.compute()
        a=sim.output['chiet_khau']
        output.config(text=f"Chiết khấu của bạn là: {a:.2f} %")

    except NameError:
        output.config(text="Lỗi: Bạn nhập sai biến (hãy nhập đúng tên biến)")
    except ValueError:
        output.config(text="Lỗi: Giá trị không hợp lệ")
    except KeyError:
        output.config(text="Lỗi: Sai tên biến input")
    

chiet_khau_bbt = Button(root, text="Tính Chiết Khấu", font=("Times New Roman", 20), command=tinh_toan, fg="red", bg="lightblue")
chiet_khau_bbt.place(x=200, y=360)

fr_output = Frame(root, width=500, height=100, bg="lightyellow")
fr_output.place(x=50, y=450)


output= Label(fr_output, text=" ", font=("Times New Roman", 15), bg="lightyellow")
output.place(x=10, y=10)

root.mainloop()