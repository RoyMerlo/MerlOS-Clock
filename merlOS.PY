import tkinter as tk
import time
import math

class MerloClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MerlOS Clock")
        self.geometry("400x450")
        self.configure(bg='#1a1a1a')
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width=400, height=400, bg='#1a1a1a', highlightthickness=0)
        self.canvas.pack()

        # Testo piccolo e trasparente in basso
        self.label = tk.Label(
            self, 
            text="POWERED BY ROY MERLO", 
            font=("Orbitron", 8), 
            fg="#005555",  # Trasparente visivo
            bg="#1a1a1a"
        )
        self.label.pack(pady=3)

        self.center_x, self.center_y = 200, 200
        self.clock_radius = 150

        self.draw_clock_face()
        self.update_clock()

    def draw_clock_face(self):
        self.canvas.create_oval(
            self.center_x - self.clock_radius,
            self.center_y - self.clock_radius,
            self.center_x + self.clock_radius,
            self.center_y + self.clock_radius,
            outline="#00ffff", width=4
        )

        # Marker moderni
        for i in range(60):
            angle = math.radians(i * 6)
            x1 = self.center_x + (self.clock_radius - 10) * math.sin(angle)
            y1 = self.center_y - (self.clock_radius - 10) * math.cos(angle)
            x2 = self.center_x + self.clock_radius * math.sin(angle)
            y2 = self.center_y - self.clock_radius * math.cos(angle)
            color = "#00ffff" if i % 5 == 0 else "#003333"
            width = 2 if i % 5 == 0 else 1
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)

        # Scritta "MerLOS" al centro
        self.canvas.create_text(
            self.center_x, self.center_y + 25,
            text="MerLOS",
            font=("Orbitron", 14, "bold"),
            fill="#00ffff",
            tags="center_text"
        )

    def update_clock(self):
        self.canvas.delete("hands")

        now = time.localtime()
        second = now.tm_sec
        minute = now.tm_min
        hour = now.tm_hour % 12

        # Lancetta secondi
        angle_sec = math.radians(second * 6)
        sec_x = self.center_x + 120 * math.sin(angle_sec)
        sec_y = self.center_y - 120 * math.cos(angle_sec)
        self.canvas.create_line(self.center_x, self.center_y, sec_x, sec_y, fill="#ff007f", width=2, tags="hands")

        # Lancetta minuti
        angle_min = math.radians(minute * 6 + second * 0.1)
        min_x = self.center_x + 100 * math.sin(angle_min)
        min_y = self.center_y - 100 * math.cos(angle_min)
        self.canvas.create_line(self.center_x, self.center_y, min_x, min_y, fill="#00ffff", width=4, tags="hands")

        # Lancetta ore
        angle_hour = math.radians((hour + minute / 60.0) * 30)
        hour_x = self.center_x + 70 * math.sin(angle_hour)
        hour_y = self.center_y - 70 * math.cos(angle_hour)
        self.canvas.create_line(self.center_x, self.center_y, hour_x, hour_y, fill="#00cccc", width=6, tags="hands")

        # Centro estetico
        self.canvas.create_oval(self.center_x - 6, self.center_y - 6, self.center_x + 6, self.center_y + 6,
                                fill="#00ffff", outline="", tags="hands")

        self.after(1000, self.update_clock)

if __name__ == "__main__":
    clock = MerloClock()
    clock.mainloop()

