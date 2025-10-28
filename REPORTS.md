# Automated Reports
## Coverage Report
```text
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
board/__init__.py         0      0   100%
board/board.py          100     11    89%   61-70, 105, 143
checker/__init__.py       0      0   100%
checker/checker.py        5      0   100%
cli/__init__.py           0      0   100%
cli/cli.py               50      8    84%   32-33, 44-46, 53-54, 71
dice/__init__.py          0      0   100%
dice/dice.py             10      0   100%
exceptions.py             8      0   100%
game/__init__.py          0      0   100%
game/game.py            122      8    93%   88, 112, 118, 136, 142, 179, 192, 199
player/__init__.py        0      0   100%
player/player.py          5      0   100%
---------------------------------------------------
TOTAL                   300     27    91%

```
## Pylint Report
```text
************* Module board.board
board/board.py:10:23: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:14:58: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:21:20: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:23:42: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:24:43: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:25:43: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:26:43: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:28:43: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:29:43: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:30:42: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:31:42: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:33:22: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:42:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:50:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:51:33: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:58:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:71:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:74:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:79:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:82:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:84:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:87:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:91:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:100:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:102:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:110:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:119:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:122:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:125:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:129:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:138:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:140:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:146:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:148:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:157:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:160:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:164:0: C0303: Trailing whitespace (trailing-whitespace)
board/board.py:166:0: C0301: Line too long (109/100) (line-too-long)
board/board.py:169:0: C0305: Trailing newlines (trailing-newlines)
board/board.py:105:21: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
board/board.py:143:21: W1309: Using an f-string that does not have any interpolated variables (f-string-without-interpolation)
board/board.py:72:0: R0912: Too many branches (18/12) (too-many-branches)
board/board.py:72:0: R0915: Too many statements (55/50) (too-many-statements)
************* Module board.test_board
board/test_board.py:14:0: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:15:33: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:34:36: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:41:39: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:45:33: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:47:45: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:51:0: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:52:37: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:57:46: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:62:0: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:69:38: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:74:37: C0303: Trailing whitespace (trailing-whitespace)
board/test_board.py:80:0: C0304: Final newline missing (missing-final-newline)
************* Module checker.checker
checker/checker.py:10:0: C0304: Final newline missing (missing-final-newline)
checker/checker.py:2:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module checker.test_checker
checker/test_checker.py:21:0: C0304: Final newline missing (missing-final-newline)
************* Module cli.cli
cli/cli.py:11:0: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:24:0: W0311: Bad indentation. Found 16 spaces, expected 12 (bad-indentation)
cli/cli.py:25:0: W0311: Bad indentation. Found 16 spaces, expected 12 (bad-indentation)
cli/cli.py:26:0: W0311: Bad indentation. Found 16 spaces, expected 12 (bad-indentation)
cli/cli.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:33:21: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:47:0: C0303: Trailing whitespace (trailing-whitespace)
cli/cli.py:68:0: C0303: Trailing whitespace (trailing-whitespace)
************* Module cli.test_cli
cli/test_cli.py:243:0: C0304: Final newline missing (missing-final-newline)
************* Module dice.dice
dice/dice.py:7:23: C0303: Trailing whitespace (trailing-whitespace)
dice/dice.py:11:20: C0303: Trailing whitespace (trailing-whitespace)
dice/dice.py:16:0: C0303: Trailing whitespace (trailing-whitespace)
dice/dice.py:17:30: C0303: Trailing whitespace (trailing-whitespace)
************* Module dice.test_dice
dice/test_dice.py:24:55: C0303: Trailing whitespace (trailing-whitespace)
dice/test_dice.py:36:0: C0304: Final newline missing (missing-final-newline)
dice/test_dice.py:6:0: C0115: Missing class docstring (missing-class-docstring)
dice/test_dice.py:13:4: W0105: String statement has no effect (pointless-string-statement)
dice/test_dice.py:27:40: W0613: Unused argument 'mock_randint' (unused-argument)
************* Module exceptions
exceptions.py:11:0: C0301: Line too long (142/100) (line-too-long)
exceptions.py:11:0: C0301: Line too long (142/100) (line-too-long)
exceptions.py:27:0: C0304: Final newline missing (missing-final-newline)
exceptions.py:12:4: W0107: Unnecessary pass statement (unnecessary-pass)
exceptions.py:18:4: W0107: Unnecessary pass statement (unnecessary-pass)
exceptions.py:23:4: W0107: Unnecessary pass statement (unnecessary-pass)
exceptions.py:27:4: W0107: Unnecessary pass statement (unnecessary-pass)
************* Module game.game
game/game.py:15:28: C0303: Trailing whitespace (trailing-whitespace)
game/game.py:18:35: C0303: Trailing whitespace (trailing-whitespace)
game/game.py:21:0: C0303: Trailing whitespace (trailing-whitespace)
game/game.py:22:37: C0303: Trailing whitespace (trailing-whitespace)
game/game.py:32:0: C0303: Trailing whitespace (trailing-whitespace)
game/game.py:37:0: C0303: Trailing whitespace (trailing-whitespace)
game/game.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
game/game.py:134:8: C0104: Disallowed name "bar" (disallowed-name)
************* Module game.test_game
game/test_game.py:365:0: C0304: Final newline missing (missing-final-newline)
game/test_game.py:14:0: R0904: Too many public methods (33/20) (too-many-public-methods)
************* Module generate_reports
generate_reports.py:1:0: C0114: Missing module docstring (missing-module-docstring)
generate_reports.py:2:0: C0116: Missing function or method docstring (missing-function-docstring)
generate_reports.py:5:32: W0621: Redefining name 'f' from outer scope (line 19) (redefined-outer-name)
generate_reports.py:5:9: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
generate_reports.py:9:0: C0103: Constant name "reports_content" doesn't conform to UPPER_CASE naming style (invalid-name)
generate_reports.py:19:5: W1514: Using open without explicitly specifying an encoding (unspecified-encoding)
************* Module main
main.py:27:0: C0303: Trailing whitespace (trailing-whitespace)
main.py:34:0: C0303: Trailing whitespace (trailing-whitespace)
main.py:45:0: C0303: Trailing whitespace (trailing-whitespace)
main.py:52:0: C0304: Final newline missing (missing-final-newline)
************* Module player.player
player/player.py:3:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module player.test_player
player/test_player.py:19:0: C0304: Final newline missing (missing-final-newline)
************* Module pygame_ui
pygameUI/pygame_ui.py:100:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:120:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:124:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:143:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:155:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:167:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:225:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:235:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:276:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:310:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:331:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:334:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:337:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:345:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:347:70: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:351:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:358:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:364:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:371:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:375:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:441:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:456:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:461:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:500:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:504:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:521:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:539:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:543:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:556:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:565:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:575:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:582:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:592:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:603:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:607:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:617:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:621:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:647:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:655:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:664:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:668:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:682:0: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:689:67: C0303: Trailing whitespace (trailing-whitespace)
pygameUI/pygame_ui.py:4:0: E0401: Unable to import 'pygame' (import-error)
pygameUI/pygame_ui.py:37:0: R0913: Too many arguments (6/5) (too-many-arguments)
pygameUI/pygame_ui.py:37:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
pygameUI/pygame_ui.py:64:0: R0913: Too many arguments (6/5) (too-many-arguments)
pygameUI/pygame_ui.py:64:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
pygameUI/pygame_ui.py:84:0: R0914: Too many local variables (61/15) (too-many-locals)
pygameUI/pygame_ui.py:84:0: R0912: Too many branches (36/12) (too-many-branches)
pygameUI/pygame_ui.py:84:0: R0915: Too many statements (181/50) (too-many-statements)
pygameUI/pygame_ui.py:473:0: R0914: Too many local variables (26/15) (too-many-locals)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (6/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (8/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (8/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (9/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:494:4: R1702: Too many nested blocks (7/5) (too-many-nested-blocks)
pygameUI/pygame_ui.py:473:0: R0912: Too many branches (56/12) (too-many-branches)
pygameUI/pygame_ui.py:473:0: R0915: Too many statements (173/50) (too-many-statements)

-----------------------------------
Your code has been rated at 8.59/10


```
