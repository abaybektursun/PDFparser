from Tkinter import *
import math

root = Tk()

y_dimension = 793.6801

w = Canvas(root, width=617.7601, height=y_dimension)
w.pack()

# Main Cube
w.create_rectangle(0.0, 0.0, 617.7601, y_dimension, fill="white")

w.create_rectangle(518.3405800999999, y_dimension - 767.9832936, 166.76, y_dimension - 746.4220783000001, fill="#476042")
w.create_rectangle(536.57505, y_dimension - 745.8297, 146.69, y_dimension - 734.3349000000001, fill="yellow")
w.create_rectangle(413.16610000000003, y_dimension - 724.7302, 200.56, y_dimension - 713.7933999999999, fill="#476042")

w.create_rectangle(335.8660799999999, y_dimension - 714.4108, 234.71439999999996, y_dimension - 703.4739999999999, fill="yellow")
w.create_rectangle(449.7332599999999, y_dimension - 714.4108, 345.74839999999995, y_dimension - 703.4739999999999, fill="#476042")
w.create_rectangle(410.56485, y_dimension - 691.9367, 174.42, y_dimension - 674.2057, fill="yellow")
w.create_rectangle(395.5453544, y_dimension - 656.7855, 187.56, y_dimension - 645.8035, fill="#476042")
w.create_rectangle(162.98930000000001, y_dimension - 639.909, 31.74, y_dimension - 624.439, fill="yellow")
w.create_rectangle(514.9953999999999, y_dimension - 613.8145000000001, 289.93, y_dimension - 601.6765, fill="#476042")
w.create_rectangle(390.2344499999999, y_dimension - 596.2945000000001, 293.04200000000003, y_dimension - 532.0615, fill="red")
w.create_rectangle(389.6755, y_dimension - 526.9345000000001, 300.73, y_dimension - 514.7965, fill="#476042")
w.create_rectangle(382.55075, y_dimension - 509.6445, 191.05, y_dimension - 428.1565, fill="yellow")
w.create_rectangle(353.2723, y_dimension - 423.0145, 194.011, y_dimension - 410.8735, fill="#476042")
w.create_rectangle(167.336, y_dimension - 379.739, 31.92, y_dimension - 364.269, fill="yellow")
w.create_rectangle(439.2026, y_dimension - 362.0655, 241.71, y_dimension - 351.0835, fill="#476042")
w.create_rectangle(415.2185, y_dimension - 344.78549999999996, 252.3395, y_dimension - 333.803, fill="yellow")
w.create_rectangle(388.0428000000001, y_dimension - 327.258, 282.51300000000003, y_dimension - 316.276, fill="#476042")
w.create_rectangle(388.07090000000005, y_dimension - 309.97549999999995, 294.25, y_dimension - 298.9935, fill="yellow")
w.create_rectangle(90.188124, y_dimension - 34.4555, 33.39, y_dimension - 23.4735, fill="#476042")
w.create_rectangle(261.79120000000006, y_dimension - 33.9755, 177.34, y_dimension - 22.9935, fill="blue")
w.create_rectangle(548.9856000000001, y_dimension - 33.7355, 331.51, y_dimension - 22.7535, fill="#476042")

w.create_rectangle(112.3301, y_dimension - 769.6901, 38.41, y_dimension - 695.77, fill="black")

w.create_rectangle(535.44, y_dimension - 641.4, 29.28, y_dimension - 641.4, fill="black")
w.create_rectangle(567.12, y_dimension - 390.24, 29.76, y_dimension - 390.24, fill="black")

w.create_rectangle(552.96, y_dimension - 294.72, 30.24, y_dimension - 294.72, fill="black")
w.create_rectangle(613.9201, y_dimension - 792.7199999999999, 613.9201, y_dimension - 1.68, fill="black")


root.mainloop()



