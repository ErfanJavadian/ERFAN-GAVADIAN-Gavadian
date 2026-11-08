# -*- coding: utf-8 -*-
"""
NEBULA X — نسخه ۱
استودیوی خلق هنر هندسی
یک فایل مستقل؛ بدون نیاز به اینترنت یا کتابخانه‌های جانبی.
اجرا: Python + Turtle (برای نمونه در Pydroid 3)
"""

import turtle
import random
import datetime
import math

# ------------------------- تنظیمات اصلی -------------------------

APP_NAME = "NEBULA X"
APP_VERSION = "1.0"

# Tuple: تنظیمات ثابت برنامه
WINDOW_SIZE = (1000, 760)
BACKGROUND = "#080B18"
PANEL = "#10172B"
PANEL_LIGHT = "#17213B"
WHITE = "#F4F6FF"
MUTED = "#AAB4D0"
GOLD = "#F5C76B"
ACCENT = "#A78BFA"

# Dictionary: پالت‌های رنگی
PALETTES = {
    "NEON": ("#7DF9FF", "#A78BFA", "#FF5FD2", "#F5C76B", "#FFFFFF"),
    "GOLD": ("#F5C76B", "#D9A441", "#FFF0C2", "#B77B35", "#FFFFFF"),
    "GALAXY": ("#8B5CF6", "#3B82F6", "#EC4899", "#22D3EE", "#FFFFFF"),
    "ICE": ("#DDF7FF", "#8BD3F5", "#5B9BD5", "#B7C8FF", "#FFFFFF"),
    "FIRE": ("#FF5B36", "#FF9F43", "#FFD166", "#E63946", "#FFF3D6"),
}

# Dictionary: نام و مشخصات سبک‌های هنری
STYLES = {
    "MANDALA": "ماندالای هندسی",
    "FLOWER": "گل هندسی",
    "POLYGON": "چندضلعی‌های چرخان",
    "SPIRAL": "مارپیچ کیهانی",
    "STARBURST": "انفجار ستاره‌ای",
}

# Set: مجموعه رنگ‌های یکتا
UNIQUE_COLORS = set(color for palette in PALETTES.values() for color in palette)

# List: تاریخچه آثار در طول اجرای برنامه
art_history = []

current_palette = "NEON"
current_size = 150
current_repeats = 12
current_speed = 0
buttons = []
page = "welcome"

# ------------------------- صفحه و قلم‌ها -------------------------

screen = turtle.Screen()
screen.setup(WINDOW_SIZE[0], WINDOW_SIZE[1])
screen.title(APP_NAME + " | Geometric Art Studio")
screen.bgcolor(BACKGROUND)
screen.tracer(0, 0)

ui = turtle.Turtle(visible=False)
ui.speed(0)
ui.penup()

pen = turtle.Turtle(visible=False)
pen.speed(0)
pen.pensize(2)
pen.penup()

# ------------------------- ابزارهای رابط کاربری -------------------------

