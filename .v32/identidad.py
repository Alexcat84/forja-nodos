# -*- coding: utf-8 -*-
"""LA IDENTIDAD DE LA VUELTA 32, LEIDA DE GIT Y NO TECLEADA (EXTRACTOR.md 5)."""
import subprocess


def git(*args):
    return subprocess.check_output(("git",) + args).decode("utf-8", "replace").strip()


APERTURA = "56a0df6"
commits = git("rev-list", "--count", APERTURA + "..HEAD")

print("| pieza | valor |")
print("|---|---|")
print("| rama | `%s` |" % git("rev-parse", "--abbrev-ref", "HEAD"))
print("| commit de apertura de la vuelta 32 | `%s` |" % APERTURA)
print("| commit ultimo al escribir esta tabla | `%s` |" % git("rev-parse", "--short", "HEAD"))
print("| commits de esta vuelta al escribir esta tabla | **%s** |" % commits)
print("| y el commit que publica esta tabla hace | **%d** |" % (int(commits) + 1))
