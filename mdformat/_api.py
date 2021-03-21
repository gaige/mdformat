from pathlib import Path
from typing import Any, Iterable, Mapping, Union

from mdformat._util import EMPTY_MAP, build_mdit
from mdformat.renderer import MDRenderer
from markdown_it.utils import AttrDict

def text(
    md: str,
    *,
    options: Mapping[str, Any] = EMPTY_MAP,
    extensions: Iterable[str] = (),
    codeformatters: Iterable[str] = (),
) -> str:
    """Format a Markdown string."""
    mdit = build_mdit(
        MDRenderer,
        mdformat_opts=options,
        extensions=extensions,
        codeformatters=codeformatters,
    )
    env = AttrDict()
    ast = mdit.parse(md, env)
    correct_links(ast)

    return mdit.renderer.render(ast, mdit.options, env)


def replace_pelican_placeholdlers(uri_key, attr_list):
    new_attrs = []
    for a in attr_list:
        if a[0] == uri_key:
            new_url = a[1]
            for placeholder in ('author', 'category', 'index', 'tag', 'filename', 'static', 'attach'):
                new_url = new_url.replace("%7B" + placeholder + "%7D", '{' + placeholder + '}')
            new_attrs += [[uri_key, new_url]]
        else:
            new_attrs += [a]
    return new_attrs

def correct_links(token_stream):
    for t in token_stream:
        if t.type == 'link_open' or t.type == 'image_open':
#            print(f"link {t}")
            t.attrs= replace_pelican_placeholdlers('href', t.attrs)
        elif t.type == 'image':
            t.attrs= replace_pelican_placeholdlers('src', t.attrs)

        if t.children:
            correct_links(t.children)

def file(
    f: Union[str, Path],
    *,
    options: Mapping[str, Any] = EMPTY_MAP,
    extensions: Iterable[str] = (),
    codeformatters: Iterable[str] = (),
) -> None:
    """Format a Markdown file in place."""
    if isinstance(f, str):
        f = Path(f)
    try:
        is_file = f.is_file()
    except OSError:  # Catch "OSError: [WinError 123]" on Windows
        is_file = False
    if not is_file:
        raise ValueError(f'Can not format "{f}". It is not a file.')
    original_md = f.read_text(encoding="utf-8")
    formatted_md = text(
        original_md,
        options=options,
        extensions=extensions,
        codeformatters=codeformatters,
    )
    f.write_text(formatted_md, encoding="utf-8")
