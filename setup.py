from distutils.core import setup

setup(
    name="ERRORNOTFOUND",
    py_modules=["ERRORNOTFOUND"],
    entry_points={"console_scripts": ["ERRORNOTFOUND=ERRORNOTFOUND:main"]},
    version="0.2.5",
    description="Low bandwidth DoS tool. ERRORNOTFOUND rewrite in Python.",
    author="Gokberk Yaltirakli",
    url="https://github.com/gkbrk/slowloris",
    keywords=["dos", "http", "ERRORNOTFOUND"],
    license="MIT",
)
