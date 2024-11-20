#!/usr/bin/env python3
import sys

# รับพารามิเตอร์ทั้งหมด ยกเว้นชื่อไฟล์
arguments = sys.argv[1:]

if len(arguments) > 0:
    # แสดงพารามิเตอร์ตัวแรก
    print(arguments[0])
else:
    # หากไม่มีพารามิเตอร์ แสดงคำว่า "none"
    print("none")
