#!/usr/bin/env python3
import sys

# ลบ argument แรก (ชื่อไฟล์โปรแกรมเอง)
arguments = sys.argv[1:]

# นับจำนวน arguments ที่เหลือ
num_parameters = len(arguments)

print(f"Number of parameters: {num_parameters}")
