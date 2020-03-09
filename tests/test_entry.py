import markdown
import mdx_macros


class DummyMacro(mdx_macros.BaseMacro):
    pass


def test_entry_with_literal():
    markdown.Markdown(extensions=[mdx_macros.MacroExtension(macros=[DummyMacro])])


def test_entry_with_string():
    markdown.Markdown(
        extensions=["macros"], config={"macros": {"macros": [DummyMacro]}},
    )
