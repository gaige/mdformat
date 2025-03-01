from markdown_it import MarkdownIt

from mdformat.renderer._tree import SyntaxTreeNode

EXAMPLE_MARKDOWN = """
## Heading here

Some paragraph text and **emphasis here** and more text here.
"""


def test_tree_to_tokens_conversion():
    tokens = MarkdownIt().parse(EXAMPLE_MARKDOWN)
    tokens_after_roundtrip = SyntaxTreeNode(tokens).to_tokens()
    assert tokens == tokens_after_roundtrip


def test_property_passthrough():
    tokens = MarkdownIt().parse(EXAMPLE_MARKDOWN)
    heading_open = tokens[0]
    tree = SyntaxTreeNode(tokens)
    heading_node = tree.children[0]
    assert heading_open.tag == heading_node.tag
    assert tuple(heading_open.map) == heading_node.map  # type: ignore
    assert heading_open.level == heading_node.level
    assert heading_open.content == heading_node.content
    assert heading_open.markup == heading_node.markup
    assert heading_open.info == heading_node.info
    assert heading_open.meta == heading_node.meta
    assert heading_open.block == heading_node.block
    assert heading_open.hidden == heading_node.hidden


def test_type():
    tokens = MarkdownIt().parse(EXAMPLE_MARKDOWN)
    tree = SyntaxTreeNode(tokens)
    # Root type is "root"
    assert tree.type == "root"
    # "_open" suffix must be stripped from nested token type
    assert tree.children[0].type == "heading"
    # For unnested tokens, node type must remain same as token type
    assert tree.children[0].children[0].type == "inline"


def test_sibling_traverse():
    tokens = MarkdownIt().parse(EXAMPLE_MARKDOWN)
    tree = SyntaxTreeNode(tokens)
    paragraph_inline_node = tree.children[1].children[0]
    text_node = paragraph_inline_node.children[0]
    assert text_node.type == "text"
    strong_node = text_node.next_sibling
    assert strong_node.type == "strong"  # type: ignore
    another_text_node = strong_node.next_sibling  # type: ignore
    assert another_text_node.type == "text"  # type: ignore
    assert another_text_node.next_sibling is None  # type: ignore
    assert another_text_node.previous_sibling.previous_sibling == text_node  # type: ignore  # noqa: E501
    assert text_node.previous_sibling is None
