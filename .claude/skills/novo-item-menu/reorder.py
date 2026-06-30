#!/usr/bin/env python3
"""Cria um novo capitulo (item de menu) e/ou realinha weight, pre e o
numero da "### Secao" de TODOS os capitulos (chapter = true) seguindo a
ordem alfabetica dos titles, em portugues (acento-insensivel).

Uso:
    # apenas realinhar os capitulos existentes
    python3 reorder.py

    # criar um novo capitulo e realinhar tudo
    python3 reorder.py --create --title "Meu Titulo" --slug minhapasta

    # so mostrar a ordem resultante, sem gravar
    python3 reorder.py --dry-run
"""
import argparse
import datetime
import re
import sys
import unicodedata
from pathlib import Path

FM_DELIM = "+++"


def repo_root() -> Path:
    # .../<root>/.claude/skills/novo-item-menu/reorder.py
    return Path(__file__).resolve().parents[3]


def strip_accents(s: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c)
    )


def sort_key(title: str):
    return (strip_accents(title).casefold(), title)


def slugify(title: str) -> str:
    base = strip_accents(title).casefold()
    return re.sub(r"[^a-z0-9]+", "", base)


def split_front_matter(text: str):
    """Retorna (fm, body) onde fm e o bloco entre os dois +++ (sem os +++)."""
    if not text.startswith(FM_DELIM):
        raise ValueError("arquivo nao comeca com +++")
    end = text.index("\n" + FM_DELIM, len(FM_DELIM))
    fm = text[len(FM_DELIM) : end]
    rest = text[end + len("\n" + FM_DELIM) :]
    return fm, rest  # rest comeca apos o segundo +++


def get_title(fm: str) -> str:
    m = re.search(r'(?m)^\s*title\s*=\s*"(.*)"\s*$', fm)
    if not m:
        raise ValueError("title nao encontrado")
    return m.group(1)


def is_chapter(fm: str) -> bool:
    return re.search(r"(?m)^\s*chapter\s*=\s*true\s*$", fm) is not None


def apply_number(path: Path, n: int) -> bool:
    text = path.read_text(encoding="utf-8")
    fm, body = split_front_matter(text)
    original = text

    fm = re.sub(r"(?m)^(\s*weight\s*=\s*)\d+\s*$", rf"\g<1>{n}", fm)
    if re.search(r'(?m)^\s*pre\s*=', fm):
        fm = re.sub(
            r'(?m)^(\s*pre\s*=\s*)".*?"\s*$',
            rf'\g<1>"<b>{n}. </b>"',
            fm,
        )
    body = re.sub(r"(?m)^(###[ \t]+Seção[ \t]+)\d+[ \t]*$", rf"\g<1>{n}", body, count=1)

    new = FM_DELIM + fm + "\n" + FM_DELIM + body
    if new != original:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def create_chapter(content_dir: Path, title: str, slug: str) -> Path:
    folder = content_dir / slug
    idx = folder / "_index.md"
    if idx.exists():
        sys.exit(f"ERRO: {idx} ja existe.")
    folder.mkdir(parents=True, exist_ok=True)
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S-03:00")
    # weight/pre/secao serao ajustados no passo de realinhamento
    content = (
        f"{FM_DELIM}\n"
        f'title = "{title}"\n'
        f"date = {now}\n"
        f"weight = 999\n"
        f"chapter = true\n"
        f'pre = "<b>999. </b>"\n'
        f"{FM_DELIM}\n\n"
        f"### Seção 999\n\n"
        f"# {title}\n\n"
        f"{{{{% children  %}}}}\n"
    )
    idx.write_text(content, encoding="utf-8")
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--create", action="store_true", help="criar um novo capitulo")
    ap.add_argument("--title", help="title do novo capitulo")
    ap.add_argument("--slug", help="nome da pasta do novo capitulo")
    ap.add_argument("--dry-run", action="store_true", help="nao grava, so mostra a ordem")
    args = ap.parse_args()

    content_dir = repo_root() / "content"
    if not content_dir.is_dir():
        sys.exit(f"ERRO: nao encontrei {content_dir}")

    if args.create:
        if not args.title:
            sys.exit("ERRO: --create exige --title")
        slug = args.slug or slugify(args.title)
        if not slug:
            sys.exit("ERRO: nao foi possivel derivar slug; informe --slug")
        if not args.dry_run:
            created = create_chapter(content_dir, args.title, slug)
            print(f"criado: {created.relative_to(repo_root())}")
        else:
            print(f"[dry-run] criaria: content/{slug}/_index.md  title={args.title!r}")

    # coletar capitulos
    chapters = []
    for idx in sorted(content_dir.glob("*/_index.md")):
        try:
            fm, _ = split_front_matter(idx.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if is_chapter(fm):
            chapters.append((get_title(fm), idx))

    # incluir o novo (dry-run nao gravou arquivo)
    if args.create and args.dry_run:
        slug = args.slug or slugify(args.title)
        chapters.append((args.title, content_dir / slug / "_index.md"))

    chapters.sort(key=lambda c: sort_key(c[0]))

    print("\n# | weight/pre/secao | pasta | title")
    changed = 0
    for n, (title, idx) in enumerate(chapters, start=1):
        folder = idx.parent.name
        if not args.dry_run and idx.exists():
            if apply_number(idx, n):
                changed += 1
        print(f"{n:>2} | {folder} | {title}")

    if not args.dry_run:
        print(f"\narquivos alterados: {changed}")


if __name__ == "__main__":
    main()