def rectangle(t, x, y, width, height, fill, outline=None):
    """رسم مستطیل برای کارت‌ها و دکمه‌ها."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(outline or fill, fill)
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    t.penup()

def write_text(t, x, y, text, size=14, color=WHITE, align="center", bold=False):
    """نوشتن متن روی صفحه."""
    t.penup()
    t.goto(x, y)
    t.color(color)
    font = ("Arial", size, "bold" if bold else "normal")
    t.write(text, align=align, font=font)

def add_button(x, y, width, height, label, action, primary=False):
    """ثبت و رسم دکمه قابل لمس."""
    fill = "#6D55D9" if primary else PANEL_LIGHT
    edge = "#B9A7FF" if primary else "#344365"
    rectangle(ui, x, y, width, height, fill, edge)
    write_text(ui, x + width / 2, y - height / 2 - 6, label, 13, WHITE, "center", True)
    buttons.append((x, y - height, x + width, y, action))

def draw_header(title, subtitle):
    write_text(ui, 0, 325, title, 25, WHITE, "center", True)
    write_text(ui, 0, 292, subtitle, 11, MUTED)

def draw_welcome():
    global page, buttons
    page = "welcome"
    buttons = []
    ui.clear()
    pen.clear()
    screen.bgcolor(BACKGROUND)

    # تزئینات هندسی پس‌زمینه
    for i in range(5):
        ui.penup()
        ui.goto(350 - i * 13, 230 - i * 13)
        ui.pendown()
        ui.pensize(1)
        ui.color("#20294A")
        ui.circle(70 + i * 13)
    for i in range(8):
        ui.penup()
        ui.goto(-390 + i * 24, -220)
        ui.dot(3, "#39436B")

    write_text(ui, 0, 210, "NEBULA X", 38, WHITE, "center", True)
    write_text(ui, 0, 165, "استودیوی خلق هنرهای هندسی", 19, GOLD, "center", True)
    write_text(ui, 0, 95, "به دنیای بی‌انتهای خلاقیت خوش آمدید", 18, WHITE)
    write_text(ui, 0, 55, "اینجا هندسه، رنگ و برنامه‌نویسی به هنر تبدیل می‌شوند.", 12, MUTED)
    rectangle(ui, -300, -5, 600, 125, PANEL, "#273354")
    write_text(ui, 0, -35, "وظیفه اصلی NEBULA X", 17, GOLD, "center", True)
    write_text(ui, 0, -68, "تبدیل الگوها و ایده‌های هندسی به آثار هنری دیجیتال", 12, WHITE)
    write_text(ui, 0, -92, "با انتخاب سبک، رنگ و تنظیمات دلخواه شما.", 11, MUTED)

    add_button(-125, -165, 250, 54, "شروع خلق اثر هنری", "studio", True)
    write_text(ui, 0, -265, "نسخه ۱.۰  |  طراحی، هندسه و خلاقیت", 10, "#7785AA")
    screen.update()

def draw_studio():
    global page, buttons
    page = "studio"
    buttons = []
    ui.clear()
    screen.bgcolor(BACKGROUND)

    # پنل کناری
    rectangle(ui, -480, 330, 285, 660, PANEL, "#263454")
    write_text(ui, -337, 292, "NEBULA X", 20, WHITE, "center", True)
    write_text(ui, -337, 264, "استودیوی طراحی", 11, GOLD)
    write_text(ui, -337, 222, "سبک‌های هنری", 13, WHITE, "center", True)

    labels = [
        ("ماندالا", "mandala"),
        ("گل هندسی", "flower"),
        ("چندضلعی", "polygon"),
        ("مارپیچ کیهانی", "spiral"),
        ("انفجار ستاره‌ای", "starburst"),
        ("اثر تصادفی", "random"),
    ]
    y = 185
    for label, action in labels:
        add_button(-445, y, 215, 38, label, action)
        y -= 48

    write_text(ui, -337, -122, "ابزارها", 13, WHITE, "center", True)
    add_button(-445, -140, 215, 36, "تغییر پالت رنگ", "palette")
    add_button(-445, -185, 215, 36, "تنظیم اندازه و تکرار", "settings")
    add_button(-445, -230, 102, 34, "گالری آثار", "gallery")
    add_button(-333, -230, 103, 34, "پاک‌سازی", "clear")
    add_button(-445, -273, 215, 34, "صفحه اصلی", "home")

    # بوم طراحی
    rectangle(ui, -160, 330, 630, 660, "#0B1022", "#202B4A")
    write_text(ui, 155, 292, "بوم خلق اثر", 15, WHITE, "center", True)
    write_text(ui, 155, 265, "یک سبک را از پنل سمت چپ انتخاب کنید.", 10, MUTED)
    write_text(ui, 155, -310, "پالت فعال: " + current_palette, 10, GOLD)
    screen.update()

def redraw_studio():
    draw_studio()

# ------------------------- موتور تولید هنر -------------------------

def prepare_pen():
    pen.clear()
    pen.penup()
    pen.goto(150, -5)
    pen.setheading(0)
    pen.pensize(2)
    pen.speed(current_speed)

def color_at(index):
    palette = PALETTES[current_palette]
    return palette[index % len(palette)]

def draw_mandala():
    prepare_pen()
    for layer in range(4):
        radius = current_size * (0.25 + layer * 0.18)
        for i in range(current_repeats * 2):
            pen.penup()
            pen.goto(150, 0)
            pen.setheading(i * 360 / (current_repeats * 2) + layer * 8)
            pen.forward(radius)
            pen.pendown()
            pen.color(color_at(i + layer))
            pen.circle(max(8, radius * 0.28))
            pen.dot(4, color_at(i + layer + 2))
    pen.penup()
    pen.goto(150, 0)
    pen.dot(12, GOLD)

def draw_flower():
    prepare_pen()
    for i in range(current_repeats * 2):
        pen.penup()
        pen.goto(150, 0)
        pen.setheading(i * 360 / (current_repeats * 2))
        pen.forward(current_size * 0.48)
        pen.pendown()
        pen.color(color_at(i))
        pen.circle(current_size * 0.42, 70)
        pen.left(110)
        pen.circle(current_size * 0.42, 70)
    pen.penup()
    pen.goto(150, 0)
    pen.dot(18, GOLD)

def draw_polygon():
    prepare_pen()
    sides = 3
    for ring in range(1, 8):
        sides = 3 + ring
        radius = current_size * (0.18 + ring * 0.105)
        pen.penup()
        pen.goto(150, 0)
        pen.setheading(ring * 9)
        pen.forward(radius)
        pen.pendown()
        pen.color(color_at(ring))
        for _ in range(sides):
            pen.forward(radius * 0.9)
            pen.left(360 / sides)
        pen.penup()

def draw_spiral():
    prepare_pen()
    pen.penup()
    pen.goto(150, 0)
    pen.pendown()
    distance = 2
    for i in range(520):
        pen.color(color_at(i // 13))
        pen.forward(distance)
        pen.left(17)
        distance += 0.32
        if distance > current_size * 0.11:
            distance = 2
    pen.penup()

def draw_starburst():
    prepare_pen()
    rays = max(24, current_repeats * 8)
    for i in range(rays):
        pen.penup()
        pen.goto(150, 0)
        pen.setheading(i * 360 / rays)
        pen.pendown()
        pen.color(color_at(i))
        length = current_size * (0.55 + (i % 5) * 0.09)
        pen.forward(length)
        pen.dot(4, color_at(i + 1))
    pen.penup()
    pen.goto(150, 0)
    pen.dot(24, GOLD)

DRAW_FUNCTIONS = {
    "mandala": draw_mandala,
    "flower": draw_flower,
    "polygon": draw_polygon,
    "spiral": draw_spiral,
    "starburst": draw_starburst,
}

def save_history(style_name):
    """ذخیره تاریخچه در فایل متنی؛ مدیریت خطا با try/except."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    record = timestamp + " | " + style_name + " | " + current_palette
    art_history.append(record)
    try:
        with open("nebula_history.txt", "a", encoding="utf-8") as file:
            file.write(record + "\n")
    except OSError:
        show_message("ذخیره فایل انجام نشد؛ فضای ذخیره‌سازی را بررسی کنید.")

