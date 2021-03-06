# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod1"  # alt
terminal = guess_terminal()
keys = [
    # spawns
    Key([mod], "f", lazy.spawn("firefox")),
    Key([mod], "r", lazy.spawn("rofi -show window")),
    Key([mod], "p", lazy.spawn("spotify")),
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "s", lazy.spawn("systemsettings5")),
    Key([mod], "g", lazy.spawn("dolphin")),
    Key([mod], "z", lazy.spawn("filezilla")),
    Key([mod], "m", lazy.spawn("discord")),

    # Switch between windows in current stack pane
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "h", lazy.layout.left()),

    # Move windows in current stack
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # flip windows any direction
    Key([mod, "control"], "k", lazy.layout.flip_up()),
    Key([mod, "control"], "j", lazy.layout.flip_down()),
    Key([mod, "control"], "h", lazy.layout.flip_left()),
    Key([mod, "control"], "l", lazy.layout.flip_right()),

    # resize windows
    Key([mod, "mod4"], "h", lazy.layout.grow_left()),
    Key([mod, "mod4"], "l", lazy.layout.grow_right()),
    Key([mod, "mod4"], "j", lazy.layout.grow_down()),
    Key([mod, "mod4"], "k", lazy.layout.grow_up()),

    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "space", lazy.layout.toggle_split()),

    # move through max windows
    Key([mod], "space", lazy.layout.next()),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),

    # group stuff
    Key([mod], "d", lazy.screen.toggle_group()),  # toggle last group
    Key([mod], "c", lazy.screen.prev_group()),  # previous group
    Key([mod], "v", lazy.screen.next_group()),  # next group

]

groups = [Group(i) for i in "1234890"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(
        border_focus=("ff82b9"),
        border_normal=("220000"),
        border_width=2,
        fair=False,
        grow_amount=1,
        lower_right=False,
        margin=3,
        name='bsp'
    ),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Source Code Pro Regular",
    fontsize=12,
    padding=3,
    background=("181a26"),
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text='TTP',
                    foreground=("ffff00"),
                    fontsize=14,
                    padding=6,
                ),
                widget.Sep(
                    padding=10,
                ),
                widget.GroupBox(
                    inactive=("444444"),
                    borderwidth=2,
                    disable_drag=True,
                    highlight_method='block',
                    margin=3,
                    rounded=False,
                    spacing=10,
                    padding=4,
                ),
                widget.Sep(
                    padding=10,
                ),
                widget.WindowName(
                    empty_group_string='TTP',
                    fontsize=14,
                    padding=9,
                ),
                widget.TextBox(
                    text='|',
                    padding=4,
                    fontsize=15,
                ),
                widget.Clock(
                    format='%j | %a, %b %d | %H:%M ',
                    fontsize=15,
                ),
            ],
            18,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},  # gitk
        {"wmclass": "makebranch"},  # gitk
        {"wmclass": "maketag"},  # gitk
        {"wname": "branchdialog"},  # gitk
        {"wname": "pinentry"},  # GPG key password entry
        {"wmclass": "ssh-askpass"},  # ssh-askpass
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
