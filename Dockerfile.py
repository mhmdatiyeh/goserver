# استخدم صورة جاهزة فيها Python مثبت
FROM python:3.10-slim

# انسخ الكود والملفات داخل الصورة
COPY main.py main.py
COPY books/ books/

# شغل السكربت باستخدام Python
CMD ["python", "main.py"]