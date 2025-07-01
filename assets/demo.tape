Output demo.gif

Set Shell "zsh"
Set FontSize 22
Set Width 1200
Set Height 600
Set Theme "Dracula"

Type "polars-prompt"
Sleep 500ms
Enter
Sleep 1s

Type `df = pl.read_csv("titanic.csv")`
Sleep 500ms
Escape
Enter
Sleep 1s

Type "dict(df.schema)"
Sleep 500ms
Escape
Enter
Sleep 1s

Type `df.group_by("Sex").agg((pl.col("Survived").mean() * 100).alias("PercentSurvived"))`
Sleep 500ms
Escape
Enter
Sleep 5s
