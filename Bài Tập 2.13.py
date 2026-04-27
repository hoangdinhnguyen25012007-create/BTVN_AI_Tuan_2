import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from tkinter import *
from tkinter.ttk import Combobox

nhu_cau_sp = ctrl.Antecedent(np.arange(0, 101, 1), 'nhu_cau_sp')
ap_luc = ctrl.Antecedent(np.arange(0, 101, 1), 'ap_luc')
bien_loi_nhuan = ctrl.Antecedent(np.arange(0, 41, 1), 'bien_loi_nhuan')
uy_tin = ctrl.Antecedent(np.arange(0, 5.5, 0.5), 'uy_tin')
nhu_cau_tm = ctrl.Antecedent(np.arange(0, 101, 1), 'nhu_cau_tm')


chiet_khau=ctrl.Consequent(np.arange(0, 71, 1), 'chiet_khau', defuzzify_method='mom')

nhu_cau_sp['thap'] = fuzz.trimf(nhu_cau_sp.universe, [0, 0, 30])
nhu_cau_sp['trung_binh'] = fuzz.trimf(nhu_cau_sp.universe, [30, 50, 70])
nhu_cau_sp['cao'] = fuzz.trimf(nhu_cau_sp.universe, [60, 80, 100])

ap_luc['thap'] = fuzz.trimf(ap_luc.universe, [0, 0, 25])
ap_luc['trung_binh'] = fuzz.trimf(ap_luc.universe, [20, 35, 50])
ap_luc['cao'] = fuzz.trimf(ap_luc.universe, [50, 75, 100])

bien_loi_nhuan['thap'] = fuzz.trimf(bien_loi_nhuan.universe, [0, 0, 15])
bien_loi_nhuan['trung_binh'] = fuzz.trimf(bien_loi_nhuan.universe, [15, 20, 25])
bien_loi_nhuan['cao'] = fuzz.trimf(bien_loi_nhuan.universe, [20, 30, 40])

uy_tin['thap'] = fuzz.trimf(uy_tin.universe, [0, 0, 4])
uy_tin['trung_binh'] = fuzz.trimf(uy_tin.universe, [4, 4.25, 4.5])
uy_tin['cao'] = fuzz.trimf(uy_tin.universe, [4.5, 4.75, 5])

nhu_cau_tm['thap'] = fuzz.trimf(nhu_cau_tm.universe, [0, 0, 1])
nhu_cau_tm['trung_binh'] = fuzz.trimf(nhu_cau_tm.universe, [0, 20, 40])
nhu_cau_tm['cao'] = fuzz.trimf(nhu_cau_tm.universe, [30, 80, 100])

chiet_khau['rat_thap'] = fuzz.trimf(chiet_khau.universe, [0, 0, 5])
chiet_khau['thap'] = fuzz.trimf(chiet_khau.universe, [5, 7.5, 10])
chiet_khau['trung_binh'] = fuzz.trimf(chiet_khau.universe, [10, 15, 20])
chiet_khau['cao'] = fuzz.trimf(chiet_khau.universe, [20, 30, 40])
chiet_khau['rat_cao'] = fuzz.trimf(chiet_khau.universe, [40, 55, 70])


rule1 = ctrl.Rule(nhu_cau_sp['cao'] & ap_luc['thap'] & bien_loi_nhuan['thap'], chiet_khau['thap'])
rule2 = ctrl.Rule(nhu_cau_sp['thap'] & ap_luc['cao'] & bien_loi_nhuan['cao'], chiet_khau['cao'])
rule3 = ctrl.Rule(uy_tin['cao'] & bien_loi_nhuan['trung_binh'] & nhu_cau_tm['cao'], chiet_khau['trung_binh'])
rule4 = ctrl.Rule(nhu_cau_tm['cao'] & ap_luc['cao'] & bien_loi_nhuan['cao'], chiet_khau['rat_cao'])
rule5 = ctrl.Rule(uy_tin['thap'] & nhu_cau_sp['trung_binh'] & bien_loi_nhuan['thap'], chiet_khau['trung_binh'])
rule6 = ctrl.Rule(nhu_cau_sp['cao'] & nhu_cau_tm['thap'] & ap_luc['thap'], chiet_khau['rat_thap'])
rule7 = ctrl.Rule(bien_loi_nhuan['cao'] & ap_luc['trung_binh'] & nhu_cau_tm['trung_binh'], chiet_khau['trung_binh'])
rule8 = ctrl.Rule(nhu_cau_sp['trung_binh'] & ap_luc['trung_binh'] & bien_loi_nhuan['trung_binh'], chiet_khau['trung_binh'])
rule9 = ctrl.Rule(nhu_cau_sp['thap'] & ap_luc['thap'] & bien_loi_nhuan['thap'], chiet_khau['rat_thap'])
rule10 = ctrl.Rule(nhu_cau_sp['cao'] & ap_luc['cao'] & bien_loi_nhuan['cao'], chiet_khau['cao'])
rule11 = ctrl.Rule(uy_tin['cao'] & ap_luc['thap'] & bien_loi_nhuan['cao'], chiet_khau['thap'])
rule12 = ctrl.Rule(uy_tin['thap'] & ap_luc['cao'] & bien_loi_nhuan['thap'], chiet_khau['cao'])
rule13 = ctrl.Rule(nhu_cau_tm['thap'] & bien_loi_nhuan['cao'], chiet_khau['thap'])
rule14 = ctrl.Rule(nhu_cau_tm['cao'] & bien_loi_nhuan['thap'], chiet_khau['cao'])
rule15 = ctrl.Rule(nhu_cau_sp['thap'] & nhu_cau_tm['cao'], chiet_khau['cao'])
rule16 = ctrl.Rule(nhu_cau_sp['cao'] & nhu_cau_tm['cao'], chiet_khau['trung_binh'])
rule17 = ctrl.Rule(ap_luc['cao'] & uy_tin['cao'], chiet_khau['cao'])
rule18 = ctrl.Rule(ap_luc['thap'] & uy_tin['cao'], chiet_khau['thap'])
rule19 = ctrl.Rule(ap_luc['trung_binh'] & uy_tin['trung_binh'], chiet_khau['trung_binh'])
rule20 = ctrl.Rule(nhu_cau_sp['trung_binh'] & bien_loi_nhuan['cao'], chiet_khau['trung_binh'])

