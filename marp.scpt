tell application "Marp"
    open file "Users:tir:code:miku:batchdata:Slides.md"
end tell

tell application "System Events" to tell process "Marp"
    set frontmost to true
    click (menu item 1 where its name starts with "Export") of menu 1 of menu bar item "File" of menu bar 1

    keystroke "g" using {shift down, command down}
    keystroke "/Users/tir/code/miku/batchdata/Slides.pdf"
    delay 1
    keystroke return
    delay 1
    keystroke return
    delay 1
    keystroke space
    delay 3
    tell application "Marp"
        quit
    end tell

end tell