def create_art(style_key):
    if style_key not in DRAW_FUNCTIONS:
        show_message("سبک انتخاب‌شده معتبر نیست.")
        return
    try:
        DRAW_FUNCTIONS[style_key]()
        save_history(STYLES[style_key])
        screen.update()
        write_text(ui, 155, -285, "اثر ساخته شد: " + STYLES[style_key], 10, GOLD)
        screen.update()
    except (turtle.TurtleGraphicsError, ValueError, OverflowError) as error:
        show_message("هنگام رسم اثر مشکلی رخ داد: " + str(error))

def random_art():
    style_key = random.choice(list(DRAW_FUNCTIONS.keys()))
    create_art(style_key)

# ------------------------- تنظیمات، گالری و پیام‌ها -------------------------

def show_message(message):
    ui.penup()
    rectangle(ui, -145, 80, 560, 70, "#1D2947", "#7C6CCB")
    write_text(ui, 135, 42, message[:72], 10, WHITE)
    screen.update()

def choose_palette():
    global current_palette
    names = ", ".join(PALETTES.keys())
    answer = screen.textinput("انتخاب رنگ", "نام پالت را وارد کنید:\n" + names)
    if answer:
        candidate = answer.strip().upper()
        if candidate in PALETTES:
            current_palette = candidate
            redraw_studio()
            show_message("پالت رنگ به " + candidate + " تغییر کرد.")
        else:
            show_message("نام پالت معتبر نیست.")

