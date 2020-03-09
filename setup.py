from setuptools import setup

setup(
    name="markdown-macros",
    version="0.1.3",
    packages=["mdx_macros"],
    author="Weston Nielson",
    author_email="wnielson@github",
    description="An extension for python-markdown that add Trac-like macro support.",
    license="MIT",
    keywords="markdown macro macros",
    url="https://github.com/wnielson/markdown-macros",
    install_requires=[
        "Markdown>=2.1.1"
    ],
    entry_points={
        "markdown.extensions": ["macros = mdx_macros:MacroExtension"]
    },
    tests_require=["nose"],
    test_suite="nose.collector",
)
