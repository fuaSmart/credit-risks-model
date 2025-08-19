"""Generate PSI/drift reports and bias audits."""

from aequitas.group import Group


def run_bias_audit(df):
    """Quantifies fairness across demographic groups."""
    g = Group()
    xtab, _ = g.get_crosstabs(df)
    return xtab
