import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from tkinter import *
from tkinter.ttk import Combobox

mat_do = ctrl.Antecedent(np.arange(0, 101, 1), 'mat_do')
khan_cap = ctrl.Antecedent(np.arange(0, 101, 1), 'khan_cap')
tai_trong = ctrl.Antecedent(np.arange(0, 101, 1), 'tai_trong')
tinh_trang_gt = ctrl.Antecedent(np.arange(0, 101, 1), 'tinh_trang_gt')
loi_nhuan = ctrl.Antecedent(np.arange(0, 40, 1), 'loi_nhuan')

don_hang_ket_hop = ctrl.Consequent(np.arange(0, 11, 1), 'don_hang_ket_hop', defuzzify_method='mom')
do_uu_tien = ctrl.Consequent(np.arange(0, 101, 1), 'do_uu_tien', defuzzify_method='mom')

mat_do['thap'] = fuzz.trimf(mat_do.universe, [0, 0, 50])
mat_do['trung_binh'] = fuzz.trimf(mat_do.universe, [25, 50, 75])
mat_do['cao'] = fuzz.trimf(mat_do.universe, [50, 75, 100])

khan_cap['thap'] = fuzz.trimf(khan_cap.universe, [0, 0, 50])
khan_cap['trung_binh'] = fuzz.trimf(khan_cap.universe, [25, 50, 75])
khan_cap['cao'] = fuzz.trimf(khan_cap.universe, [50, 75, 100])

tai_trong['thap'] = fuzz.trimf(tai_trong.universe, [0, 0, 50])
tai_trong['trung_binh'] = fuzz.trimf(tai_trong.universe, [25, 50, 75])
tai_trong['cao'] = fuzz.trimf(tai_trong.universe, [50, 75, 100])

tinh_trang_gt['thap'] = fuzz.trimf(tinh_trang_gt.universe, [0, 0, 50])
tinh_trang_gt['trung_binh'] = fuzz.trimf(tinh_trang_gt.universe, [25, 50, 75])
tinh_trang_gt['cao'] = fuzz.trimf(tinh_trang_gt.universe, [50, 75, 100])

loi_nhuan['thap'] = fuzz.trimf(loi_nhuan.universe, [0, 0, 20])
loi_nhuan['trung_binh'] = fuzz.trimf(loi_nhuan.universe, [10, 20, 30])
loi_nhuan['cao'] = fuzz.trimf(loi_nhuan.universe, [20, 30, 40])

don_hang_ket_hop['thap'] = fuzz.trimf(don_hang_ket_hop.universe, [0, 0, 4])
don_hang_ket_hop['trung_binh'] = fuzz.trimf(don_hang_ket_hop.universe, [3, 5, 7])
don_hang_ket_hop['cao'] = fuzz.trimf(don_hang_ket_hop.universe, [6, 10, 10])

do_uu_tien['thap'] = fuzz.trimf(do_uu_tien.universe, [0, 0, 50])
do_uu_tien['trung_binh'] = fuzz.trimf(do_uu_tien.universe, [25, 50, 75])
do_uu_tien['cao'] = fuzz.trimf(do_uu_tien.universe, [50, 75, 100])