mophong=ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20])
sim = ctrl.ControlSystemSimulation(mophong)


root = Tk()
root.title("Tính Chiết Khấu")
root.geometry("600x600")

tieude = Label(root, text="Hệ thống tối ưu hóa và tăng thu nhập", font=("Arial", 20))
tieude.pack(pady=20)

uy_tin_label = Label(root, text="Uy tín cửa hàng (1-5): ", font=("Times New Roman", 15))
uy_tin_label.place(x=50, y=100)
gt_uy_tin = Scale(root, from_=1, to=5, orient="horizontal", length=250, tickinterval=0.5, resolution=0.5)
gt_uy_tin.place(x=250, y=85)

ap_luc_label = Label(root, text="Áp lực đối thủ : ", font=("Times New Roman", 15))
ap_luc_label.place(x=50, y=160)
gt_ap_luc = Scale(root, from_=0, to=100, orient="horizontal", length=250)
gt_ap_luc.place(x=250, y=145)

bien_loi_nhuan_label = Label(root, text="Biên lợi nhuận (0-40)%: ", font=("Times New Roman", 15))
bien_loi_nhuan_label.place(x=50, y=210)
gt_bien_loi_nhuan = Scale(root, from_=0, to=40, orient="horizontal", length=250)
gt_bien_loi_nhuan.place(x=250, y=195)

nhu_cau_sp_label = Label(root, text="Nhu cầu sản phẩm (0-100): ", font=("Times New Roman", 15))
nhu_cau_sp_label.place(x=50, y=260)
gt_nhu_cau_sp = Scale(root, from_=0, to=100, orient="horizontal", length=250)
gt_nhu_cau_sp.place(x=250, y=245)

nhu_cau_tm_label = Label(root, text="Nhu cầu theo mùa (0-100): ", font=("Times New Roman", 15))
nhu_cau_tm_label.place(x=50, y=310)
gt_nhu_cau_tm = Scale(root, from_=0, to=100, orient="horizontal", length=250)
gt_nhu_cau_tm.place(x=250, y=295)

def tinh_toan():
    try :
        sim.input['nhu_cau_sp'] = gt_nhu_cau_sp.get()
        sim.input['ap_luc'] = gt_ap_luc.get()
        sim.input['bien_loi_nhuan'] = gt_bien_loi_nhuan.get()
        sim.input['uy_tin'] = gt_uy_tin.get()
        sim.input['nhu_cau_tm'] = gt_nhu_cau_tm.get()

        sim.compute()
        output.config(text=f"Chiết khấu được đề xuất: {sim.output['chiet_khau']:.2f}%")
    except ValueError:
        output.config(text="Vui lòng nhập giá trị hợp lệ cho tất cả các biến đầu vào.")

chiet_khau_bbt = Button(root, text="Tính Chiết Khấu", font=("Times New Roman", 20), command=tinh_toan, fg="red", bg="lightblue")
chiet_khau_bbt.place(x=200, y=360)

fr_output = Frame(root, width=500, height=100, bg="lightgray",)
fr_output.place(x=50, y=450)

output = Label(fr_output, text="Kết quả sẽ hiển thị tại đây",font=("Times New Roman", 15),bg="lightgray", fg="black",)
output.place(x=10, y=10)



root.mainloop()