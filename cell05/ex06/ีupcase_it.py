#!/usr/bin/env python3
import sys

# ตรวจสอบจำนวนพารามิเตอร์
if len(sys.argv) == 2:
    # แปลงพารามิเตอร์แรกเป็นตัวพิมพ์ใหญ่
    print(sys.argv[1].upper())
else:
    # แสดง "none" ถ้าพารามิเตอร์ไม่เท่ากับ 1
    print("none")