rule1 = ctrl.Rule(mat_do['cao'] & tai_trong['thap'] & tinh_trang_gt['thap'], don_hang_ket_hop['cao'])
rule2 = ctrl.Rule(mat_do['trung_binh'] & tinh_trang_gt['cao'] & khan_cap['trung_binh'], don_hang_ket_hop['trung_binh'])
rule3 = ctrl.Rule(tai_trong['cao'] & mat_do['cao'] & loi_nhuan['trung_binh'], don_hang_ket_hop['trung_binh'])
rule4 = ctrl.Rule(mat_do['thap'] & khan_cap['cao'] & tinh_trang_gt['trung_binh'], don_hang_ket_hop['trung_binh'])
rule5 = ctrl.Rule(loi_nhuan['cao'] & khan_cap['cao'] & tinh_trang_gt['cao'], don_hang_ket_hop['trung_binh'])
rule6 = ctrl.Rule(khan_cap['cao'] & loi_nhuan['cao'], do_uu_tien['cao'])
rule7 = ctrl.Rule(khan_cap['trung_binh'] & tinh_trang_gt['trung_binh'], do_uu_tien['trung_binh'])
rule8 = ctrl.Rule(khan_cap['thap'] & mat_do['cao'] & loi_nhuan['thap'], do_uu_tien['thap'])
rule9 = ctrl.Rule(mat_do['thap'] & tai_trong['cao'], don_hang_ket_hop['thap'])
rule10 = ctrl.Rule(mat_do['trung_binh'] & tai_trong['thap'], don_hang_ket_hop['trung_binh'])
rule11 = ctrl.Rule(tinh_trang_gt['cao'] & khan_cap['cao'], don_hang_ket_hop['thap'])
rule12 = ctrl.Rule(mat_do['trung_binh'] & tai_trong['trung_binh'] & tinh_trang_gt['trung_binh'], don_hang_ket_hop['trung_binh'])
rule13 = ctrl.Rule(khan_cap['cao'], do_uu_tien['cao'])
rule14 = ctrl.Rule(khan_cap['trung_binh'] & loi_nhuan['trung_binh'], do_uu_tien['trung_binh'])
rule15 = ctrl.Rule(khan_cap['thap'] & loi_nhuan['thap'], do_uu_tien['thap'])
rule16 = ctrl.Rule(loi_nhuan['cao'] & khan_cap['trung_binh'], do_uu_tien['cao'])

mophong=ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16])
sim = ctrl.ControlSystemSimulation(mophong)


root = Tk()
root.title("Hệ thống ưu tiên đơn hàng")
root.geometry("600x600")

tieude = Label(root, text="Hệ thống ưu tiên đơn hàng", font=("Arial", 20))
tieude.pack(pady=20)

mat_do_label = Label(root, text="Mật độ đơn hàng (0-100): ", font=("Times New Roman", 15))
mat_do_label.place(x=50, y=100)
mat_do_scale = Scale(root, from_=0, to=100, orient="horizontal", length=250)
mat_do_scale.place(x=250, y=85)

khan_cap_label = Label(root, text="Độ khẩn cấp (0-100): ", font=("Times New Roman", 15))
khan_cap_label.place(x=50, y=150)
khan_cap_scale = Scale(root, from_=0, to=100, orient="horizontal", length=250)
khan_cap_scale.place(x=250, y=135)

tai_trong_label = Label(root, text="Tải trọng (0-100): ", font=("Times New Roman", 15))
tai_trong_label.place(x=50, y=200)
tai_trong_scale = Scale(root, from_=0, to=100, orient="horizontal", length=250)
tai_trong_scale.place(x=250, y=185)

tinh_trang_gt_label = Label(root, text="Tình trạng giao thông (0-100): ", font=("Times New Roman", 15))
tinh_trang_gt_label.place(x=50, y=250)
tinh_trang_gt_scale = Scale(root, from_=0, to=100, orient="horizontal", length=250)
tinh_trang_gt_scale.place(x=250, y=235)

loi_nhuan_label = Label(root, text="Lợi nhuận (0-40): ", font=("Times New Roman", 15))
loi_nhuan_label.place(x=50, y=300)
loi_nhuan_scale = Scale(root, from_=0, to=40, orient="horizontal", length=250)
loi_nhuan_scale.place(x=250, y=285)

def tinh_toan():
    try :
        sim.input['mat_do'] = mat_do_scale.get()
        sim.input['khan_cap'] = khan_cap_scale.get()
        sim.input['tai_trong'] = tai_trong_scale.get()
        sim.input['tinh_trang_gt'] = tinh_trang_gt_scale.get()
        sim.input['loi_nhuan'] = loi_nhuan_scale.get()

        sim.compute()

        output.config(text=f"Đơn hàng kết hợp: {sim.output['don_hang_ket_hop']:.2f} đơn hàng\nĐộ ưu tiên: {sim.output['do_uu_tien']:.2f} %")

    except KeyError :
        output.config(text="Giá trị input bị lỗi")

bbt = Button(root, text="Tính toán", command=tinh_toan)
bbt.place(x=250, y=350)

fr = LabelFrame(root, text="Kết quả", font=("Times New Roman", 15), fg="blue", bg="lightgray")
fr.place(x=50, y=400, width=500, height=150)

output = Label(fr, text="", font=("Times New Roman", 15))
output.place(x=10, y=10)

root.mainloop()