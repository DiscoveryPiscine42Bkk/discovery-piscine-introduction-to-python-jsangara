from datetime import datetime

farm_tasks = []

def show_menu():
    print("\n--- ระบบจัดการงานฟาร์มหมา ---")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    print("\n📌 เลือกงานที่ต้องการเพิ่ม:")
    print("1. ให้อาหารเช้า")
    print("2. ตัดแต่งขนหมา")
    print("3. ตรวจสุขภาพประจำสัปดาห์")
    print("4. ล้างกรงหมา")
    print("5. ฉีดวัคซีน")
    print("6. พาออกมาเดิน")

    job_choice = input("เลือกหมายเลขงาน (1-6): ")

    job_dict = {
        "1": "ให้อาหารเช้า",
        "2": "ตัดแต่งขนหมา",
        "3": "ตรวจสุขภาพประจำสัปดาห์",
        "4": "ล้างกรงหมา",
        "5": "ฉีดวัคซีน",
        "6": "พาออกมาเดิน"
    }

    if job_choice in job_dict:
        name = job_dict[job_choice]
    elif job_choice == "6":
        name = input("ป้อนชื่องานที่ต้องการเพิ่ม: ")
    else:
        print("❌ เลือกไม่ถูกต้อง")
        return
    print("เลือกประเภทงาน:")
    print("1. สัตว์เลี้ยง")
    print("2. อื่นๆ")
    category_choice = input("เลือก (1 หรือ 2): ")
    category = "สัตว์เลี้ยง" if category_choice == "1" else "อื่นๆ"

    date_created = datetime.now().strftime("%Y-%m-%d")

    farm_tasks.append({
        "name": name,
        "category": category,
        "date": date_created
    })

    print(f"✅ เพิ่มงาน '{name}' เรียบร้อยแล้ว (วันที่: {date_created})")

def list_tasks():
    if not farm_tasks:
        print("🔍 ยังไม่มีงานในระบบ")
    else:
        print("\n📋 รายการงานทั้งหมด:")
        for i, task in enumerate(farm_tasks, start=1):
            print(f"{i}. {task['name']} ({task['category']}) - เพิ่มเมื่อ: {task['date']}")

def delete_task():
    list_tasks()
    try:
        index = int(input("ป้อนหมายเลขงานที่ต้องการลบ: ")) - 1
        if 0 <= index < len(farm_tasks):
            removed = farm_tasks.pop(index)
            print(f"🗑 ลบงาน: {removed['name']} แล้วเรียบร้อย")
        else:
            print("❌ ไม่พบงานหมายเลขนั้น")
    except ValueError:
        print("⚠️ โปรดใส่ตัวเลขเท่านั้น")
def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1
        print("\n📊 สรุปจำนวนงาน:")
    for cat, count in summary.items():
        print(f"- {cat}: {count} งาน")

while True:
    show_menu()
    choice = input("เลือกเมนู (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        list_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        summarize_tasks()
    elif choice == "5":
        print("👋 ออกจากโปรแกรมแล้ว")
        break
    else:
        print("❌ โปรดเลือกเมนู 1-5 เท่านั้น")