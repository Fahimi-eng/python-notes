from setuptools import setup, find_packages

setup(
    name="mylibrary",                    # نام پکیج (همه کوچک، با خط تیره یا زیرخط)
    version="1.0.0",                     # نسخه (رشته)
    author="Alireza Fahimi",             # نام نویسنده
    author_email="alireza@example.com",  # ایمیل نویسنده (اختیاری)
    description="A simple library management system",  # توضیح کوتاه
    long_description=open("README.md", encoding="utf-8").read(),  # توضیح بلند از فایل README
    long_description_content_type="text/markdown",  # نوع فایل README
    url="https://github.com/fahimi_eng",  # آدرس مخزن (اختیاری)
    packages=find_packages(),            # جست‌وجو و شناسایی خودکار پکیج‌ها
    install_requires=[                   # وابستگی‌های مورد نیاز
        # "requests>=2.25.0",
        # "numpy>=1.19.0",
    ],
    python_requires=">=3.6",             # حداقل نسخه پایتون مورد نیاز
    classifiers=[                        # دسته‌بندی برای PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,           # شامل فایل‌های غیر پایتونی (مثل JSON, TXT)
    zip_safe=False,                      # برای امنیت بهتر
)