# Changelog

This log documents all Python API or CLI breaking backwards incompatible changes.
Note that there is currently no guarantee for a stable Markdown formatting style across versions.

## 0.6.0

**NOTE:** Parser extension plugin API has changed in this release.

- Removed
  - `mdformat.renderer.MARKERS`
  - `mdformat.plugins.ParserExtensionInterface.render_token`
  - `start` and `stop` keyword arguments removed from `mdformat.renderer.MDRenderer.render`.
    Use `mdformat.renderer.MDRenderer.render_tree` to render a part of a Markdown document.
- Added
  - Modes for setting a word wrap width and removing word wrap
  - `mdformat.plugins.ParserExtensionInterface.RENDERER_FUNCS`
  - A class for representing linear `markdown-it` token stream as a tree: `mdformat.renderer.RenderTreeNode`
  - `mdformat.renderer.MDRenderer.render_tree` for rendering a `RenderTreeNode`

## 0.5.7

- Fixed
  - CLI crash when formatting standard error output and the operating system reports a terminal window width of zero or less
    ([#131](https://github.com/executablebooks/mdformat/issues/131)).
    Thank you [ehontoria](https://github.com/ehontoria) for the issue.

## 0.5.6

- Changed
  - Style: Reduce asterisk escaping
    ([#120](https://github.com/executablebooks/mdformat/issues/120))
  - Style: Reduce underscore escaping
    ([#119](https://github.com/executablebooks/mdformat/issues/119)).
    Thank you [dustinmichels](https://github.com/dustinmichels) for the issue.

## 0.5.5

- Changed
  - Style: Don't convert shortcut reference links into full reference links
    ([#111](https://github.com/executablebooks/mdformat/issues/111))

## 0.5.4

- Changed
  - Style: Reduce hash (`#`) escaping

## 0.5.0

- Changed
  - Style: Convert list marker types.
    Prefer "-" for bullet lists and "." for ordered lists.
  - Style: Remove trailing whitespace from empty list items.

## 0.4.0

- Changed
  - Style: Only surround link destination with angle brackets if required by CommonMark spec
  - Style: Thematic breaks are now 70 characters wide

## 0.3.5

- Fixed
  - Markdown equality validation falsely triggering when code formatter plugins were used.
    Thanks [chrisjsewell](https://github.com/chrisjsewell) for writing the tests to find the bug.

## 0.3.3

- Added
  - `CHANGES_AST` to extension plugin API.
    The feature allows plugins that alter Markdown AST to skip validation
    ([#49](https://github.com/executablebooks/mdformat/pull/49)).

## 0.3.2

- Changed
  - Style: Keep reference links as reference links ([#32](https://github.com/executablebooks/mdformat/issues/32)).
    Thank you [chrisjsewell](https://github.com/chrisjsewell) for the issue and the PR.
- Added
  - Option to number ordered list items consecutively using the `--number` flag ([#33](https://github.com/executablebooks/mdformat/issues/33)).
    Thank you [chrisjsewell](https://github.com/chrisjsewell) for the issue and the PR.
  - Parser extension plugins can now add their own CLI / Python API options ([#35](https://github.com/executablebooks/mdformat/pull/35)).
    Thanks [chrisjsewell](https://github.com/chrisjsewell) for the PR.
- Fixed
  - Image links that require surrounding angle brackets no longer break formatting ([#40](https://github.com/executablebooks/mdformat/issues/40)).

## 0.3.1

- Added
  - Plugin system for extending the parser ([#13](https://github.com/executablebooks/mdformat/issues/13)).
    Thank you [chrisjsewell](https://github.com/chrisjsewell) for the issue and the PR.
  - Exported `mdformat.renderer.MDRenderer` and `mdformat.renderer.MARKERS`

## 0.3.0

- Changed
  - Code formatter plugin function signature changed to `Callable[[str, str], str]`.
    The second input argument is full info string of the code block.

## 0.2.0

- Changed
  - Style: Use backtick for code fences whenever possible

## 0.1.2

- Added
  - Support for code formatter plugins

## 0.1.0

- Added
  - Initial mdformat release
