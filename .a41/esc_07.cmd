awk "NR>=203 && NR<=213 {print NR\": \"substr(\$0,1,90)}" fuentes/scott_radical_candor/cap_13.md