def change_settings():
    global current_size, current_repeats
    size_answer = screen.textinput("تنظیم اندازه", "اندازه اثر را از ۸۰ تا ۲۲۰ وارد کنید:")
    if size_answer is None:
        return
    repeat_answer = screen.textinput("تنظیم تکرار", "تعداد تکرار را از ۶ تا ۳۰ وارد کنید:")
    if repeat_answer is None:
        return
    try:
        new_size = int(size_answer)
        new_repeats = int(repeat_answer)
        if not 80 <= new_size <= 220:
            raise ValueError("اندازه باید بین ۸۰ تا ۲۲۰ باشد.")
        if not 6 <= new_repeats <= 30:
            raise ValueError("تکرار باید بین ۶ تا ۳۰ باشد.")
        current_size = new_size
        current_repeats = new_repeats
        show_message("تنظیمات با موفقیت به‌روزرسانی شد.")
    except ValueError:
        show_message("ورودی نامعتبر است؛ فقط عددهای مجاز را وارد کنید.")

def show_gallery():
    ui.clear()
    buttons.clear()
    draw_header("گالری آثار", "آخرین فعالیت‌های ثبت‌شده در NEBULA X")
    try:
        with open("nebula_history.txt", "r", encoding="utf-8") as file:
            records = file.readlines()[-10:]
        if not records:
            write_text(ui, 0, 80, "هنوز اثری ثبت نشده است.", 14, MUTED)
        else:
            y = 190
            for record in reversed(records):
                write_text(ui, 0, y, record.strip()[:90], 10, WHITE)
                y -= 32
    except FileNotFoundError:
        write_text(ui, 0, 80, "هنوز تاریخچه‌ای وجود ندارد. ابتدا یک اثر بسازید.", 12, MUTED)
    except OSError:
        write_text(ui, 0, 80, "خواندن تاریخچه امکان‌پذیر نیست.", 12, GOLD)
    add_button(-110, -245, 220, 48, "بازگشت به استودیو", "studio", True)
    screen.update()

def clear_canvas():
    pen.clear()
    show_message("بوم طراحی پاک شد.")

# ------------------------- کنترل رویدادهای لمس و کلیک -------------------------

def on_click(x, y):
    for x1, y1, x2, y2, action in reversed(buttons):
        if x1 <= x <= x2 and y1 <= y <= y2:
            if action == "studio":
                draw_studio()
            elif action == "home":
                draw_welcome()
            elif action == "palette":
                choose_palette()
            elif action == "settings":
                change_settings()
            elif action == "gallery":
                show_gallery()
            elif action == "clear":
                clear_canvas()
            elif action == "random":
                random_art()
            elif action in DRAW_FUNCTIONS:
                create_art(action)
            return

# ------------------------- راه‌اندازی برنامه -------------------------

def main():
    screen.onclick(on_click)
    draw_welcome()
    screen.mainloop()

if __name__ == "__main__":
    main()
