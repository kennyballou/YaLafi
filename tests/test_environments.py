
#
#   test  of environments
#

from yalafi import parameters, parser, utils

p = parser.Parser(parameters.Parameters())

latex_proof = r"""
1\begin{proof}
2\end{proof}3

A\begin{proof}B\end{proof}C

X\begin{proof}[Proof]Y\end{proof}Z
"""
plain_proof_should_be = r"""
1

Beweis.
2

3

A

Beweis.
B

C

X

Proof.
Y

Z
"""
def test_proof():
    toks = p.parse(latex_proof)
    plain_proof, pos = utils.get_txt_pos(toks)

    assert plain_proof_should_be == plain_proof

latex_table = r"""
A\begin{table}B\end{table}C
"""
plain_table_should_be = r"""
A

[Tabelle]

C
"""
def test_table():
    toks = p.parse(latex_table)
    plain_table, pos = utils.get_txt_pos(toks)

    assert plain_table_should_be == plain_table

latex_comment = r"""
A\begin{comment}B\end{comment}C
X
\begin{comment}
Y
\end{comment}
Z
"""
plain_comment_should_be = r"""
AC
X
Z
"""
def test_comment():
    toks = p.parse(latex_comment)
    plain_comment, pos = utils.get_txt_pos(toks)

    assert plain_comment_should_be == plain_comment

latex_unknown = r"""
A\begin{x}B\end{x}C
X
\begin{x}
Y
\end{x}
Z
"""
plain_unknown_should_be = r"""
ABC
X
Y
Z
"""
def test_unknown():
    toks = p.parse(latex_unknown)
    plain_unknown, pos = utils.get_txt_pos(toks)

    assert plain_unknown_should_be == plain_unknown
